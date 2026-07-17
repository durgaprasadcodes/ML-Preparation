import numpy as np

# =========== 1D array =============
a = np.array([1,2,3])

print(a)
print(a.size) 
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

# # =========== 2D Arrays ============

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)
print(a.size) 
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)


# =========== 3D Arrays ===========

a = np.array([
    [[1,2,3]],
    [[4,5,6]],
    [[7,8,9]]
])

print("Three Dimensionla Array : ",a)

print(a.ndim)
print(a.size)

# ========== ZEROS ARRAYS ===========

zeros = np.zeros(5)

zeros+=5
print(zeros)
a = zeros[0]
print(a,type(a))

# =========== ONES ARRAY ============ 

ones = np.ones((2,5))
print(ones)
a = ones[0]
print(a,type(a))

# ========== FULL ARRAY ============

full = np.full(5,10)

print(full)

full = np.full((3,3),5)
print(full)

#  ======= IDENTITY MATRIX =======

a = np.eye(5,5)
print(a)