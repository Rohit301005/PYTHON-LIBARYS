import pandas as pd

df = pd.read_csv("PYTHON-LIBARYS\Pandas\import_and_selection\data.csv")
# Filetring = keeping the rows that matchs a condition

tall_pokemon =  df[df["Height"] >= 2]
print(tall_pokemon)