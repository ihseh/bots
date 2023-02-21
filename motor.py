import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
import constants as c

class MOTOR:

	def __init__(self, jointName):
		self.jointName = jointName
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.offset = c.phaseOffset
		a = np.linspace(0, 2*math.pi, c.length)
		self.targetAngles = np.array(self.amplitude * np.sin(self.frequency * a + self.offset))


	def Set_Value(self, t, ID):
		pyrosim.Set_Motor_For_Joint(
	      bodyIndex = ID,
	      jointName = self.jointName,
	      controlMode = p.POSITION_CONTROL,
	      targetPosition = self.targetAngles[t],
	      maxForce = 100)

	def Save_Values(self): #Modify
		np.save("data/targetAnglesBackleg.npy", targetAngles_Backleg)
		np.save("data/targetAnglesFrontleg.npy", targetAngles_Frontleg)