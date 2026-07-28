import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

plt.plot(x,y)
plt.title("Testing Data")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

