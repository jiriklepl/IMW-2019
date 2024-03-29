# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v2.resources import gender_view_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_gender__view__pb2
from google.ads.googleads.v2.services import gender_view_service_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_services_dot_gender__view__service__pb2


class GenderViewServiceStub(object):
  """Proto file describing the Gender View service.

  Service to manage gender views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetGenderView = channel.unary_unary(
        '/google.ads.googleads.v2.services.GenderViewService/GetGenderView',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_gender__view__service__pb2.GetGenderViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_gender__view__pb2.GenderView.FromString,
        )


class GenderViewServiceServicer(object):
  """Proto file describing the Gender View service.

  Service to manage gender views.
  """

  def GetGenderView(self, request, context):
    """Returns the requested gender view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GenderViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetGenderView': grpc.unary_unary_rpc_method_handler(
          servicer.GetGenderView,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_gender__view__service__pb2.GetGenderViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_gender__view__pb2.GenderView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.GenderViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
