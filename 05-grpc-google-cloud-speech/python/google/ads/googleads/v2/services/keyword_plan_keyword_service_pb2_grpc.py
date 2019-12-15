# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v2.resources import keyword_plan_keyword_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__keyword__pb2
from google.ads.googleads.v2.services import keyword_plan_keyword_service_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2


class KeywordPlanKeywordServiceStub(object):
  """Proto file describing the keyword plan keyword service.

  Service to manage Keyword Plan ad group keywords.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetKeywordPlanKeyword = channel.unary_unary(
        '/google.ads.googleads.v2.services.KeywordPlanKeywordService/GetKeywordPlanKeyword',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2.GetKeywordPlanKeywordRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__keyword__pb2.KeywordPlanKeyword.FromString,
        )
    self.MutateKeywordPlanKeywords = channel.unary_unary(
        '/google.ads.googleads.v2.services.KeywordPlanKeywordService/MutateKeywordPlanKeywords',
        request_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2.MutateKeywordPlanKeywordsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2.MutateKeywordPlanKeywordsResponse.FromString,
        )


class KeywordPlanKeywordServiceServicer(object):
  """Proto file describing the keyword plan keyword service.

  Service to manage Keyword Plan ad group keywords.
  """

  def GetKeywordPlanKeyword(self, request, context):
    """Returns the requested Keyword Plan keyword in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateKeywordPlanKeywords(self, request, context):
    """Creates, updates, or removes Keyword Plan keywords. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeywordPlanKeywordServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetKeywordPlanKeyword': grpc.unary_unary_rpc_method_handler(
          servicer.GetKeywordPlanKeyword,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2.GetKeywordPlanKeywordRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__keyword__pb2.KeywordPlanKeyword.SerializeToString,
      ),
      'MutateKeywordPlanKeywords': grpc.unary_unary_rpc_method_handler(
          servicer.MutateKeywordPlanKeywords,
          request_deserializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2.MutateKeywordPlanKeywordsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v2_dot_services_dot_keyword__plan__keyword__service__pb2.MutateKeywordPlanKeywordsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.KeywordPlanKeywordService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
