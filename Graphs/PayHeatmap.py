import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


rate_puf = pd.read_csv('Files/Rate_PUF.csv')
us_states = gpd.read_file('Geopandas/ne_110m_admin_1_states_provinces.shp')

us_states = us_states[us_states['iso_a2'] == 'US']

average_rates = rate_puf.groupby('StateCode')['IndividualRate'].mean().reset_index()
average_rates.columns = ['StateCode', 'IndividualRate']

state_boundaries = us_states.merge(average_rates, left_on='iso_3166_2', right_on='StateCode', how='left')
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
state_boundaries.plot(column='IndividualRate', cmap='OrRd', legend=True, ax=ax)
plt.title('Average Rate by State', fontsize=16)
plt.axis('off')
plt.show()