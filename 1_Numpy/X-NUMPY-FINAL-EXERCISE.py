import numpy as np

# ========== PROBLEM 1 ===========

arr = np.arange(1,11)
print(arr)
arr = np.zeros((3,3))
print(arr)
arr = np.ones((4,4))
print(arr)


# ========= PROBLEM 2 ===========

arr = np.arange(1,13)
arr = arr.reshape(4,3)
print(arr)

# ========= PROBLEM 3 ===========

arr = np.arange(1, 17).reshape(4,4)
print(arr)

print(arr[0])
print(arr[:,-1])
print(arr[1:3,1:3])


# ========= PROBLEM 4 ===========

arr = np.array([12, 25, 18, 30, 15])

print(np.sum(arr))
print(np.std(arr))
print(np.var(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.max(arr))
print(np.min(arr))

# ========= PROBLEM 5 ===========

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[arr>35])

# ========= PROBLEM 6 ===========

arr = np.array([1,2,3,4,5])

print(arr*10)
print(arr**2)
print(arr+100)

# ========= Mini ML-Style Exercise ===========

marks = np.array([45, 67, 89, 32, 76, 55, 91, 40])

print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(marks[marks>np.mean(marks)])
print(marks[marks>=40])