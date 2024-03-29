# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import feed_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__pb2
from google.ads.googleads.v1.services import feed_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2


class FeedServiceStub(object):
  """Proto file describing the Feed service.

  Service to manage feeds.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeed = channel.unary_unary(
        '/google.ads.googleads.v1.services.FeedService/GetFeed',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2.GetFeedRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__pb2.Feed.FromString,
        )
    self.MutateFeeds = channel.unary_unary(
        '/google.ads.googleads.v1.services.FeedService/MutateFeeds',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2.MutateFeedsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2.MutateFeedsResponse.FromString,
        )


class FeedServiceServicer(object):
  """Proto file describing the Feed service.

  Service to manage feeds.
  """

  def GetFeed(self, request, context):
    """Returns the requested feed in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateFeeds(self, request, context):
    """Creates, updates, or removes feeds. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeedServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeed,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2.GetFeedRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__pb2.Feed.SerializeToString,
      ),
      'MutateFeeds': grpc.unary_unary_rpc_method_handler(
          servicer.MutateFeeds,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2.MutateFeedsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_feed__service__pb2.MutateFeedsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.FeedService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
