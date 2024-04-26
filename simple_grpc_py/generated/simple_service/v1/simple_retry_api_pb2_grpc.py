"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ...simple_service.v1 import simple_retry_api_pb2 as simple__service_dot_v1_dot_simple__retry__api__pb2

class SimpleRetryAPIStub(object):
    """A configurable retry api
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RetriableAction = channel.unary_unary('/simple_service.v1.SimpleRetryAPI/RetriableAction', request_serializer=simple__service_dot_v1_dot_simple__retry__api__pb2.RetriableActionRequest.SerializeToString, response_deserializer=simple__service_dot_v1_dot_simple__retry__api__pb2.RetriableActionResponse.FromString)

class SimpleRetryAPIServicer(object):
    """A configurable retry api
    """

    def RetriableAction(self, request, context):
        """request a specific series of responses
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SimpleRetryAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {'RetriableAction': grpc.unary_unary_rpc_method_handler(servicer.RetriableAction, request_deserializer=simple__service_dot_v1_dot_simple__retry__api__pb2.RetriableActionRequest.FromString, response_serializer=simple__service_dot_v1_dot_simple__retry__api__pb2.RetriableActionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('simple_service.v1.SimpleRetryAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SimpleRetryAPI(object):
    """A configurable retry api
    """

    @staticmethod
    def RetriableAction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simple_service.v1.SimpleRetryAPI/RetriableAction', simple__service_dot_v1_dot_simple__retry__api__pb2.RetriableActionRequest.SerializeToString, simple__service_dot_v1_dot_simple__retry__api__pb2.RetriableActionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)