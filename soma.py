import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo .csv
df = pd.read_csv('caixa1.csv')

# Convertendo a coluna 'datalanc' para o formato datetime
df['datalanc'] = pd.to_datetime(df['datalanc'])

# Agrupando por data e calculando a soma dos valores
soma_por_dia = df.groupby(df['datalanc'].dt.date)['valor'].sum()

# Plotando o gráfico
plt.figure(figsize=(10, 6))
soma_por_dia.plot(kind='line', marker='o')
plt.title('Soma dos Valores Lançados por Dia')
plt.xlabel('Data')
plt.ylabel('Soma dos Valores')
plt.grid(True)
plt.show()