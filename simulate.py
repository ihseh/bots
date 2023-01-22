import pybullet as p
physicsClient = p.connect(p.GUI)
for x in range(1000):
	p.stepSimulation()
p.disconnect()
