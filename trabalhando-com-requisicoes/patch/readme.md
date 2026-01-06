# Método PATCH (Update)

O método **PATCH** é utilizado para **atualizar parcialmente** um recurso em uma API REST.

É muito usado quando precisamos alterar somente alguns campos (como status, nome ou e-mail) sem reenviar todo o objeto.

---

### Exemplo prático: Atualizando um usuário no GoRest

```python
import requests

url = "https://gorest.co.in/public/v2/users"
token = "2e6907c786f1d5d9647520feb572ab44c48c569e7be9c0f480fbc911335a6a87"

headers = {
    "Authorization": f"Bearer { token }"
}

gabriel_id = "8264297"

# GET
url_gabriel = f"{url}/{gabriel_id}"

status_usuario = requests.get(url_gabriel, headers=headers)

resposta_json = status_usuario.json()

resposta_json.get('status')

#update
dados = {
    'id': gabriel_id,
    'status': 'inactive',
}

url_gabriel

respose = requests.patch(url_gabriel, headers=headers, data=dados)
```

## Pontos importantes sobre PATCH

- **PATCH atualiza apenas campos específicos**, sem substituir todo o usuário.
- **PUT substitui tudo**, exigindo enviar todos os campos do recurso.
