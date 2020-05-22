# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import news_pb2 as news__pb2


class NewsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetNews = channel.unary_unary(
        '/pb.News/GetNews',
        request_serializer=news__pb2.GetNewsRequest.SerializeToString,
        response_deserializer=news__pb2.GetNewsResponse.FromString,
        )


class NewsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetNews(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NewsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetNews': grpc.unary_unary_rpc_method_handler(
          servicer.GetNews,
          request_deserializer=news__pb2.GetNewsRequest.FromString,
          response_serializer=news__pb2.GetNewsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pb.News', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
