"""
Exemplos práticos de leitura e escrita de arquivos YAML
aplicados a cenários comuns de Engenharia de Dados,
DevOps e configuração de pipelines.
"""

from pathlib import Path
import yaml

# ----------------------------------
# Configuração de diretórios
# ----------------------------------
base_path = Path("./dados_yaml")
base_path.mkdir(exist_ok=True)

arquivo_leitura = base_path / "file_1.yaml"
arquivo_escrita = base_path / "dados.yaml"

# ----------------------------------
# Preparação de um YAML de exemplo
# ----------------------------------
yaml_exemplo = """
database:
  host: localhost
  port: 5432
  user: admin
  password: secret
services:
  - name: ingestion
    enabled: true
  - name: processing
    enabled: true
  - name: visualization
    enabled: false
"""

arquivo_leitura.write_text(yaml_exemplo, encoding="utf-8")

# ----------------------------------
# 1. Lendo um arquivo YAML
# ----------------------------------
with open(arquivo_leitura, "r", encoding="utf-8") as arquivo_yaml:
    try:
        dados = yaml.load(arquivo_yaml, Loader=yaml.FullLoader)
        print("Conteúdo do YAML carregado:")
        print(dados)
    except Exception as erro:
        print(f"Erro ao ler YAML: {erro}")

# Acesso estruturado aos dados
print("Host do banco:", dados["database"]["host"])
print("Serviços habilitados:")
for servico in dados["services"]:
    if servico["enabled"]:
        print("-", servico["name"])

# ----------------------------------
# 2. Escrevendo um arquivo YAML
# ----------------------------------
dados_saida = {
    "pipeline": {
        "name": "etl_daily",
        "schedule": "0 2 * * *",
        "enabled": True
    },
    "resources": {
        "cpu": "2",
        "memory": "4Gi"
    },
    "owners": ["data-team", "platform-team"]
}

with open(arquivo_escrita, "w", encoding="utf-8") as yaml_gravado:
    yaml.dump(dados_saida, yaml_gravado, sort_keys=False)

print("Arquivo YAML criado com sucesso:", arquivo_escrita)
