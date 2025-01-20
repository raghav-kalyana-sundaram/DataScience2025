import pandas as pd

# Load the dataset
rate_puf = pd.read_csv('Rate_PUF_Modified.csv')

# Ensure the 'StateCode' column exists and modify every 200th row
if 'StateCode' in rate_puf.columns:
    rows_to_modify = range(0, len(rate_puf), 900)
    rate_puf.loc[rows_to_modify, 'StateCode'] = 'WA'

# Verify the changes
print(rate_puf.iloc[rows_to_modify][['StateCode']])

# Save the modified dataset
rate_puf.to_csv('Rate_PUF_Modified.csv', index=False)