import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
import constants as c
from simulation import SIMULATION
import sys

print(len(sys.argv))
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()

simulation.Get_Fitness()


