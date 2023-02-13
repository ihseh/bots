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
length = 1000
backLegSensorValues = np.zeros(length)
frontLegSensorValues = np.zeros(length)

#Motor Values

#Backleg
amplitude_Backleg = math.pi/4
frequency_Backleg = 10
phaseOffset_Backleg = 0
a_Backleg = np.linspace(0, 2*math.pi, length)
targetAngles_Backleg = np.array(amplitude_Backleg * np.sin(frequency_Backleg * a_Backleg + phaseOffset_Backleg))

#FrontLeg
amplitude_Frontleg = math.pi/4
frequency_Frontleg = 10
phaseOffset_Frontleg = 0
a_Frontleg = np.linspace(0, 2*math.pi, length)
targetAngles_Frontleg = np.array(amplitude_Frontleg * np.sin(frequency_Frontleg * a_Frontleg + phaseOffset_Frontleg))

#np.save("data/targetAngles.npy", targetAngles)
#exit("OK LEAVING NOW. YEAH, I THINK IM GONNA LEAVE NOW.")
for x in range(length):
	p.stepSimulation()
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_Backleg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = targetAngles_Backleg[x],
	maxForce = 100)
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_Frontleg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = targetAngles_Frontleg[x],
	maxForce = 100)
	time.sleep(1/400)
	#print(x)
p.disconnect()
#print(backLegSensorValues)
np.save("data/backLegSensorVals.npy", backLegSensorValues)
np.save("data/frontLegSensorVals.npy", frontLegSensorValues)


