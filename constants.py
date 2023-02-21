import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random

length = 1000

backLegSensorValues = np.zeros(length)
frontLegSensorValues = np.zeros(length)

amplitude_Backleg = math.pi/4
frequency_Backleg = 10
phaseOffset_Backleg = 0

amplitude_Frontleg = math.pi/4
frequency_Frontleg = 10
phaseOffset_Frontleg = math.pi/8

a_Backleg = np.linspace(0, 2*math.pi, length)
targetAngles_Backleg = np.array(amplitude_Backleg * np.sin(frequency_Backleg * a_Backleg + phaseOffset_Backleg))

a_Frontleg = np.linspace(0, 2*math.pi, length)
targetAngles_Frontleg = np.array(amplitude_Frontleg * np.sin(frequency_Frontleg * a_Frontleg + phaseOffset_Frontleg))