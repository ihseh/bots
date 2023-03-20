import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time


class SOLUTION:

	def __init__(self, ID):
		self.weights = ((np.random.rand(3,2)) * 2) - 1
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
		pyrosim.Send_Cube(name="Torso", pos=[c.x,c.y,c.z] , size=[c.length,c.width,c.height])
		pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [c.x-.5,c.y,c.z-.5])
		pyrosim.Send_Cube(name="Backleg", pos=[-.5,0,-.5] , size=[c.length,c.width,c.height])
		pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [c.x+.5,0,c.z-.5])
		pyrosim.Send_Cube(name="Frontleg", pos=[.5,0,-.5] , size=[c.length,c.width,c.height])
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
		for row in range(3):
			for col in range(2):
				weight = self.weights[row,col]
				# print(weight)
				pyrosim.Send_Synapse( sourceNeuronName = row , targetNeuronName = col+3 , weight = weight)
		pyrosim.End()

	def Mutate(self):
		randRow = random.randint(0,2) 
		randCol = random.randint(0,1)
		self.weights[randRow,randCol] = random.random() * 2 - 1


	def Set_ID(self, ID):
		self.myID = ID



