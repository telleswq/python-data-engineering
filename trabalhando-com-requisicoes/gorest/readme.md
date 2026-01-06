# Introdução Go Rest

REST API — HTTP Response Codes

Os códigos de resposta HTTP informam o **resultado de uma requisição** feita a uma API REST.

Eles indicam se a operação foi bem-sucedida, se houve erro do cliente ou do servidor, entre outros.

---

### 2xx – Sucesso

- **200 OK** – Tudo funcionou como esperado.
- **201 Created** – Um recurso foi criado com sucesso (geralmente após um POST). O header `Location` indica a URL do recurso criado.
- **204 No Content** – A requisição foi processada com sucesso, mas não há conteúdo de retorno (ex.: DELETE).

---

### 3xx – Redirecionamento

- **304 Not Modified** – O recurso não foi modificado. Pode-se usar a versão em cache.

---

### 4xx – Erro do Cliente

- **400 Bad Request** – Requisição inválida. Ex.: JSON mal formatado ou parâmetros incorretos.
- **401 Unauthorized** – Falha na autenticação.
- **403 Forbidden** – Usuário autenticado, mas não tem permissão para acessar o endpoint.
- **404 Not Found** – O recurso requisitado não existe.
- **405 Method Not Allowed** – Método HTTP não permitido para o endpoint. Checar o header `Allow`.
- **415 Unsupported Media Type** – Tipo de mídia ou versão inválida na requisição.
- **422 Unprocessable Entity** – Falha na validação dos dados (ex.: POST com dados inválidos).
- **429 Too Many Requests** – Requisição rejeitada devido a limite de taxa (rate limiting).

---

### 🛑 5xx – Erro do Servidor

- **500 Internal Server Error** – Erro interno do servidor, geralmente causado por falhas no programa ou processamento.
