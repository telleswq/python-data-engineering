# Strings

Quando trabalhamos com **pipelines**, **ETL** e **tratamento de dados**, manipular strings é praticamente inevitável. Aqui vão as funções essenciais que você realmente usa na prática:

---

## **1. `in` (contains implícito)**

Usado para verificar se um texto contém outro texto.

**Exemplo:**

```python
"error" in message

```

✔️ Útil para validação, filtros e regras de negócio.

---

## **2. `startswith()` / `endswith()`**

Verificam se a string começa ou termina com algo específico.

**Exemplo:**

```python
file_name.startswith("2025_")
file_name.endswith(".csv")

```

✔️ Muito usado para lidar com nomes de arquivos em blobs, datalakes, S3 etc.

---

## **3. `join()`**

Une uma lista de strings em um único texto.

**Exemplo:**

```python
",".join(lista)

```

✔️ Excelente para montar colunas, logs e formatos customizados.

---

## **4. `len()`**

Retorna o tamanho da string.

**Exemplo:**

```python
len(nome)

```

Usado em validações, qualidade de dados e limpeza.

---

## **5. `split()`**

Divide uma string em partes.

**Exemplo:**

```python
linha.split(",")

```

✔️ Muito usado em parsing, leitura de arquivos e pré-processamento.

---

## **6. f-strings (formatação moderna)**

A forma mais eficiente e legível de interpolar variáveis.

**Exemplo:**

```python
f"Arquivo processado: {file_name}"

```

Simplifica logs, prints e criação de mensagens para ETLs.
