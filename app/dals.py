from datetime import date
from typing import Union

from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from .models import Worker


###########################################################
# BLOCK FOR INTERACTION WITH DATABASE IN BUSINESS CONTEXT #
###########################################################


class WorkerDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_worker(
        self,
        name: str,
        surname: str,
        email: EmailStr,
        hashed_password: str,
        salary: float,
        promotion_date: date,
    ) -> Worker:
        new_worker = Worker(
            name=name,
            surname=surname,
            email=email,
            hashed_password=hashed_password,
            salary=salary,
            promotion_date=promotion_date,
        )
        self.db_session.add(new_worker)
        await self.db_session.flush()
        return new_worker

    async def get_worker_by_id(self, worker_id: int) -> Union[Worker, None]:
        query = select(Worker).where(Worker.worker_id == worker_id)
        res = await self.db_session.execute(query)
        worker_row = res.fetchone()
        if worker_row is not None:
            return worker_row[0]

    async def get_worker_by_email(self, email: str) -> Union[Worker, None]:
        query = select(Worker).where(Worker.email == email)
        res = await self.db_session.execute(query)
        worker_row = res.fetchone()
        if worker_row is not None:
            return worker_row[0]

