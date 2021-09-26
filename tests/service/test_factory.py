import pytest

from madmails.model.sender_type import MailSenderType
from madmails.service.factory import MailSenderFactory
from madmails.service.gmail.impl import GmailSender


def test_factory_return_gmail_sender_when_sender_type_gmail():
    mail_sender = MailSenderFactory.get_mail_sender(MailSenderType.GMAIL)
    assert isinstance(mail_sender, GmailSender)


def test_factory_raise_error_when_unknown_sender_type():
    with pytest.raises(NotImplementedError):
        MailSenderFactory.get_mail_sender(MailSenderType.SENDGRID)
