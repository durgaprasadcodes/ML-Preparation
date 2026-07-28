import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 120, 150, 170, 200]

plt.plot(months, sales, label="Sales")

plt.title("Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Revenue")

plt.grid(True)

plt.legend()

plt.show()