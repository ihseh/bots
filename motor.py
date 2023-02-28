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
		#print(self.jointName)


	def Set_Value(self, desiredAngle, ID):
		pyrosim.Set_Motor_For_Joint(
	      bodyIndex = ID,
	      jointName = self.jointName,
	      controlMode = p.POSITION_CONTROL,
	      #targetPosition = self.targetAngles[t],
	      targetPosition = desiredAngle,
	      maxForce = 100)
