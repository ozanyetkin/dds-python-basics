import pandas as pd

df = pd.DataFrame(
    {"Name": ["Alice", "Bob", "Charlie", "David"], "Age": [25, None, 30, None]}
)
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

df = pd.DataFrame({"customer_id": [1, 2, 3], "review_text": ["Great!", "", None]})
filtered_df = df[df["review_text"].notnull() & (df["review_text"] != "")]
print(filtered_df)

df = pd.DataFrame({"Name": ["Alice", "Bob", "Bob", "David"], "Age": [25, 30, 30, 40]})

# Remove duplicate rows
df_cleaned = df.drop_duplicates()
print(df_cleaned)

df = pd.DataFrame({"City": ["New York", "new york", "NY", "Los Angeles"]})
df["City"] = df["City"].str.lower()
print(df)

df = pd.DataFrame({"Income": [30000, 32000, 31000, 1200000]})
Q1 = df["Income"].quantile(0.25)
Q3 = df["Income"].quantile(0.75)
IQR = Q3 - Q1
df_filtered = df[(df["Income"] >= Q1 - 1.5 * IQR) & (df["Income"] <= Q3 + 1.5 * IQR)]
print(df_filtered)
