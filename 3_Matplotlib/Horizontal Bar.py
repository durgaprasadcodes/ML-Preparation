import matplotlib.pyplot as plt
import numpy as pd

months = ['Jan','Feb','Mar','Apr','May','Jun']
sales  = [2500,3000,3500,2000,1500,2500]

plt.title("Monthly Sales")
plt.barh(months,sales,label='Sales')
plt.legend()
plt.show()