"""
Interface module for a MailSender.
"""
from typing import Protocol

from madmails.model.mail import SendMailRequest


class MailSender(Protocol):
    """MailSender is an interface that expose a contract to send an email."""

    def send(self, send_mail_request: SendMailRequest):
        """Route and sends a mail given inputs from send_mail_request"""
