import pandas as pd
import matplotlib.pyplot as plt

rate_puf = pd.read_csv('DataScience2025/Files/Rate_PUF.csv', usecols=['RatingAreaId', 'IndividualRate', 'IndividualTobaccoRate'])

tobacco_data = rate_puf.dropna()

plt.figure(figsize=(10, 6))

plt.boxplot(tobacco_data['IndividualRate'], positions=[1], widths=0.4, patch_artist=True,
            boxprops=dict(facecolor='skyblue', color='blue'), medianprops=dict(color='blue'))

plt.boxplot(tobacco_data['IndividualTobaccoRate'], positions=[2], widths=0.4, patch_artist=True,
            boxprops=dict(facecolor='lightcoral', color='red'), medianprops=dict(color='red'))

plt.xticks([1, 2], ['Non-Tobacco Users', 'Tobacco Users'], fontsize=12)
plt.title('Impact of Tobacco Use on Premiums', fontsize=16)
plt.ylabel('Premium Rate', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()