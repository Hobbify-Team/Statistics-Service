FROM postgres:10.5

COPY ./compose/local/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
    
COPY ./compose/local/postgres/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start