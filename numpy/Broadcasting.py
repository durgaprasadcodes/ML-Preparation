import numpy as np

a = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

b = np.array([
    [1],
    [2]
])

print(a.shape)
print(b.shape)

print(a*b)

# If (a,b) & (c,d) are the Shapes of Two Matrixes Then
#       Broadcasting Only Works on This Condition 
# (a == c or a == 1 or c == 1) and (b ==d or b == 1 or d == 1)