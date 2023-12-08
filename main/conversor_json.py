import csv

with open('../files/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

import json

def escrever_arquivo_json(data,caminho_arquivo):
    # Dados a serem escritos no arquivo JSON
    dados_json=[]
    for row in data:
        dados_json.append(row)

    with open(caminho_arquivo, 'w') as arquivo:
        # Escreve os dados no arquivo JSON
        json.dump(dados_json, arquivo, indent=2)

    print(f"Arquivo JSON '{caminho_arquivo}' criado com sucesso!")

