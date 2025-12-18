import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df = pd.read_csv("C:/Projetos/ecommerce_estatistica.csv")

#Historigrama preços
hist_graphc = px.histogram(df, x="Preço", color="Temporada", opacity=0.5, barmode="group")
hist_graphc.update_layout(
    title = 'Quantidade de produtos por preço em cada temporada',
    xaxis_title = 'Preços',
    yaxis_title = 'Quantidade de produtos',
)

#Dispersão
scatter_graphc = px.scatter(df, x='Qtd_Vendidos_Cod', y='Desconto_MinMax', color="Preço")
scatter_graphc.update_layout(
    title = 'Quantidade de produtos vendidos pelo desconto',
    xaxis_title = 'Quantidade de Vendas',
    yaxis_title = 'Nivel de desconto',
)

#Mapa de calor
corr = df[['Preço', 'Qtd_Vendidos_Cod', 'Desconto', 'Marca_Cod', 'Temporada_Cod']].corr()
hot_graphc = px.imshow(corr, text_auto='.2f', zmax=-1, zmin=1, color_continuous_scale=px.colors.sequential.RdBu)
hot_graphc.update_layout(
    title = 'Mapa de correlação',
    xaxis_title = 'Variáveis',
    yaxis_title = 'Variáveis'
)

#Grafico de Barras
order_marca = df['Marca'].value_counts().index.tolist()
barr_graphc = px.bar(df, x='Marca', category_orders={'Marca':order_marca})
barr_graphc.update_layout(
    title = 'Popularidade de Marca',
    xaxis_title = 'Marca',
)

#Grafico pizza
pie_graphc = px.pie(df, names='Temporada', color='Temporada', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)
pie_graphc.update_layout(
    title = 'Porcentagem de produtos por temporada',
    legend_title = 'Temporadas',
)

#Grafico Densidade
density_graphc = px.histogram(df, x='Preço', histnorm='density')
density_graphc.update_layout(
    title = 'Densidade dos preços',
    xaxis_title = 'Valor',
    yaxis_title = 'Densidades',
)

#Grafico de regressão preço x vendas
regress_graphc = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod', trendline='ols')
regress_graphc.update_layout(
    title = 'Relação entre Preço e Quantidade de vendas',
    xaxis_title = 'Valor',
    yaxis_title= 'Quantidade vendido',
)

app = Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure = hist_graphc),
    dcc.Graph(figure= scatter_graphc),
    dcc.Graph(figure= hot_graphc),
    dcc.Graph(figure= barr_graphc),
    dcc.Graph(figure= pie_graphc),
    dcc.Graph(figure= density_graphc),
    dcc.Graph(figure= regress_graphc),
])

app.run(debug=True, port=8050)