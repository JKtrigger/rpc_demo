import server
from service_chat import NullMessage

# 
def test_chatting_service():
    chatting = server.ChattingService()
    response = chatting.MessageStream(NullMessage, {})
    response = next(response)
    assert response.author == 'maxim'
    assert response.text == '100'


def test_send_message():
    chatting = server.ChattingService()
    message = chatting.MessageStream(NullMessage, {})
    response = chatting.SendMessage(message, {})
    assert response.ListFields() == []
