# Aquarela-Analytics

Processo seletivo consiste em criar uma api de gerenciamento de colaboradores de uma empresa fictícia.

## Tecnologias Utilizadas:
- Fastapi
- SQlAlchemy
- PostgreSQL
- Passlib
- Alembic
- Docker
- Docker Compose

## Funcionalidades

- Cadastrar colaborador
- Buscar todos do colaboradores
- Buscar colaborador por matricula
- Atualizar dados do colaborador 
- Alterar senha do colaborador 
- Promover colaborador 
- Demitir colaborador 
- Deletar colaborador

## Executar Docker Compose

Execute o comando abaixo para executar o docker compose
```bash
docker compose -f docker-compose.yml up --build
```

O servidor estará rodando em http://127.0.0.1:8000

## Enpoints

### GET /colaborador/buscar-todos
Obtém a lista de todos os colaboradores.

Requisição:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/colaborador/buscar-todos' \
  -H 'accept: application/json'
```

Resposta:
```json
[
  {
    "id": 1,
    "nome": "João",
    "sobrenome": "Pereira",
    "matricula": "C001",
    "cargo": {
      "nome": "Gerente",
      "cd_codigo": "C001",
      "salario": 8000,
      "id": 1
    },
    "lider": {
      "nome": "Carlos Silva",
      "matricula": "L001",
      "id": 1
    },
    "status": {
      "nome": "Ativo",
      "cd_status": "S001",
      "id": 1
    }
  },
  {
    "id": 2,
    "nome": "Maria",
    "sobrenome": "Oliveira",
    "matricula": "C002",
    "cargo": {
      "nome": "Analista",
      "cd_codigo": "C002",
      "salario": 5000,
      "id": 2
    },
    "lider": {
      "nome": "Ana Souza",
      "matricula": "L002",
      "id": 2
    },
    "status": {
      "nome": "Ativo",
      "cd_status": "S001",
      "id": 1
    }
  },
  {
    "id": 3,
    "nome": "José",
    "sobrenome": "Silva",
    "matricula": "C003",
    "cargo": {
      "nome": "Assistente",
      "cd_codigo": "C003",
      "salario": 3000,
      "id": 3
    },
    "lider": {
      "nome": "Carlos Silva",
      "matricula": "L001",
      "id": 1
    },
    "status": {
      "nome": "Demitido",
      "cd_status": "S002",
      "id": 2
    }
  }
]
```

### GET /colaborador/matricula/{matricula_colaborador}
Obtém um colaborador específico pela matrícula.

Requisição:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/colaborador/matricula/C001' \
  -H 'accept: application/json'
```

Resposta:
```json
{
  "id": 1,
  "nome": "João",
  "sobrenome": "Pereira",
  "matricula": "C001",
  "cargo": {
    "nome": "Gerente",
    "cd_codigo": "C001",
    "salario": 8000,
    "id": 1
  },
  "lider": {
    "nome": "Carlos Silva",
    "matricula": "L001",
    "id": 1
  },
  "status": {
    "nome": "Ativo",
    "cd_status": "S001",
    "id": 1
  }
}
```

### POST /colaborador/
Cria um novo colaborador.

Requisição:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/colaborador/' \
  -H 'Content-Type: application/json' \
  -d '{
    "nome": "Alexander",
    "sobrenome": "Braga",
    "matricula": "7899",
    "senha": "senha1234",
    "id_cargo": 3,
    "id_status": 1,
    "id_lider": 1
  }'
```

Resposta:
```json
{
  "id": 4,
  "nome": "Alexander",
  "sobrenome": "Braga",
  "matricula": "7899",
  "cargo": {
    "nome": "Assistente",
    "cd_codigo": "C003",
    "salario": 3000,
    "id": 3
  },
  "lider": {
    "nome": "Carlos Silva",
    "matricula": "L001",
    "id": 1
  },
  "status": {
    "nome": "Ativo",
    "cd_status": "S001",
    "id": 1
  }
}
```

### PUT /colaborador/matricula/{matricula_colaborador}
Atualiza os dados de um colaborador existente.

Requisição:
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/colaborador/matricula/7899' \
  -H 'Content-Type: application/json' \
  -d '{
    "nome": "Alexander Teste",
    "sobrenome": "Braga Teste"
  }'
```

Resposta:
```json
{
  "id": 4,
  "nome": "Alexander Teste",
  "sobrenome": "Braga Teste",
  "matricula": "7899",
  "cargo": {
    "nome": "Assistente",
    "cd_codigo": "C003",
    "salario": 3000,
    "id": 3
  },
  "lider": {
    "nome": "Carlos Silva",
    "matricula": "L001",
    "id": 1
  },
  "status": {
    "nome": "Ativo",
    "cd_status": "S001",
    "id": 1
  }
}
```

### PUT /colaborador/{matricula_colaborador}/promover
Promove um colaborador a um novo cargo e status.

Requisição:
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/colaborador/7899/promover' \
  -H 'Content-Type: application/json' \
  -d '{
    "id_cargo": 1,
    "id_lider": 2
  }'
```

Resposta:
```json
{
  "id": 4,
  "nome": "Alexander Teste",
  "sobrenome": "Braga Teste",
  "matricula": "7899",
  "cargo": {
    "nome": "Gerente",
    "cd_codigo": "C001",
    "salario": 8000,
    "id": 1
  },
  "lider": {
    "nome": "Ana Souza",
    "matricula": "L002",
    "id": 2
  },
  "status": {
    "nome": "Ativo",
    "cd_status": "S001",
    "id": 1
  }
}
```

### PUT /colaborador/alterar_senha
Altera a senha de um colaborador.

Requisição:
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/colaborador/alterar_senha' \
  -H 'Content-Type: application/json' \
  -d '{
    "matricula": "C001",
    "senha": "1234567"
  }'
```

Resposta:
```json
{
  "message": "Senha alterada com sucesso"
}
```

### PUT /colaborador/{matricula_colaborador}/demitir
Demitir um colaborador.

Requisição:
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/colaborador/C001/demitir' \
  -H 'Content-Type: application/json'
```

Resposta:
```json
{
  "id": 1,
  "nome": "João",
  "sobrenome": "Pereira",
  "matricula": "C001",
  "cargo": {
    "nome": "Gerente",
    "cd_codigo": "C001",
    "salario": 8000,
    "id": 1
  },
  "lider": {
    "nome": "Carlos Silva",
    "matricula": "L001",
    "id": 1
  },
  "status": {
    "nome": "Demitido",
    "cd_status": "S002",
    "id": 2
  }
}
```

### DELETE /colaborador/matricula/{matricula_colaborador}
Remove um colaborador da base de dados.

Requisição:
```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/colaborador/matricula/7899' \
  -H 'accept: application/json'

```

Resposta:
```json
{
  "message": "Colaborador excluido."
}
```