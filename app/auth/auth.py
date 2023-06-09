from typing import Union

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import settings
from ..dals import WorkerDAL
from ..models import Worker
from ..session import get_db
from ..hashing import Hasher

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def _get_worker_by_email_for_auth(email: str, session: AsyncSession):
    async with session.begin():
        worker_dal = WorkerDAL(session)
        return await worker_dal.get_worker_by_email(
            email=email,
        )


async def authenticate_worker(
    email: str, password: str, db: AsyncSession
) -> Union[Worker, None]:
    worker = await _get_worker_by_email_for_auth(email=email, session=db)
    if worker is None:
        return
    if not Hasher.verify_password(password, worker.hashed_password):
        return
    return worker


async def get_current_worker_from_token(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    worker = await _get_worker_by_email_for_auth(email=email, session=db)
    if worker is None:
        raise credentials_exception
    return worker
