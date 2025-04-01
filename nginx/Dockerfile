FROM nginx:alpine

# Supprimez la configuration par défaut
RUN rm /etc/nginx/conf.d/default.conf

# Copiez votre configuration dans le dossier de configuration d'Nginx
COPY default.conf /etc/nginx/conf.d/default.conf
