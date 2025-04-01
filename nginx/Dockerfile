FROM nginx:alpine

# Supprimer la configuration par défaut
RUN rm /etc/nginx/conf.d/default.conf

# Copier votre configuration Nginx personnalisée dans le conteneur
COPY default.conf /etc/nginx/conf.d/default.conf
