
# AMZ Advocate App

Este projeto é uma aplicação web para apresentar o currículo de uma advogada e permitir que usuários enviem perguntas através de um formulário de contato.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

```
amz-advocate-app/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── venv/
│   ├── .env
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── assets/
│   │   └── images/
│   │       ├── banner.jpg
│   │       ├── logo.png
│   │       └── profile.jpg
│   ├── public/
│   │   ├── form.html
│   │   ├── index.html
│   │   ├── scripts.js
│   │   └── styles.css
│   ├── Dockerfile
│   └── docker-compose.yml
```

## Tecnologias Utilizadas

- **Frontend**: HTML5, CSS, JavaScript, Nginx
- **Backend**: Python, Flask, MongoDB
- **Conteinerização**: Docker, Docker Compose

## Pré-requisitos

- Docker
- Docker Compose

## Como Executar

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/username/amz-advocate-app.git
cd amz-advocate-app
```

### 2. Configuração do Backend

No diretório `backend`, configure as variáveis de ambiente no arquivo `.env` (se necessário) e instale as dependências:

```bash
cd backend
pip install -r requirements.txt
```

### 3. Construir e Iniciar os Contêineres

No diretório raiz do projeto, use Docker Compose para construir e iniciar todos os serviços:

```bash
docker-compose up --build
```

Isso iniciará os seguintes serviços:
- **Frontend**: Acessível em `http://localhost:8081`
- **Backend**: Acessível internamente como `http://backend:5000` e externamente em `http://localhost:5000`
- **MongoDB**: Acessível internamente como `mongodb://mongo:27017/advocate_app`

### 4. Acessar a Aplicação

- **Frontend**: Acesse `http://localhost:8081` no seu navegador para visualizar a aplicação.
- **Backend**: Acesse `http://localhost:5000` para verificar o backend (se houver endpoints de API pública).

## Contribuindo

Se desejar contribuir para este projeto, sinta-se à vontade para abrir um PR (Pull Request). Antes de contribuir, certifique-se de seguir as diretrizes de contribuição e a formatação do código.



## Contato

Para questões e suporte, entre em contato com [chaves.lucas@amzlabs.com](mailto:chaves.lucas@amzlabs.com).
