# get row numbers of numpy array if any element is having larger value than a specified value

import numpy as np
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr.shape, arr)

x =3
new_arr = np.any(arr > x, axis=1)
print(new_arr)

Arr = np.where(np.any(arr > x, axis=1))
print(Arr)



