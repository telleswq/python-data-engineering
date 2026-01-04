"""
Exemplos práticos de manipulação de strings
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Processamento de arquivos CSV em um pipeline ETL
- Validação de nomes de arquivos
- Parsing de linhas
- Geração de logs
"""

# -----------------------------
# Dados de entrada simulados
# -----------------------------
file_name = "2025_vendas_clientes.csv"
message = "pipeline finished with error on step 3"
linha_csv = "123,João Silva,joao@email.com,2025-01-03"

# -----------------------------
# 1. `in` — contains implícito
# -----------------------------
if "error" in message:
    print("Erro identificado no pipeline")

# -----------------------------
# 2. `startswith()` / `endswith()`
# -----------------------------
if file_name.startswith("2025_") and file_name.endswith(".csv"):
    print(f"Arquivo válido para processamento: {file_name}")
else:
    print("Arquivo inválido")

# -----------------------------
# 3. `join()`
# -----------------------------
colunas = ["id", "nome", "email", "data_cadastro"]
header_csv = ",".join(colunas)
print(f"Header gerado dinamicamente: {header_csv}")

# -----------------------------
# 4. `len()`
# -----------------------------
nome_cliente = "João Silva"

if len(nome_cliente) < 3:
    print("Nome inválido")
else:
    print(f"Nome válido ({len(nome_cliente)} caracteres)")

# -----------------------------
# 5. `split()`
# -----------------------------
dados = linha_csv.split(",")

registro = {
    "id": dados[0],
    "nome": dados[1],
    "email": dados[2],
    "data_cadastro": dados[3]
}

print("Registro parseado:")
print(registro)

# -----------------------------
# 6. f-strings
# -----------------------------
status = "SUCESSO"
print(f"ETL finalizado com status: {status} | Arquivo: {file_name}")
