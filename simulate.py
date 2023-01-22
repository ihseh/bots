import pybullet as p
physicsClient = p.connect(p.GUI)
for 1000:
	p.stepSimulation()
p.disconnect()
