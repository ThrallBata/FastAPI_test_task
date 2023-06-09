from datetime import date

from pydantic import BaseModel, EmailStr


class WorkerCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    is_active: bool
    password: str
    salary: float
    promotion_date: date


class ShowWorker(BaseModel):
    worker_id: int
    name: str
    surname: str
    email: EmailStr
    is_active: bool
    salary: float
    promotion_date: date


class ShowWorkerProfile(BaseModel):
    name: str
    surname: str
    salary: float
    promotion_date: date


class Token(BaseModel):
    access_token: str
    token_type: str


