import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df = pd.read_csv("C:/Projetos/ecommerce_estatistica.csv")

print(df['Marca_Freq'])

#Histograma dos preços
plt.figure(figsize = (10,8))
sns.histplot(df, x='Preço', kde = True, hue = 'Temporada', element='step')
plt.title("Histograma de Preços por Temporada")
plt.xlabel("Preços")
plt.ylabel("Quantidade de produtos")
plt.show()

#Grafico de dispersão
plt.figure(figsize = (10,8))
sns.scatterplot(data=df, x='Qtd_Vendidos_Cod', y='Desconto_MinMax', s=40, alpha = 0.6)
plt.title("Relação entre Preço e Quantidade Vendida (Codificada)")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Descontos")
plt.grid(alpha = 0.3)
plt.show()

#Mapa de Calor
corr = df[['Preço', 'Qtd_Vendidos_Cod', 'Desconto', 'Marca_Cod', 'Temporada_Cod']].corr()
plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True, cmap='viridis')
plt.title("Mapa de Calor das Correlações")
plt.show()

#Grafico de Barras das Marcas
plt.figure(figsize = (10,8))
ordem_marcas = df['Marca'].value_counts().index
sns.countplot(df, x='Marca', order = ordem_marcas)
plt.title("Marcas")
plt.xticks(rotation = 90)
plt.show()

#Grafico de pizza das Temporadas
df['Temporada'].value_counts().plot(kind='pie', autopct = '%1.1f%%', figsize = (10,8), startangle = 90)
plt.xticks(rotation=45)
plt.ylabel('')
plt.title('Porcentagem de itens de cada Temporadas')
plt.show()

#Grafico Densidade Preço
plt.figure(figsize = (10,8))
sns.kdeplot(data=df, x='Preço', fill = True, cmap='viridis')
plt.title("Densidade dos Preços")
plt.show()

#Grafico de Regressão preço x vendas
plt.figure(figsize=(8,5))
sns.regplot(data=df, x='Preço', y='Qtd_Vendidos_Cod')
plt.title('Regressão Preço x Vendas')
plt.ylabel("Quantidade Vendida")
plt.show()