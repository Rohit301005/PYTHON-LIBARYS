# np.isinf(array) 10^10000
# 1/0

import numpy as np
arr = np.array([1,2,3,np.inf, 34,-np.inf,90])
print(np.isinf(arr))