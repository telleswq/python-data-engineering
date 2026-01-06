# Método Post

O método **POST** é usado para **enviar dados a uma API** e criar novos recursos.

Na GoRest, podemos criar usuários enviando informações como nome, gênero, e-mail e status.

---

### Exemplo prático

```python
import requests

url = "<https://gorest.co.in/public/v2/users>"
token = "SEU_TOKEN_AQUI"

headers = {
    "Authorization": f"Bearer {token}"
}

dados = {
    "name": 'Gabriel',
    "gender": 'male',
    "email": 'telles@gmail.com',
    "status": 'active',
}

# Use json=dados para enviar JSON corretamente
resposta = requests.post(
    url,
    headers=headers,
    json=dados
)

print(resposta.status_code)

usuario_gabriel = resposta.json()
print(usuario_gabriel)
```

### Explicação do código

- `headers` → Contém o token de autorização (`Bearer token`).
- `json=dados` → Envia os dados em **JSON**, que é o formato esperado pela API GoRest.
  - Evita erros como 404 ou 415, que acontecem ao usar `data=dados`.
- `resposta.status_code` → Retorna o código HTTP da requisição:
  - **201 Created** → Usuário criado com sucesso
  - **401 Unauthorized** → Token inválido ou sem permissão
- `resposta.json()` → Converte a resposta JSON em um dicionário Python para manipulação.

### Quando usar POST?

- Criar novos registros em uma API
- Enviar dados processados de pipelines para um serviço externo
- Registrar eventos ou métricas em sistemas REST
