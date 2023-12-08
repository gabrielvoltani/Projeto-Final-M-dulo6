import csv
import xml.etree.ElementTree as ET

with open('../files/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

def escrever_arquivo_xml(data,caminho_arquivo):
    root = ET.Element('ListaDeProdutos')
    for row in data:
        item = ET.SubElement(root, 'produto')
        for key, value in row.items():
            child = ET.SubElement(item, key)
            child.text = value
    tree = ET.ElementTree(root)
    tree.write(caminho_arquivo)
    print(f"Arquivo XML '{caminho_arquivo}' criado com sucesso!")