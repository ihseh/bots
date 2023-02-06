import numpy as np
import matplotlib.pyplot as matplotlib
backLegSensorValues = np.load("data/backLegSensorVals.npy")
frontLegSensorValues = np.load("data/frontLegSensorVals.npy")
#print(backLegSensorValues)
matplotlib.plot(backLegSensorValues, label = "Back Leg", linewidth = 4)
matplotlib.plot(frontLegSensorValues, label = "Front Leg")
matplotlib.legend()
matplotlib.show()
