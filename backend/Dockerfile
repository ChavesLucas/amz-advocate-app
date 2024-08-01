# Usar uma imagem base Python
FROM python:3.9-slim

# Configuração do diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários para o contêiner
COPY . /app

# Instalar dependências
RUN pip install -r requirements.txt

# Comando para rodar a aplicação
CMD ["python", "app/main.py"]
