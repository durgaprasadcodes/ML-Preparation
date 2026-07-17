import numpy as np

# Scalar Operations
a = np.array([1,2,3,4,5])

print(a+5)
print(a-10)
print(a*5)
print(a/6)
print(a**3)
print(a%2)

# Vectorized math functions

a = np.random.rand(5)

print(np.sqrt(a))
print(np.round(a))
print(np.pi)
print(np.ceil(a))
print(np.floor(a))

# Element-Wise Operations

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

print(a)
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a%b)

# Comparison Opertaions

a = np.array([91,80,92,78,60,78,95])
print(a >=90 )
print(a <90 )
print(a == 78)