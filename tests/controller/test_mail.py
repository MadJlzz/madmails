from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from madmails.main import app

test_client = TestClient(app)


def test_send_mail_with_wrong_input_returns_error():
    response = test_client.request(method="POST", url="/mail/send")
    assert response.status_code == 422
    assert response.reason == 'Unprocessable Entity'
    assert response.json() == {"detail": [{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}]}


def test_send_mail_delegate_correctly_to_sender_service(mocker: MockerFixture):
    # Important: https://docs.python.org/3/library/unittest.mock.html#where-to-patch
    factory_mock = mocker.patch("madmails.controller.mail.MailSenderFactory.get_mail_sender", autospec=True)

    response = test_client.request(method="POST",
                                   url="/mail/send",
                                   headers={"Content-Type": "application/json"},
                                   json={
                                       "to_recipient": ["foo@bar.dev"],
                                       "cc_recipient": ["bar@foo.dev"],
                                       "subject": "theSubject",
                                       "body": "theBody",
                                       "footer": "theFooter"
                                   })
    assert response.status_code == 200
    assert factory_mock.called is True
    assert factory_mock.return_value.send.call_count == 1


def test_send_mail_factory_throws_error(mocker: MockerFixture):
    factory_mock = mocker.patch("madmails.controller.mail.MailSenderFactory.get_mail_sender", autospec=True)
    factory_mock.side_effect = NotImplementedError()

    response = test_client.request(method="POST",
                                   url="/mail/send",
                                   headers={"Content-Type": "application/json"},
                                   json={
                                       "to_recipient": ["foo@bar.dev"],
                                       "cc_recipient": ["bar@foo.dev"],
                                       "subject": "theSubject",
                                       "body": "theBody",
                                       "footer": "theFooter"
                                   })

    assert response.status_code == 500
    assert response.reason == "Internal Server Error"
