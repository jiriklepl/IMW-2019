# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.recaptchaenterprise.v1beta1 import recaptchaenterprise_pb2 as google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class RecaptchaEnterpriseServiceV1Beta1Stub(object):
  """Service to determine the likelihood an event is legitimate.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateAssessment = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/CreateAssessment',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.CreateAssessmentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Assessment.FromString,
        )
    self.AnnotateAssessment = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/AnnotateAssessment',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.AnnotateAssessmentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.AnnotateAssessmentResponse.FromString,
        )
    self.CreateKey = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/CreateKey',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.CreateKeyRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Key.FromString,
        )
    self.ListKeys = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/ListKeys',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.ListKeysRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.ListKeysResponse.FromString,
        )
    self.GetKey = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/GetKey',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.GetKeyRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Key.FromString,
        )
    self.UpdateKey = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/UpdateKey',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.UpdateKeyRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Key.FromString,
        )
    self.DeleteKey = channel.unary_unary(
        '/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/DeleteKey',
        request_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.DeleteKeyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class RecaptchaEnterpriseServiceV1Beta1Servicer(object):
  """Service to determine the likelihood an event is legitimate.
  """

  def CreateAssessment(self, request, context):
    """Creates an Assessment of the likelihood an event is legitimate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AnnotateAssessment(self, request, context):
    """Annotates a previously created Assessment to provide additional information
    on whether the event turned out to be authentic or fradulent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateKey(self, request, context):
    """Creates a new reCAPTCHA Enterprise key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListKeys(self, request, context):
    """Returns the list of all keys that belong to a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKey(self, request, context):
    """Returns the specified key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateKey(self, request, context):
    """Updates the specified key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteKey(self, request, context):
    """Deletes the specified key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RecaptchaEnterpriseServiceV1Beta1Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateAssessment': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAssessment,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.CreateAssessmentRequest.FromString,
          response_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Assessment.SerializeToString,
      ),
      'AnnotateAssessment': grpc.unary_unary_rpc_method_handler(
          servicer.AnnotateAssessment,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.AnnotateAssessmentRequest.FromString,
          response_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.AnnotateAssessmentResponse.SerializeToString,
      ),
      'CreateKey': grpc.unary_unary_rpc_method_handler(
          servicer.CreateKey,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.CreateKeyRequest.FromString,
          response_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Key.SerializeToString,
      ),
      'ListKeys': grpc.unary_unary_rpc_method_handler(
          servicer.ListKeys,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.ListKeysRequest.FromString,
          response_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.ListKeysResponse.SerializeToString,
      ),
      'GetKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetKey,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.GetKeyRequest.FromString,
          response_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Key.SerializeToString,
      ),
      'UpdateKey': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateKey,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.UpdateKeyRequest.FromString,
          response_serializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.Key.SerializeToString,
      ),
      'DeleteKey': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteKey,
          request_deserializer=google_dot_cloud_dot_recaptchaenterprise_dot_v1beta1_dot_recaptchaenterprise__pb2.DeleteKeyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
