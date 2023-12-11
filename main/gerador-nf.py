import conversor_xml as conv_xml
import conversor_json as conv_json
import conversor_yaml as conv_yaml

import argparse
import csv

#cria o parser de comandas do cmd
parser = argparse.ArgumentParser(
                    prog='Gerador-NF',
                    description='Gera NF em XML, JSON e YAML',
                    epilog='Passe o formato da saída desejado')

#adiciona argumentos obrigatorios
parser.add_argument('formato',action='store')
parser.add_argument('path',action='store')

#inicializa a listagem dos argumentos
args = parser.parse_args()

#armazena o valor do argumento formato numa variavel
formato = args.formato

#armazena o valor do argumento formato numa variavel
caminho = args.path

#abre arquivo csv selecionado 
with open(caminho, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

#condicional que lê o formato e seleciona qual das funções aplicar
if formato=='json':
    conv_json.escrever_arquivo_json(data,'../files/saida_json.json')
elif formato=='xml':
    conv_xml.escrever_arquivo_xml(data,'../files/saida_xml.xml')
elif formato=='yaml':
    conv_yaml.escrever_arquivo_yaml(data,'../files/saida_yaml.yaml')
else:
    print('formato nao suportado')
