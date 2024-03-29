# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v2.resources import campaign_label_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_campaign__label__pb2
from google.ads.googleads.v2.services import campaign_label_service_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2


class CampaignLabelServiceStub(object):
  """Proto file describing the Campaign Label service.

  Service to manage labels on campaigns.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignLabel = channel.unary_unary(
        '/google.ads.googleads.v2.services.CampaignLabelService/GetCampaignLabel',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2.GetCampaignLabelRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_campaign__label__pb2.CampaignLabel.FromString,
        )
    self.MutateCampaignLabels = channel.unary_unary(
        '/google.ads.googleads.v2.services.CampaignLabelService/MutateCampaignLabels',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2.MutateCampaignLabelsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2.MutateCampaignLabelsResponse.FromString,
        )


class CampaignLabelServiceServicer(object):
  """Proto file describing the Campaign Label service.

  Service to manage labels on campaigns.
  """

  def GetCampaignLabel(self, request, context):
    """Returns the requested campaign-label relationship in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCampaignLabels(self, request, context):
    """Creates and removes campaign-label relationships.
    Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignLabelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignLabel': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignLabel,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2.GetCampaignLabelRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_campaign__label__pb2.CampaignLabel.SerializeToString,
      ),
      'MutateCampaignLabels': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCampaignLabels,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2.MutateCampaignLabelsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_campaign__label__service__pb2.MutateCampaignLabelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.CampaignLabelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
