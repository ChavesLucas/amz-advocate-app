# Use uma imagem base do Nginx
FROM nginx:alpine

# Copie os arquivos do diretório public para o diretório padrão do Nginx
COPY public /usr/share/nginx/html

# Copie os arquivos de assets para o diretório de assets no Nginx
COPY assets /usr/share/nginx/html/assets

# Exponha a porta 80 para acessar a aplicação
EXPOSE 80
