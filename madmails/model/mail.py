"""
This module contains the models related to the mail API.
"""
from typing import Optional, Set

from pydantic import BaseModel


class SendMailRequest(BaseModel):
    """
    `SendMailRequest` is the model used for someone that wants
    to send a mail.

    Attributes:

        - to_recipient is a list of unique persons that are the direct recipient of the mail
        - cc_recipient is a list of unique persons that are in copy of the mail
        - subject is the title of the mail
        - body is the content to pass for the mail
        - footer is the content located at the end of the mail. Generally, this is a signature.
    """
    to_recipient: Set[str]
    cc_recipient: Optional[Set[str]]

    subject: str
    body: str
    footer: Optional[str]
