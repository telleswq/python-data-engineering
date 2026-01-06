"""
Método POST — Envio de dados para APIs REST

Este exemplo demonstra como criar um novo recurso em uma API
utilizando o método HTTP POST, algo comum em pipelines de
Engenharia de Dados para envio de dados processados,
eventos ou registros externos.
"""

import requests

# Endpoint da API GoRest
URL = "https://gorest.co.in/public/v2/users"

# Token de autenticação (substituir pelo seu token válido)
TOKEN = "SEU_TOKEN_AQUI"

# Headers com autenticação Bearer
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Dados que serão enviados para a API
dados = {
    "name": "Gabriel",
    "gender": "male",
    "email": "telles@gmail.com",
    "status": "active"
}

# Enviando a requisição POST
resposta = requests.post(
    URL,
    headers=headers,
    json=dados
)

# Verificando o status da resposta
status_resposta = resposta.status_code
print("Status HTTP:", status_resposta)

# Tratamento da resposta
if status_resposta == 201:
    usuario_criado = resposta.json()
    print("Usuário criado com sucesso")
    print(usuario_criado)

elif status_resposta == 401:
    print("Erro de autenticação. Token inválido ou sem permissão.")

else:
    print("Erro ao criar usuário")
    print(resposta.text)
