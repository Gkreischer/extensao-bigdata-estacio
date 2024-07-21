import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo .csv
df = pd.read_csv('caixa1.csv')

# Convertendo a coluna 'datalanc' para o formato datetime
df['datalanc'] = pd.to_datetime(df['datalanc'])

# Criando uma coluna para o ano e mês
df['ano_mes'] = df['datalanc'].dt.to_period('M')

# Agrupando por ano e mês e calculando a soma dos valores
soma_por_mes = df.groupby('ano_mes')['valor'].sum()

# Plotando o gráfico de barras com barras mais largas
plt.figure(figsize=(12, 6))
bars = plt.bar(soma_por_mes.index.astype(str), soma_por_mes.values, color='blue', width=0.8)

# Adicionando rótulos para os totais nas barras
for bar, valor in zip(bars, soma_por_mes.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{valor:.2f}', 
             ha='center', va='bottom')

plt.title('Soma Total dos Valores por Mês')
plt.xlabel('Ano-Mês')
plt.ylabel('Soma dos Valores')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
