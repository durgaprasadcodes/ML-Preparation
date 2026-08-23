import numpy as np

a = np.array([[91,90,88,89,67,64,58,85],[6,7,89,56,46,37,99,49]])

sorted_data = np.sort(a).flatten()

print(sorted_data)

new_arr = sorted_data[sorted_data>80]

print(new_arr)

new_arr = sorted_data[sorted_data<80]

print(new_arr)

new_arr = sorted_data[sorted_data==89]

print(new_arr)

new_arr = sorted_data[sorted_data<75]

print(new_arr)

