"""
Exemplos práticos de criação e extração de arquivos ZIP
aplicados a cenários comuns de Engenharia de Dados,
como recebimento e distribuição de datasets compactados.
"""

from pathlib import Path
import zipfile
import shutil

# ----------------------------------
# Configuração de diretórios
# ----------------------------------
base_path = Path("./dados_zip")
to_zip_path = base_path / "to_zip"
unzip_path = base_path / "unzip"

base_path.mkdir(exist_ok=True)
to_zip_path.mkdir(exist_ok=True)
unzip_path.mkdir(exist_ok=True)

arquivo_zip = base_path / "files_1.zip"

# ----------------------------------
# Preparando arquivos de exemplo
# ----------------------------------
(to_zip_path / "arquivo_1.txt").write_text(
    "Conteúdo do primeiro arquivo", encoding="utf-8"
)

(to_zip_path / "arquivo_2.txt").write_text(
    "Conteúdo do segundo arquivo", encoding="utf-8"
)

# ----------------------------------
# 1. Criando um arquivo ZIP
# ----------------------------------
shutil.make_archive(
    base_name=str(base_path / "files_1"),
    format="zip",
    root_dir=to_zip_path
)

print("Arquivo ZIP criado com sucesso:", arquivo_zip)

# ----------------------------------
# 2. Extraindo arquivos de um ZIP
# ----------------------------------
with zipfile.ZipFile(arquivo_zip, "r") as zipp:
    zipp.extractall(unzip_path)

print("Arquivos extraídos para:", unzip_path)

# ----------------------------------
# 3. Listando arquivos dentro do ZIP
# ----------------------------------
with zipfile.ZipFile(arquivo_zip, "r") as zipp:
    print("Arquivos contidos no ZIP:")
    for nome in zipp.namelist():
        print("-", nome)
