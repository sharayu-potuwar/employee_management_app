import os
from app.utils import secrets

secret = secrets.Secret()


PROJECT_ID = os.environ["PROJECT_ID"]
SECRET_ID = os.environ["SECRET_ID"]

DB_CONNECTION_NAME = os.environ["DB_CONNECTION_NAME"]
DB_USER_NAME = os.environ["DB_USER_NAME"]
DB_SECRET_NAME = secret.access_secret_version(PROJECT_ID, SECRET_ID, 1)
DB_NAME = os.environ["DB_NAME"]
DB_PORT = os.environ["DB_PORT"]
