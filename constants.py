import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random

simLength = 1000

amplitude = math.pi/4
frequency = 10
phaseOffset = 0

# amplitude_Backleg = math.pi/4
# frequency_Backleg = 10
# phaseOffset_Backleg = 0

# amplitude_Frontleg = math.pi/4
# frequency_Frontleg = 10
# phaseOffset_Frontleg = math.pi/8

length = 1
width = 1
height = 1
x = 0
y = 0
z = 1.5

numberOfGenerations = 10

populationSize = 10