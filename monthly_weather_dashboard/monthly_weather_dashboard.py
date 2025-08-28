# Days
from matplotlib.pyplot import subplots
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import alphas

days = list(range(1, 31))

# Temperature (°C) for 30 days
temperature = [31.5, 29.6, 31.9, 34.6, 29.3, 30.7, 28.9, 32.1, 33.2, 30.0,
               31.8, 29.9, 32.5, 30.2, 31.0, 29.7, 30.4, 32.8, 33.0, 30.9,
               31.2, 29.8, 30.5, 32.0, 31.7, 30.3, 29.5, 32.4, 33.1, 30.6]

# Humidity (%) for 30 days
humidity = [59.0, 83.5, 64.9, 54.4, 73.2, 66.1, 68.0, 62.5, 70.3, 64.0,
            61.2, 69.5, 65.0, 67.8, 63.2, 72.1, 66.5, 60.9, 71.4, 68.2,
            65.7, 63.8, 69.0, 61.5, 67.0, 64.8, 70.2, 66.3, 62.7, 69.8]

# Rainfall (mm) for 30 days
rainfall = [2.0, 0.3, 1.9, 2.0, 6.5, 0.0, 3.2, 1.0, 0.5, 2.5,
            4.0, 1.7, 0.0, 3.5, 2.8, 1.2, 0.0, 4.2, 3.0, 1.5,
            2.2, 0.8, 3.1, 2.0, 1.9, 0.0, 4.5, 2.7, 1.0, 3.3]
fig, ax1 = subplots(2,2, figsize=(12,8))
ax1[0,0].plot(days,temperature,color='orange',marker='o',linestyle='-',label='Temperature')
ax1[0,0].set_title("Daily Temperature")
ax1[0,0].set_xlabel("Days")
ax1[0,0].set_ylabel("Temperature")
ax1[0,0].legend()

ax1[1,0].plot(days,humidity,color='cyan',marker='o',linestyle='-',label='Humidity')
ax1[1,0].set_title("Daily Humidity")
ax1[1,0].set_xlabel("Days")
ax1[1,0].set_ylabel("Humidity")
ax1[1,0].legend()

ax1[1,1].plot(days,rainfall,color='blue',marker='o',linestyle='-',label='Rainfall')
ax1[1,1].set_title("Daily Rainfall")
ax1[1,1].set_xlabel("Days")
ax1[1,1].set_ylabel("Rainfall")
ax1[1,1].legend()

slope, intercept = np.polyfit(temperature, rainfall, 1)
regression_line = slope * np.array(temperature) + intercept
ax1[0,1].plot(temperature, regression_line, color='blue', label='Regression Line',alpha=0.3)
ax1[0,1].scatter(temperature,rainfall,color='red',marker='o',linestyle='-',label='Temperature vs Rainfall')
ax1[0,1].set_title("Temperature vs Rainfall")
ax1[0,1].set_xlabel("Temperature")
ax1[0,1].set_ylabel("Rainfall")
ax1[0,1].legend()

plt.show()