import pandas as pd
import matplotlib.pyplot as plt 

rate_puf = pd.read_csv('DataScience2025/Files/Rate_PUF.csv', usecols=['Age', 'IndividualRate', 'IndividualTobaccoRate'])

age_premium_data = rate_puf.groupby('Age')[['IndividualRate', 'IndividualTobaccoRate']].mean().reset_index()

age_premium_data['Age'] = pd.to_numeric(age_premium_data['Age'], errors='coerce')

age_premium_data = age_premium_data.sort_values(by='Age')

plt.figure(figsize=(15, 10))

plt.plot(age_premium_data['Age'], age_premium_data['IndividualRate'], label='Non-Tobacco Users', marker='o')
plt.plot(age_premium_data['Age'], age_premium_data['IndividualTobaccoRate'], label='Tobacco Users', marker='o')

plt.title('Premium Variation by Age', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Average Premium Rate', fontsize=14)
plt.legend(title='User Type', fontsize=12)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()