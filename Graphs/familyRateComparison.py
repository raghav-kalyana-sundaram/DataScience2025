import pandas as pd
import matplotlib.pyplot as plt

rate_puf = pd.read_csv('DataScience2025/Files/Rate_PUF.csv', usecols=['Couple', 'PrimarySubscriberAndOneDependent', 'PrimarySubscriberAndTwoDependents', 'PrimarySubscriberAndThreeOrMoreDependents'])

family_tier_data = rate_puf.mean().reset_index()
family_tier_data.columns = ['FamilyTier', 'AverageRate']

plt.figure(figsize=(10, 15))
plt.bar(family_tier_data['FamilyTier'], family_tier_data['AverageRate'], color='skyblue')


plt.title('Average Premium Rates by Family Tier', fontsize=16)
plt.xlabel('Family Tier', fontsize=14)
plt.ylabel('Average Premium Rate', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()