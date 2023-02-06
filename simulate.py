import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(100)
for x in range(100):
	p.stepSimulation()
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
	time.sleep(1/60)
	#print(x)
p.disconnect()
print(backLegSensorValues)
np.save("data/sensorVals.npy", backLegSensorValues)

