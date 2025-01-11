import pandas as pd

network_puf_1 = '../../Data/2023/Network_PUF.csv'
network_puf_2 = '../../Data/2022/Network_PUF.csv'
network_puf_3 = '../../Data/2021/Network_PUF.csv'
network_puf_4 = '../../Data/2020/Network_PUF.csv'
network_puf_5 = '../../Data/2019/Network_PUF.csv'
network_puf_6 = '../../Data/2018/Network_PUF.csv'
network_puf_7 = '../../Data/2017/Network_PUF.csv'
network_puf_8 = '../../Data/2016/Network_PUF.csv'
network_puf_9 = '../../Data/2015/Network_PUF.csv'
network_puf_10 = '../../Data/2014/Network_PUF.csv'

df1 = pd.read_csv(network_puf_1)
df2 = pd.read_csv(network_puf_2)
df3 = pd.read_csv(network_puf_3)
df4 = pd.read_csv(network_puf_4)
df5 = pd.read_csv(network_puf_5)
df6 = pd.read_csv(network_puf_5)
df7 = pd.read_csv(network_puf_5)
df8 = pd.read_csv(network_puf_5)
df9 = pd.read_csv(network_puf_5)
df10 = pd.read_csv(network_puf_5)
BigD = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0) 
BigD.to_csv('../../Data/ConcatedData/Network_PUF.csv')