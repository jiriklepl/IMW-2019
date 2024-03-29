# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v2.resources import label_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_label__pb2
from google.ads.googleads.v2.services import label_service_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2


class LabelServiceStub(object):
  """Service to manage labels.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLabel = channel.unary_unary(
        '/google.ads.googleads.v2.services.LabelService/GetLabel',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2.GetLabelRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_label__pb2.Label.FromString,
        )
    self.MutateLabels = channel.unary_unary(
        '/google.ads.googleads.v2.services.LabelService/MutateLabels',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2.MutateLabelsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2.MutateLabelsResponse.FromString,
        )


class LabelServiceServicer(object):
  """Service to manage labels.
  """

  def GetLabel(self, request, context):
    """Returns the requested label in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateLabels(self, request, context):
    """Creates, updates, or removes labels. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LabelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLabel': grpc.unary_unary_rpc_method_handler(
          servicer.GetLabel,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2.GetLabelRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_label__pb2.Label.SerializeToString,
      ),
      'MutateLabels': grpc.unary_unary_rpc_method_handler(
          servicer.MutateLabels,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2.MutateLabelsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_label__service__pb2.MutateLabelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.LabelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
