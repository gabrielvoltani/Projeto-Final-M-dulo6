# Projeto final G3: conversor de arquivos
Este repositório contém os scripts para o projeto do Módulo 6 de Git e Versionamento de dados da trilha de dados da Ada feito pelo grupo 3. O grupo é composto por:

* Anthony Zaneta Mattos de Avila
* Thaís De Souza Marins
* Luiz Gustavo Nogueira Silva
* Gabriel Voltani Vatanabe
* Jonas Henrique Arjona Gonçalves Vieira

Os scripts desse repositório repositório criam um conversor de arquivos CSV em um dos três formatos suportados: XML, JSON ou YAML.

# Como executar esse repositório?
Primeiro, instale os pacotes necessários usando o `requirements.txt`. 

```python
pip install -r requirements.txt
```

As bibliotecas que foram usadas e precisam ser importadas são:

```python
import csv
import xml
import json
import yaml
import argparse
```

Os scripts iniciados com `conversor_` são os respectivos arquivos de cada formato de saída: XML, JSON ou YAML. O script `gerador-nf.py` atua como um intermediador dos formatos. Usamos ele para fazer a conversão através do CMD.

Navegamos na linha de comando até a pasta `main` e executamos o seguinte comando:

```
python gerador-nf.py <FORMATO_ESCOLHIDO_DE_SAIDA> <ENDERECO_DO_CSV>
```

Dentro da própria pasta `files` teremos o arquivo convertido no formato escolhido.

É importante mencionar que caso façamos a conversão de mais de um arquivo para o mesmo formato a saída da primeira conversão será substituída pela saída da segunda conversão. Os arquivos de um mesmo formato são salvos todos com o mesmo nome.

# Como contribuir?
Um ponto ainda precisa ser melhorado:

* Poderíamos modificar cada um dos scripts conversores para dinamicamente selecionar o nome dos arquivos, de forma que as saídas não se sobrescrevessem. Isso seria feito checando a quantidade de arquivos do formato selecionado e sempre adicionando um número ao final dos nomes.