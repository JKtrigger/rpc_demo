from concurrent.futures import ThreadPoolExecutor

import grpc
import service_chat


def _message():
    return "100"


def _author():
    return "maxim"


class ChattingService(service_chat.ChattingServicer):
    """ Some Chat Server Logic
    """
    collect_message = []

    def MessageStream(self, request: service_chat.NullMessage, context: dict):
        """Need to implement something """
        yield service_chat.Message(author=_author(), text=_message())
        gen = iter(self.collect_message)
        yield next(gen)

    def SendMessage(self, message: service_chat.Message, context: dict):
        """Need to implement something """
        self.collect_message.append(message)
        return service_chat.NullMessage()


class ChatServer:
    def __init__(self):
        self.port = 5001
        self.host = '[::]'
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        service_chat.add_rpc_chat(ChattingService(), self.server)

    def serve(self):
        self.server.add_insecure_port(f'{self.host}:{self.port}')
        self.server.start()
        print(f'Listening on {self.host}:{self.port}')
        print('Press CTRL+C to stop...')
        try:
            self.server.wait_for_termination()
        except KeyboardInterrupt:
            self.server.stop(None)


if __name__ == "__main__":
    chat_server = ChatServer()
    chat_server.serve()
