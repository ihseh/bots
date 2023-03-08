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

class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                #self.motors[jointName].Set_Value(desiredAngle, self.robotId) #doesn't work
                #print("GHIHIHIHIHAIHGAIGHAIH")

                #for i in self.motors: #TO GET AROUND THE MOTOR KEY NOT ==ing THE JOINTNAME -> ONLY SEEMS TO WORK FOR ONE LEG AT ONCE, NEVER BOTH
                    #print("HERE")
                    #print(i)
                    #print("JointName: " + jointName)
                   # print("i: " + str(i))
                    #if jointName in str(i): #THIS ONLY WORKS FOR ONE OF THE LEGS, I THINK
                        #print("MATCH")
                        #self.motors[i].Set_Value(desiredAngle, self.robotId)
                print("REACHED TEMP SECTION")
                for i in self.motors:#Temporary, for submission video
                    self.motors[i].Set_Value(desiredAngle, self.robotId)

                print(neuronName, jointName, desiredAngle)

        #for i in self.motors:
            #self.motors[i].Set_Value(t, self.robotId)

    def Think(self):
        self.nn.Update()
        self.nn.Print()


