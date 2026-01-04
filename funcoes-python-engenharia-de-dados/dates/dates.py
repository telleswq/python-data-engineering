"""
Exemplos práticos de manipulação de datas
aplicados ao contexto de Engenharia de Dados.

Cenário:
- Particionamento de dados
- Logs de pipeline
- Validação e parsing de datas vindas de arquivos e APIs
- Cálculo de janelas de processamento
"""

import datetime

# ----------------------------------
# 1. datetime.date + today()
# ----------------------------------
hoje = datetime.date.today()

print("Data atual:", hoje)
print("Ano:", hoje.year)
print("Mês:", hoje.month)
print("Dia:", hoje.day)

# Exemplo de uso comum: particionamento de dados
particao = f"year={hoje.year}/month={hoje.month:02d}/day={hoje.day:02d}"
print("Partição de dados:", particao)

# ----------------------------------
# 2. datetime.datetime (data + hora)
# ----------------------------------
agora = datetime.datetime.now()
print("Timestamp atual:", agora)

# Uso típico em logs e auditoria
log_message = f"Pipeline executado em {agora}"
print(log_message)

# ----------------------------------
# 3. Formatação com strftime()
# ----------------------------------
timestamp_formatado = agora.strftime("%Y-%m-%d %H:%M:%S")
print("Timestamp formatado:", timestamp_formatado)

# Exemplo: nome de arquivo com timestamp
file_name = f"dados_processados_{agora.strftime('%Y%m%d_%H%M%S')}.csv"
print("Nome do arquivo:", file_name)

# ----------------------------------
# 4. Converter string em data (strptime)
# ----------------------------------
data_string = "2025-11-25"
data_convertida = datetime.datetime.strptime(data_string, "%Y-%m-%d")

print("Data convertida:", data_convertida)
print("Tipo do objeto:", type(data_convertida))

# Uso comum: dados vindos de CSV, JSON ou API
data_evento = data_convertida.date()
print("Data do evento:", data_evento)

# ----------------------------------
# 5. timedelta (cálculo de datas)
# ----------------------------------
ontem = hoje - datetime.timedelta(days=1)
amanha = hoje + datetime.timedelta(days=1)

print("Ontem:", ontem)
print("Amanhã:", amanha)

# Exemplo prático: janela de processamento
inicio_janela = hoje - datetime.timedelta(days=7)
fim_janela = hoje

print("Janela de processamento:")
print("Início:", inicio_janela)
print("Fim:", fim_janela)