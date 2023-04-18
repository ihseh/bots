import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:

    def __init__(self, solID):

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(solID) + ".nndf")
        #delete the brain file
        self.solutionID = str(solID)
        os.system("rm brain" + self.solutionID + ".nndf")

        self.timeInAir = 0
        self.longestJump = 0
        self.currentJump = 0
        self.runMode = "DEFAULT?"

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        #print('ROBOT ACTING')
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[bytes(jointName,'utf-8')].Set_Value(desiredAngle, self.robotId)
                #self.motors[str(jointName)].Set_Value(desiredAngle, self.robotId) #doesn't work
                #print(neuronName, jointName, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):

        for x in range(c.simLength):
            sen1 = self.sensors["FrontLowerLeg"].values[x]
            sen2 = self.sensors["BackLowerLeg"].values[x]      
            sen3 = self.sensors["LeftLowerLeg"].values[x]
            sen4 = self.sensors["RightLowerLeg"].values[x]
            # sen5 = self.sensors["Torso"].values[x]

            # if (sen1 == -1) and (sen2 == -1) and (sen3 == -1) and (sen4 == -1) and (sen5 == -1):
            if (sen1 == -1) and (sen2 == -1) and (sen3 == -1) and (sen4 == -1):

                if self.runMode == "GUI":
                    print("IN AIR")
                self.timeInAir += 1
                self.currentJump += 1
                if self.currentJump > self.longestJump:
                    self.longestJump = self.currentJump
            else:
                if self.runMode == "GUI":
                    print("ON GROUND")
                self.currentJump = 0
                self.timeInAir -= .5

            if self.runMode == "GUI":
                print(f"currentJump = {self.currentJump}")
                print(f"longestJump = {self.longestJump}")
                print(f"total timeInAir = {self.timeInAir}")


        f = open("tmp" + self.solutionID + ".txt" , "w")

        # print(f"timeInAir = {self.timeInAir}")
        # print(f"longestJump = {self.longestJump}")
        fitness = self.timeInAir + (self.longestJump*2)

        f.write(str(fitness))
        # f.write(str(self.timeInAir))

        f.close()

        os.system("mv tmp" + self.solutionID + ".txt fitness" + self.solutionID + ".txt")

        exit(" -- Exit from robot.Get_Fitness")


