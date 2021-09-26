import pytest
from pydantic import ValidationError

from madmails.model.mail import SendMailRequest


def test_recipient_with_invalid_address_throw_validation_error():
    with pytest.raises(ValidationError):
        SendMailRequest(to_recipient={"notAValidEmailAddress"},
                        cc_recipient={"alsoNotAValidEmailAddress"},
                        subject="theSubject",
                        body="theBody")


def test_request_with_required_field_not_set_throw_validation_error():
    with pytest.raises(ValidationError):
        SendMailRequest(cc_recipient={"foo@bar.dev"}, footer="theFoot")


def test_correct_request_model_with_all_fields():
    request = SendMailRequest(to_recipient={"foo@bar.dev"},
                              cc_recipient={"bar@foo.dev"},
                              subject="theSubject",
                              body="theBody",
                              footer="theFooter")
    assert request.to_recipient is not None
    assert request.cc_recipient is not None
    assert request.subject is not None
    assert request.body is not None
    assert request.footer is not None


def test_correct_request_model_with_required_only_fields():
    request = SendMailRequest(
        to_recipient={"foo@bar.dev"},
        subject="theSubject",
        body="theBody",
    )
    assert request.cc_recipient is None
    assert request.footer is None
