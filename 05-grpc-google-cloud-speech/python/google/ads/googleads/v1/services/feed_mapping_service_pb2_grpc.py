# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import feed_mapping_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__mapping__pb2
from google.ads.googleads.v1.services import feed_mapping_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2


class FeedMappingServiceStub(object):
  """Proto file describing the FeedMapping service.

  Service to manage feed mappings.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeedMapping = channel.unary_unary(
        '/google.ads.googleads.v1.services.FeedMappingService/GetFeedMapping',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2.GetFeedMappingRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__mapping__pb2.FeedMapping.FromString,
        )
    self.MutateFeedMappings = channel.unary_unary(
        '/google.ads.googleads.v1.services.FeedMappingService/MutateFeedMappings',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2.MutateFeedMappingsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2.MutateFeedMappingsResponse.FromString,
        )


class FeedMappingServiceServicer(object):
  """Proto file describing the FeedMapping service.

  Service to manage feed mappings.
  """

  def GetFeedMapping(self, request, context):
    """Returns the requested feed mapping in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateFeedMappings(self, request, context):
    """Creates or removes feed mappings. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeedMappingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeedMapping': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeedMapping,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2.GetFeedMappingRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__mapping__pb2.FeedMapping.SerializeToString,
      ),
      'MutateFeedMappings': grpc.unary_unary_rpc_method_handler(
          servicer.MutateFeedMappings,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2.MutateFeedMappingsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__mapping__service__pb2.MutateFeedMappingsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.FeedMappingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
