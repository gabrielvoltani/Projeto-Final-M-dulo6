import yaml

def escrever_arquivo_yaml(data,caminho_arquivo):
    # Dados a serem escritos no arquivo JSON
    dados_yaml=[]
    for row in data:
        dados_yaml.append(row)

    with open(caminho_arquivo, 'w') as arquivo:
        # Escreve os dados no arquivo yaml
        yaml.dump(dados_yaml, arquivo, default_flow_style=False)

    print(f"Arquivo yaml '{caminho_arquivo}' criado com sucesso!")