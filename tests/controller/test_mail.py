from fastapi.testclient import TestClient

from madmails.main import app

test_client = TestClient(app)


def test_send_mail_with_wrong_input_returns_error():
    response = test_client.request(method="POST", url="/mail/send")
    assert response.status_code == 422
    assert response.reason == 'Unprocessable Entity'
    assert response.json() == {"detail": [{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}]}


def test_send_mail_delegate_correctly_to_sender_service(mocker):
    sender_mock = mocker.patch("madmails.service.factory.MailSenderFactory.get_mail_sender")
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
    assert sender_mock.call_count == 1
    # How do I mock this??
    # assert sender_mock.send.call_count == 1


def test_send_mail_factory_throws_error():
    # TODO: write this unit test after reading more about mocking in Python.
    assert True
