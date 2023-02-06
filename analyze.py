import numpy as np
import matplotlib.pyplot as matplotlib
backLegSensorValues = np.load("data/sensorVals.npy")
print(backLegSensorValues)
matplotlib.plot(backLegSensorValues)
matplotlib.show()
