"""
Requisições HTTP são a base da comunicação entre clientes e servidores.

Este arquivo demonstra, de forma prática, como um script Python
atua como cliente HTTP consumindo uma API REST, algo extremamente
comum em pipelines de Engenharia de Dados.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# ==========================================================
# GET — Buscar informações
# ==========================================================
"""
O método GET é usado para buscar dados existentes no servidor.

Exemplo:
"Preciso dos dados do usuário 1"
"""

response_get = requests.get(f"{BASE_URL}/users/1")

print("GET status code:", response_get.status_code)

if response_get.status_code == 200:
    dados_usuario = response_get.json()
    print("Dados do usuário:")
    print(dados_usuario)
else:
    print("Erro ao buscar usuário")


# ==========================================================
# POST — Enviar dados / Criar algo
# ==========================================================
"""
POST é usado para enviar dados novos ao servidor.

Exemplo:
"Aqui estão os novos dados, crie esse registro para mim"
"""

novo_usuario = {
    "name": "Gabriel",
    "username": "Wq",
    "email": "sincer@dataway.com"
}

response_post = requests.post(
    f"{BASE_URL}/users",
    json=novo_usuario
)

print("\nPOST status code:", response_post.status_code)

if response_post.status_code in (200, 201):
    print("Usuário criado:")
    print(response_post.json())
else:
    print("Erro ao criar usuário")


# ==========================================================
# PATCH — Atualizar dados parcialmente
# ==========================================================
"""
PATCH é usado para atualizar apenas parte de um recurso existente.

Exemplo:
"Atualize o email do usuário 1"
"""

atualizacao = {
    "email": "novo_email@dataway.com"
}

response_patch = requests.patch(
    f"{BASE_URL}/users/1",
    json=atualizacao
)

print("\nPATCH status code:", response_patch.status_code)

if response_patch.status_code == 200:
    print("Dados atualizados:")
    print(response_patch.json())
else:
    print("Erro ao atualizar usuário")


# ==========================================================
# DELETE — Remover dados
# ==========================================================
"""
DELETE remove um recurso no servidor.

Exemplo:
"Remova o usuário 1"
"""

response_delete = requests.delete(f"{BASE_URL}/users/1")

print("\nDELETE status code:", response_delete.status_code)

if response_delete.status_code in (200, 204):
    print("Usuário removido com sucesso")
else:
    print("Erro ao remover usuário")


# ==========================================================
# Observação sobre Status Codes
# ==========================================================
"""
1xx -> Informacional
2xx -> Sucesso
3xx -> Redirecionamento
4xx -> Erro do cliente
5xx -> Erro do servidor

Em pipelines de dados, sempre valide:
- status_code
- estrutura do payload
- mensagens de erro
"""
