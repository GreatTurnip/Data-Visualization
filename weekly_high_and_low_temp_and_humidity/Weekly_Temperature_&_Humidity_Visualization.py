import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
high_temp = [32, 31, 33, 30, 29, 28, 31]
low_temp = [24, 23, 22, 21, 20, 19, 22]
humidity = [60, 55, 65, 70, 50, 45, 55]
fig, ax1=plt.subplots()
ax1.plot(days,high_temp,label='High Temperature',marker='o',color='red',linestyle='-',linewidth=4)
ax1.plot(days,low_temp,label='Low Temperature',marker='o',color='green',linestyle='-',linewidth=4)
ax1.set_title("Weekly High and Low Temperature")
ax1.set_xlabel("Days of The Week")
ax1.set_ylabel("Temperature")
ax1.legend()
ax2 = ax1.twinx()
ax2.bar(days,humidity,color='blue',label='Humidity',alpha=0.2)
ax2.legend(loc='upper left')
ax1.grid(True)
plt.show()
