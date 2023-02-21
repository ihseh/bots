import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
import constants as c


class SENSOR:

	def __init__(self, linkName):

		self.linkName = linkName
		self.values = np.zeros(c.length)
		#print(self.values)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		#print(self.values)
	
	def Save_Values(self): #Modify
		np.save("data/backLegSensorVals.npy", backLegSensorValues)
		np.save("data/frontLegSensorVals.npy", frontLegSensorValues)
