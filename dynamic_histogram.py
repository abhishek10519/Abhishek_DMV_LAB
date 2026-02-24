import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
    ax.clear() 

   
    data = np.random.randn(100)
    ax.hist(data, bins=10, color='orange', edgecolor='black')

    
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 30)
    ax.set_title("Dynamic Histogram")

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()