from datetime import timedelta

from fastapi import FastAPI, Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from .schemas import ShowWorker, WorkerCreate, Token, ShowWorkerProfile
from .workers import _create_new_worker
from .session import get_db
from .models import Worker
from app.auth.auth import authenticate_worker, get_current_worker_from_token
from app.auth.security import create_access_token


app = FastAPI()


@app.get("/profile", response_model=ShowWorkerProfile)
async def worker_inf(
    current_worker: Worker = Depends(get_current_worker_from_token),
) -> ShowWorkerProfile:
    return ShowWorkerProfile(
            name=current_worker.name,
            surname=current_worker.surname,
            salary=current_worker.salary,
            promotion_date=current_worker.promotion_date
        )


@app.post("/signup", response_model=ShowWorker)
async def create_worker(body: WorkerCreate, db: AsyncSession = Depends(get_db)) -> ShowWorker:
    try:
        return await _create_new_worker(body, db)
    except IntegrityError as err:
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


@app.post("/login/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    worker = await authenticate_worker(form_data.username, form_data.password, db)
    if not worker:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": worker.email,},
        expires_delta=access_token_expires,
    )
    return Token(
            access_token=access_token,
            token_type='bearer'
        )
