import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
for x in range(1000):
	p.stepSimulation()
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_Backleg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = random.uniform(-math.pi/2.0, math.pi/2.0),
	maxForce = 100)
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_Frontleg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = random.uniform(-math.pi/2.0, math.pi/2.0),
	maxForce = 100)
	time.sleep(1/60)
	time.sleep(1/60)
	#print(x)
p.disconnect()
#print(backLegSensorValues)
np.save("data/backLegSensorVals.npy", backLegSensorValues)
np.save("data/frontLegSensorVals.npy", frontLegSensorValues)


