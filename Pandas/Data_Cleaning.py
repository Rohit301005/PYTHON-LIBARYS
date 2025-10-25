import pandas as pd 

# data_cleaning = the process fixing/removig
#                 incomplete,incorret or irrelvent data
#                 ~75% of work done in pandas is data cleaning


df = pd.read_csv("PYTHON-LIBARYS\Pandas\import_and_selection\data.csv")

# Drop irrelevent data

# df = df.drop(columns=["Legendary"])
# print(df)

# Handling missing data

# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Typ2" : "None"})
# print(df.to_string())

# fix inconsistance value
# df["Type1"] = df["Type1"].replace({"Grass" : "GRASS"})
# print(df.to_string())

# standarize value
# df["Name"] = df["Name"].str.lower()
# print(df)

# fix datatype
# df["Legendary"] = df["Ledendary"].astype(bool)
# print(df)

# remove duplicate value
# df = df.drop_duplicates()
# print(df)