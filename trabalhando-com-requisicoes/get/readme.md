# Método GET

Para consumir APIs em Engenharia de Dados, o Python oferece a biblioteca **requests**, que simplifica chamadas HTTP como GET, POST, DELETE e PUT.

O método **GET** é usado para **buscar informações** em um servidor.

---

### Exemplo prático: Consumindo usuários da GoRest API

```python
!pip install requests
import requests

url = "<https://gorest.co.in/public/v2/users>"
resposta = requests.get(url)

status_resposta = resposta.status_code

if status_resposta == 200:
    usuarios = resposta.json()
    print(usuarios)
else:
    print(f'Algo de errado aconteceu: { status_resposta }')
```

### O que está acontecendo no código?

- `requests.get(url)`
  Envia uma requisição HTTP GET para a API.
- `resposta.status_code`
  Retorna o código HTTP (200, 401, 404, etc.).
- `resposta.json()`
  Converte o corpo da resposta em JSON (lista/dicionário Python).
- O bloco `if` garante que só processamos os dados se o servidor respondeu com **200 (OK)**.

---

### Quando usar GET?

- Buscar listas em APIs públicas (usuários, produtos, dados meteorológicos…)
- Consumir endpoints de consulta em sistemas internos
- Baixar datasets via HTTP

GET **não deve alterar dados** — apenas ler.
