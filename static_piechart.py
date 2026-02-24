import matplotlib.pyplot as plt


labels = ['A', 'B', 'C', 'D']

values = [30, 25, 20, 25]


plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.title("Static Pie Chart")

plt.show()