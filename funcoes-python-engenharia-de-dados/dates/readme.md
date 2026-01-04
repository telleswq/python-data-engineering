# Dates

Manipular datas é parte essencial de qualquer pipeline — seja para particionamento, logs, janelas de processamento ou validações de qualidade dos dados. Aqui estão as funções mais usadas no dia a dia:

---

## **1. `import datetime`**

Pacote padrão do Python para trabalhar com datas, horas e operações temporais.

```python
import datetime

```

---

## **2. `datetime.date`**

Cria ou representa apenas a _data_ (sem hora).

```python
hoje = datetime.date.today()

```

---

## **3. `today()`**

Retorna a data atual.

Muito usado para carimbar partições (`/year=2025/month=11/day=25/`).

```python
hoje = datetime.date.today()

```

---

## **4. `datetime.datetime`**

Trabalha com data + hora.

Usado em logs, timestamp de eventos, auditoria de pipelines.

```python
agora = datetime.datetime.now()

```

---

## **5. Formatar data como string – `strftime()`**

Transforma objetos de data em textos formatados.

```python
agora.strftime("%Y-%m-%d %H:%M:%S")

```

Muito usado para nomear arquivos, partições e logs.

---

## **6. Converter string em data – `strptime()`**

Lê textos e transforma em datas.

```python
data = datetime.datetime.strptime("2025-11-25", "%Y-%m-%d")

```

Essencial para ingestão de CSV, JSON, logs e APIs.

---

## **7. `timedelta`**

Permite cálculos com datas: somar/subtrair dias, horas, minutos…

```python
ontem = datetime.date.today() - datetime.timedelta(days=1)

```

Útil para busca de arquivos “do dia anterior”, janelas de processamento, schedules etc.
