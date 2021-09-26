"""
Factory that helps create MailSender objects.
"""
from madmails.model.sender_type import MailSenderType
from madmails.service.gmail.impl import GmailSender
from madmails.service.mail import MailSender


class MailSenderFactory:
    """
    Factory that helps create MailSender objects.
    """

    @staticmethod
    def get_mail_sender(mail_sender_type: MailSenderType) -> MailSender:
        """
        Return the appropriate MailSender given a MailSenderType.

        Args:
            mail_sender_type: is the service to use for sending mails

        Returns:
            the wanted implementation of MailSender

        Raises:
            NotImplementedError if no implementation has been found.
        """
        if mail_sender_type == MailSenderType.GMAIL:
            return GmailSender()

        raise NotImplementedError(f"sender {mail_sender_type} has not been implemented yet")
