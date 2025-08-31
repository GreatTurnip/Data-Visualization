import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
matplotlib.use("TkAgg")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [5000, 7000, 6500, 8000, 7500, 6000, 9000]

fig,ax=plt.subplots()
ax.set_xlabel("Days")
ax.set_ylabel("Steps")
ax.set_xlim(-0.5, len(days)-0.5)
ax.set_ylim(0, max(steps)+1000)
ax.set_xticks(range(len(days)))
ax.set_xticklabels(days)
line, =ax.plot([],[],marker='o',color='blue')
def update(frame):
    line.set_data(range(frame+1),steps[:frame+1])
    return line,
ani=animation.FuncAnimation(fig,update,frames=len(days),interval=500,blit=True)
plt.show()