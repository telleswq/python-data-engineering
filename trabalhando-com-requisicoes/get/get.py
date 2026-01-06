"""
Método GET — Consumo de APIs em Engenharia de Dados

Este exemplo demonstra como consumir dados de uma API REST
utilizando o método HTTP GET com a biblioteca requests.

O GET é utilizado exclusivamente para leitura de dados
e não deve causar alterações no servidor.
"""

import requests

# Endpoint da API GoRest (usuários públicos)
URL = "https://gorest.co.in/public/v2/users"

# Enviando a requisição GET
resposta = requests.get(URL)

# Capturando o status da resposta
status_resposta = resposta.status_code

# Validação do status HTTP
if status_resposta == 200:
    usuarios = resposta.json()

    print("Requisição realizada com sucesso")
    print(f"Quantidade de usuários retornados: {len(usuarios)}")

    # Exemplo: exibindo apenas os primeiros registros
    for usuario in usuarios[:3]:
        print(usuario)

else:
    print(f"Erro ao consumir a API. Status HTTP: {status_resposta}")
