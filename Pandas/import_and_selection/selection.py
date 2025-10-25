import pandas as pd

df = pd.read_csv("PYTHON-LIBARYS\Pandas\import_and_selection\data.csv",index_col="Name")

# Selection by column

# print(df["Name"])
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name","Height","Weight"]])

# Selection by ROW/S
# print(df.loc["Pikachu" ,["Height", "Wieght"]])
print(df.loc["Pikachu"])
