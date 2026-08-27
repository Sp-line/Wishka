from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka as setup_fastapi_dishka
from fastapi import FastAPI
from taskiq_nats import PullBasedJetStreamBroker

from app.dependencies.infrastructure import InfrastructureProvider

if TYPE_CHECKING:
    from collections.abc import AsyncIterator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await app.state.dishka_container.get(PullBasedJetStreamBroker)

    yield


def create() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    container = make_async_container(
        InfrastructureProvider(),
    )

    setup_fastapi_dishka(container, app)

    return app
