import pandas as pd

# Read from CSV
df = pd.read_csv("data.csv")

# Drop the name column
df = df.drop(columns=["Name"])

# Fill the missing value in age with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill the missing value in income with the mean
df["Income"] = df["Income"].fillna(df["Income"].mean())

print(df)