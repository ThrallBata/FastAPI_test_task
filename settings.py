import os
from envparse import Env
import os

from dotenv import load_dotenv

load_dotenv()
env = Env()

REAL_DATABASE_URL = os.environ.get(
    "REAL_DATABASE_URL",
    "postgresql+asyncpg://postgres:02vfrcbv@0.0.0.0:5432/postgres1",
)

APP_PORT = env.int("APP_PORT", default="8080")

#settings token
SECRET_KEY = env.str("SECRET_KEY", default="secret_key")
ALGORITHM = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)

