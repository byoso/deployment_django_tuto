FROM nginxinc/nginx-unprivileged:1-alpine3.18
LABEL maintainer="ppws.fr"

COPY ./nginx/* /etc/nginx/
COPY ./run.sh /run.sh

USER root

RUN apk add --no-cache openssl bash && \
    mkdir -p /vol/static && \
    chmod -R 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown -R nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static
VOLUME /vol/www

USER nginx

CMD ["/run.sh"]
