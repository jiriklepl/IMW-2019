# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.monitoring.v3 import uptime_pb2 as google_dot_monitoring_dot_v3_dot_uptime__pb2
from google.monitoring.v3 import uptime_service_pb2 as google_dot_monitoring_dot_v3_dot_uptime__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class UptimeCheckServiceStub(object):
  """The UptimeCheckService API is used to manage (list, create, delete, edit)
  Uptime check configurations in the Stackdriver Monitoring product. An Uptime
  check is a piece of configuration that determines which resources and
  services to monitor for availability. These configurations can also be
  configured interactively by navigating to the [Cloud Console]
  (http://console.cloud.google.com), selecting the appropriate project,
  clicking on "Monitoring" on the left-hand side to navigate to Stackdriver,
  and then clicking on "Uptime".
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListUptimeCheckConfigs = channel.unary_unary(
        '/google.monitoring.v3.UptimeCheckService/ListUptimeCheckConfigs',
        request_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckConfigsRequest.SerializeToString,
        response_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckConfigsResponse.FromString,
        )
    self.GetUptimeCheckConfig = channel.unary_unary(
        '/google.monitoring.v3.UptimeCheckService/GetUptimeCheckConfig',
        request_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.GetUptimeCheckConfigRequest.SerializeToString,
        response_deserializer=google_dot_monitoring_dot_v3_dot_uptime__pb2.UptimeCheckConfig.FromString,
        )
    self.CreateUptimeCheckConfig = channel.unary_unary(
        '/google.monitoring.v3.UptimeCheckService/CreateUptimeCheckConfig',
        request_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.CreateUptimeCheckConfigRequest.SerializeToString,
        response_deserializer=google_dot_monitoring_dot_v3_dot_uptime__pb2.UptimeCheckConfig.FromString,
        )
    self.UpdateUptimeCheckConfig = channel.unary_unary(
        '/google.monitoring.v3.UptimeCheckService/UpdateUptimeCheckConfig',
        request_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.UpdateUptimeCheckConfigRequest.SerializeToString,
        response_deserializer=google_dot_monitoring_dot_v3_dot_uptime__pb2.UptimeCheckConfig.FromString,
        )
    self.DeleteUptimeCheckConfig = channel.unary_unary(
        '/google.monitoring.v3.UptimeCheckService/DeleteUptimeCheckConfig',
        request_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.DeleteUptimeCheckConfigRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListUptimeCheckIps = channel.unary_unary(
        '/google.monitoring.v3.UptimeCheckService/ListUptimeCheckIps',
        request_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckIpsRequest.SerializeToString,
        response_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckIpsResponse.FromString,
        )


class UptimeCheckServiceServicer(object):
  """The UptimeCheckService API is used to manage (list, create, delete, edit)
  Uptime check configurations in the Stackdriver Monitoring product. An Uptime
  check is a piece of configuration that determines which resources and
  services to monitor for availability. These configurations can also be
  configured interactively by navigating to the [Cloud Console]
  (http://console.cloud.google.com), selecting the appropriate project,
  clicking on "Monitoring" on the left-hand side to navigate to Stackdriver,
  and then clicking on "Uptime".
  """

  def ListUptimeCheckConfigs(self, request, context):
    """Lists the existing valid Uptime check configurations for the project
    (leaving out any invalid configurations).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUptimeCheckConfig(self, request, context):
    """Gets a single Uptime check configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUptimeCheckConfig(self, request, context):
    """Creates a new Uptime check configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUptimeCheckConfig(self, request, context):
    """Updates an Uptime check configuration. You can either replace the entire
    configuration with a new one or replace only certain fields in the current
    configuration by specifying the fields to be updated via `updateMask`.
    Returns the updated configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUptimeCheckConfig(self, request, context):
    """Deletes an Uptime check configuration. Note that this method will fail
    if the Uptime check configuration is referenced by an alert policy or
    other dependent configs that would be rendered invalid by the deletion.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUptimeCheckIps(self, request, context):
    """Returns the list of IP addresses that checkers run from
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UptimeCheckServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListUptimeCheckConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.ListUptimeCheckConfigs,
          request_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckConfigsRequest.FromString,
          response_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckConfigsResponse.SerializeToString,
      ),
      'GetUptimeCheckConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetUptimeCheckConfig,
          request_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.GetUptimeCheckConfigRequest.FromString,
          response_serializer=google_dot_monitoring_dot_v3_dot_uptime__pb2.UptimeCheckConfig.SerializeToString,
      ),
      'CreateUptimeCheckConfig': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUptimeCheckConfig,
          request_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.CreateUptimeCheckConfigRequest.FromString,
          response_serializer=google_dot_monitoring_dot_v3_dot_uptime__pb2.UptimeCheckConfig.SerializeToString,
      ),
      'UpdateUptimeCheckConfig': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUptimeCheckConfig,
          request_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.UpdateUptimeCheckConfigRequest.FromString,
          response_serializer=google_dot_monitoring_dot_v3_dot_uptime__pb2.UptimeCheckConfig.SerializeToString,
      ),
      'DeleteUptimeCheckConfig': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUptimeCheckConfig,
          request_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.DeleteUptimeCheckConfigRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListUptimeCheckIps': grpc.unary_unary_rpc_method_handler(
          servicer.ListUptimeCheckIps,
          request_deserializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckIpsRequest.FromString,
          response_serializer=google_dot_monitoring_dot_v3_dot_uptime__service__pb2.ListUptimeCheckIpsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.monitoring.v3.UptimeCheckService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
