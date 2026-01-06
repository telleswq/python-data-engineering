"""
Introdução a REST API e HTTP Response Codes.

Este arquivo demonstra como interpretar códigos de resposta HTTP
ao consumir APIs REST, algo essencial em pipelines de Engenharia de Dados.

Um pipeline bem feito não apenas consome dados, mas valida:
- status da requisição
- sucesso ou falha
- tipo do erro
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def verificar_resposta(response):
    """
    Analisa o status code da resposta HTTP e imprime
    a categoria do resultado.
    """

    status = response.status_code

    if 200 <= status < 300:
        print(f"Sucesso (2xx) - Status: {status}")

    elif 300 <= status < 400:
        print(f"Redirecionamento (3xx) - Status: {status}")

    elif 400 <= status < 500:
        print(f"Erro do cliente (4xx) - Status: {status}")

    elif 500 <= status < 600:
        print(f"Erro do servidor (5xx) - Status: {status}")

    else:
        print(f"Status desconhecido: {status}")


# ==========================================================
# Exemplo 1 — 200 OK (GET bem-sucedido)
# ==========================================================
response_ok = requests.get(f"{BASE_URL}/users/1")

print("\nExemplo 200 OK")
verificar_resposta(response_ok)


# ==========================================================
# Exemplo 2 — 404 Not Found
# ==========================================================
response_not_found = requests.get(f"{BASE_URL}/users/99999")

print("\nExemplo 404 Not Found")
verificar_resposta(response_not_found)


# ==========================================================
# Exemplo 3 — 201 Created (POST)
# ==========================================================
novo_usuario = {
    "name": "Gabriel",
    "username": "Wq",
    "email": "sincer@dataway.com"
}

response_created = requests.post(
    f"{BASE_URL}/users",
    json=novo_usuario
)

print("\nExemplo 201 Created")
verificar_resposta(response_created)


# ==========================================================
# Exemplo 4 — 204 No Content (DELETE)
# ==========================================================
response_no_content = requests.delete(f"{BASE_URL}/users/1")

print("\nExemplo 204 No Content")
verificar_resposta(response_no_content)


# ==========================================================
# Observações importantes para Engenharia de Dados
# ==========================================================
"""
Boas práticas em pipelines:

- Nunca assumir que a requisição deu certo
- Sempre validar status_code
- Tratar 4xx e 5xx separadamente
- Logar erros com contexto (URL, payload, status)
- Implementar retry para erros transitórios (5xx, 429)

Status codes são sinais claros do que aconteceu com a requisição.
"""
