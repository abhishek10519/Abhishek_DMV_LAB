import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
bars = ax.bar(categories, values, color='skyblue')
ax.set_ylim(0, 15)

def animate(frame):
    
    new_values = np.random.randint(1, 15, 5)

    for bar, new_height in zip(bars, new_values):
        bar.set_height(new_height)

    return bars

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()