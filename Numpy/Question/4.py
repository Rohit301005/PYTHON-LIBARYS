#  how to remove a row in numpy array ehich contain null value

import numpy as np
arr = np.array([[10,5,2.5,6,890],
                [23,44,11,34,26],
                [78,34,np.nan, 233,1],
                [34,12,23,44,55]])
print(arr)
print(np.isnan(arr))
print(np.isnan(arr).any(axis=1))
print(arr[np.isnan(arr).any(axis=1)])