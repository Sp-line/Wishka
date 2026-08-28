from dishka.integrations.taskiq import FromDishka
from dishka.integrations.taskiq import inject
from fastapi_mail import FastMail
from fastapi_mail import MessageSchema
from fastapi_mail import MessageType
from pydantic import EmailStr
from pydantic import NameEmail

from app.core.taskiq_broker import broker


@broker.task
@inject(patch_module=True)
async def send_verification_email_task(
    fm: FromDishka[FastMail],
    email_to: EmailStr,
    verification_link: str,
) -> None:
    recipient = NameEmail(name="Wishka User", email=str(email_to))
    message = MessageSchema(
        subject="Verify your email address on Wishka",
        recipients=[recipient],
        template_body={"link": verification_link},
        subtype=MessageType.html,
    )

    await fm.send_message(message, template_name="mail/verify_email.html")


@broker.task
@inject(patch_module=True)
async def send_reset_password_email_task(
    fm: FromDishka[FastMail],
    email_to: EmailStr,
    reset_link: str,
) -> None:
    recipient = NameEmail(name="Wishka User", email=str(email_to))
    message = MessageSchema(
        subject="Reset your Wishka password",
        recipients=[recipient],
        template_body={"link": reset_link},
        subtype=MessageType.html,
    )

    await fm.send_message(message, template_name="mail/reset_password.html")
