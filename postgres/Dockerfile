# PostgreSQL 18 (latest stable major) on Debian
FROM postgres:18.6

# Debian 13 dropped legacy zone names from tzdata; Windows JVMs (DBeaver)
# still send Asia/Katmandu, so alias it to the current name
RUN ln -s Kathmandu /usr/share/zoneinfo/Asia/Katmandu

# Init scripts run once, on first start with an empty data volume
COPY init/ /docker-entrypoint-initdb.d/

EXPOSE 5432
