import numpy as np
import time

n = 10_000_000
start_time = time.perf_counter()
py_list = [i for i in range(n)]
py_list = [i+5 for i in py_list]
end_time = time.perf_counter()

print( "Python List Process Time (CPU time)",end_time - start_time )

start_time = time.perf_counter()
np_array = np.arange(n)
np_array+=5
end_time = time.perf_counter()

print( "Numpy List Process Time (CPU time)",end_time - start_time )