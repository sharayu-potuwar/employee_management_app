import os
import ssl

import sqlalchemy
from app.config import config


class Dbconnection:
    def __init__(self):
        pass

    def connect_tcp_socket(self) -> sqlalchemy.engine.base.Engine:
        """Initializes a TCP connection pool for a Cloud SQL instance of Postgres."""
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
        db_host = (
            config.DB_CONNECTION_NAME
        )  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
        db_user = config.DB_USER_NAME  # e.g. 'my-db-user'
        db_pass = config.DB_SECRET_NAME  # e.g. 'my-db-password'
        db_name = config.DB_NAME  # e.g. 'my-database'
        db_port = config.DB_PORT  # e.g. 5432

        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                host=db_host,
                port=db_port,
                database=db_name,
            ),
            # ...
        )
        return pool
