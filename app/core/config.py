import logging
from enum import StrEnum
from enum import auto

from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import NatsDsn
from pydantic import PostgresDsn
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from app.core.types.log import LogLevel  # noqa: TC001


class RunConfig(BaseModel):
    host: str = "0.0.0.0"  # noqa: S104
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DBDriver(StrEnum):
    ASYNCPG = auto()
    PSYCOPG = auto()


class TestDBConfig(BaseModel):
    image: str = "postgres:15-alpine"
    driver: DBDriver = DBDriver.ASYNCPG


class TestAPIConfig(BaseModel):
    base_url: HttpUrl = HttpUrl("http://test")


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AuthConfig(BaseModel):
    secret: SecretStr
    reset_password_token_secret: str
    verification_token_secret: str

    lifetime_seconds: int = 86400 * 7
    cookie_secure: bool

    verification_link: HttpUrl = HttpUrl("http://localhost:3000/login?token={token}")
    reset_link: HttpUrl = HttpUrl("http://localhost:3000/reset-password?token={token}")


class ClientConfig(BaseModel):
    client_id: str
    client_secret: str
    redirect_url: HttpUrl
    associate_by_email: bool = True
    is_verified_by_default: bool = True


class GoogleConfig(ClientConfig):
    redirect_url: HttpUrl = HttpUrl("http://localhost:3000/google/callback/")


class OAuthClientConfig(BaseModel):
    google: GoogleConfig


class LoggingConfig(BaseModel):
    log_level: LogLevel = "info"
    log_format: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"  # noqa: E501
    log_datefmt: str = "%Y-%m-%d %H:%M:%S"

    @property
    def log_level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level.upper()]


class TaskiqConfig(BaseModel):
    url: NatsDsn
    subject: str = "taskiq.tasks.>"
    stream_name: str = "tasks_stream"
    pull_consume_batch: int = 1
    pull_consume_timeout: float | None = None
    worker_queue: str = "default"
    log_format: str = "[%(asctime)s.%(msecs)03d][%(processName)s] %(module)16s:%(lineno)-3d %(levelname)-7s - %(message)s"  # noqa: E501

    @property
    def durable(self) -> str:
        return f"worker_{self.worker_queue}"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    test_db: TestDBConfig = TestDBConfig()
    test_api: TestAPIConfig = TestAPIConfig()
    logging: LoggingConfig = LoggingConfig()
    db: DatabaseConfig
    auth: AuthConfig
    oauth: OAuthClientConfig
    taskiq: TaskiqConfig

    model_config = SettingsConfigDict(
        env_file=("app/.env.template", "app/.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        extra="ignore",
    )


settings = Settings()
