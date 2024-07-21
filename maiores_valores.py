import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



# Lendo o arquivo .csv
df = pd.read_csv('caixa1.csv')

# Convertendo a coluna 'datalanc' para o formato datetime
df['datalanc'] = pd.to_datetime(df['datalanc'])

# Criando uma coluna para o ano e mês
df['ano_mes'] = df['datalanc'].dt.to_period('M')

# Agrupando por data e calculando a soma dos valores
soma_por_dia = df.groupby(['ano_mes', df['datalanc'].dt.date])['valor'].sum()

# Encontrando os dias com os maiores valores por mês
dias_maiores_valores = soma_por_dia.groupby(level=0).idxmax().apply(lambda x: x[1])

# Plotando o gráfico
plt.figure(figsize=(12, 6))
soma_por_dia.index = soma_por_dia.index.droplevel(0)
plt.plot(soma_por_dia.index, soma_por_dia, marker='o', label='Valores Diários')

# Destacando os dias com os maiores valores
plt.scatter(dias_maiores_valores, soma_por_dia[dias_maiores_valores], color='red', zorder=5, label='Maior Valor por Mês')

# Adicionando rótulos para os dias com os maiores valores
for dia, valor in zip(dias_maiores_valores, soma_por_dia[dias_maiores_valores]):
    plt.annotate(f'{dia.day}-{dia.month}-{dia.year}\n{valor}', (dia, valor), textcoords="offset points", xytext=(0,5), ha='center')

plt.title('Soma dos Valores Lançados por Dia')
plt.xlabel('Data')
plt.ylabel('Soma dos Valores')
plt.grid(True)
plt.legend()
plt.show()
