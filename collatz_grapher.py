# Imports
import numpy as np
import matplotlib.pyplot as plt
import sys
from collatz_lib import run_collatz

# Script
try:
    x_min = int(input("Enter a minimum value of x (int): "))
    x_max = int(input("Enter a maximum value of x (int): "))
    if not x_min < x_max:
        raise(ValueError)
except ValueError:
    print("ValueError: x_max must be greater than x_min.")
    sys.exit()

x = list(range(x_min,x_max))
y1 = []
y2 = []

for i in x:
    _, stop, highest = run_collatz(i)
    y1.append(stop)
    y2.append(highest)

fig, axs = plt.subplots(2, 1)
axs[0].plot(x, y1, 'or--') # plots stopping times
axs[0].set_ylabel('Stopping Time')
axs[0].grid(True)

axs[1].plot(x, y2, 'ob--') # plots mamimums times
axs[1].set_ylabel('Maximum')
axs[1].grid(True)

fig.tight_layout()
plt.savefig('collatz_plot.png', bbox_inches='tight')
plt.show()