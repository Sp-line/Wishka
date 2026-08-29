from collections.abc import AsyncIterable  # noqa: TC003
from collections.abc import AsyncIterator  # noqa: TC003
from typing import Any

import aioboto3
from dishka import Provider
from dishka import Scope
from dishka import provide
from fastapi_mail import FastMail
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002
from taskiq_nats import PullBasedJetStreamBroker  # noqa: TC002
from types_aiobotocore_s3 import S3Client  # noqa: TC002

from app.core.config import settings
from app.core.models.db import Database
from app.core.taskiq_broker import broker


class InfrastructureProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_database(self) -> AsyncIterator[Database]:  # pragma: no cover
        db = Database(
            url=str(settings.db.url),
            echo=settings.db.echo,
            echo_pool=settings.db.echo_pool,
            pool_size=settings.db.pool_size,
            max_overflow=settings.db.max_overflow,
        )

        yield db

        await db.dispose()

    @provide(scope=Scope.REQUEST)
    async def get_db_session(
        self,
        db: Database,
    ) -> AsyncIterator[AsyncSession]:  # pragma: no cover
        async for session in db.session_getter():
            yield session

    @provide(scope=Scope.APP)
    async def get_taskiq_broker(
        self,
    ) -> AsyncIterable[PullBasedJetStreamBroker]:  # pragma: no cover
        if not broker.is_worker_process:
            await broker.startup()

        yield broker

        if not broker.is_worker_process:
            await broker.shutdown()

    @provide(scope=Scope.APP)
    async def get_fast_mail(self) -> FastMail:
        return FastMail(settings.mail.conf)

    @provide(scope=Scope.APP)
    def get_aioboto3_session(self) -> aioboto3.Session:
        return aioboto3.Session()

    @provide(scope=Scope.APP)
    async def get_s3_client(self, session: aioboto3.Session) -> AsyncIterator[S3Client]:
        client_kwargs: dict[str, Any] = {
            "service_name": "s3",
            "region_name": settings.s3.region,
            "endpoint_url": str(settings.s3.endpoint_url),
            "aws_access_key_id": settings.s3.access_key.get_secret_value(),
            "aws_secret_access_key": settings.s3.secret_key.get_secret_value(),
        }

        async with session.client(**client_kwargs) as client:
            yield client
