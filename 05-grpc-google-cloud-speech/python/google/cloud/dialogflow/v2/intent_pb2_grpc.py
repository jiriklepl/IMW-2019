# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.dialogflow.v2 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class IntentsStub(object):
  """An intent represents a mapping between input from a user and an action to
  be taken by your application. When you pass user input to the
  [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
  [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) method, the
  Dialogflow API analyzes the input and searches
  for a matching intent. If no match is found, the Dialogflow API returns a
  fallback intent (`is_fallback` = true).

  You can provide additional information for the Dialogflow API to use to
  match user input to an intent by adding the following to your intent.

  *   **Contexts** - provide additional context for intent analysis. For
  example, if an intent is related to an object in your application that
  plays music, you can provide a context to determine when to match the
  intent if the user input is "turn it off". You can include a context
  that matches the intent when there is previous user input of
  "play music", and not when there is previous user input of
  "turn on the light".

  *   **Events** - allow for matching an intent by using an event name
  instead of user input. Your application can provide an event name and
  related parameters to the Dialogflow API to match an intent. For
  example, when your application starts, you can send a welcome event
  with a user name parameter to the Dialogflow API to match an intent with
  a personalized welcome message for the user.

  *   **Training phrases** - provide examples of user input to train the
  Dialogflow API agent to better match intents.

  For more information about intents, see the
  [Dialogflow
  documentation](https://cloud.google.com/dialogflow/docs/intents-overview).
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListIntents = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/ListIntents',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.ListIntentsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.ListIntentsResponse.FromString,
        )
    self.GetIntent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/GetIntent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.GetIntentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.Intent.FromString,
        )
    self.CreateIntent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/CreateIntent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.CreateIntentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.Intent.FromString,
        )
    self.UpdateIntent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/UpdateIntent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.UpdateIntentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.Intent.FromString,
        )
    self.DeleteIntent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/DeleteIntent',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.DeleteIntentRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BatchUpdateIntents = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/BatchUpdateIntents',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.BatchUpdateIntentsRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.BatchDeleteIntents = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Intents/BatchDeleteIntents',
        request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.BatchDeleteIntentsRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class IntentsServicer(object):
  """An intent represents a mapping between input from a user and an action to
  be taken by your application. When you pass user input to the
  [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
  [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) method, the
  Dialogflow API analyzes the input and searches
  for a matching intent. If no match is found, the Dialogflow API returns a
  fallback intent (`is_fallback` = true).

  You can provide additional information for the Dialogflow API to use to
  match user input to an intent by adding the following to your intent.

  *   **Contexts** - provide additional context for intent analysis. For
  example, if an intent is related to an object in your application that
  plays music, you can provide a context to determine when to match the
  intent if the user input is "turn it off". You can include a context
  that matches the intent when there is previous user input of
  "play music", and not when there is previous user input of
  "turn on the light".

  *   **Events** - allow for matching an intent by using an event name
  instead of user input. Your application can provide an event name and
  related parameters to the Dialogflow API to match an intent. For
  example, when your application starts, you can send a welcome event
  with a user name parameter to the Dialogflow API to match an intent with
  a personalized welcome message for the user.

  *   **Training phrases** - provide examples of user input to train the
  Dialogflow API agent to better match intents.

  For more information about intents, see the
  [Dialogflow
  documentation](https://cloud.google.com/dialogflow/docs/intents-overview).
  """

  def ListIntents(self, request, context):
    """Returns the list of all intents in the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetIntent(self, request, context):
    """Retrieves the specified intent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateIntent(self, request, context):
    """Creates an intent in the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateIntent(self, request, context):
    """Updates the specified intent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteIntent(self, request, context):
    """Deletes the specified intent and its direct or indirect followup intents.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchUpdateIntents(self, request, context):
    """Updates/Creates multiple intents in the specified agent.

    Operation <response: [BatchUpdateIntentsResponse][google.cloud.dialogflow.v2.BatchUpdateIntentsResponse]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchDeleteIntents(self, request, context):
    """Deletes intents in the specified agent.

    Operation <response: [google.protobuf.Empty][google.protobuf.Empty]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IntentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListIntents': grpc.unary_unary_rpc_method_handler(
          servicer.ListIntents,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.ListIntentsRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.ListIntentsResponse.SerializeToString,
      ),
      'GetIntent': grpc.unary_unary_rpc_method_handler(
          servicer.GetIntent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.GetIntentRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.Intent.SerializeToString,
      ),
      'CreateIntent': grpc.unary_unary_rpc_method_handler(
          servicer.CreateIntent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.CreateIntentRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.Intent.SerializeToString,
      ),
      'UpdateIntent': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateIntent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.UpdateIntentRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.Intent.SerializeToString,
      ),
      'DeleteIntent': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteIntent,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.DeleteIntentRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BatchUpdateIntents': grpc.unary_unary_rpc_method_handler(
          servicer.BatchUpdateIntents,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.BatchUpdateIntentsRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'BatchDeleteIntents': grpc.unary_unary_rpc_method_handler(
          servicer.BatchDeleteIntents,
          request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2.BatchDeleteIntentsRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.dialogflow.v2.Intents', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
