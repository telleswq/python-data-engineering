# Dict Comprehension

O **Dict Comprehension** permite criar ou transformar dicionários de forma mais simples, rápida e elegante — semelhante ao List Comprehension, mas aplicado a pares **chave: valor**.

---

### Exemplo tradicional (sem dict comprehension)

```python
piloto = {
    'classe': 'formula 1',
    'nome': 'Lewis Hamilton',
    'nacionalidade': 'Britânico',
    'equipe': 'Mercedes'
}

piloto_valor_upper = {}

for chave, valor in piloto.items():
    piloto_valor_upper[chave] = valor.upper()

piloto_valor_upper

```

### Usando Dict Comprehension (forma mais simples)

```python
piloto_valor_upper_comprehension = {
    chave: valor.upper()
    for chave, valor in piloto.items()
}

piloto_valor_upper_comprehension

```

### Estrutura geral

```python
{ chave_expressao: valor_expressao for chave, valor in iterável if condição }

```

### No exemplo acima:

- **chave_expressão:** `chave`
- **valor_expressão:** `valor.upper()`
- **iterável:** `piloto.items()`

---

O Dict Comprehension deixa o código mais direto, reduzido e fácil de entender quando você domina o padrão.
