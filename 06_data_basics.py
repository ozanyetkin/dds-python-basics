import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, None, 35, 45, 20],
        "Gender": ["F", "M", "M", "M", "F"],
        "Income": [50000, 60000, None, 80000, 55000],
        "Country": ["US", "UK", "UK", "US", "US"],
        "Purchased": ["Yes", "No", "Yes", "No", "Yes"],
    }
)
