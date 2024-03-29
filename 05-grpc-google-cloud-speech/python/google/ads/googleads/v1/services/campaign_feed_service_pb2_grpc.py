# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import campaign_feed_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__feed__pb2
from google.ads.googleads.v1.services import campaign_feed_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2


class CampaignFeedServiceStub(object):
  """Proto file describing the CampaignFeed service.

  Service to manage campaign feeds.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignFeed = channel.unary_unary(
        '/google.ads.googleads.v1.services.CampaignFeedService/GetCampaignFeed',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2.GetCampaignFeedRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__feed__pb2.CampaignFeed.FromString,
        )
    self.MutateCampaignFeeds = channel.unary_unary(
        '/google.ads.googleads.v1.services.CampaignFeedService/MutateCampaignFeeds',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2.MutateCampaignFeedsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2.MutateCampaignFeedsResponse.FromString,
        )


class CampaignFeedServiceServicer(object):
  """Proto file describing the CampaignFeed service.

  Service to manage campaign feeds.
  """

  def GetCampaignFeed(self, request, context):
    """Returns the requested campaign feed in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCampaignFeeds(self, request, context):
    """Creates, updates, or removes campaign feeds. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignFeedServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignFeed,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2.GetCampaignFeedRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__feed__pb2.CampaignFeed.SerializeToString,
      ),
      'MutateCampaignFeeds': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCampaignFeeds,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2.MutateCampaignFeedsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_campaign__feed__service__pb2.MutateCampaignFeedsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.CampaignFeedService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
