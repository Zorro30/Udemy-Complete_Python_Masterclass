import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)

y = 2 * x + 5 # (y = mx + c)

plt.title("This is the title.")
plt.xlabel("This is X label")
plt.ylabel("This is Y label")

plt.plot(x,y)
plt.show()