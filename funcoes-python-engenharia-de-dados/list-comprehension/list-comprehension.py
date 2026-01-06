"""
Exemplos práticos de List Comprehension
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Transformação de dados
- Limpeza
- Criação de colunas derivadas
- Pré-processamento em pipelines
"""

# ----------------------------------
# Dados de entrada simulados
# ----------------------------------
numeros = [1, 2, 3, 4, 5, 6]

# ----------------------------------
# Exemplo tradicional (sem list comprehension)
# ----------------------------------
numeros_ao_quadrado = []

for numero in numeros:
    numeros_ao_quadrado.append(numero ** 2)

print("Resultado sem list comprehension:")
print(numeros_ao_quadrado)

# ----------------------------------
# Usando List Comprehension
# ----------------------------------
numeros_ao_quadrado_comprehension = [numero ** 2 for numero in numeros]

print("Resultado com list comprehension:")
print(numeros_ao_quadrado_comprehension)

# ----------------------------------
# Exemplo prático em Engenharia de Dados
# ----------------------------------

# Lista de valores vindos de uma coluna numérica
valores_brutos = [10, -5, 20, 0, -3, 15]

# Filtrar apenas valores válidos (maiores que zero)
valores_validos = [valor for valor in valores_brutos if valor > 0]

print("Valores válidos:", valores_validos)

# Criar uma coluna derivada (ex: normalização simples)
valores_normalizados = [valor / 100 for valor in valores_validos]

print("Valores normalizados:", valores_normalizados)

# ----------------------------------
# Exemplo com strings (dados textuais)
# ----------------------------------
arquivos = [
    "2025_vendas.csv",
    "2024_clientes.csv",
    "2025_produtos.csv",
    "readme.txt"
]

# Selecionar apenas arquivos CSV de 2025
arquivos_2025 = [
    arquivo
    for arquivo in arquivos
    if arquivo.startswith("2025_") and arquivo.endswith(".csv")
]

print("Arquivos de 2025:", arquivos_2025)