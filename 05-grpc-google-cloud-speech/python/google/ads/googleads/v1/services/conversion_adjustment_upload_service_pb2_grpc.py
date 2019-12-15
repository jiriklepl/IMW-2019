# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.services import conversion_adjustment_upload_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__adjustment__upload__service__pb2


class ConversionAdjustmentUploadServiceStub(object):
  """Service to upload conversion adjustments.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadConversionAdjustments = channel.unary_unary(
        '/google.ads.googleads.v1.services.ConversionAdjustmentUploadService/UploadConversionAdjustments',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__adjustment__upload__service__pb2.UploadConversionAdjustmentsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__adjustment__upload__service__pb2.UploadConversionAdjustmentsResponse.FromString,
        )


class ConversionAdjustmentUploadServiceServicer(object):
  """Service to upload conversion adjustments.
  """

  def UploadConversionAdjustments(self, request, context):
    """Processes the given conversion adjustments.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConversionAdjustmentUploadServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadConversionAdjustments': grpc.unary_unary_rpc_method_handler(
          servicer.UploadConversionAdjustments,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__adjustment__upload__service__pb2.UploadConversionAdjustmentsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__adjustment__upload__service__pb2.UploadConversionAdjustmentsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.ConversionAdjustmentUploadService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
