# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import conversion_action_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_conversion__action__pb2
from google.ads.googleads.v1.services import conversion_action_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2


class ConversionActionServiceStub(object):
  """Proto file describing the Conversion Action service.

  Service to manage conversion actions.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConversionAction = channel.unary_unary(
        '/google.ads.googleads.v1.services.ConversionActionService/GetConversionAction',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2.GetConversionActionRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_conversion__action__pb2.ConversionAction.FromString,
        )
    self.MutateConversionActions = channel.unary_unary(
        '/google.ads.googleads.v1.services.ConversionActionService/MutateConversionActions',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2.MutateConversionActionsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2.MutateConversionActionsResponse.FromString,
        )


class ConversionActionServiceServicer(object):
  """Proto file describing the Conversion Action service.

  Service to manage conversion actions.
  """

  def GetConversionAction(self, request, context):
    """Returns the requested conversion action.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateConversionActions(self, request, context):
    """Creates, updates or removes conversion actions. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConversionActionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConversionAction': grpc.unary_unary_rpc_method_handler(
          servicer.GetConversionAction,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2.GetConversionActionRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_conversion__action__pb2.ConversionAction.SerializeToString,
      ),
      'MutateConversionActions': grpc.unary_unary_rpc_method_handler(
          servicer.MutateConversionActions,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2.MutateConversionActionsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_conversion__action__service__pb2.MutateConversionActionsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.ConversionActionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
