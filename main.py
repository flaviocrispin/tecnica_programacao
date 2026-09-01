import pandas as pd

#criar um dataframe a partir de um arquivo CSV
df = pd.read_csv(r"DimCustomer.csv")
#imprimir as primeiras linhas do dataframe
print (df.head())