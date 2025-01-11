import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('DataScience2025/Files/Business_Rules_PUF.csv')

# Extract the required variables
year = df['BusinessYear']
copay_tier1 = df['StateCode']
copay_tier2 = df['DependentMaximumAgRule']
copay_out = df['MedicalDentalIndicator']

# Create a scatter plot
plt.scatter(year, copay_tier1, label='State')
plt.scatter(year, copay_tier2, label='Maximum Age')
plt.scatter(year, copay_out, label='MedicalDentalIndicator')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Copay')
plt.title('Year vs Copay')

# Show legend
plt.legend()

# Show the plot
plt.show()
