# FROM gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.14.2

# RUN cloud-sql-proxy gcp-devops-436118:us-central1:main-instance

FROM google/cloud-sdk:489.0.0-stable

RUN apt-get -y update; apt-get -y install curl

RUN curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.14.2/cloud-sql-proxy.linux.amd64

RUN chmod +x cloud-sql-proxy

CMD ["./cloud-sql-proxy", "--address", "0.0.0.0", "gcp-devops-436118:us-central1:main-instance"]
