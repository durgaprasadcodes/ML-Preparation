import matplotlib.pyplot as plt
import numpy as pd

data = [35, 42, 45, 48, 51, 55, 56, 60, 62, 65, 68, 72, 75, 78, 80, 85, 90]

plt.hist(
    data,
    bins=5,
    density=True,
    edgecolor="black"
)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Data Distribution")

plt.show()