import pandas as pd

df = pd.read_csv("C:/Projetos/ecommerce_estatistica.csv")
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(df.head())
print(df.info())