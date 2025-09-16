import pandas_module as mp

# Load CSV
df = mp.readfile("example_file(emp).csv")

# Show first rows
df.show()

# Access column
print(df["salary"])

# Access row
print(df[2])   # 3rd row

# Access cell
print(df[2]["name"])

# Modify column
df["bonus"] = [1000, 2000, 3000, 4000, 5000]

# Modify cell
df[2]["salary"] = 75000

# Save file
df.save_to_file("updated_emps.csv")

# Aggregations
print("Total Salary:", df["salary"].sum())
print("Max Salary:", df["salary"].max())
print("Min Salary:", df["salary"].min())
