import grpc

from service_chat import ChattingStub, Message


def send_message():
    channel = grpc.insecure_channel('127.0.0.1:5001')
    stub = ChattingStub(channel)
    message = Message()
    message.author = "username"
    message.text = "text"
    stub.SendMessage(message)
    for i in stub.MessageStream(message):
        print(i.text, i.author)
    channel.close()


if __name__ == "__main__":
    send_message()
