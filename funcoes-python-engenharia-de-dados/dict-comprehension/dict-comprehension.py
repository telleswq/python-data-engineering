"""
Exemplos práticos de Dict Comprehension
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Transformação de registros
- Padronização de dados
- Criação de estruturas derivadas
- Limpeza e preparação para pipelines
"""

# ----------------------------------
# Exemplo tradicional (sem dict comprehension)
# ----------------------------------
piloto = {
    "classe": "formula 1",
    "nome": "Lewis Hamilton",
    "nacionalidade": "Britânico",
    "equipe": "Mercedes"
}

piloto_valor_upper = {}

for chave, valor in piloto.items():
    piloto_valor_upper[chave] = valor.upper()

print("Resultado sem dict comprehension:")
print(piloto_valor_upper)

# ----------------------------------
# Usando Dict Comprehension
# ----------------------------------
piloto_valor_upper_comprehension = {
    chave: valor.upper()
    for chave, valor in piloto.items()
}

print("Resultado com dict comprehension:")
print(piloto_valor_upper_comprehension)

# ----------------------------------
# Exemplo prático em Engenharia de Dados
# ----------------------------------

# Registro bruto vindo de uma API ou CSV
registro_bruto = {
    "id": "123",
    "nome": "joão silva",
    "email": "JOAO@EMAIL.COM",
    "status": "ativo",
    "idade": "35"
}

# Padronizar valores de texto e manter apenas campos relevantes
registro_padronizado = {
    chave: valor.lower()
    for chave, valor in registro_bruto.items()
    if chave in {"nome", "email", "status"}
}

print("Registro padronizado:")
print(registro_padronizado)

# ----------------------------------
# Exemplo: conversão de tipos
# ----------------------------------
# Dados vindos como string (muito comum em ingestões)
registro_convertido = {
    chave: int(valor) if chave == "idade" else valor
    for chave, valor in registro_bruto.items()
}

print("Registro com tipos ajustados:")
print(registro_convertido)

# ----------------------------------
# Exemplo: criação de dicionário a partir de listas
# ----------------------------------
colunas = ["id", "nome", "email"]
valores = ["123", "João Silva", "joao@email.com"]

registro_final = {
    coluna: valor
    for coluna, valor in zip(colunas, valores)
}

print("Registro final estruturado:")
print(registro_final)
