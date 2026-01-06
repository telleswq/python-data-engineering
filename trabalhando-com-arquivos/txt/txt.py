"""
Exemplos práticos de leitura e escrita de arquivos TXT
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Leitura de logs
- Input/output simples em pipelines
- Processamento linha a linha
"""

from pathlib import Path

# ----------------------------------
# Configuração de diretórios
# ----------------------------------
base_path = Path("./dados_txt")
base_path.mkdir(exist_ok=True)

arquivo_leitura = base_path / "file_1.txt"
arquivo_multilinha = base_path / "file_2.txt"
arquivo_escrita = base_path / "file_3.txt"

# ----------------------------------
# Preparação de arquivos TXT de exemplo
# ----------------------------------
arquivo_leitura.write_text(
    "Pipeline iniciado\nPipeline em execução\nPipeline finalizado",
    encoding="utf-8"
)

arquivo_multilinha.write_text(
    "info: start process\nwarning: missing value\nerror: invalid format",
    encoding="utf-8"
)

# ----------------------------------
# 1. Lendo um arquivo TXT completo
# ----------------------------------
with open(arquivo_leitura, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo completo do arquivo:")
print(conteudo)

# ----------------------------------
# 2. Lendo um TXT linha por linha
# ----------------------------------
with open(arquivo_multilinha, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.read().splitlines()

print("Processando linhas:")
for linha in linhas:
    print(linha.upper())

# ----------------------------------
# 3. Escrevendo em um arquivo TXT
# ----------------------------------
with open(arquivo_escrita, "w", encoding="utf-8") as arquivo:
    arquivo.write("Hello World!")

print("Arquivo TXT escrito com sucesso:", arquivo_escrita)
