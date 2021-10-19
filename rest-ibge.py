#%%
# Importações das Bibliotecas:
import json
import requests
import pandas as pd

# Requisição da API e Formatação:
response = requests.get(r'https://servicodados.ibge.gov.br/api/v1/localidades/estados/')
estados = json.loads(response.content)

# Contagem de Estados:
estados_dict = {}

for estado in estados:
    regiao = estado['regiao']['nome']
    if regiao not in estados_dict:
        estados_dict[regiao] = 1
    else:
        estados_dict[regiao] += 1

# Reformatação do dicionário:
df = pd.DataFrame(list(estados_dict.items()), columns=['Região', 'Qtd. Estados'])
df = df.set_index('Região')

# Arquivação como CSV (Separador: Pipe -> |)
df.to_csv('csv/estados.csv', sep='|')
