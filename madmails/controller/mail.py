"""
This module expose endpoints related to the mail resource.
"""
import fastapi
from loguru import logger

from madmails.model.mail import SendMailRequest
from madmails.model.sender_type import MailSenderType
from madmails.service.factory import MailSenderFactory

router = fastapi.APIRouter()


@router.post("/mail/send")
async def send_email(send_mail_request: SendMailRequest):
    logger.info(f"Content of the mail is: [{send_mail_request}]")

    # Delegating the sending to the appropriate service.
    # TODO: get the configuration of the MailSenderType through a configuration file / environment variables.
    mail_sender = MailSenderFactory.get_mail_sender(MailSenderType.GMAIL)
    mail_sender.send(send_mail_request)

    return {"message": "success"}
