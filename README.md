<h1 align="center">📖 Church System API</h1>

<p align="center">
  <strong>Sistema completo de gestão para comunidades religiosas</strong><br>
  Desenvolvido com <code>Django + DRF</code>, autenticação <code>JWT</code>, documentação <code>Swagger</code> e orquestração via <code>Docker</code>.
</p>

---

## 🚀 Tecnologias Utilizadas

- 🐍 [Python 3.11+](https://www.python.org/)
- 🌐 [Django 5.2.1](https://www.djangoproject.com/)
- 🛠️ [Django Rest Framework](https://www.django-rest-framework.org/)
- 🔐 [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- 📘 [drf-spectacular (Swagger/Redoc)](https://drf-spectacular.readthedocs.io/)
- 🧵 [Celery + Redis](https://docs.celeryq.dev/)
- 🐳 [Docker + Docker Compose](https://docs.docker.com/compose/)
- 🎨 [Jazzmin (Admin Customizado)](https://github.com/farridav/django-jazzmin)

---

## 🗂️ Estrutura do Projeto
```
app_name/
├── admin.py
├── apps.py
├── filters.py
├── forms.py
├── models.py
├── serializers.py
├── urls.py
└── views.py
```

---

Cada app Django está organizado de forma modular para facilitar manutenção, escalabilidade e reutilização de código.

---

## 📄 Documentação da API

- 📘 **Swagger UI**: [`/api/v1/docs/`](http://localhost:8000/api/v1/docs/)
- 📕 **Redoc**: [`/api/v1/redoc/`](http://localhost:8000/api/v1/redoc/)
- 📜 **Schema OpenAPI**: [`/api/v1/schema/`](http://localhost:8000/api/v1/schema/)

---

## 🔐 Autenticação JWT

- `POST /api/token/` – Obter token de acesso e refresh  
- `POST /api/token/refresh/` – Renovar token de acesso

---

## 🧱 Endpoints Disponíveis
```
/api/v1/calendarios/
/api/v1/comunidades/
/api/v1/contatos/
/api/v1/dizimos/
/api/v1/enderecos/
/api/v1/membroSetores/
/api/v1/membroTurmas/
/api/v1/movimentacaoProdutos/
/api/v1/pessoas/
/api/v1/produtos/
/api/v1/sacramentos/
/api/v1/setores/
/api/v1/tesouraria/
/api/v1/tipoEventos/
/api/v1/tipoSacramentos/
/api/v1/turmas/
```

---

## 🐳 Como Rodar com Docker

### 🧩 Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### ▶️ Subindo o ambiente

# Subir os containers
docker-compose up --build

---

🔧 Comandos úteis

# Acessar o container
docker-compose exec web bash

# Criar superusuário
docker-compose exec web python manage.py createsuperuser

# Aplicar migrações
docker-compose exec web python manage.py migrate

---

⚙️ Variáveis de Ambiente
Crie um arquivo .env na raiz com:

DJANGO_SECRET_KEY=changeme
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres

---

🧪 Scripts de Desenvolvimento

# Rodar testes
docker-compose exec web python manage.py test

# Formatar código com Black
docker-compose exec web black .

# Verificar com Flake8
docker-compose exec web flake8 .

---

📦 Principais Dependências
Veja todas em requirements.txt. Destaques:

djangorestframework

djangorestframework_simplejwt

drf-spectacular

django-jazzmin

celery

psycopg2-binary

---

🏠 Página Inicial da API
```
GET /
{
  "message": "Bem-vindo à API do Church System",
  "documentacao": "/api/v1/docs/",
  "admin": "/admin/"
}
```
---

🛠️ Manutenção & Contribuição
Este projeto está em desenvolvimento contínuo. Sinta-se livre para abrir uma issue, sugerir melhorias ou enviar um pull request.

---

📄 Licença
MIT License © [Almeida System]
