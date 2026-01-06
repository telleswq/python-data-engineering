# JSON (JavaScript Object Notation)

O **JSON** é um formato estruturado baseado em pares **chave: valor**, muito utilizado em APIs, arquivos de configuração e comunicação entre sistemas.

Ele suporta **listas**, **dicionários** e estruturas **aninhadas**, permitindo representar dados complexos de maneira simples e legível.

---

## Lendo um arquivo JSON

```python
import json

with open('./dados_json/file_1.json') as arquivo_json1:
    dados = json.load(arquivo_json1)

type(dados)
dados
```

O `json.load()` converte o conteúdo do arquivo JSON para um **dicionário Python**.

## Acessando dados do JSON

```python
temporada = dados.get('season')
temporada

pilotos = dados.get('pilots')
pilotos

```

O método `.get()` acessa valores específicos pelas chaves, evitando erros caso a chave não exista.

## Escrevendo um novo arquivo JSON

```python
novo_piloto = {
    'name': 'Gabriel Telles',
    'team': 'McLaren',
    'nationality': 'Brazilian'
}

with open('./dados_json/novo_piloto.json', 'w') as arquivo_json2:
    json.dump(novo_piloto, arquivo_json2)

```

O `json.dump()` salva um dicionário Python como um arquivo JSON.
