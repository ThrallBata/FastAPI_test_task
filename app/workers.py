from typing import Union

from .schemas import ShowWorker
from .schemas import WorkerCreate
from .dals import WorkerDAL
from .hashing import Hasher
from .models import Worker


async def _create_new_worker(body: WorkerCreate, session) -> ShowWorker:
    async with session.begin():
        worker_dal = WorkerDAL(session)
        worker = await worker_dal.create_worker(
            name=body.name,
            surname=body.surname,
            email=body.email,
            hashed_password=Hasher.get_password_hash(body.password),
            salary=body.salary,
            promotion_date=body.promotion_date
        )
        return ShowWorker(
            worker_id=worker.worker_id,
            name=worker.name,
            surname=worker.surname,
            email=worker.email,
            is_active=worker.is_active,
            salary=worker.salary,
            promotion_date=worker.promotion_date
        )


async def _get_worker_by_id(worker_id, session) -> Union[Worker, None]:
    async with session.begin():
        worker_dal = WorkerDAL(session)
        worker = await worker_dal.get_worker_by_id(
            worker_id=worker_id,
        )
        if worker is not None:
            return worker


def check_worker_permissions(target_worker: Worker, current_worker: Worker) -> bool:
    if target_worker.worker_id != current_worker.worker_id:
        return False
    return True
