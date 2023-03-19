from chat.proto import chat_pb2_grpc as service
from chat.proto import chat_pb2 as scheme

Message = scheme.Message
ChattingStub = service.ChattingStub
ChattingServicer = service.ChattingServicer
add_rpc_chat = service.add_ChattingServicer_to_server
NullMessage = scheme.Null

__all__ = ["Message", "ChattingStub", "ChattingServicer", "NullMessage", "add_rpc_chat"]
