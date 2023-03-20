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

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)

simulation.Run()

simulation.Get_Fitness()


