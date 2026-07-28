import matplotlib.pyplot as plt
import numpy as np

months = [3,4,5,6]

sales_2024 = [20,25,30,40]

sales_2025 = [18,28,35,45]

plt.title("Sales Graph")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.plot(months,sales_2024)
plt.plot(months,sales_2025)

plt.show()