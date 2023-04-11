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

    def __init__(self, runMode, solID):
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
        self.robot = ROBOT(solID)


    def Run(self):

        for x in range(c.simLength):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)

            sen1 = self.robot.sensors["FrontLowerLeg"].Get_Value(x)
            sen2 = self.robot.sensors["BackLowerLeg"].Get_Value(x) 
            sen3 = self.robot.sensors["LeftLowerLeg"].Get_Value(x)
            sen4 = self.robot.sensors["RightLowerLeg"].Get_Value(x)  
            sen5 = self.robot.sensors["Torso"].Get_Value(x)  

            if (sen1 == -1) and (sen2 == -1) and (sen3 == -1) and (sen4 == -1) and (sen5 == -1):
                self.robot.timeInAir += 1

            time.sleep(1/3000)

            #print(x)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
        
    def __del__(self):

        p.disconnect()

    