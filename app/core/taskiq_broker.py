import logging

import taskiq_fastapi
from taskiq import TaskiqEvents
from taskiq import TaskiqState
from taskiq.middlewares import TaskiqAdminMiddleware
from taskiq_nats import PullBasedJetStreamBroker

from app.core.config import settings

log = logging.getLogger(__name__)

broker = PullBasedJetStreamBroker(
    servers=str(settings.taskiq.url),
    subject=settings.taskiq.subject,
    stream_name=settings.taskiq.stream_name,
    durable=settings.taskiq.durable,
    pull_consume_batch=settings.taskiq.pull_consume_batch,
    pull_consume_timeout=settings.taskiq.pull_consume_timeout,
).with_middlewares(
    TaskiqAdminMiddleware(
        url=str(settings.taskiq.admin_url),
        api_token=settings.taskiq.api_token.get_secret_value(),
        taskiq_broker_name=settings.taskiq.broker_name,
    ),
)

taskiq_fastapi.init(broker, "main:app")


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def on_worker_startup(state: TaskiqState) -> None:
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.taskiq.log_format,
        datefmt=settings.logging.log_datefmt,
    )
    log.info("Worker startup complete, got state: %s", state)
