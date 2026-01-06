# Método Delete

O método **DELETE** remove um recurso da API.

No GoRest, para deletar um usuário, enviamos a requisição diretamente para o endpoint contendo o ID.

---

### Exemplo usando exatamente o código fornecido

```python
import requests

url = "<https://gorest.co.in/public/v2/users>"
token = "2e6907c786f1d5d9647520feb572ab44c48c569e7be9c0f480fbc911335a6a87"

headers = {
    "Authorization": f"Bearer { token }"
}

gabriel_id = "8264297"

# CRUD (C-> Criar, R -> Leitura, U->Atualização, D-> Remover)

#delete
dados = {
    'id': gabriel_id
}

url_completa = f"{url}/{gabriel_id}"
url_completa

usuario_removido = requests.delete(url_completa, headers=headers, data=dados)

usuario_removido
```

## Pontos importantes sobre DELETE

- O ID já está na URL → **não é obrigatório enviar `dados`** no delete.
- Mas, como no exemplo original, enviar `data` não causa erro.
- O retorno é só o **status_code**, normalmente sem corpo.
