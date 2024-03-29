# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import customer_extension_setting_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_customer__extension__setting__pb2
from google.ads.googleads.v1.services import customer_extension_setting_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2


class CustomerExtensionSettingServiceStub(object):
  """Proto file describing the CustomerExtensionSetting service.

  Service to manage customer extension settings.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCustomerExtensionSetting = channel.unary_unary(
        '/google.ads.googleads.v1.services.CustomerExtensionSettingService/GetCustomerExtensionSetting',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2.GetCustomerExtensionSettingRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_customer__extension__setting__pb2.CustomerExtensionSetting.FromString,
        )
    self.MutateCustomerExtensionSettings = channel.unary_unary(
        '/google.ads.googleads.v1.services.CustomerExtensionSettingService/MutateCustomerExtensionSettings',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2.MutateCustomerExtensionSettingsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2.MutateCustomerExtensionSettingsResponse.FromString,
        )


class CustomerExtensionSettingServiceServicer(object):
  """Proto file describing the CustomerExtensionSetting service.

  Service to manage customer extension settings.
  """

  def GetCustomerExtensionSetting(self, request, context):
    """Returns the requested customer extension setting in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCustomerExtensionSettings(self, request, context):
    """Creates, updates, or removes customer extension settings. Operation
    statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerExtensionSettingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCustomerExtensionSetting': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomerExtensionSetting,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2.GetCustomerExtensionSettingRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_customer__extension__setting__pb2.CustomerExtensionSetting.SerializeToString,
      ),
      'MutateCustomerExtensionSettings': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCustomerExtensionSettings,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2.MutateCustomerExtensionSettingsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_customer__extension__setting__service__pb2.MutateCustomerExtensionSettingsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.CustomerExtensionSettingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
