import os
from envparse import Env

from dotenv import load_dotenv

load_dotenv()
env = Env()

# REAL_DATABASE_URL = os.environ.get(
#     "REAL_DATABASE_URL",
#     "postgresql+asyncpg://postgres:02vfrcbv@0.0.0.0:5432/postgres1",
# )
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
REAL_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

APP_PORT = env.int("APP_PORT", default="8080")

#settings token
SECRET_KEY = env.str("SECRET_KEY", default="secret_key")
ALGORITHM = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)

