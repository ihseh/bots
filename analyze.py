import numpy as np
import matplotlib.pyplot as matplotlib
#backLegSensorValues = np.load("data/backLegSensorVals.npy")
#frontLegSensorValues = np.load("data/frontLegSensorVals.npy")
#print(backLegSensorValues)
#matplotlib.plot(backLegSensorValues, label = "Back Leg", linewidth = 4)
#matplotlib.plot(frontLegSensorValues, label = "Front Leg")


targetAngles = np.load("data/targetAngles.npy")
matplotlib.plot(targetAngles, label = "Target Angles", linewidth = 1)


matplotlib.legend()
matplotlib.show()
