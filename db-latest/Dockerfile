FROM mariadb:11.2

ENV MARIADB_ROOT_PASSWORD=1234
ENV MARIADB_DATABASE=chatbot

COPY ./init.sql /docker-entrypoint-initdb.d/

VOLUME /var/lib/mysql

EXPOSE 3300