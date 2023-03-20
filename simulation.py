import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
import constants as c

from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self, runMode):
        if (runMode == "DIRECT"):
            physicsClient = p.connect(p.DIRECT)
        elif (runMode == "GUI"):
            physicsClient = p.connect(p.GUI)
        else:
            print("INVALID RUN MODE")
            exit("EXITTING")
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):

        for x in range(c.simLength):
          p.stepSimulation()
          self.robot.Sense(x)
          self.robot.Think()
          self.robot.Act(x)
          
          
          time.sleep(1/3000)
          #print(x)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
        
    def __del__(self):

        p.disconnect()

    