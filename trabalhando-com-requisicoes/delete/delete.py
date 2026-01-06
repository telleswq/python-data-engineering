"""
Método DELETE — Remoção de recursos em APIs REST

Este exemplo demonstra como remover um usuário da API GoRest
utilizando o método HTTP DELETE.

Em operações DELETE, normalmente o servidor retorna apenas
o status HTTP, sem corpo de resposta.
"""

import requests

# Endpoint base da API GoRest
BASE_URL = "https://gorest.co.in/public/v2/users"

# Token de autenticação (substituir por um token válido)
TOKEN = "SEU_TOKEN_AQUI"

# Headers com autenticação
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# ID do usuário que será removido
usuario_id = "8264297"

# URL completa do recurso
url_usuario = f"{BASE_URL}/{usuario_id}"

# --------------------------------------------------
# DELETE — Remoção do usuário
# --------------------------------------------------
resposta_delete = requests.delete(
    url_usuario,
    headers=headers
)

# Validação da resposta
status_resposta = resposta_delete.status_code
print("Status HTTP:", status_resposta)

if status_resposta in (200, 204):
    print("Usuário removido com sucesso")

elif status_resposta == 401:
    print("Erro de autenticação. Token inválido ou sem permissão.")

elif status_resposta == 404:
    print("Usuário não encontrado.")

else:
    print("Erro ao remover usuário")
    print(resposta_delete.text)
