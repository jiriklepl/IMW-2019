# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import ad_schedule_view_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__schedule__view__pb2
from google.ads.googleads.v1.services import ad_schedule_view_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__schedule__view__service__pb2


class AdScheduleViewServiceStub(object):
  """Proto file describing the AdSchedule View service.

  Service to fetch ad schedule views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAdScheduleView = channel.unary_unary(
        '/google.ads.googleads.v1.services.AdScheduleViewService/GetAdScheduleView',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__schedule__view__service__pb2.GetAdScheduleViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__schedule__view__pb2.AdScheduleView.FromString,
        )


class AdScheduleViewServiceServicer(object):
  """Proto file describing the AdSchedule View service.

  Service to fetch ad schedule views.
  """

  def GetAdScheduleView(self, request, context):
    """Returns the requested ad schedule view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdScheduleViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAdScheduleView': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdScheduleView,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__schedule__view__service__pb2.GetAdScheduleViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__schedule__view__pb2.AdScheduleView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.AdScheduleViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
