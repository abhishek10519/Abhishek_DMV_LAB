import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

x_data = []
y_data = []

line, = ax.plot([], [], color='green')

def animate(frame):
    x_data.append(frame)
    y_data.append(np.random.randint(0, 100))

   
    x_data_trim = x_data[-50:]
    y_data_trim = y_data[-50:]

    line.set_data(x_data_trim, y_data_trim)
    return line,

ani = animation.FuncAnimation(fig, animate, interval=200)

plt.show()