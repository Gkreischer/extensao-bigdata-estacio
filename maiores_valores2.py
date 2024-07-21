import pandas as pd
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

# Convertendo dias_maiores_valores para uma lista de datetime.date
dias_maiores_valores = list(dias_maiores_valores)

# Filtrando soma_por_dia para incluir apenas os dias com os maiores valores
soma_maiores_valores = soma_por_dia[soma_por_dia.index.get_level_values(1).isin(dias_maiores_valores)]

# Resetando o índice para facilitar o acesso aos dados
soma_maiores_valores = soma_maiores_valores.reset_index()

# Plotando o gráfico de barras com barras mais largas
plt.figure(figsize=(12, 6))
bars = plt.bar(soma_maiores_valores['datalanc'], soma_maiores_valores['valor'], color='blue', width=0.8)

# Adicionando rótulos para os valores nas barras
for bar, valor, data in zip(bars, soma_maiores_valores['valor'], soma_maiores_valores['datalanc']):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{data.day}-{data.month}-{data.year}\n{valor}', 
             ha='center', va='bottom')

plt.title('Maiores Valores por Dia')
plt.xlabel('Data')
plt.ylabel('Soma dos Valores')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
