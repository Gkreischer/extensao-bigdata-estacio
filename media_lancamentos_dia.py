import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo .csv
df = pd.read_csv('caixa1.csv')

# Convertendo a coluna 'datalanc' para o formato datetime
df['datalanc'] = pd.to_datetime(df['datalanc'])

# Agrupando por data e calculando a média dos valores
media_por_dia = df.groupby(df['datalanc'].dt.date)['valor'].mean()

# Plotando o gráfico
plt.figure(figsize=(10, 6))
media_por_dia.plot(kind='line', marker='o')
plt.title('Média dos Valores Lançados por Dia')
plt.xlabel('Data')
plt.ylabel('Média dos Valores')
plt.grid(True)
plt.show()