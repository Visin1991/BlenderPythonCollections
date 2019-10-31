import bpy

def GetObject(name):
    return bpy.data.objects[name]


cube = GetObject('Cube')

print(cube.location)