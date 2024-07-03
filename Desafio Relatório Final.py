import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Carregar os dados
arquivoexcel = 'impact-report Limpo.xlsx'
data = pd.read_excel(arquivoexcel)
data['Referral Date'] = pd.to_datetime(data['Referral Date'])

# Faturamento total nos anos de 2023 e 2024
faturamento_total = data.groupby('Sub Id 2')['Action Earnings'].sum()

# Previsão de faturamento em julho de 2024
dados_junho_2024 = data[
    (data['Referral Date'].dt.year == 2024) & 
    (data['Referral Date'].dt.month == 6) & 
    ((data['Event Type'] == 'Free Trial API') | (data['Event Type'] == 'Paid Trial API'))
]
dados_junho_2024_bruto = dados_junho_2024['Action Id'].count()
taxa_media_conversao_2024 = 0.2559
previsao_faturamento_julho2024 = dados_junho_2024_bruto * taxa_media_conversao_2024

# Faturamento mensal de janeiro a junho de 2024
dados_2024 = data[data['Referral Date'].dt.year == 2024]
dados_2024['Referral Date'] = pd.to_datetime(dados_2024['Referral Date'])
faturamento_mensal_2024 = dados_2024.groupby(dados_2024['Referral Date'].dt.month)['Action Earnings'].sum()
meses = [calendar.month_name[i] for i in range(1, 7)]  # Janeiro a junho
faturamento_mensal_2024.index = meses

# Quantidade de clientes por país (removendo países sem valores)
data_filtrado = data[data['Action Earnings'] > 0]
quantidade_clientes_por_pais = data_filtrado.groupby('Customer Country')['Action Id'].count().sort_values()
quantidade_clientes_por_pais = quantidade_clientes_por_pais[quantidade_clientes_por_pais > 0]  # Remove países sem valores

# Status das licenças gratuitas
status_gratuitos = data[(data['Event Type'] == 'Free Trial API') | (data['Event Type'] == 'Online Sale API')]
quantidade_status_gratuitos = status_gratuitos.groupby('Status')['Event Type'].count()

# Status das licenças pagas
status_pagos = data[(data['Event Type'] == 'POS Pro Sale API') | (data['Event Type'] == 'Paid Trial API')]
quantidade_status_pagos = status_pagos.groupby('Status')['Event Type'].count()

# Criando a figura global e os subplots com tamanho menor
fig, axs = plt.subplots(3, 2, figsize=(14, 12))

# Gráfico 1: Faturamento Total por Sub Id 2
axs[0, 0].bar(faturamento_total.index, faturamento_total.values, color='skyblue')
axs[0, 0].set_title('Faturamento Total por Sub Id 2', fontsize=9, pad=20)
axs[0, 0].set_ylabel('Faturamento Total', labelpad=10)
axs[0, 0].tick_params(axis='x', rotation=45)
axs[0, 0].bar_label(axs[0, 0].containers[0], label_type='edge', padding=3)

# Gráfico 2: Previsão de Faturamento para Julho de 2024
axs[0, 1].text(0.5, 0.5, f'R${previsao_faturamento_julho2024:.2f}', fontsize=35, ha='center')
axs[0, 1].axis('off')
axs[0, 1].set_title('Previsão para Julho de 2024', fontsize=11, pad=10)

# Gráfico 3: Faturamento Mensal de Janeiro a Junho de 2024
axs[1, 0].bar(faturamento_mensal_2024.index, faturamento_mensal_2024.values, color='skyblue')
axs[1, 0].set_title('Faturamento Mensal Jan-Jun 2024', fontsize=9, pad=10)
axs[1, 0].set_xlabel('Mês', labelpad=-28)
axs[1, 0].set_ylabel('Faturamento Total', labelpad=10)
axs[1, 0].tick_params(axis='x', rotation=45)
for i, v in enumerate(faturamento_mensal_2024):
    axs[1, 0].text(i, v + 1, str(v), ha='center', va='bottom')

# Gráfico 4: Quantidade de Clientes por País (estilo pirâmide)
axs[1, 1].plot(quantidade_clientes_por_pais.index, quantidade_clientes_por_pais.values, marker='o', color='lightgreen')
axs[1, 1].set_title('Quantidade de Clientes por País', fontsize=9, pad=10)
axs[1, 1].set_xlabel('País', labelpad=10)
axs[1, 1].set_ylabel('Quantidade de Clientes', labelpad=10)
axs[1, 1].tick_params(axis='x', rotation=45)
axs[1, 1].grid(True)

# Gráfico 5: Status das Licenças Gratuitas (gráfico de pizza)
axs[2, 0].pie(quantidade_status_gratuitos, labels=quantidade_status_gratuitos.index, autopct='%1.1f%%', startangle=200)
axs[2, 0].set_title('Status Licenças Free e Paid Trial', fontsize=9, pad=1)

# Gráfico 6: Status das Licenças Pagas (gráfico de pizza)
axs[2, 1].pie(quantidade_status_pagos, labels=quantidade_status_pagos.index, autopct='%1.1f%%', startangle=200)
axs[2, 1].set_title('Status Licenças Online e POS Pro', fontsize=9, pad=1)

# Ajustando o layout geral
plt.tight_layout()

# Mostrando todos os gráficos na tela
plt.show()
