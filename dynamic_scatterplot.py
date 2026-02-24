import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots()

ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

x_data = []
y_data = []
scat = ax.scatter([], [], color='red')

def animate(frame):
    x_data.append(frame)
    y_data.append(np.random.randint(0, 100))  
    x_trim = x_data[-50:]
    y_trim = y_data[-50:]

    scat.set_offsets(np.column_stack((x_trim, y_trim)))
    return scat,

ani = animation.FuncAnimation(fig, animate, interval=200)

plt.show()
