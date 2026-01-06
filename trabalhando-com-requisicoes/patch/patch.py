"""
Método PATCH — Atualização parcial de recursos em APIs REST

Este exemplo demonstra como atualizar parcialmente um recurso
utilizando o método HTTP PATCH na API GoRest.

PATCH é utilizado quando precisamos alterar apenas alguns campos
de um recurso, sem reenviar todo o objeto.
"""

import requests

# Endpoint base da API GoRest
BASE_URL = "https://gorest.co.in/public/v2/users"

# Token de autenticação (substituir por um token válido)
TOKEN = "SEU_TOKEN_AQUI"

# Headers com autenticação
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# ID do usuário que será atualizado
usuario_id = "8264297"

# URL completa do recurso
url_usuario = f"{BASE_URL}/{usuario_id}"

# --------------------------------------------------
# 1. Consultando o status atual do usuário (GET)
# --------------------------------------------------
resposta_get = requests.get(url_usuario, headers=headers)

if resposta_get.status_code == 200:
    usuario_atual = resposta_get.json()
    print("Status atual do usuário:", usuario_atual.get("status"))
else:
    print("Erro ao buscar usuário")
    print(resposta_get.status_code)
    exit()

# --------------------------------------------------
# 2. Atualizando parcialmente o usuário (PATCH)
# --------------------------------------------------
dados_update = {
    "status": "inactive"
}

resposta_patch = requests.patch(
    url_usuario,
    headers=headers,
    json=dados_update
)

# Validação da resposta
if resposta_patch.status_code == 200:
    usuario_atualizado = resposta_patch.json()
    print("Usuário atualizado com sucesso")
    print("Novo status:", usuario_atualizado.get("status"))

elif resposta_patch.status_code == 401:
    print("Erro de autenticação. Token inválido ou sem permissão.")

elif resposta_patch.status_code == 404:
    print("Usuário não encontrado.")

else:
    print("Erro ao atualizar usuário")
    print(resposta_patch.status_code)
    print(resposta_patch.text)
