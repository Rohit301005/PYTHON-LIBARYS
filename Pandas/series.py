import pandas as pd

# Series = A Pandas 1-Dimensional labled array that can hold any datatype
#          Think of it like a single column in a spredsheet (1-Demensional)

data =  [100,10,200,23,500]
#series = pd.Series(data) #default index
series = pd.Series(data , index=["a","b","c","d","e"])
# print(series) 
# print(series.loc["b"]) #loc is used by labled location
# series.loc["c"] = 400
# print(series)
# print(series.iloc[0]) #iloc is used for integer location
# print(series[series>= 200]) #flitering value