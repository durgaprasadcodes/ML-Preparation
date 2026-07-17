import numpy as np

arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.argmin(arr))

# AXIS BASED AGGREGATION  [ axis=0 means column ,axis=1 means row]

print(np.sum(arr,axis=0))
print(np.mean(arr,axis=0))
print(np.std(arr,axis=0))
print(np.var(arr,axis=0))
print(np.min(arr,axis=0))
print(np.max(arr,axis=0))
print(np.argmax(arr,axis=0))
print(np.argmin(arr,axis=0))

print(np.sum(arr,axis=1))
print(np.mean(arr,axis=1))
print(np.sum(arr,axis=1))
print(np.mean(arr,axis=1))
print(np.std(arr,axis=1))
print(np.var(arr,axis=1))
print(np.min(arr,axis=1))
print(np.max(arr,axis=1))
print(np.argmax(arr,axis=1))
print(np.argmin(arr,axis=1))