import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
import constants as c

class ROBOT:

    def __init__(self):

        self.motorss = {}

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
                self.sensors = {}
                # for linkName in pyrosim.linkNamesToIndices:
                #     print(linkName)