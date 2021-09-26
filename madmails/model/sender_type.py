"""
This module defines the mail senders that are supported.
"""
from enum import Enum


class MailSenderType(str, Enum):
    GMAIL = "gmail"
