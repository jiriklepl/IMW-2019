# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.api.servicecontrol.v1 import service_controller_pb2 as google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2


class ServiceControllerStub(object):
  """[Google Service Control API](/service-control/overview)

  Lets clients check and report operations against a [managed
  service](https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService).
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Check = channel.unary_unary(
        '/google.api.servicecontrol.v1.ServiceController/Check',
        request_serializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.CheckRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.CheckResponse.FromString,
        )
    self.Report = channel.unary_unary(
        '/google.api.servicecontrol.v1.ServiceController/Report',
        request_serializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.ReportRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.ReportResponse.FromString,
        )


class ServiceControllerServicer(object):
  """[Google Service Control API](/service-control/overview)

  Lets clients check and report operations against a [managed
  service](https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService).
  """

  def Check(self, request, context):
    """Checks an operation with Google Service Control to decide whether
    the given operation should proceed. It should be called before the
    operation is executed.

    If feasible, the client should cache the check results and reuse them for
    60 seconds. In case of server errors, the client can rely on the cached
    results for longer time.

    NOTE: the [CheckRequest][google.api.servicecontrol.v1.CheckRequest] has the
    size limit of 64KB.

    This method requires the `servicemanagement.services.check` permission
    on the specified service. For more information, see
    [Google Cloud IAM](https://cloud.google.com/iam).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Report(self, request, context):
    """Reports operation results to Google Service Control, such as logs and
    metrics. It should be called after an operation is completed.

    If feasible, the client should aggregate reporting data for up to 5
    seconds to reduce API traffic. Limiting aggregation to 5 seconds is to
    reduce data loss during client crashes. Clients should carefully choose
    the aggregation time window to avoid data loss risk more than 0.01%
    for business and compliance reasons.

    NOTE: the [ReportRequest][google.api.servicecontrol.v1.ReportRequest] has
    the size limit of 1MB.

    This method requires the `servicemanagement.services.report` permission
    on the specified service. For more information, see
    [Google Cloud IAM](https://cloud.google.com/iam).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServiceControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Check': grpc.unary_unary_rpc_method_handler(
          servicer.Check,
          request_deserializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.CheckRequest.FromString,
          response_serializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.CheckResponse.SerializeToString,
      ),
      'Report': grpc.unary_unary_rpc_method_handler(
          servicer.Report,
          request_deserializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.ReportRequest.FromString,
          response_serializer=google_dot_api_dot_servicecontrol_dot_v1_dot_service__controller__pb2.ReportResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.api.servicecontrol.v1.ServiceController', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
