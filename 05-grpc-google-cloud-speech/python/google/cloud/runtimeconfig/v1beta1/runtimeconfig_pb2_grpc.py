# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.runtimeconfig.v1beta1 import resources_pb2 as google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2
from google.cloud.runtimeconfig.v1beta1 import runtimeconfig_pb2 as google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class RuntimeConfigManagerStub(object):
  """RuntimeConfig API represents configuration objects and operations on those
  configuration objects.
  RuntimeConfig objects consist of Variables logically grouped in the those
  objects.
  Variables are simple key-value pairs. Variables can be watched for changes or
  deletions. Variable key can be hieararchical, e.g. ports/serving_port,
  ports/monitoring_port, etc. Variable names can be hierarchical. No variable
  name can be prefix of another.
  Config objects represent logical containers for variables, e.g. flags,
  passwords, etc.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListConfigs = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListConfigs',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListConfigsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListConfigsResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetConfig',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.RuntimeConfig.FromString,
        )
    self.CreateConfig = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateConfig',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.CreateConfigRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.RuntimeConfig.FromString,
        )
    self.UpdateConfig = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/UpdateConfig',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.UpdateConfigRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.RuntimeConfig.FromString,
        )
    self.DeleteConfig = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteConfig',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.DeleteConfigRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListVariables = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListVariables',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListVariablesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListVariablesResponse.FromString,
        )
    self.GetVariable = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetVariable',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.GetVariableRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.FromString,
        )
    self.WatchVariable = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/WatchVariable',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.WatchVariableRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.FromString,
        )
    self.CreateVariable = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateVariable',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.CreateVariableRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.FromString,
        )
    self.UpdateVariable = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/UpdateVariable',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.UpdateVariableRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.FromString,
        )
    self.DeleteVariable = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteVariable',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.DeleteVariableRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListWaiters = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListWaiters',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListWaitersRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListWaitersResponse.FromString,
        )
    self.GetWaiter = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetWaiter',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.GetWaiterRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Waiter.FromString,
        )
    self.CreateWaiter = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateWaiter',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.CreateWaiterRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.DeleteWaiter = channel.unary_unary(
        '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteWaiter',
        request_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.DeleteWaiterRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class RuntimeConfigManagerServicer(object):
  """RuntimeConfig API represents configuration objects and operations on those
  configuration objects.
  RuntimeConfig objects consist of Variables logically grouped in the those
  objects.
  Variables are simple key-value pairs. Variables can be watched for changes or
  deletions. Variable key can be hieararchical, e.g. ports/serving_port,
  ports/monitoring_port, etc. Variable names can be hierarchical. No variable
  name can be prefix of another.
  Config objects represent logical containers for variables, e.g. flags,
  passwords, etc.
  """

  def ListConfigs(self, request, context):
    """Lists all the RuntimeConfig resources within project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfig(self, request, context):
    """Gets information about a RuntimeConfig resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateConfig(self, request, context):
    """Creates a new RuntimeConfig resource. The configuration name must be
    unique within project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateConfig(self, request, context):
    """Updates a RuntimeConfig resource. The configuration must exist beforehand.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteConfig(self, request, context):
    """Deletes a RuntimeConfig resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListVariables(self, request, context):
    """Lists variables within given a configuration, matching any provided
    filters. This only lists variable names, not the values, unless
    `return_values` is true, in which case only variables that user has IAM
    permission to GetVariable will be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVariable(self, request, context):
    """Gets information about a single variable.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchVariable(self, request, context):
    """Watches a specific variable and waits for a change in the variable's value.
    When there is a change, this method returns the new value or times out.

    If a variable is deleted while being watched, the `variableState` state is
    set to `DELETED` and the method returns the last known variable `value`.

    If you set the deadline for watching to a larger value than internal
    timeout (60 seconds), the current variable value is returned and the
    `variableState` will be `VARIABLE_STATE_UNSPECIFIED`.

    To learn more about creating a watcher, read the
    [Watching a Variable for
    Changes](/deployment-manager/runtime-configurator/watching-a-variable)
    documentation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateVariable(self, request, context):
    """Creates a variable within the given configuration. You cannot create
    a variable with a name that is a prefix of an existing variable name, or a
    name that has an existing variable name as a prefix.

    To learn more about creating a variable, read the
    [Setting and Getting
    Data](/deployment-manager/runtime-configurator/set-and-get-variables)
    documentation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateVariable(self, request, context):
    """Updates an existing variable with a new value.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteVariable(self, request, context):
    """Deletes a variable or multiple variables.

    If you specify a variable name, then that variable is deleted. If you
    specify a prefix and `recursive` is true, then all variables with that
    prefix are deleted. You must set a `recursive` to true if you delete
    variables by prefix.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListWaiters(self, request, context):
    """List waiters within the given configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWaiter(self, request, context):
    """Gets information about a single waiter.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateWaiter(self, request, context):
    """Creates a Waiter resource. This operation returns a long-running Operation
    resource which can be polled for completion. However, a waiter with the
    given name will exist (and can be retrieved) prior to the operation
    completing. If the operation fails, the failed Waiter resource will
    still exist and must be deleted prior to subsequent creation attempts.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteWaiter(self, request, context):
    """Deletes the waiter with the specified name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RuntimeConfigManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.ListConfigs,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListConfigsRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListConfigsResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.GetConfigRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.RuntimeConfig.SerializeToString,
      ),
      'CreateConfig': grpc.unary_unary_rpc_method_handler(
          servicer.CreateConfig,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.CreateConfigRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.RuntimeConfig.SerializeToString,
      ),
      'UpdateConfig': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateConfig,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.UpdateConfigRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.RuntimeConfig.SerializeToString,
      ),
      'DeleteConfig': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteConfig,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.DeleteConfigRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListVariables': grpc.unary_unary_rpc_method_handler(
          servicer.ListVariables,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListVariablesRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListVariablesResponse.SerializeToString,
      ),
      'GetVariable': grpc.unary_unary_rpc_method_handler(
          servicer.GetVariable,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.GetVariableRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.SerializeToString,
      ),
      'WatchVariable': grpc.unary_unary_rpc_method_handler(
          servicer.WatchVariable,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.WatchVariableRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.SerializeToString,
      ),
      'CreateVariable': grpc.unary_unary_rpc_method_handler(
          servicer.CreateVariable,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.CreateVariableRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.SerializeToString,
      ),
      'UpdateVariable': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateVariable,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.UpdateVariableRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Variable.SerializeToString,
      ),
      'DeleteVariable': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteVariable,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.DeleteVariableRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListWaiters': grpc.unary_unary_rpc_method_handler(
          servicer.ListWaiters,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListWaitersRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.ListWaitersResponse.SerializeToString,
      ),
      'GetWaiter': grpc.unary_unary_rpc_method_handler(
          servicer.GetWaiter,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.GetWaiterRequest.FromString,
          response_serializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2.Waiter.SerializeToString,
      ),
      'CreateWaiter': grpc.unary_unary_rpc_method_handler(
          servicer.CreateWaiter,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.CreateWaiterRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'DeleteWaiter': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteWaiter,
          request_deserializer=google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_runtimeconfig__pb2.DeleteWaiterRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
