# Básico requisição http

Requisições HTTP são formas de comunicação entre **cliente** (um usuário, sistema, API ou script Python) e um **servidor**.

O cliente envia um pedido e o servidor responde dizendo se conseguiu atender ou não, retornando:

- **Status da operação** (ex.: 200, 404, 401)
- **Dados** (quando houver)
- **Mensagens de erro ou confirmação**

Em Engenharia de Dados, requisições HTTP são usadas para:

- Consumir APIs públicas ou privadas
- Coletar dados para pipelines
- Buscar informações atualizadas diariamente
- Registrar eventos enviando dados para serviços externos

---

## **GET — Buscar informações**

É o tipo de requisição mais comum.

O cliente faz uma pergunta ao servidor, como:

> “Preciso dos dados do usuário 1.”

Se tudo estiver certo, o servidor responde:

- Status: **2xx (sucesso)**
- Os dados solicitados

Exemplo de resposta típica:

```
{
	"id": 1,
	"name": "Gabriel",
	"usurname": "Wq",
	"email": "sincer@dataway.com"
}

```

Mas se o cliente não tiver permissão, o servidor retorna, por exemplo:

- Status: **401 (não autorizado)**
- Sem dados ou com uma mensagem de erro

## **POST — Enviar dados / Criar algo**

POST é usado quando o cliente quer **enviar informações novas** para o servidor.

Exemplos no dia a dia de Engenharia de Dados:

- Enviar dados processados para outra API
- Criar registros em um serviço externo
- Disparar eventos (logs, histórico, métricas)

É como dizer ao servidor:

> “Aqui estão os novos dados. Crie esse registro para mim.”

Se tudo der certo → **2xx**

---

## **PUT / PATCH — Atualizar dados**

Quando o cliente quer **atualizar algo que já existe**, ele envia uma requisição informando o que deve ser alterado.

Exemplo:

> “Atualize os dados do usuário 1.”

Resposta bem-sucedida:

- Status: **2xx**
- Mensagem: “dados atualizados”

---

## **DELETE — Remover dados**

DELETE é usado quando o sistema quer **deletar** algo no servidor.

Exemplo:

> “Remova o usuário 1.”

Se a operação for concluída, o servidor retorna:

- Status: **2xx (sucesso)**
- Às vezes, nenhuma mensagem além da confirmação

---

## **HTTP Status Codes**

### **1xx – Informational**

O servidor está recebendo e entendendo a requisição, mas ainda não terminou.

### **2xx – Success**

A operação deu certo.

Exemplos comuns:

- **200** – OK
- **201** – Criado
- **204** – Sem conteúdo (mas funcionou)

### **3xx – Redirection**

O cliente foi redirecionado para outro endereço.

### **4xx – Client Error**

O erro está na requisição do cliente.

Exemplos:

- **400** – Requisição inválida
- **401** – Não autorizado
- **404** – Não encontrado

### **5xx – Server Error**

O servidor tentou, mas falhou ao processar.

Exemplos:

- **500** – Erro interno
- **503** – Serviço indisponível
