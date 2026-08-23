import matplotlib.pyplot as plt
import numpy as np

x = np.array(['week1','week2','week3','week4','week5'])
y = np.array([2000,1500,3000,4000,3000])

plt.title("Weekly Expenses")
plt.xlabel("Weeks")
plt.ylabel("Expenses")

plt.plot(x,y,label='expenses')
plt.legend()
plt.show()