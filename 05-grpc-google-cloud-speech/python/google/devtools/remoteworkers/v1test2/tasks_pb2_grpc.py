# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.devtools.remoteworkers.v1test2 import tasks_pb2 as google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2


class TasksStub(object):
  """DEPRECATED. GetTask should be replaced by Lease.payload, UpdateTaskResult by
  Lease.result and logs should be precreated prior to sending to the bot (eg,
  via CommandTask.expected_outputs.stdout_destination).
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTask = channel.unary_unary(
        '/google.devtools.remoteworkers.v1test2.Tasks/GetTask',
        request_serializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.GetTaskRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.Task.FromString,
        )
    self.UpdateTaskResult = channel.unary_unary(
        '/google.devtools.remoteworkers.v1test2.Tasks/UpdateTaskResult',
        request_serializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.UpdateTaskResultRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.TaskResult.FromString,
        )
    self.AddTaskLog = channel.unary_unary(
        '/google.devtools.remoteworkers.v1test2.Tasks/AddTaskLog',
        request_serializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.AddTaskLogRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.AddTaskLogResponse.FromString,
        )


class TasksServicer(object):
  """DEPRECATED. GetTask should be replaced by Lease.payload, UpdateTaskResult by
  Lease.result and logs should be precreated prior to sending to the bot (eg,
  via CommandTask.expected_outputs.stdout_destination).
  """

  def GetTask(self, request, context):
    """DEPRECATED - use Lease.payload instead.
    GetTask reads the current state of the task. Tasks must be created through
    some other interface, and should be immutable once created and exposed to
    the bots.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTaskResult(self, request, context):
    """DEPRECATED - use Lease.result instead.
    UpdateTaskResult updates the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddTaskLog(self, request, context):
    """DEPRECATED - precreate logs prior to sending to bot.
    AddTaskLog creates a new streaming log. The log is streamed and marked as
    completed through other interfaces (i.e., ByteStream). This can be called
    by the bot if it wants to create a new log; the server can also predefine
    logs that do not need to be created (e.g. `stdout`).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TasksServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTask': grpc.unary_unary_rpc_method_handler(
          servicer.GetTask,
          request_deserializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.GetTaskRequest.FromString,
          response_serializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.Task.SerializeToString,
      ),
      'UpdateTaskResult': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTaskResult,
          request_deserializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.UpdateTaskResultRequest.FromString,
          response_serializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.TaskResult.SerializeToString,
      ),
      'AddTaskLog': grpc.unary_unary_rpc_method_handler(
          servicer.AddTaskLog,
          request_deserializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.AddTaskLogRequest.FromString,
          response_serializer=google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_tasks__pb2.AddTaskLogResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.devtools.remoteworkers.v1test2.Tasks', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
