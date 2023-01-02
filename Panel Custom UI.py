import bpy

class PANEL_CUSTOM_UI(bpy.types.Panel):
    """Create custom Panel"""
    bl_label="Panel Custom UI"
    bl_idname="OBJECT_PT_panel"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category = "Panel Custom UI"
      
      
    def draw(self, context):
        
        layout = self.layout
        
        row=layout.row()
        row.label(text = "ROW 5454")
        
def register():
    bpy.utils.register_class(PANEL_CUSTOM_UI)
    
def unregister():
    bpy.utils.register_class(PANEL_CUSTOM_UI)


if __name__ == "__main__":
    register()
