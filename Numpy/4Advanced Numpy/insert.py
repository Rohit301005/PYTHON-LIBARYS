"""
np.insert(array, index,value,axis=None)
array - original array
index-
value-
axis-
axis=0 row wise
axis= 1 column wise
"""

import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
new_arr = np.insert(arr , 2, 20)
print(new_arr)