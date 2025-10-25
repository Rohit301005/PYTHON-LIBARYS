import pandas as pd

# Series = A Pandas 1-Dimensional labled array that can hold any datatype
#          Think of it like a single column in a spredsheet (1-Demensional)

data =  [100,10,200]
series = pd.Series(data)
print(series)