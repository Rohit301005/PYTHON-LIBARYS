# np.nan_to_num(array, nan = value) default = 0

import numpy as np
arr= np.array([1,2,np.nan,4,5,np.nan])
cleand = np.nan_to_num(arr)
print(cleand)
res = np.nan_to_num(arr, nan = 100)
print(res)