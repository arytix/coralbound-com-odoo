FROM odoo:17.0

ARG LOCALE=en_US.UTF-8

ENV LANGUAGE=${LOCALE}
ENV LC_ALL=${LOCALE}
ENV LANG=${LOCALE}

USER 0

RUN apt-get -y update && apt-get install -y --no-install-recommends locales netcat-openbsd \
    && locale-gen ${LOCALE}

# Create directory for custom addons
RUN mkdir -p /mnt/custom-addons && \
    chown -R odoo:odoo /mnt/custom-addons

WORKDIR /app

# Copy custom addons
COPY ./custom-addons /mnt/custom-addons/

COPY --chmod=755 entrypoint.sh ./

ENTRYPOINT ["/bin/sh"]

CMD ["entrypoint.sh"]
