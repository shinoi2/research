# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import plate_pb2 as plate__pb2


class PlateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.predict = channel.unary_unary(
                '/PlateService/predict',
                request_serializer=plate__pb2.PlateRequest.SerializeToString,
                response_deserializer=plate__pb2.PlateResponse.FromString,
                )


class PlateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'predict': grpc.unary_unary_rpc_method_handler(
                    servicer.predict,
                    request_deserializer=plate__pb2.PlateRequest.FromString,
                    response_serializer=plate__pb2.PlateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PlateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PlateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PlateService/predict',
            plate__pb2.PlateRequest.SerializeToString,
            plate__pb2.PlateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
