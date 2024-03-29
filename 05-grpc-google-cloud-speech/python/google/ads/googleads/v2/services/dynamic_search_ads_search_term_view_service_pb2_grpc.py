# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v2.resources import dynamic_search_ads_search_term_view_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_dynamic__search__ads__search__term__view__pb2
from google.ads.googleads.v2.services import dynamic_search_ads_search_term_view_service_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_services_dot_dynamic__search__ads__search__term__view__service__pb2


class DynamicSearchAdsSearchTermViewServiceStub(object):
  """Proto file describing the Dynamic Search Ads Search Term View service.

  Service to fetch dynamic search ads views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDynamicSearchAdsSearchTermView = channel.unary_unary(
        '/google.ads.googleads.v2.services.DynamicSearchAdsSearchTermViewService/GetDynamicSearchAdsSearchTermView',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_dynamic__search__ads__search__term__view__service__pb2.GetDynamicSearchAdsSearchTermViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_dynamic__search__ads__search__term__view__pb2.DynamicSearchAdsSearchTermView.FromString,
        )


class DynamicSearchAdsSearchTermViewServiceServicer(object):
  """Proto file describing the Dynamic Search Ads Search Term View service.

  Service to fetch dynamic search ads views.
  """

  def GetDynamicSearchAdsSearchTermView(self, request, context):
    """Returns the requested dynamic search ads search term view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DynamicSearchAdsSearchTermViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDynamicSearchAdsSearchTermView': grpc.unary_unary_rpc_method_handler(
          servicer.GetDynamicSearchAdsSearchTermView,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_dynamic__search__ads__search__term__view__service__pb2.GetDynamicSearchAdsSearchTermViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_dynamic__search__ads__search__term__view__pb2.DynamicSearchAdsSearchTermView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.DynamicSearchAdsSearchTermViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
