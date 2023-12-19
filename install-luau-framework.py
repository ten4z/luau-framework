import bpy
import os
from PIL import Image

codigo = """
color.loadpalette()
while true do
    buttons.read()
    screen.print(20, 20,"Olá PlayStation Vita!.", 1, color.red)
    screen.flip()
    if buttons.released.start then break end
end
"""

class MY_OT_custom(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Criar Estruturas"
    
    def execute(self, context):
        #self.report({'INFO'}, "Renderizando a Imagem.")

        scene = bpy.context.scene

        projeto = "VITACOD1A"

        current_directory = bpy.data.filepath
        filename = projeto + "/script.lua"

        filepath = bpy.data.filepath  
        path = os.path.dirname(filepath)
        name = "script.lua"                
        directory = projeto    
        parent_dir = path            
        mode = 777              
        path = os.path.join(parent_dir, directory)                      
        if not os.path.isdir(path):               
            os.makedirs(path, mode)             
        complete_filepath = os.path.join(path, name)        
        scene.render.image_settings.file_format = 'PNG'
        scene.render.filepath = os.path.join(path, 'icon0.png')
        bpy.ops.render.render(write_still = 1) 
        
        image = Image.open(os.path.join(path, 'icon0.png'))

        result = image.quantize(colors=32, method=2)

        result.save(os.path.join(path, 'png8bit.png'))
           
        with open(complete_filepath, "w") as file:
            file.write(codigo)
            file.close()        
        return {'FINISHED'}

class MY_PT_custom(bpy.types.Panel):
    bl_label = "Luau Framework"
    bl_idname = "OBJECT_PT_Luau"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        obj = context.object    
        layout = self.layout    
        row = layout.row()
        row.operator(MY_OT_custom.bl_idname)        
        layout.label(text="finalizado.")

bl_info = {
    "name": "Luau Framework",
    "author": "Ziga Multimedia",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "Objects > Luau Framework",
    "description": "Luau is a Tool to create a Lua Game Project to launch on PS Vita.",
    "category": "Game Engine",
}

def register():
    bpy.utils.register_class(MY_PT_custom)
    bpy.utils.register_class(MY_OT_custom)

def unregister():
    bpy.utils.unregister_class(MY_OT_custom)
    bpy.utils.unregister_class(MY_PT_custom)

if __name__ == "__main__":
    register()