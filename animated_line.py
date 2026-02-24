import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

line, = ax.plot([], [], color='blue')

x_data = []
y_data = []

def animate(frame):
    x_data.append(frame)
    y_data.append(frame)  
    line.set_data(x_data, y_data)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10, 100), interval=100)

plt.show()