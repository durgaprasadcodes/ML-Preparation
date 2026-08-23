import matplotlib.pyplot as plt

departments = ["IT","HR","Finance","Sales"]
employees = [50,20,35,40]

plt.bar(
    departments,
    employees,
    color="hotpink",
    edgecolor="black",
    width=0.6
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.show()