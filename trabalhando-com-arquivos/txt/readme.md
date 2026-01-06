# TXT (Text Files)

Arquivos **TXT** são arquivos de texto puro, sem formatação especial.

São úteis para armazenar **logs**, listas simples, rascunhos, mensagens, ou qualquer conteúdo textual básico.

Por serem muito simples, são amplamente usados para **input/output rápidos** em pipelines de dados.

---

## Lendo um arquivo TXT completo

```python
with open('./dados_txt/file_1.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

## Lendo um TXT linha por linha

```python
with open('./dados_txt/file_2.txt', 'r') as arquivo_multilinha:
    conteudo_multilinha = arquivo_multilinha.read().splitlines()

    for linha in conteudo_multilinha:
        print(linha.upper())

```

`splitlines()` separa o conteúdo em uma lista, onde cada item é uma linha.

## Escrevendo em um arquivo TXT

```python
with open('./dados_txt/file_3.txt', 'w') as arquivo_3:
    arquivo_3.write('Hello World!')

```

A opção `'w'` sobrescreve o arquivo caso ele já exista.
