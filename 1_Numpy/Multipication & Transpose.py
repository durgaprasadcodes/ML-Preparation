import numpy as np

a = np.array([[1,2,3,4,5],[2,3,6,2,1]])
b = np.array([[6,7,8,9,10],[4,5,7,4,9]])

print(a@b.T)

print(b.transpose())

# RULE
"""
     
     Matrix Multiplication Rule is = (m,n) @ (n,p)
     where m == n 

"""
 