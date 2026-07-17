import numpy as np

# ========= ARRANGE METHOD ==========

arr = np.arange(2,10)
print(arr)
arr = np.arange(0,11,2)
print(arr)

# ======== RANDOM ARRAYS ============

arr = np.random.rand(2,10,2)
print(arr)
arr = np.random.randint(2,10,5)
print(arr)

# ======== SHAPE =========

a = np.array([[[1,2,3]],[[2,3,4,]],[[6,7,8]]])
print(a)
print(a.shape)
print(a.ndim)

# ====== ReShape ========

a = np.random.randint(0,15,10).reshape(-1,2)
print(a)


# ======= FLATTEN ========
a = np.arange(10).reshape(2,-1)

print(a)

a = a.flatten()

print(a)