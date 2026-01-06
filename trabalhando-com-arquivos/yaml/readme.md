# YAML (YAML Ain't Markup Language)

O **YAML** é semelhante ao JSON, mas mais legível e organizado.

Muito utilizado em **arquivos de configuração**, como:

- Docker
- Kubernetes
- Pipelines de Cloud

A sintaxe é baseada em **indentação**, tornando os arquivos mais “humanos” e fáceis de ler.

É ideal para descrever **estruturas e parâmetros** de forma clara.

---

## Lendo um arquivo YAML

```python
!pip install pyyaml

import yaml

with open('./dados_yaml/file_1.yaml', 'r') as arquivo_yaml:
    try:
        dados = yaml.load(arquivo_yaml, Loader=yaml.FullLoader)
        print(dados)
    except Exception as erro:
        print(f"erro: {erro}")
```

O `yaml.load()` converte o YAML em **dicionário Python**.
O `Loader=yaml.FullLoader` garante segurança e compatibilidade com estruturas complexas.

---

## Escrevendo um arquivo YAML

```python
dados = {
    'list': [1, 42, 3.141, 1337, 'help'],
    'string': 'bla',
    'dict': {
        'foo': 'bar',
        'key': 'value',
        'bar': 50
    }
}

with open('./dados_yaml/dados.yaml', 'w') as yaml_gravado:
    yaml.dump(dados, yaml_gravado)

```

O `yaml.dump()` converte um **dicionário Python** em YAML e salva em arquivo.
