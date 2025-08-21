import matplotlib.pyplot as plt
days = ["Sun","Mon","Tue","Wed","Thur","Friday","Sat"]
temp = [25, 27, 26, 28, 30, 29, 31]
plt.figure(figsize=(8,5))
plt.plot(days,temp,marker='o',color='cyan',linestyle='-',linewidth=3)
plt.title("Weekly Temperature Graph")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature(Celsius)")
plt.grid(True)
plt.show()