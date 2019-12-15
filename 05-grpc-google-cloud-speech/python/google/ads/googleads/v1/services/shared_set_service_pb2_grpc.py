# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import shared_set_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_shared__set__pb2
from google.ads.googleads.v1.services import shared_set_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2


class SharedSetServiceStub(object):
  """Proto file describing the Shared Set service.

  Service to manage shared sets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSharedSet = channel.unary_unary(
        '/google.ads.googleads.v1.services.SharedSetService/GetSharedSet',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2.GetSharedSetRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_shared__set__pb2.SharedSet.FromString,
        )
    self.MutateSharedSets = channel.unary_unary(
        '/google.ads.googleads.v1.services.SharedSetService/MutateSharedSets',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2.MutateSharedSetsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2.MutateSharedSetsResponse.FromString,
        )


class SharedSetServiceServicer(object):
  """Proto file describing the Shared Set service.

  Service to manage shared sets.
  """

  def GetSharedSet(self, request, context):
    """Returns the requested shared set in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateSharedSets(self, request, context):
    """Creates, updates, or removes shared sets. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SharedSetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSharedSet': grpc.unary_unary_rpc_method_handler(
          servicer.GetSharedSet,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2.GetSharedSetRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_shared__set__pb2.SharedSet.SerializeToString,
      ),
      'MutateSharedSets': grpc.unary_unary_rpc_method_handler(
          servicer.MutateSharedSets,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2.MutateSharedSetsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_shared__set__service__pb2.MutateSharedSetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.SharedSetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
