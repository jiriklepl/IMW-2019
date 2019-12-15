# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.dialogflow.v2beta1 import agent_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2
from google.cloud.dialogflow.v2beta1 import validation_result_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_validation__result__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AgentsStub(object):
  """Agents are best described as Natural Language Understanding (NLU) modules
  that transform user requests into actionable data. You can include agents
  in your app, product, or service to determine user intent and respond to the
  user in a natural way.

  After you create an agent, you can add [Intents][google.cloud.dialogflow.v2beta1.Intents], [Contexts][google.cloud.dialogflow.v2beta1.Contexts],
  [Entity Types][google.cloud.dialogflow.v2beta1.EntityTypes], [Webhooks][google.cloud.dialogflow.v2beta1.WebhookRequest], and so on to
  manage the flow of a conversation and match user input to predefined intents
  and actions.

  You can create an agent using both Dialogflow Standard Edition and
  Dialogflow Enterprise Edition. For details, see
  [Dialogflow
  Editions](https://cloud.google.com/dialogflow/docs/editions).

  You can save your agent for backup or versioning by exporting the agent by
  using the [ExportAgent][google.cloud.dialogflow.v2beta1.Agents.ExportAgent] method. You can import a saved
  agent by using the [ImportAgent][google.cloud.dialogflow.v2beta1.Agents.ImportAgent] method.

  Dialogflow provides several
  [prebuilt
  agents](https://cloud.google.com/dialogflow/docs/agents-prebuilt)
  for common conversation scenarios such as determining a date and time,
  converting currency, and so on.

  For more information about agents, see the
  [Dialogflow
  documentation](https://cloud.google.com/dialogflow/docs/agents-overview).
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/GetAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.GetAgentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.Agent.FromString,
        )
    self.SetAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/SetAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.SetAgentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.Agent.FromString,
        )
    self.DeleteAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/DeleteAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.DeleteAgentRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SearchAgents = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/SearchAgents',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.SearchAgentsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.SearchAgentsResponse.FromString,
        )
    self.TrainAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/TrainAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.TrainAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ExportAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/ExportAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.ExportAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ImportAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/ImportAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.ImportAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.RestoreAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/RestoreAgent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.RestoreAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.GetValidationResult = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.Agents/GetValidationResult',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.GetValidationResultRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_validation__result__pb2.ValidationResult.FromString,
        )


class AgentsServicer(object):
  """Agents are best described as Natural Language Understanding (NLU) modules
  that transform user requests into actionable data. You can include agents
  in your app, product, or service to determine user intent and respond to the
  user in a natural way.

  After you create an agent, you can add [Intents][google.cloud.dialogflow.v2beta1.Intents], [Contexts][google.cloud.dialogflow.v2beta1.Contexts],
  [Entity Types][google.cloud.dialogflow.v2beta1.EntityTypes], [Webhooks][google.cloud.dialogflow.v2beta1.WebhookRequest], and so on to
  manage the flow of a conversation and match user input to predefined intents
  and actions.

  You can create an agent using both Dialogflow Standard Edition and
  Dialogflow Enterprise Edition. For details, see
  [Dialogflow
  Editions](https://cloud.google.com/dialogflow/docs/editions).

  You can save your agent for backup or versioning by exporting the agent by
  using the [ExportAgent][google.cloud.dialogflow.v2beta1.Agents.ExportAgent] method. You can import a saved
  agent by using the [ImportAgent][google.cloud.dialogflow.v2beta1.Agents.ImportAgent] method.

  Dialogflow provides several
  [prebuilt
  agents](https://cloud.google.com/dialogflow/docs/agents-prebuilt)
  for common conversation scenarios such as determining a date and time,
  converting currency, and so on.

  For more information about agents, see the
  [Dialogflow
  documentation](https://cloud.google.com/dialogflow/docs/agents-overview).
  """

  def GetAgent(self, request, context):
    """Retrieves the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetAgent(self, request, context):
    """Creates/updates the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAgent(self, request, context):
    """Deletes the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchAgents(self, request, context):
    """Returns the list of agents.

    Since there is at most one conversational agent per project, this method is
    useful primarily for listing all agents across projects the caller has
    access to. One can achieve that with a wildcard project collection id "-".
    Refer to [List
    Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TrainAgent(self, request, context):
    """Trains the specified agent.


    Operation <response: [google.protobuf.Empty][google.protobuf.Empty]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExportAgent(self, request, context):
    """Exports the specified agent to a ZIP file.


    Operation <response: [ExportAgentResponse][google.cloud.dialogflow.v2beta1.ExportAgentResponse]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImportAgent(self, request, context):
    """Imports the specified agent from a ZIP file.

    Uploads new intents and entity types without deleting the existing ones.
    Intents and entity types with the same name are replaced with the new
    versions from ImportAgentRequest.


    Operation <response: [google.protobuf.Empty][google.protobuf.Empty]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreAgent(self, request, context):
    """Restores the specified agent from a ZIP file.

    Replaces the current agent version with a new one. All the intents and
    entity types in the older version are deleted.


    Operation <response: [google.protobuf.Empty][google.protobuf.Empty]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetValidationResult(self, request, context):
    """Gets agent validation result. Agent validation is performed during
    training time and is updated automatically when training is completed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AgentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAgent': grpc.unary_unary_rpc_method_handler(
          servicer.GetAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.GetAgentRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.Agent.SerializeToString,
      ),
      'SetAgent': grpc.unary_unary_rpc_method_handler(
          servicer.SetAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.SetAgentRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.Agent.SerializeToString,
      ),
      'DeleteAgent': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.DeleteAgentRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SearchAgents': grpc.unary_unary_rpc_method_handler(
          servicer.SearchAgents,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.SearchAgentsRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.SearchAgentsResponse.SerializeToString,
      ),
      'TrainAgent': grpc.unary_unary_rpc_method_handler(
          servicer.TrainAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.TrainAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ExportAgent': grpc.unary_unary_rpc_method_handler(
          servicer.ExportAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.ExportAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ImportAgent': grpc.unary_unary_rpc_method_handler(
          servicer.ImportAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.ImportAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'RestoreAgent': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.RestoreAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'GetValidationResult': grpc.unary_unary_rpc_method_handler(
          servicer.GetValidationResult,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2.GetValidationResultRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_validation__result__pb2.ValidationResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.dialogflow.v2beta1.Agents', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
