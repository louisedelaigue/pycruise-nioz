import pandas as pd

# Import CTD bottles
df0 = pd.read_csv('data/ctd-bottles-variants/00-ctd-bottles-2-1.csv', 
                  na_values=-999)

df1 = pd.read_csv('data/ctd-bottles-variants/01-ctd-bottles-2-1.csv',
                  na_values=-999,
                  skiprows=3)

df2 = pd.read_csv('data/ctd-bottles-variants/02-ctd-bottles-2-1.csv',
                  na_values=-999,
                  skiprows=[1],
                  encoding ='cp1252')

df3 = pd.read_csv('data/ctd-bottles-variants/03-ctd-bottles-2-1.csv',
                  na_values=-999,
                  skiprows=[0, 1, 2, 4],
                  sep = ',',
                  encoding ='cp1252')

df4 = pd.read_table('data/ctd-bottles-variants/04-ctd-bottles-2-1.txt',
                  na_values=-999,
                  sep='\t',
                  skiprows=[0, 1, 2, 4])

df5 = pd.read_excel('data/ctd-bottles-variants/05-ctd-bottles-2-1.xlsx',
                  na_values=-999,
                  skiprows=[0,1,2,4])

df6 = pd.read_excel('data/ctd-bottles-variants/06-ctd-bottles-2-1.xlsx',
                  na_values=[-999, -777],
                  skiprows=[0,1,2,4])

df7 = pd.read_excel('data/ctd-bottles-variants/07-ctd-bottles-2-1.xlsx',
                  na_values=[-999, -777],
                  skiprows=[0,1,2,4])

df8 = pd.read_csv('data/ctd-bottles-variants/08-ctd-bottles-2-1.csv',
                  na_values=[-999, -777],
                  skiprows=[0,1,2,4],
                  skipfooter=3,
                  engine='python')

# Plot salinity profile
df0.plot.scatter('salinity', 'depth')
df1.plot.scatter('salinity', 'depth')
df2.plot.scatter('salinity', 'depth')
df3.plot.scatter('salinity', 'depth')
df4.plot.scatter('salinity', 'depth')
df5.plot.scatter('salinity', 'depth')
df6.plot.scatter('salinity', 'depth')
df7.plot.scatter('Practical salinity', 'Depth')
df8.plot.scatter('Practical salinity', 'Depth')
