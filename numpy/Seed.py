import numpy as np

n= 5
while n:
    a = np.random.rand(1)
    print("New Array : ",a)
    n-=1

n= 5
np.random.seed(3)
while n:
    a = np.random.rand(1)
    print("Values Change at Every 3 time : ",a)
    n-=1