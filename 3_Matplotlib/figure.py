
import matplotlib.pyplot as plt

# Create one Figure with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1
axes[0, 0].plot([1, 2, 3, 4], [10, 20, 15, 30])
axes[0, 0].set_title("Line Plot")

# Plot 2
axes[0, 1].bar(["A", "B", "C"], [10, 20, 15])
axes[0, 1].set_title("Bar Plot")

# Plot 3
axes[1, 0].scatter([1, 2, 3, 4], [10, 25, 15, 35])
axes[1, 0].set_title("Scatter Plot")

# Plot 4
axes[1, 1].hist([10, 20, 20, 30, 30, 30, 40, 50])
axes[1, 1].set_title("Histogram")

# Adjust spacing
fig.tight_layout()

# Display
plt.show()