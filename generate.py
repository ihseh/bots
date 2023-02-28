import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x = 0
y = 0
z = 1.5

def Generate_Body():
	#Create World
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[0,-5,z] , size=[length,width,height])
	pyrosim.End()

	#Create Body
	pyrosim.Start_URDF("body.urdf")
	#Robot From Slides
	# pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
	# pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [x,y,z+.5])
	# pyrosim.Send_Cube(name="Link1", pos=[0,0,.5] , size=[length,width,height])
	# pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
	# pyrosim.Send_Cube(name="Link2", pos=[0,0,.5] , size=[length,width,height])
	# pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,.5,.5])
	# pyrosim.Send_Cube(name="Link3", pos=[0,.5,0] , size=[length,width,height])
	# pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
	# pyrosim.Send_Cube(name="Link4", pos=[0,.5,0] , size=[length,width,height])
	# pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,.5,-.5])
	# pyrosim.Send_Cube(name="Link5", pos=[0,0,-.5] , size=[length,width,height])
	# pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
	# pyrosim.Send_Cube(name="Link6", pos=[0,0,-.5] , size=[length,width,height])

	#Robot for submission
	pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
	pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [x-.5,y,z-.5])
	pyrosim.Send_Cube(name="Backleg", pos=[-.5,0,-.5] , size=[length,width,height])
	pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [x+.5,0,z-.5])
	pyrosim.Send_Cube(name="Frontleg", pos=[.5,0,-.5] , size=[length,width,height])


	pyrosim.End()


def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
	pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
	pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")



	
	pyrosim.End()

Generate_Body()
Generate_Brain()