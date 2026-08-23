import numpy as np

# ============= ONE DIMENSIONAL SLICING ==============
a = np.array([10, 20, 30, 40, 50])

print(a)
print(a[0])
print(a[-1])
print(a[2:])
print(a[3:5])
print(a[1::2])
print(a[::-1])

# ============= TWO DIMENSIONAL SLICING ==============

a = np.array([
    [1,2,3],
    [5,6,7],
    [8,9,10]
])

print(a[:2,:2])
print(a[:1,::-1])
print(a[::-1,::-1])
print(a[:0:-1 ,::-1])
print(a[:2,1:])


