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
	pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
	pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [x+.5,y,z+.5])
	pyrosim.Send_Cube(name="Link1", pos=[.5,0,.5] , size=[length,width,height])
	pyrosim.End()


Create_World()
Create_Robot()