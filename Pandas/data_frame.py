import pandas as pd

data  ={
    "Name":["Rohit","Akash","Shayani"],
    "Age":[20,19,19]
}

# df = pd.DataFrame(data) #default indexing
df = pd.DataFrame(data, index=["Emp 1","Emp 2", "Emp 3"]) 
# print(df)
# print(df.loc["Emp 2"])
# print(df.iloc[1])


# Add a new column 
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new row
new_rows = pd.DataFrame([{"Name" : "Bijit", "Age" : 20, "Job" : "Care Taker"}],
                    [{"Name" : "Uday", "Age" : 20, "Job" : "Badmashi"}] ,
                    index=["Emp 4", "Emp 5"])
df = pd.concat([df, new_rows])
print(df)