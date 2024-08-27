import pandas as pd

# Carregar o CSV em um DataFrame
df = pd.read_csv('musicas.csv', delimiter='|')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Realizar operações básicas, se necessário
print(df.info())
print(df.describe())
