import numpy as np
import matplotlib.pyplot as plt

data = [10,14,34,24,19,17,16,28,35,33]
plt.hist(data, bins=5)

plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.grid(True)
plt.show()