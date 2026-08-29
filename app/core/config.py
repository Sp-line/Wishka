import logging
from enum import StrEnum
from enum import auto
from pathlib import Path

from fastapi_mail import ConnectionConfig
from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import NatsDsn
from pydantic import PostgresDsn
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from app.core.types.log import LogLevel  # noqa: TC001

BASE_DIR: Path = Path(__file__).resolve().parent.parent


class RunConfig(BaseModel):
    host: str = "0.0.0.0"  # noqa: S104
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"


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
    reset_password_token_secret: SecretStr
    verification_token_secret: SecretStr

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
    subject: str = "taskiq.tasks"
    stream_name: str = "tasks_stream"
    durable: str = "worker_tasks"
    pull_consume_batch: int = 1
    pull_consume_timeout: float | None = None
    worker_queue: str = "default"
    log_format: str = "[%(asctime)s.%(msecs)03d][%(processName)s] %(module)16s:%(lineno)-3d %(levelname)-7s - %(message)s"  # noqa: E501


class MailConfig(BaseModel):
    mail_username: str
    mail_from: str
    mail_password: SecretStr
    mail_port: int = 465
    mail_server: str = "smtp.gmail.com"
    mail_starttls: bool = False
    mail_ssl_tls: bool = True
    use_credentials: bool = True
    validate_certs: bool = True
    template_folder: Path = BASE_DIR / "templates"

    @property
    def conf(self) -> ConnectionConfig:
        return ConnectionConfig(
            MAIL_USERNAME=self.mail_username,
            MAIL_PASSWORD=self.mail_password,
            MAIL_FROM=self.mail_from,
            MAIL_PORT=self.mail_port,
            MAIL_SERVER=self.mail_server,
            MAIL_STARTTLS=self.mail_starttls,
            MAIL_SSL_TLS=self.mail_ssl_tls,
            USE_CREDENTIALS=self.use_credentials,
            VALIDATE_CERTS=self.validate_certs,
            TEMPLATE_FOLDER=self.template_folder,
        )


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
    mail: MailConfig

    model_config = SettingsConfigDict(
        env_file=("app/.env.template", "app/.env", ".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        extra="ignore",
    )


settings = Settings()
