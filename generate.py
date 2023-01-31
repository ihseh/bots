import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[0,-5,z] , size=[length,width,height])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
	pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [x+.5,y,z+.5])
	pyrosim.Send_Cube(name="Leg", pos=[x+1,y,z+1] , size=[length,width,height])
	pyrosim.End()


Create_World()
Create_Robot()