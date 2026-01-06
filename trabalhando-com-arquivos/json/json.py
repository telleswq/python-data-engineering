"""
Exemplos práticos de leitura e escrita de arquivos JSON
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Ingestão de dados vindos de APIs
- Leitura de arquivos JSON
- Acesso a estruturas aninhadas
- Escrita de novos arquivos JSON
"""

import json
from pathlib import Path

# ----------------------------------
# Configuração de diretórios
# ----------------------------------
base_path = Path("./dados_json")
base_path.mkdir(exist_ok=True)

arquivo_leitura = base_path / "file_1.json"
arquivo_escrita = base_path / "novo_piloto.json"

# ----------------------------------
# Preparação de um JSON de exemplo
# ----------------------------------
dados_exemplo = {
    "season": 2025,
    "category": "Formula 1",
    "pilots": [
        {
            "name": "Lewis Hamilton",
            "team": "Ferrari",
            "nationality": "British"
        },
        {
            "name": "Max Verstappen",
            "team": "Red Bull",
            "nationality": "Dutch"
        }
    ]
}

with open(arquivo_leitura, "w", encoding="utf-8") as arquivo_json:
    json.dump(dados_exemplo, arquivo_json, indent=4)

# ----------------------------------
# 1. Lendo um arquivo JSON
# ----------------------------------
with open(arquivo_leitura, "r", encoding="utf-8") as arquivo_json:
    dados = json.load(arquivo_json)

print("Tipo do objeto carregado:")
print(type(dados))

print("Conteúdo do JSON:")
print(dados)

# ----------------------------------
# 2. Acessando dados do JSON
# ----------------------------------
temporada = dados.get("season")
print("Temporada:", temporada)

pilotos = dados.get("pilots", [])
print("Pilotos:", pilotos)

# Exemplo de acesso a dados aninhados
nomes_pilotos = [piloto.get("name") for piloto in pilotos]
print("Nomes dos pilotos:", nomes_pilotos)

# ----------------------------------
# 3. Escrevendo um novo arquivo JSON
# ----------------------------------
novo_piloto = {
    "name": "Gabriel Telles",
    "team": "McLaren",
    "nationality": "Brazilian"
}

with open(arquivo_escrita, "w", encoding="utf-8") as arquivo_json:
    json.dump(novo_piloto, arquivo_json, indent=4)

print("Novo arquivo JSON criado:", arquivo_escrita)
