FROM python:3-slim

RUN useradd -m -U gdc

COPY --chown=gdc:gdc gitea_declarative_config /home/gdc/src/gitea_declarative_config
COPY --chown=akf:akf files /

RUN pip install /home/gdc/src/gitea_declarative_config
#  && chmod 644 /tmp/certs \
#  && mv /tmp/certs/* /usr/local/share/ca-certificates/ \
#  && update-ca-certificates

USER gdc
WORKDIR /home/gdc

ENTRYPOINT [ "/entrypoint.sh" ]