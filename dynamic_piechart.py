import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

labels = ['A', 'B', 'C', 'D']

def animate(frame):
    ax.clear()  

    
    values = np.random.randint(1, 10, 4)

    
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Dynamic Pie Chart")

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()