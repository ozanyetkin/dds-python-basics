import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read from CSV
df = pd.read_csv("data.csv")

# Drop the name column
df = df.drop(columns=["Name"])

# Fill the missing value in age with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill the missing value in income with the mean
df["Income"] = df["Income"].fillna(df["Income"].mean())

# Use one hot encoding for the Gender column
encoder = OneHotEncoder()
df_encoded = (
    encoder.fit_transform(df["Gender"].values.reshape(-1, 1)).toarray().astype(int)
)
df["Gender_F"] = df_encoded[:, 0]
df["Gender_M"] = df_encoded[:, 1]

# Use one hot encoding for the Country column
encoder_country = OneHotEncoder()
df_encoded_country = (
    encoder_country.fit_transform(df["Country"].values.reshape(-1, 1))
    .toarray()
    .astype(int)
)
for i, category in enumerate(encoder_country.categories_[0]):
    df["Country_" + category] = df_encoded_country[:, i]

df.drop(columns=["Gender", "Country"], inplace=True)

# Convert the "Yes" and "No" values in the "Purchased" column to 1 and 0
df["Purchased"] = df["Purchased"].map({"Yes": 1, "No": 0})

print(df)

# Assign "Purchased" to y and the rest to X
y = df["Income"]
X = df.drop(columns=["Income"])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Actual:", y_test.values)