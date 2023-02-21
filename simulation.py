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

    def __init__(self):
        
        
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):

        for x in range(c.length):
          p.stepSimulation()
          self.robot.Sense(x)
          self.robot.Act(x)
          
          
          time.sleep(1/600)
          #print(x)

    def __del__(self):

        p.disconnect()