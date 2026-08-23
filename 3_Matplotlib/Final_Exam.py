import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line Plot
axes[0, 0].plot(
    [1, 2, 3, 4],
    [10, 20, 15, 30],
    label='Sales'
)
axes[0, 0].set_title("Line Plot")
axes[0, 0].legend()


# 2. Bar Plot
axes[0, 1].bar(
    ["A", "B", "C"],
    [10, 20, 15],
    label='Sales'
)
axes[0, 1].set_title("Bar Plot")
axes[0, 1].legend()


# 3. Pie Plot
axes[1, 0].pie(
    [10, 20, 15],
    autopct="%.3f%%",
    labels=['Jan', 'Feb', 'Mar']
)
axes[1, 0].set_title("Pie Plot")


# 4. Horizontal Bar Plot
axes[1, 1].barh(
    ["A", "B", "C"],
    [10, 20, 15],
    label='Sales'
)
axes[1, 1].set_title("Horizontal Plot")
axes[1, 1].legend()


fig.tight_layout()

plt.show()