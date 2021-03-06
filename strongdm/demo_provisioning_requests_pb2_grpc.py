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

from . import demo_provisioning_requests_pb2 as demo__provisioning__requests__pb2


class DemoProvisioningRequestsStub(object):
    """DemoProvisioningRequests coordinate provisioning of demo resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.DemoProvisioningRequests/Create',
                request_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestCreateRequest.SerializeToString,
                response_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestCreateResponse.FromString,
                )
        self.ListForOrganization = channel.unary_unary(
                '/v1.DemoProvisioningRequests/ListForOrganization',
                request_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListForOrganizationRequest.SerializeToString,
                response_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListForOrganizationResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.DemoProvisioningRequests/Delete',
                request_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestDeleteRequest.SerializeToString,
                response_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestDeleteResponse.FromString,
                )
        self.ListAll = channel.unary_unary(
                '/v1.DemoProvisioningRequests/ListAll',
                request_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListAllRequest.SerializeToString,
                response_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListAllResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/v1.DemoProvisioningRequests/Update',
                request_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestUpdateRequest.SerializeToString,
                response_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestUpdateResponse.FromString,
                )


class DemoProvisioningRequestsServicer(object):
    """DemoProvisioningRequests coordinate provisioning of demo resources.
    """

    def Create(self, request, context):
        """Create
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListForOrganization(self, request, context):
        """ListForOrganization gets a list of DemoProvisioningRequests in your organization
        matching a given set of criteria. This operation can be done by account
        administrators.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete deletes a DemoProvisioningRequest.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAll(self, request, context):
        """ListAll gets a list of DemoProvisioningRequests across all orgs matching a given
        set of criteria. This operation can only be done by operators and the
        trial provisioner.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update updates a DemoProvisioningRequest.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DemoProvisioningRequestsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestCreateRequest.FromString,
                    response_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestCreateResponse.SerializeToString,
            ),
            'ListForOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.ListForOrganization,
                    request_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListForOrganizationRequest.FromString,
                    response_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListForOrganizationResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestDeleteRequest.FromString,
                    response_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestDeleteResponse.SerializeToString,
            ),
            'ListAll': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAll,
                    request_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListAllRequest.FromString,
                    response_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestListAllResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=demo__provisioning__requests__pb2.DemoProvisioningRequestUpdateRequest.FromString,
                    response_serializer=demo__provisioning__requests__pb2.DemoProvisioningRequestUpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.DemoProvisioningRequests', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DemoProvisioningRequests(object):
    """DemoProvisioningRequests coordinate provisioning of demo resources.
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
        return grpc.experimental.unary_unary(request, target, '/v1.DemoProvisioningRequests/Create',
            demo__provisioning__requests__pb2.DemoProvisioningRequestCreateRequest.SerializeToString,
            demo__provisioning__requests__pb2.DemoProvisioningRequestCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListForOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.DemoProvisioningRequests/ListForOrganization',
            demo__provisioning__requests__pb2.DemoProvisioningRequestListForOrganizationRequest.SerializeToString,
            demo__provisioning__requests__pb2.DemoProvisioningRequestListForOrganizationResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.DemoProvisioningRequests/Delete',
            demo__provisioning__requests__pb2.DemoProvisioningRequestDeleteRequest.SerializeToString,
            demo__provisioning__requests__pb2.DemoProvisioningRequestDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.DemoProvisioningRequests/ListAll',
            demo__provisioning__requests__pb2.DemoProvisioningRequestListAllRequest.SerializeToString,
            demo__provisioning__requests__pb2.DemoProvisioningRequestListAllResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.DemoProvisioningRequests/Update',
            demo__provisioning__requests__pb2.DemoProvisioningRequestUpdateRequest.SerializeToString,
            demo__provisioning__requests__pb2.DemoProvisioningRequestUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
