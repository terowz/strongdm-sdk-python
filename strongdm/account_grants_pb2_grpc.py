# Copyright 2020 StrongDM Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import account_grants_pb2 as account__grants__pb2


class AccountGrantsStub(object):
    """AccountGrants assign a resource directly to an account, giving the account the permission to connect to that resource.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.AccountGrants/Create',
                request_serializer=account__grants__pb2.AccountGrantCreateRequest.SerializeToString,
                response_deserializer=account__grants__pb2.AccountGrantCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.AccountGrants/Get',
                request_serializer=account__grants__pb2.AccountGrantGetRequest.SerializeToString,
                response_deserializer=account__grants__pb2.AccountGrantGetResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.AccountGrants/Delete',
                request_serializer=account__grants__pb2.AccountGrantDeleteRequest.SerializeToString,
                response_deserializer=account__grants__pb2.AccountGrantDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.AccountGrants/List',
                request_serializer=account__grants__pb2.AccountGrantListRequest.SerializeToString,
                response_deserializer=account__grants__pb2.AccountGrantListResponse.FromString,
                )


class AccountGrantsServicer(object):
    """AccountGrants assign a resource directly to an account, giving the account the permission to connect to that resource.
    """

    def Create(self, request, context):
        """Create registers a new AccountGrant.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one AccountGrant by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete removes a AccountGrant by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List gets a list of AccountGrants matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountGrantsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=account__grants__pb2.AccountGrantCreateRequest.FromString,
                    response_serializer=account__grants__pb2.AccountGrantCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=account__grants__pb2.AccountGrantGetRequest.FromString,
                    response_serializer=account__grants__pb2.AccountGrantGetResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=account__grants__pb2.AccountGrantDeleteRequest.FromString,
                    response_serializer=account__grants__pb2.AccountGrantDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=account__grants__pb2.AccountGrantListRequest.FromString,
                    response_serializer=account__grants__pb2.AccountGrantListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.AccountGrants', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountGrants(object):
    """AccountGrants assign a resource directly to an account, giving the account the permission to connect to that resource.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.AccountGrants/Create',
            account__grants__pb2.AccountGrantCreateRequest.SerializeToString,
            account__grants__pb2.AccountGrantCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.AccountGrants/Get',
            account__grants__pb2.AccountGrantGetRequest.SerializeToString,
            account__grants__pb2.AccountGrantGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.AccountGrants/Delete',
            account__grants__pb2.AccountGrantDeleteRequest.SerializeToString,
            account__grants__pb2.AccountGrantDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.AccountGrants/List',
            account__grants__pb2.AccountGrantListRequest.SerializeToString,
            account__grants__pb2.AccountGrantListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
