import os
import pandas as pd

files = os.listdir('Files')
print(files)

total_data_points = 0

for file in files:
    data = pd.read_csv('Files/' + file)
    print(file, 'has', data.shape)
    total_data_points += data.shape[0] * data.shape[1]

print('Total data points:', total_data_points)