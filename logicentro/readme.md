# Como executar a aplicação

### Requisitos
```
* Python
* Django
* Django REST Framework
* Postman (para fazer requisições)
```

```
É recomendado instalar o Django juntamente com o Django REST Framework em um ambiente virtual 
Após estar com tudo devidamente instalado, é necessário estar no diretório raiz do projeto,
(onde fica o arquivo manage.py) abrir o prompt de comando e digitar:

> python manage.py runserver

Após isso basta colocar no Postman uma das url's abaixo descritas e fazer requisições 
```

# Documentação da API

Esta API permite gerenciar veículos, motoristas, operações, confrontos, usuários e empresas. A API foi construída usando **Django REST Framework** e segue os padrões RESTful.

### Base URL:
```
/api/
```

---

## **Veículos**

### Endpoint:
```
/api/veiculos/
```

### Métodos disponíveis:

- **GET** `/api/veiculos/`: Retorna a lista de todos os veículos.
- **GET** `/api/veiculos/{id}/`: Retorna os detalhes de um veículo específico.
- **POST** `/api/veiculos/`: Cria um novo veículo.
- **PUT/PATCH** `/api/veiculos/{id}/`: Atualiza um veículo existente.
- **DELETE** `/api/veiculos/{id}/`: Exclui um veículo existente.

### Corpo da requisição (para POST e PUT/PATCH):

```json
{
  "placa": "string",
  "marca": "string",
  "modelo": "string",
  "ano": "integer",
  "tipo_veiculo": "string",
  "situacao": "A"  // 'A' para Ativo, 'I' para Inativo
}
```

---

## **Motoristas**

### Endpoint:
```
/api/motoristas/
```

### Métodos disponíveis:

- **GET** `/api/motoristas/`: Retorna a lista de todos os motoristas.
- **GET** `/api/motoristas/{id}/`: Retorna os detalhes de um motorista específico.
- **POST** `/api/motoristas/`: Cria um novo motorista.
- **PUT/PATCH** `/api/motoristas/{id}/`: Atualiza um motorista existente.
- **DELETE** `/api/motoristas/{id}/`: Exclui um motorista existente.

### Corpo da requisição (para POST e PUT/PATCH):

```json
{
  "nome": "string",
  "cpf": "string",
  "cnh": "string",
  "telefone": "string",  // Opcional
  "situacao": "A"  // 'A' para Ativo, 'I' para Inativo
}
```

---

## **Operações**

### Endpoint:
```
/api/operacoes/
```

### Métodos disponíveis:

- **GET** `/api/operacoes/`: Retorna a lista de todas as operações.
- **GET** `/api/operacoes/{id}/`: Retorna os detalhes de uma operação específica.
- **POST** `/api/operacoes/`: Cria uma nova operação.
- **PUT/PATCH** `/api/operacoes/{id}/`: Atualiza uma operação existente.
- **DELETE** `/api/operacoes/{id}/`: Exclui uma operação existente.

### Corpo da requisição (para POST e PUT/PATCH):

```json
{
  "veiculo": "id_do_veiculo",
  "placa": "string",
  "motorista": "id_do_motorista",
  "empresa_origem": "id_da_empresa_origem",
  "dta_saida": "YYYY-MM-DDTHH:MM:SS",  // Data e hora de saída
  "usu_cadsaida": "id_do_usuario_que_registrou_a_saida",
  "empresa_destino": "id_da_empresa_destino",
  "dta_entrada": "YYYY-MM-DDTHH:MM:SS",  // Data e hora de entrada
  "usu_cadentrada": "id_do_usuario_que_registrou_a_entrada",
  "status": "string",
  "nro_mdfe": "integer",  // Opcional
  "nro_notafiscal": "integer",  // Opcional
  "nro_lacre": "integer"
}
```

---

## **Confrontos**

### Endpoint:
```
/api/confrontos/
```

### Métodos disponíveis:

- **GET** `/api/confrontos/`: Retorna a lista de todos os confrontos.
- **GET** `/api/confrontos/{id}/`: Retorna os detalhes de um confronto específico.
- **POST** `/api/confrontos/`: Cria um novo confronto.
- **PUT/PATCH** `/api/confrontos/{id}/`: Atualiza um confronto existente.
- **DELETE** `/api/confrontos/{id}/`: Exclui um confronto existente.

### Corpo da requisição (para POST e PUT/PATCH):

```json
{
  "operacao": "id_da_operacao",
  "usu_confronto": "id_do_usuario_que_realizou_o_confronto",
  "dta_confronto": "YYYY-MM-DDTHH:MM:SS",  // Data e hora do confronto
  "situacao": "string",
  "justificativa": "string",
  "observacao": "string"  // Opcional
}
```

---

## **Empresas**

### Endpoint:
```
/api/empresas/
```

### Métodos disponíveis:

- **GET** `/api/empresas/`: Retorna a lista de todas as empresas.
- **GET** `/api/empresas/{id}/`: Retorna os detalhes de uma empresa específica.
- **POST** `/api/empresas/`: Cria uma nova empresa.
- **PUT/PATCH** `/api/empresas/{id}/`: Atualiza uma empresa existente.
- **DELETE** `/api/empresas/{id}/`: Exclui uma empresa existente.

### Corpo da requisição (para POST e PUT/PATCH):

```json
{
  "cnpj": "string",
  "nome": "string",
  "logradouro": "string",
  "cidade": "string",
  "estado": "string",
  "situacao": "A"  // 'A' para Ativo, 'I' para Inativo
}
```

---

## **Usuários**

### Endpoint:
```
/api/usuarios/
```

### Métodos disponíveis:

- **GET** `/api/usuarios/`: Retorna a lista de todos os usuários.
- **GET** `/api/usuarios/{id}/`: Retorna os detalhes de um usuário específico.
- **POST** `/api/usuarios/`: Cria um novo usuário.
- **PUT/PATCH** `/api/usuarios/{id}/`: Atualiza um usuário existente.
- **DELETE** `/api/usuarios/{id}/`: Exclui um usuário existente.

### Corpo da requisição (para POST e PUT/PATCH):

```json
{
  "nome": "string",
  "email": "string",
  "usuario": "string",
  "senha": "string",
  "cargo": "string",
  "situacao": "A"  // 'A' para Ativo, 'I' para Inativo
}
```

---

## Exemplos de Requisição

### **GET** todos os veículos:
```
GET /api/veiculos/
```

### **GET** veículo por ID:
```
GET /api/veiculos/{id}/
```

### **POST** criar um veículo:
```
POST /api/veiculos/
```

Corpo da requisição:
```json
{
  "placa": "XYZ-1234",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2020,
  "tipo_veiculo": "Carro",
  "situacao": "A"
}
```

### **PUT** atualizar um veículo:
```
PUT /api/veiculos/{id}/
```

Corpo da requisição:
```json
{
  "placa": "XYZ-1234",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2021,
  "tipo_veiculo": "Carro",
  "situacao": "A"
}
```

### **DELETE** excluir um veículo:
```
DELETE /api/veiculos/{id}/
```

---

Essa documentação cobre os principais métodos e endpoints da API.
