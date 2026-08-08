import matplotlib.pyplot as plt
import numpy as np

Industry = np.array(["IT", "FINANCE", "HR"])
Employees = np.array([5000, 4500, 3000])

plt.pie(
    Employees,
    labels=Industry,
    autopct="%.2f%%",
    colors=['red','green','blue'],
    explode=[.1,.1,.1],
    startangle=90
)

plt.show()