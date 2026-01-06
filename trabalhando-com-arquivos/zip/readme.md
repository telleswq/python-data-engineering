# ZIP

Arquivos **ZIP** servem para **compactar** um ou vários arquivos, reduzindo tamanho e facilitando transporte.

Em **Engenharia de Dados**, é comum receber datasets compactados para:

- economizar espaço
- agilizar transferência de dados

Para processar os arquivos dentro de um ZIP, é necessário **descompactar** primeiro.

---

## Extraindo arquivos de um ZIP

```python
import zipfile

with zipfile.ZipFile('./dados_zip/files_1.zip') as zipp:
    zipp.extractall('./dados_zip/unzip')
```

O método `extractall()` descompacta todos os arquivos para a pasta especificada.

---

## Criando um arquivo ZIP

```python
import shutil

# Destino, Formato, Pasta (conteúdo a ser zipado)
shutil.make_archive('./dados_zip/pasta_zipada.zip', 'zip', './dados_zip/to_zip')

```

O `shutil.make_archive()` cria um arquivo ZIP a partir de uma pasta inteira.
