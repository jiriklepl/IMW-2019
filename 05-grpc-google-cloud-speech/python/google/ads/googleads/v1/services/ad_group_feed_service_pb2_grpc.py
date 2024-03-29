# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import ad_group_feed_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__group__feed__pb2
from google.ads.googleads.v1.services import ad_group_feed_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2


class AdGroupFeedServiceStub(object):
  """Proto file describing the AdGroupFeed service.

  Service to manage ad group feeds.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAdGroupFeed = channel.unary_unary(
        '/google.ads.googleads.v1.services.AdGroupFeedService/GetAdGroupFeed',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2.GetAdGroupFeedRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__group__feed__pb2.AdGroupFeed.FromString,
        )
    self.MutateAdGroupFeeds = channel.unary_unary(
        '/google.ads.googleads.v1.services.AdGroupFeedService/MutateAdGroupFeeds',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2.MutateAdGroupFeedsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2.MutateAdGroupFeedsResponse.FromString,
        )


class AdGroupFeedServiceServicer(object):
  """Proto file describing the AdGroupFeed service.

  Service to manage ad group feeds.
  """

  def GetAdGroupFeed(self, request, context):
    """Returns the requested ad group feed in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateAdGroupFeeds(self, request, context):
    """Creates, updates, or removes ad group feeds. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdGroupFeedServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAdGroupFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdGroupFeed,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2.GetAdGroupFeedRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__group__feed__pb2.AdGroupFeed.SerializeToString,
      ),
      'MutateAdGroupFeeds': grpc.unary_unary_rpc_method_handler(
          servicer.MutateAdGroupFeeds,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2.MutateAdGroupFeedsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_ad__group__feed__service__pb2.MutateAdGroupFeedsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.AdGroupFeedService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
