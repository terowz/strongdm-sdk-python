# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import accounts_pb2 as accounts__pb2


class AccountsStub(object):
  """Accounts are users, services or tokens who connect to and act within the strongDM network.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/v1.Accounts/Create',
        request_serializer=accounts__pb2.AccountCreateRequest.SerializeToString,
        response_deserializer=accounts__pb2.AccountCreateResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/v1.Accounts/Get',
        request_serializer=accounts__pb2.AccountGetRequest.SerializeToString,
        response_deserializer=accounts__pb2.AccountGetResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/v1.Accounts/Update',
        request_serializer=accounts__pb2.AccountUpdateRequest.SerializeToString,
        response_deserializer=accounts__pb2.AccountUpdateResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/v1.Accounts/Delete',
        request_serializer=accounts__pb2.AccountDeleteRequest.SerializeToString,
        response_deserializer=accounts__pb2.AccountDeleteResponse.FromString,
        )
    self.List = channel.unary_unary(
        '/v1.Accounts/List',
        request_serializer=accounts__pb2.AccountListRequest.SerializeToString,
        response_deserializer=accounts__pb2.AccountListResponse.FromString,
        )


class AccountsServicer(object):
  """Accounts are users, services or tokens who connect to and act within the strongDM network.
  """

  def Create(self, request, context):
    """Create registers a new Account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get reads one Account by ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update patches a Account by ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete removes a Account by ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List gets a list of Accounts matching a given set of criteria.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccountsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=accounts__pb2.AccountCreateRequest.FromString,
          response_serializer=accounts__pb2.AccountCreateResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=accounts__pb2.AccountGetRequest.FromString,
          response_serializer=accounts__pb2.AccountGetResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=accounts__pb2.AccountUpdateRequest.FromString,
          response_serializer=accounts__pb2.AccountUpdateResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=accounts__pb2.AccountDeleteRequest.FromString,
          response_serializer=accounts__pb2.AccountDeleteResponse.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=accounts__pb2.AccountListRequest.FromString,
          response_serializer=accounts__pb2.AccountListResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.Accounts', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
