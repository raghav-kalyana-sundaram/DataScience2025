import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('../../Business_Rules_PUF.csv')

# Extract the required variables
year = df['BusinessYear']
copay_tier1 = df['CopayTier1']
copay_tier2 = df['CopayTier2']
copay_out = df['CopayOUT']

# Create a scatter plot
plt.scatter(year, copay_tier1, label='Copay Tier 1')
plt.scatter(year, copay_tier2, label='Copay Tier 2')
plt.scatter(year, copay_out, label='Copay OUT')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Copay')
plt.title('Year vs Copay')

# Show legend
plt.legend()

# Show the plot
plt.show()
