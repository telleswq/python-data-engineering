"""
Exemplos práticos de leitura e escrita de arquivos XML
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Leitura de XMLs estruturados (ex: notas fiscais, integrações)
- Acesso a atributos e textos
- Conversão de dicionário Python para XML
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from dicttoxml import dicttoxml

# ----------------------------------
# Configuração de diretórios
# ----------------------------------
base_path = Path("./dados_xml")
base_path.mkdir(exist_ok=True)

arquivo_leitura = base_path / "file_1.xml"
arquivo_escrita = base_path / "novo_piloto.xml"

# ----------------------------------
# Preparação de um XML de exemplo
# ----------------------------------
xml_exemplo = """<?xml version="1.0" encoding="UTF-8"?>
<temporada>
    <corrida nome="GP Brasil">
        <item id="1">Lewis Hamilton</item>
        <item id="2">Max Verstappen</item>
    </corrida>
    <corrida nome="GP Monaco">
        <item id="3">Charles Leclerc</item>
        <item id="4">Lando Norris</item>
    </corrida>
</temporada>
"""

arquivo_leitura.write_text(xml_exemplo, encoding="utf-8")

# ----------------------------------
# 1. Lendo um arquivo XML
# ----------------------------------
arvore = ET.parse(arquivo_leitura)
raiz = arvore.getroot()

print("Elemento raiz:", raiz.tag)

for elemento in raiz:
    corrida_nome = elemento.attrib.get("nome")
    print("Corrida:", corrida_nome)

    for sub_elemento in elemento.findall("item"):
        print("Atributos:", sub_elemento.attrib)
        print("Texto:", sub_elemento.text)

# ----------------------------------
# 2. Convertendo dicionário para XML
# ----------------------------------
novo_piloto = {
    "name": "Gabriel Telles",
    "team": "McLaren",
    "nationality": "Brazilian"
}

xml_convertido = dicttoxml(novo_piloto)

with open(arquivo_escrita, "w", encoding="utf-8") as arquivo:
    arquivo.write(xml_convertido.decode("utf-8"))

print("Arquivo XML criado com sucesso:", arquivo_escrita)
