import pandas as pd

# Import CTD bottles
df0 = pd.read_csv('data/ctd-bottles-variants/00-ctd-bottles-2-1.csv', na_values=-999)

df1 = pd.read_csv('data/ctd-bottles-variants/01-ctd-bottles-2-1.csv',
                  na_values=-999,
                  skiprows=3)

df2 = pd.read_csv('data/ctd-bottles-variants/02-ctd-bottles-2-1.csv',
                  na_values=-999,
                  encoding ='cp1252')

df3 = pd.read_csv('data/ctd-bottles-variants/03-ctd-bottles-2-1.csv',
                  na_values=-999,
                  skiprows=3,
                  sep = ',',
                  encoding ='cp1252')

df4 = pd.read_table('data/ctd-bottles-variants/04-ctd-bottles-2-1.txt',
                  na_values=-999,
                  sep='\t',
                  skiprows=3)

df5 = pd.read_excel('data/ctd-bottles-variants/05-ctd-bottles-2-1.xlsx',
                  na_values=-999,
                  skiprows=3)


# Plot salinity profile
df0.plot.scatter('salinity', 'depth')
df1.plot.scatter('salinity', 'depth')
df2.plot.scatter('salinity', 'depth')
df3.plot.scatter('salinity', 'depth')
df4.plot.scatter('salinity', 'depth')
df5.plot.scatter('salinity', 'depth')
