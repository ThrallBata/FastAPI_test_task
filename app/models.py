from sqlalchemy import Boolean, Integer, Float, DateTime
from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Worker(Base):
    __tablename__ = "workers"

    worker_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    promotion_date = Column(DateTime, nullable=False)
