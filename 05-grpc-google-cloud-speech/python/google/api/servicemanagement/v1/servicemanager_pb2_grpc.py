# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.api import service_pb2 as google_dot_api_dot_service__pb2
from google.api.servicemanagement.v1 import resources_pb2 as google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2
from google.api.servicemanagement.v1 import servicemanager_pb2 as google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class ServiceManagerStub(object):
  """[Google Service Management API](/service-management/overview)
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListServices = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/ListServices',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServicesRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServicesResponse.FromString,
        )
    self.GetService = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/GetService',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GetServiceRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2.ManagedService.FromString,
        )
    self.CreateService = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/CreateService',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.CreateServiceRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.DeleteService = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/DeleteService',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.DeleteServiceRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.UndeleteService = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/UndeleteService',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.UndeleteServiceRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ListServiceConfigs = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/ListServiceConfigs',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceConfigsRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceConfigsResponse.FromString,
        )
    self.GetServiceConfig = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/GetServiceConfig',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GetServiceConfigRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_service__pb2.Service.FromString,
        )
    self.CreateServiceConfig = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/CreateServiceConfig',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.CreateServiceConfigRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_service__pb2.Service.FromString,
        )
    self.SubmitConfigSource = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/SubmitConfigSource',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.SubmitConfigSourceRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ListServiceRollouts = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/ListServiceRollouts',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceRolloutsRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceRolloutsResponse.FromString,
        )
    self.GetServiceRollout = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/GetServiceRollout',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GetServiceRolloutRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2.Rollout.FromString,
        )
    self.CreateServiceRollout = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/CreateServiceRollout',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.CreateServiceRolloutRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.GenerateConfigReport = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/GenerateConfigReport',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GenerateConfigReportRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GenerateConfigReportResponse.FromString,
        )
    self.EnableService = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/EnableService',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.EnableServiceRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.DisableService = channel.unary_unary(
        '/google.api.servicemanagement.v1.ServiceManager/DisableService',
        request_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.DisableServiceRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class ServiceManagerServicer(object):
  """[Google Service Management API](/service-management/overview)
  """

  def ListServices(self, request, context):
    """Lists managed services.

    Returns all public services. For authenticated users, also returns all
    services the calling user has "servicemanagement.services.get" permission
    for.

    **BETA:** If the caller specifies the `consumer_id`, it returns only the
    services enabled on the consumer. The `consumer_id` must have the format
    of "project:{PROJECT-ID}".
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetService(self, request, context):
    """Gets a managed service. Authentication is required unless the service is
    public.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateService(self, request, context):
    """Creates a new managed service.
    Please note one producer project can own no more than 20 services.

    Operation<response: ManagedService>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteService(self, request, context):
    """Deletes a managed service. This method will change the service to the
    `Soft-Delete` state for 30 days. Within this period, service producers may
    call
    [UndeleteService][google.api.servicemanagement.v1.ServiceManager.UndeleteService]
    to restore the service. After 30 days, the service will be permanently
    deleted.

    Operation<response: google.protobuf.Empty>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UndeleteService(self, request, context):
    """Revives a previously deleted managed service. The method restores the
    service using the configuration at the time the service was deleted.
    The target service must exist and must have been deleted within the
    last 30 days.

    Operation<response: UndeleteServiceResponse>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListServiceConfigs(self, request, context):
    """Lists the history of the service configuration for a managed service,
    from the newest to the oldest.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetServiceConfig(self, request, context):
    """Gets a service configuration (version) for a managed service.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateServiceConfig(self, request, context):
    """Creates a new service configuration (version) for a managed service.
    This method only stores the service configuration. To roll out the service
    configuration to backend systems please call
    [CreateServiceRollout][google.api.servicemanagement.v1.ServiceManager.CreateServiceRollout].

    Only the 100 most recent service configurations and ones referenced by
    existing rollouts are kept for each service. The rest will be deleted
    eventually.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitConfigSource(self, request, context):
    """Creates a new service configuration (version) for a managed service based
    on
    user-supplied configuration source files (for example: OpenAPI
    Specification). This method stores the source configurations as well as the
    generated service configuration. To rollout the service configuration to
    other services,
    please call
    [CreateServiceRollout][google.api.servicemanagement.v1.ServiceManager.CreateServiceRollout].

    Only the 100 most recent configuration sources and ones referenced by
    existing service configurtions are kept for each service. The rest will be
    deleted eventually.

    Operation<response: SubmitConfigSourceResponse>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListServiceRollouts(self, request, context):
    """Lists the history of the service configuration rollouts for a managed
    service, from the newest to the oldest.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetServiceRollout(self, request, context):
    """Gets a service configuration
    [rollout][google.api.servicemanagement.v1.Rollout].
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateServiceRollout(self, request, context):
    """Creates a new service configuration rollout. Based on rollout, the
    Google Service Management will roll out the service configurations to
    different backend services. For example, the logging configuration will be
    pushed to Google Cloud Logging.

    Please note that any previous pending and running Rollouts and associated
    Operations will be automatically cancelled so that the latest Rollout will
    not be blocked by previous Rollouts.

    Only the 100 most recent (in any state) and the last 10 successful (if not
    already part of the set of 100 most recent) rollouts are kept for each
    service. The rest will be deleted eventually.

    Operation<response: Rollout>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateConfigReport(self, request, context):
    """Generates and returns a report (errors, warnings and changes from
    existing configurations) associated with
    GenerateConfigReportRequest.new_value

    If GenerateConfigReportRequest.old_value is specified,
    GenerateConfigReportRequest will contain a single ChangeReport based on the
    comparison between GenerateConfigReportRequest.new_value and
    GenerateConfigReportRequest.old_value.
    If GenerateConfigReportRequest.old_value is not specified, this method
    will compare GenerateConfigReportRequest.new_value with the last pushed
    service configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnableService(self, request, context):
    """Enables a [service][google.api.servicemanagement.v1.ManagedService] for a
    project, so it can be used for the project. See [Cloud Auth
    Guide](https://cloud.google.com/docs/authentication) for more information.

    Operation<response: EnableServiceResponse>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DisableService(self, request, context):
    """Disables a [service][google.api.servicemanagement.v1.ManagedService] for a
    project, so it can no longer be be used for the project. It prevents
    accidental usage that may cause unexpected billing charges or security
    leaks.

    Operation<response: DisableServiceResponse>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServiceManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListServices': grpc.unary_unary_rpc_method_handler(
          servicer.ListServices,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServicesRequest.FromString,
          response_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServicesResponse.SerializeToString,
      ),
      'GetService': grpc.unary_unary_rpc_method_handler(
          servicer.GetService,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GetServiceRequest.FromString,
          response_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2.ManagedService.SerializeToString,
      ),
      'CreateService': grpc.unary_unary_rpc_method_handler(
          servicer.CreateService,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.CreateServiceRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'DeleteService': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteService,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.DeleteServiceRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'UndeleteService': grpc.unary_unary_rpc_method_handler(
          servicer.UndeleteService,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.UndeleteServiceRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ListServiceConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.ListServiceConfigs,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceConfigsRequest.FromString,
          response_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceConfigsResponse.SerializeToString,
      ),
      'GetServiceConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetServiceConfig,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GetServiceConfigRequest.FromString,
          response_serializer=google_dot_api_dot_service__pb2.Service.SerializeToString,
      ),
      'CreateServiceConfig': grpc.unary_unary_rpc_method_handler(
          servicer.CreateServiceConfig,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.CreateServiceConfigRequest.FromString,
          response_serializer=google_dot_api_dot_service__pb2.Service.SerializeToString,
      ),
      'SubmitConfigSource': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitConfigSource,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.SubmitConfigSourceRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ListServiceRollouts': grpc.unary_unary_rpc_method_handler(
          servicer.ListServiceRollouts,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceRolloutsRequest.FromString,
          response_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.ListServiceRolloutsResponse.SerializeToString,
      ),
      'GetServiceRollout': grpc.unary_unary_rpc_method_handler(
          servicer.GetServiceRollout,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GetServiceRolloutRequest.FromString,
          response_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2.Rollout.SerializeToString,
      ),
      'CreateServiceRollout': grpc.unary_unary_rpc_method_handler(
          servicer.CreateServiceRollout,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.CreateServiceRolloutRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'GenerateConfigReport': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateConfigReport,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GenerateConfigReportRequest.FromString,
          response_serializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.GenerateConfigReportResponse.SerializeToString,
      ),
      'EnableService': grpc.unary_unary_rpc_method_handler(
          servicer.EnableService,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.EnableServiceRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'DisableService': grpc.unary_unary_rpc_method_handler(
          servicer.DisableService,
          request_deserializer=google_dot_api_dot_servicemanagement_dot_v1_dot_servicemanager__pb2.DisableServiceRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.api.servicemanagement.v1.ServiceManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
