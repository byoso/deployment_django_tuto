FROM nginxinc/nginx-unprivileged:1-alpine3.18
LABEL maintainer="ppws.fr"

COPY ./nginx/default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

USER root

RUN mkdir -p /vol/static && \
    chmod -R 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown -R nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]
