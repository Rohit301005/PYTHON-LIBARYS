import pandas as pd

#  aggregate function = reduce a set of value in a single summary value
#                       Used to summarize and analyse data
#                       Often used with groupby() function

df  = pd.read_csv("PYTHON-LIBARYS\Pandas\import_and_selection\data.csv")

# Whole DataFrame
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single column
# print(df["Height"].mean())


group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())
