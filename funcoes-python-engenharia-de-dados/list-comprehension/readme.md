# List Comprehension

A **List Comprehension** é uma forma mais simples, rápida e “Pythonica” de criar listas a partir de outras lista

### 👇 Exemplo tradicional (sem list comprehension)

```python
numeros = [1, 2, 3, 4, 5, 6]
numeros

numeros_ao_quadrado = []
for numero in numeros:
    numeros_ao_quadrado.append(numero ** 2)

numeros_ao_quadrado
```

### Usando List Comprehension (forma mais simples)

```python
numeros_ao_quadrado_comprehension = [numero ** 2 for numero in numeros]
numeros_ao_quadrado_comprehension

```

### Vantagens da List Comprehension

- Código mais curto e limpo
- Execução mais rápida
- Fácil de ler quando você se acostuma

### No exemplo:

- **expressão:** `numero ** 2`
- **item:** `numero`
- **iterável:** `numeros`
