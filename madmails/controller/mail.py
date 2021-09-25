import fastapi
from loguru import logger

from madmails.model.mail import SendMailRequest

router = fastapi.APIRouter()


@router.post("/mail/send")
async def send_email(send_mail_request: SendMailRequest):
    logger.info(f"Content of the mail is: [{send_mail_request}]")
    return send_mail_request
