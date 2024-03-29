# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import mobile_device_constant_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_mobile__device__constant__pb2
from google.ads.googleads.v1.services import mobile_device_constant_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_mobile__device__constant__service__pb2


class MobileDeviceConstantServiceStub(object):
  """Proto file describing the mobile device constant service.

  Service to fetch mobile device constants.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMobileDeviceConstant = channel.unary_unary(
        '/google.ads.googleads.v1.services.MobileDeviceConstantService/GetMobileDeviceConstant',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_mobile__device__constant__service__pb2.GetMobileDeviceConstantRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_mobile__device__constant__pb2.MobileDeviceConstant.FromString,
        )


class MobileDeviceConstantServiceServicer(object):
  """Proto file describing the mobile device constant service.

  Service to fetch mobile device constants.
  """

  def GetMobileDeviceConstant(self, request, context):
    """Returns the requested mobile device constant in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MobileDeviceConstantServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMobileDeviceConstant': grpc.unary_unary_rpc_method_handler(
          servicer.GetMobileDeviceConstant,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_mobile__device__constant__service__pb2.GetMobileDeviceConstantRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_mobile__device__constant__pb2.MobileDeviceConstant.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.MobileDeviceConstantService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
