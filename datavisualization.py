import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import folium
"""
#plt.plot(5,5,'o')
#plt.xlabel('valor de x')
#plt.ylabel('valor de y')
#plt.title('figura')
#plt.show()

#plot with pandas
data = [{'india':8880,'china':5123},
        {'india':8670,'china':6682},
        {'india':8147,'china':3308},
        {'india':7338,'china':1863},
        {'india':5704,'china':1527}]

india_china_df= pd.DataFrame(data,index=['1980','1981','1982','1983','1984'])
#india_china_df.plot(kind='line')
#plt.show()

india_china_df['india'].plot(kind='hist')
plt.show()
"""
df = pd.read_excel('Canada.xlsx',
    skiprows=range(20),
    skipfooter=2)
#get info
#print(df.info())
#columns e index
colunas = df.columns.tolist()
indices = df.index.tolist()
#dimensoes
#print(df.shape)

df.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
#print(df.head())


df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df['Total'] = df.sum(axis=1)

#sumario do dataframe
#df.describe


#filtrando pela coluna
#df['nomeColuna']
#ou df[['nomeColuna','nomeColuna2']]

#print(df[['Country', 1980, 1981,1982,1983,1984,1985]])

#Filtrando pela linha ou indice
#df.loc('nomeColuna')
#df.iloc(1)#indice da coluna

#o indice padrao do dataset é numerico de acordo com o tamanho do arquivo
#para ajustar e tornar os nomes dos países como indíces, usar o seguinte:
df.set_index('Country', inplace=True)
#visualizando todos os dados do Japao
#print(df.loc['Japan'])
#para um ano especifico
#print(df.loc['Japan', 1985])

#parar evitar problema de ambiguidade com os dados, renomear as coluns numericas para Strings
df.columns = list(map(str, df.columns))
years = list(map(str, range(1980, 2014)))


#filtrando de acordo com um criterio
condicao = df['Continent'] == 'Asia'



#PLOTING
#print(plt.style.available)
plt.style.use(['seaborn-v0_8-dark'])
"""
#dados do Haiti
haiti = df.loc['Haiti',years]
haiti.index = haiti.index.map(int)
#haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

#Anotação no grafico
#plt.text(2000, 6000, '2010 Earthquake')

#Comparando
df_CI = df.loc[['India', 'China'], years]
df_CI = df_CI.transpose() #linhas viram colunas e colunas viram linhas
df_CI.index = df_CI.index.map(int)
df_CI.plot(kind='line')
"""
#plt.show()

#Tipos de graficos
"""
bar for vertical bar plots
barh for horizontal bar plots
hist for histogram
box for boxplot
kde or density for density plots
area for area plots
pie for pie plots
scatter for scatter plots
hexbin for hexbin plot
"""


#Area Plot
#Usado para representar dados acumulados ou porcentagens com o passar dos anos

df_area = df

#ordenando em ordem descendente pela coluna Total
df_area.sort_values(['Total'], ascending=False, axis=0, inplace=True)
#MATPLOTLIB PLOTA OS INDICES NOS EIXOS HORIZONTAIS
#para ajustar, usar o transpose. Assim, os anos ficarão na linha horizontal do gráfico e as quantidades ficarão na vertical
df_area_top5 = df_area.head()
df_area_top5 = df_area_top5[years].transpose()

""""
df_area_top5.plot(kind='area')
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()
"""

#histogram - representar a distribuição de frequencia em um dataset numérico
""""
df_histo = df['2013'].plot(kind='hist')
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()


#usando numpy
count,bin_edges = np.histogram(df['2013'])
df_histo = df['2013'].plot(kind='hist', xticks= bin_edges)
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()


#BarChart - usado para comparar os valores de uma variável em um determinado ponto no tempo
df_iceland= df.loc['Iceland', years]
df_iceland.plot(kind='bar')
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()


#pie charts
df_continents = df.groupby('Continent', axis=0).sum()
print(df_continents.head())
df_continents['Total'].plot(kind='pie')
plt.show()


#box-plot
df_japan = df.loc[['Japan'], years].transpose()
df_japan.plot(kind='box')
plt.show()


#scatter plot - verfifica a correlação entre duas variáveis
df_total = 1
df_total.plot(kind='scatter', x='year',y='total',)
plt.show()
"""
#waffle charts - mostrar progresso em direção a um objetivo
#word cloud
#seaborn - regression plots


#folium - creating maps
world_map = folium.Map(location=[56.130,-106.35],
                        zoom_start=4,
                        tiles='Stamen Toner')

#adding a marker
marker = folium.map.FeatureGroup()
marker.add_child(
    folium.features.CircleMarker(
        [51.25,-85.32], radius=5,
        color='red', fill_color='red'
    )
)
world_map.add_child(marker)
#world_map.save('world_map.html')

#cloropleth maps - mostra areas com cores diferentes, onde as cores são mais escuras de acordo com o seu valor 
#numerico



#dashboarding
#bibliotecas - Dash, Panel, Voila, Streamlit, bokeh, ipywidgets, bowtie, flask
#https://pyviz.org/dashboarding/
#https://www.theguardian.com/news/datablog/2013/mar/15/john-snow-cholera-map

#Plotly