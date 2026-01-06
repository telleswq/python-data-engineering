"""
Exemplos práticos de leitura e escrita de arquivos CSV
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Ingestão de dados via CSV
- Transformação de registros
- Escrita de dados para integração entre sistemas
"""

import csv
from pathlib import Path

# ----------------------------------
# Configuração de diretórios
# ----------------------------------
base_path = Path("./dados_csv")
base_path.mkdir(exist_ok=True)

arquivo_leitura = base_path / "file_1.csv"
arquivo_escrita = base_path / "file_2.csv"

# ----------------------------------
# Preparação de um CSV de exemplo (leitura)
# ----------------------------------
dados_exemplo = [
    ["id", "nome", "pais"],
    ["1", "João Silva", "Brasil"],
    ["2", "Maria Souza", "Portugal"],
    ["3", "Carlos Lima", "Argentina"]
]

with open(arquivo_leitura, "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados_exemplo)

# ----------------------------------
# 1. Lendo um CSV com csv.DictReader
# ----------------------------------
with open(arquivo_leitura, "r", encoding="utf-8") as arquivo_csv:
    dados = csv.DictReader(arquivo_csv, delimiter=",")

    registros = []
    for linha in dados:
        registros.append(linha)

print("Registros lidos do CSV:")
print(registros)

# ----------------------------------
# Exemplo de transformação dos dados
# ----------------------------------
# Padronizar nomes e filtrar apenas registros do Brasil
registros_tratados = [
    {
        "id": registro["id"],
        "nome": registro["nome"].upper(),
        "pais": registro["pais"]
    }
    for registro in registros
    if registro["pais"] == "Brasil"
]

print("Registros tratados:")
print(registros_tratados)

# ----------------------------------
# 2. Escrevendo um CSV com csv.writer
# ----------------------------------
dados_paises = [
    ["name", "area", "country_code2", "country_code3"],
    ["Albania", 28748, "AL", "ALB"],
    ["Algeria", 2381741, "DZ", "DZA"],
    ["Brazil", 8515767, "BR", "BRA"]
]

with open(arquivo_escrita, "w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerows(dados_paises)

print("Arquivo CSV escrito com sucesso:", arquivo_escrita)
