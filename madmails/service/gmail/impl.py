"""
Implementation of a MailSender using Gmail.
"""
from madmails.model.mail import SendMailRequest

from loguru import logger


class GmailSender:
    """
    Connector to the Gmail API for sending emails.
    More information from the documentation here: https://developers.google.com/gmail/api/guides
    """

    def send(self, send_mail_request: SendMailRequest):
        logger.info(f"Sending mail using Gmail API: [{send_mail_request}]")
