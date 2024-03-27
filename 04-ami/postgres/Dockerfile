FROM postgres:15
LABEL maintainer='Jan Rozhon <jan@rozhon.eu>'


COPY *.sql /docker-entrypoint-initdb.d/
COPY *.sh /docker-entrypoint-initdb.d/

