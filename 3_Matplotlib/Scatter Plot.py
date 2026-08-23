import matplotlib.pyplot as plt
import numpy as np

age = np.array([20, 25, 30, 35, 40, 45])
salary = np.array([25000, 32000, 40000, 48000, 60000, 70000])

plt.scatter(age, salary)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.show()