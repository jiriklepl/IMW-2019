# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.services import conversion_upload_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2


class ConversionUploadServiceStub(object):
  """Service to upload conversions.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadClickConversions = channel.unary_unary(
        '/google.ads.googleads.v1.services.ConversionUploadService/UploadClickConversions',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadClickConversionsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadClickConversionsResponse.FromString,
        )
    self.UploadCallConversions = channel.unary_unary(
        '/google.ads.googleads.v1.services.ConversionUploadService/UploadCallConversions',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadCallConversionsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadCallConversionsResponse.FromString,
        )


class ConversionUploadServiceServicer(object):
  """Service to upload conversions.
  """

  def UploadClickConversions(self, request, context):
    """Processes the given click conversions.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadCallConversions(self, request, context):
    """Processes the given call conversions.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConversionUploadServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadClickConversions': grpc.unary_unary_rpc_method_handler(
          servicer.UploadClickConversions,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadClickConversionsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadClickConversionsResponse.SerializeToString,
      ),
      'UploadCallConversions': grpc.unary_unary_rpc_method_handler(
          servicer.UploadCallConversions,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadCallConversionsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__upload__service__pb2.UploadCallConversionsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.ConversionUploadService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
