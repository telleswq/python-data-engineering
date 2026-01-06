# XML (Extensible Markup Language)

Usado bastante em **notas fiscais**, o **XML** é um formato marcado, parecido com o HTML, utilizado para representar **dados estruturados**.

Embora seja mais verboso, ele ainda é muito comum em:

- sistemas legados
- integrações corporativas
- documentos padronizados
- comunicação entre serviços governamentais

O XML é ideal quando você precisa de:

- **estrutura rígida**
- **validação**
- **padronização do formato**

---

## Lendo um arquivo XML

```python
import xml.etree.ElementTree as ET

arvore = ET.parse('./dados_xml/file_1.xml')
raiz = arvore.getroot()
raiz

for elemento in raiz:
    for sub_elemento in elemento.findall('item'):
        print(sub_elemento.attrib)
        print(sub_elemento.text)

```

Este método percorre os elementos e permite acessar atributos e textos do XML.

## Convertendo um dicionário para XML

```python
!pip install dicttoxml

import dicttoxml

novo_piloto = {
    'name': 'Gabriel Telles',
    'team': 'McLaren',
    'nationality': 'Brazilian'
}

xml = dicttoxml.dicttoxml(novo_piloto)

with open('./dados_xml/novo_piloto.xml', 'w') as f:
    f.write(str(xml, 'utf-8'))

```

Aqui, o dicionário Python é convertido para XML e salvo em um novo arquivo.
