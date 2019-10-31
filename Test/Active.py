import bpy

def Active(objName):
    #Pass bpy.name.objects datablock to scene class
    bpy.context.scene.objects.active = bpy.data.objects[objName]
    
Active('Sphere')

print("Active object:",bpy.context.object.name)