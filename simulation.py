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
          
          # pyrosim.Set_Motor_For_Joint(
          # bodyIndex = self.robot.robotId,
          # jointName = b'Torso_Backleg',
          # controlMode = p.POSITION_CONTROL,
          # targetPosition = c.targetAngles_Backleg[x],
          # maxForce = 100)
          # pyrosim.Set_Motor_For_Joint(
          # bodyIndex = self.robot.robotId,
          # jointName = b'Torso_Frontleg',
          # controlMode = p.POSITION_CONTROL,
          # targetPosition = c.targetAngles_Frontleg[x],
          # maxForce = 100)
          time.sleep(1/600)
          print(x)

    def __del__(self):

        p.disconnect()