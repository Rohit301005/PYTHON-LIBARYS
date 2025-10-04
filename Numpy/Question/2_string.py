# create a program to change a string element in a specified Numpy array to uppercase, lowercase,capitalise the first letter, title-case , or swapcase

import numpy as np
arr = np.array(["I", "am", "Rohit"])
print(type(arr))
print(arr.shape)

upper_arr = np.char.upper(arr)
print(upper_arr)

lower_arr = np.char.lower(arr)
print(lower_arr)

cap_arr = np.char.capitalize(arr)
print(cap_arr)

title_arr = np.char.title(arr)
print(title_arr)

swap_arr = np.char.swapcase(arr)
print(swap_arr)