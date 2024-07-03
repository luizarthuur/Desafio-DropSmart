import pandas as pd
import matplotlib.pyplot as plt
import calendar

arquivoexcel = 'impact-report Limpo.xlsx'

data = pd.read_excel(arquivoexcel)

data['Referral Date'] = pd.to_datetime(data['Referral Date'])

#Faturamento total nos anos de 2023 e 2024
faturamento_total = data.groupby('Sub Id 2')['Action Earnings'].sum()

# Visualizar os dados em um gráfico de barras
plt.figure(figsize=(12, 6))
ax = faturamento_total.plot(kind='bar', color='skyblue')
plt.title('Faturamento Total (somando 2023 e 2024) por Sub Id 2')
plt.xlabel('Sub Id 2')
plt.ylabel('Faturamento Total')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Adicionar rótulos de dados
for i in ax.containers:
    ax.bar_label(i, label_type='edge', padding=3)

# Mostrar o gráfico
plt.show()

dados_2024 = data[
    (data['Referral Date'].dt.year == 2024)]  

#Faturamento total em 2024
faturamento_total_2024 = dados_2024.groupby('Sub Id 2')['Action Earnings'].sum()

# Visualizar os dados em um gráfico de barras
plt.figure(figsize=(12, 6))
ax = faturamento_total_2024.plot(kind='bar', color='skyblue')
plt.title('Faturamento Total em 2023 por Sub Id 2')
plt.xlabel('Sub Id 2')
plt.ylabel('Faturamento Total')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Adicionar rótulos de dados
for i in ax.containers:
    ax.bar_label(i, label_type='edge', padding=3)

# Mostrar o gráfico
plt.show()

dados_previsao_2024 = data[
    (data['Referral Date'].dt.year == 2024) & 
    ((data['Event Type'] == 'Free Trial API') | (data['Event Type'] == 'Paid Trial API'))
]

faturamento_mensal_2024 = dados_2024.groupby(dados_2024['Action Date'].dt.month)['Action Earnings'].sum()

#Calculo da média de conversão em 2024
dados_totais_previsao_2024 = dados_previsao_2024.groupby(dados_previsao_2024['Action Date'].dt.month)['Action Id'].count()

dados_junho_2024 = data[
    (data['Referral Date'].dt.year == 2024) & 
    (data['Referral Date'].dt.month == 6) & 
    ((data['Event Type'] == 'Free Trial API') | (data['Event Type'] == 'Paid Trial API'))
]

dados_junho_2024_bruto = dados_junho_2024['Action Id'].count()


taxa_media_conversao_2024 = 0.2559

#Previsão de faturamento em Julho
previsao_faturamento_julho2024 =  dados_junho_2024_bruto * taxa_media_conversao_2024

plt.figure(figsize=(4, 4))
plt.text(0.5, 0.5, f'{previsao_faturamento_julho2024}', fontsize=36, ha='center')
plt.axis('off')  # Remove os eixos para um visual limpo
plt.title('Previsão de Faturamento para Julho de 2024')

# Mostrando o gráfico
plt.show()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

dados_2024['Referral Date'] = pd.to_datetime(dados_2024['Referral Date'])

# Agrupar os dados por mês e somar os valores de 'Action Earnings'
faturamento_mensal_2024 = dados_2024.groupby(dados_2024['Referral Date'].dt.month)['Action Earnings'].sum()

# Converter os índices numéricos para nomes de meses
meses = [calendar.month_name[i] for i in range(1, 7)]  # Janeiro a junho

# Atribuir os nomes dos meses ao índice da série
faturamento_mensal_2024.index = meses

# Visualizar os dados em um gráfico de barras
plt.figure(figsize=(12, 6))
faturamento_mensal_2024.plot(kind='bar', color='skyblue')
plt.title('Faturamento Mensal de Janeiro a Junho de 2024')
plt.xlabel('Mês')
plt.ylabel('Faturamento Total')
plt.xticks(rotation=45)
plt.tight_layout()

# Adicionar rótulos de dados
for i, v in enumerate(faturamento_mensal_2024):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

# Mostrar o gráfico
plt.show()

data_filtrado = data[data['Action Earnings'] > 0]

#Faturamento por país
faturamento_por_pais = data_filtrado.groupby('Customer Country')['Action Earnings'].sum()

# Ordenando os países pelo faturamento (do maior para o menor)
faturamento_por_pais = faturamento_por_pais.sort_values()

# Criando um gráfico estilo pirâmide (barras horizontais invertidas)
plt.figure(figsize=(10, 8))
plt.barh(faturamento_por_pais.index, faturamento_por_pais.values, color='skyblue')
plt.xlabel('Faturamento Total')
plt.ylabel('País')
plt.title('Faturamento por País')
plt.grid(axis='x')  # Adiciona linhas de grade apenas no eixo x
plt.gca().invert_yaxis()  # Inverte a ordem dos países para parecer uma pirâmide
plt.tight_layout()

# Mostrando o gráfico
plt.show()


#Quantidade de clientes por país
quantidade_clientes_por_pais = data_filtrado.groupby('Customer Country') ['Action Id'].count()

# Ordenando os países pela quantidade de clientes (do maior para o menor)
quantidade_clientes_por_pais = quantidade_clientes_por_pais.sort_values(ascending=True)

# Criando um gráfico estilo pirâmide para quantidade de clientes por país (barras horizontais invertidas)
plt.figure(figsize=(10, 8))
plt.barh(quantidade_clientes_por_pais.index, quantidade_clientes_por_pais.values, color='lightgreen')
plt.xlabel('Quantidade de Clientes')
plt.ylabel('País')
plt.title('Quantidade de Clientes por País')
plt.grid(axis='x')  # Adiciona linhas de grade apenas no eixo x
plt.gca().invert_yaxis()  # Inverte a ordem dos países para parecer uma pirâmide
plt.tight_layout()

# Mostrando o gráfico
plt.show()

status_gratuitos = data[(data['Event Type'] == 'Free Trial API') | (data['Event Type'] == 'Online Sale API')]


status_pagos = data[(data['Event Type'] == 'POS Pro Sale API') | (data['Event Type'] == 'Paid Trial API')]

#Status das licenças gratuitas
quantidade_status_gratuitos = status_gratuitos.groupby('Status') ['Event Type'].count()

# Criando um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(quantidade_status_gratuitos, labels=quantidade_status_gratuitos.index, autopct='%1.1f%%', startangle=200)
plt.title('Status das licenças Free Trial API e Paid Trial API')
plt.axis('equal')  # Mantém o gráfico de pizza circular
plt.tight_layout()

# Mostrando o gráfico
plt.show()

#Status das licenças pagas
quantidade_status_pagos = status_pagos.groupby('Status') ['Event Type'].count()

# Criando um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(quantidade_status_pagos, labels=quantidade_status_pagos.index, autopct='%1.1f%%', startangle=200)
plt.title('Status das licenças Online Sale API e POS Pro Sale API ')
plt.axis('equal')  # Mantém o gráfico de pizza circular
plt.tight_layout()

# Mostrando o gráfico
plt.show()
