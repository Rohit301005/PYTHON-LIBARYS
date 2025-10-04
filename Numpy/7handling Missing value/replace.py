import numpy as np
arr = np.array([1,2,3,np.inf, 34,-np.inf,90])
print(np.isinf(arr))

cleand = np.nan_to_num(arr, posinf = 100, neginf= 5)
print(cleand)