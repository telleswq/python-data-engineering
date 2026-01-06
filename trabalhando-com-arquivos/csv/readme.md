# CSV(Comma-Separated Values)

O **CSV** é um dos formatos mais usados em Engenharia de Dados. Ele organiza informações em **linhas e colunas**, como uma planilha.

Cada **linha** representa um registro e cada **coluna** representa um campo.

É um formato:

- leve
- fácil de ler
- compatível com quase todas as ferramentas de dados
- ideal para integrar sistemas diferentes

---

## Lendo um arquivo CSV com `csv.DictReader`

```python
import csv

with open('./dados_csv/file_1.csv', 'r') as arquivo_csv:
    dados = csv.DictReader(arquivo_csv, delimiter=',')
    for linha in dados:
        print(f"valor: {linha}")
```

Este método transforma cada linha do CSV em um **dicionário**, usando o cabeçalho do arquivo como chave.

## Escrevendo um arquivo CSV com `csv.writer`

```python
dados_paises = [
    ['name', 'area', 'country_code2', 'country_code3'],
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
]

with open('./dados_csv/file_2.csv', 'w', encoding='UTF8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerows(dados_paises)

```

Aqui, criamos um CSV a partir de uma lista de listas.

Cada sublista corresponde a uma linha que será escrita no arquivo
