import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time


class SOLUTION:

	def __init__(self, ID):
		self.weights = ((np.random.rand(c.numSensorNeurons,c.numMotorNeurons)) * 2) - 1
		self.myID = ID

	# def Evaluate(self, directOrGUI):
	# 	self.Create_World()
	# 	self.Create_Body()
	# 	self.Create_Brain()
	# 	os.system("python simulate.py " + str(directOrGUI) + " " + str(self.myID) + " &")

	# 	#read fitness value
	# 	while not os.path.exists("fitness" + str(self.myID) + ".txt"):
	# 		time.sleep(0.01)

	# 	f = open("fitness" + str(self.myID) + ".txt", "r")
	# 	self.fitness = float(f.readline())
	# 	f.close()
		
	# 	print("FITNESS = " + str(self.fitness))

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python simulate.py " + str(directOrGUI) + " " + str(self.myID) + " &")

	def Wait_For_Simulation_To_End(self):
		#read fitness value
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.01)

		f = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(f.readline())
		f.close()
		
		#print("FITNESS = " + str(self.fitness))

		#delete fitness file
		os.system("rm fitness" + str(self.myID) + ".txt")


	def Create_World(self):
		#Create World
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[0,-5,c.z] , size=[c.length,c.width,c.height])
		pyrosim.End()

	def Create_Body(self):
		#Create Body
		pyrosim.Start_URDF("body.urdf")
		#torso
		pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length,c.width,c.height])
		#backleg
		pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0] , size=[.2,1,.2])
		#frontleg
		pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,.5,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Frontleg", pos=[0,.5,0] , size=[.2,1,.2])
		#left leg
		pyrosim.Send_Joint(name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="Leftleg", pos=[-.5,0,0] , size=[1,.2,.2])
		#right leg
		pyrosim.Send_Joint(name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="Rightleg", pos=[.5,0,0] , size=[1,.2,.2])
		#front lower leg
		pyrosim.Send_Joint(name = "Frontleg_FrontLowerLeg" , parent= "Frontleg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#back lower leg
		pyrosim.Send_Joint(name = "Backleg_BackLowerLeg" , parent= "Backleg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#right lower leg
		pyrosim.Send_Joint(name = "Rightleg_RightLowerLeg" , parent= "Rightleg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#left lower leg
		pyrosim.Send_Joint(name = "Leftleg_LeftLowerLeg" , parent= "Leftleg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#end
		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")

		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
		pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_Rightleg")
		pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_Leftleg")

		pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Frontleg_FrontLowerLeg")
		pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Backleg_BackLowerLeg")
		pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Leftleg_LeftLowerLeg")
		pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Rightleg_RightLowerLeg")


		for row in range(c.numSensorNeurons):
			for col in range(c.numMotorNeurons):
				weight = self.weights[row,col]
				# print(weight)
				pyrosim.Send_Synapse( sourceNeuronName = row , targetNeuronName = col+c.numSensorNeurons , weight = weight)
		pyrosim.End()


	def Mutate(self):
		randRow = random.randint(0,c.numSensorNeurons -1) 
		randCol = random.randint(0,c.numMotorNeurons -1)
		self.weights[randRow,randCol] = random.random() * 2 - 1


	def Set_ID(self, ID):
		self.myID = ID



