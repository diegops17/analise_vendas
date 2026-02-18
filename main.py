import pandas as pd
import openpyxl

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)

    #O.any() significa que pega algum valor
    condicao = (tabela_vendas['Vendas'] > 49980).any()

    if condicao:
        #print(f'No mês de {mes} alguém bateu a meta de 49980')
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 49980, 'Vendedor'].values[0] #O .loc é para pegar uma linha
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 49980, 'Vendas'].values[0]

        print(f'No mês de {mes} o vendedor {vendedor}, total de vendas R$ {vendas} reais.')