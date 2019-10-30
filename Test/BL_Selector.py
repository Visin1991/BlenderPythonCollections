import bpy

def mySelector(objName,additive=False):
	#By default,clear other selections
	if not additive:
		bpy.ops.object.select_all(action='DESELECT')

	#Set the 'select' property of the datablock to True
	bpy.data.objects[objName].select_set(True)
    


bpy.ops.mesh.primitive_cube_add(radius=1,location=(0,0,0))

bpy.ops.mesh.primitive_uv_sphere_add(radius = 1,location=(1,1,1))	


#Select only 'Cube'
mySelector('Cube')

#Select 'Sphere', Keeping other selections.  Select both the Cube and Sphere
mySelector('Sphere',True)

#Translate selected objects 1 unit along the x-axis
bpy.ops.transform.translate(value=(1,0,0))

