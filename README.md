# 🏋️‍♀️ WorkoutAPI - Projeto de API com FastAPI

Este projeto foi desenvolvido como parte do curso da [DIO (Digital Innovation One)](https://www.dio.me/) sobre **FastAPI**, com foco em criar uma API RESTful moderna e assíncrona, utilizando práticas e ferramentas de produção.

Unindo duas paixões — **codar** e **treinar** — nasceu a **WorkoutAPI**, uma API simples de competição de Crossfit, mas ideal para aplicar os fundamentos de construção de APIs com Python moderno.

---

<div align="center">
  <img src="mer.jpg" alt="MER - Modelagem de Entidade e Relacionamento" width="400"/>
</div>



## 🚀 Tecnologias e Stack

- **Python 3.11.4**
- **FastAPI** — Framework moderno e de alta performance para APIs com Python
- **SQLAlchemy** — ORM para integração com banco de dados
- **Alembic** — Controle de versão do banco de dados
- **Pydantic** — Validação de dados baseada em tipos
- **PostgreSQL** — Banco de dados relacional (via Docker)
- **Docker + Docker Compose** — Contêineres para PostgreSQL
- **FastAPI Pagination** — Lib para paginação dos endpoints
- **Makefile** — Scripts automatizados para facilitar a execução

---

## 📌 O que é FastAPI?

> FastAPI é um framework web moderno e rápido (alta performance), para construção de APIs com Python 3.6+ baseado em **type hints**. Foi projetado para ser fácil de usar, de codar e pronto para produção.

Saiba mais: [Documentação Oficial](https://fastapi.tiangolo.com/)

---

## 🧠 Conceitos Aplicados

- Código **assíncrono** com `async def`
- CRUD completo com SQLAlchemy + FastAPI
- Criação e controle de **migrations** com Alembic
- Utilização de **type hints** e modelos com Pydantic
- Tratamento de exceções como `sqlalchemy.exc.IntegrityError`
- **Query Parameters**, paginação e customização de retorno
- Documentação automática via Swagger UI (`/docs`)

---

## 🗂️ Modelagem de Dados

A modelagem da API simula um cenário de competição com atletas, centros de treinamento e categorias. Abaixo, a modelagem de entidade-relacionamento (MER):

## 📸 Captura de Tela

<div align="center">
  <img src="assets/mer.jpg" alt="MER da aplicação WorkoutAPI" width="500"/>
</div>


---

## 📦 Instalação e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/Tatianakami/workoutapi.git
cd workoutapi
2. Criar ambiente virtual com pyenv
bash
Copiar
Editar
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
Ou utilize qualquer outro gerenciador de ambientes virtuais da sua preferência.

3. Subir o banco de dados com Docker
bash
Copiar
Editar
make run-docker
4. Criar e aplicar as migrations
bash
Copiar
Editar
make create-migrations d="create_tabelas_iniciais"
make run-migrations
5. Rodar a API
bash
Copiar
Editar
make run
Acesse a documentação interativa em:
👉 http://127.0.0.1:8000/docs

📌 Desafios Propostos no Projeto
✅ Adicionar query parameters:

nome e cpf nos endpoints de atleta

✅ Customizar respostas:

Endpoint get_all de atletas retorna nome, centro_treinamento e categoria

✅ Tratar exceções de integridade (ex: CPF duplicado):

Retornar erro 303 com mensagem personalizada

✅ Adicionar paginação com fastapi-pagination:

Suporte a limit e offset nos endpoints

📚 Referências
📘 FastAPI: https://fastapi.tiangolo.com/

📘 Pydantic: https://docs.pydantic.dev/latest/

📘 SQLAlchemy: https://docs.sqlalchemy.org/en/20/

📘 Alembic: https://alembic.sqlalchemy.org/en/latest/

📘 FastAPI Pagination: https://uriyyo-fastapi-pagination.netlify.app/

👩‍💻 Autora
Desenvolvido por Tatiana LimaKami durante o curso da DIO (Digital Innovation One).
🔗 LinkedIn | 🌐 GitHub

📝 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

yaml
Copiar
Editar

---


