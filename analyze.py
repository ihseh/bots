import numpy as np
import matplotlib.pyplot as matplotlib
#backLegSensorValues = np.load("data/backLegSensorVals.npy")
#frontLegSensorValues = np.load("data/frontLegSensorVals.npy")
#print(backLegSensorValues)
#matplotlib.plot(backLegSensorValues, label = "Back Leg", linewidth = 4)
#matplotlib.plot(frontLegSensorValues, label = "Front Leg")


targetAnglesBackleg = np.load("data/targetAnglesBackleg.npy")
targetAnglesFrontleg = np.load("data/targetAnglesFrontleg.npy")
matplotlib.plot(targetAnglesBackleg, label = "Back Leg", linewidth = 1)
matplotlib.plot(targetAnglesFrontleg, label = "Front Leg", linewidth = 1)

matplotlib.legend()
matplotlib.show()
