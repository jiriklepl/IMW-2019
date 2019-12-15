# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.texttospeech.v1beta1 import cloud_tts_pb2 as google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2


class TextToSpeechStub(object):
  """Service that implements Google Cloud Text-to-Speech API.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListVoices = channel.unary_unary(
        '/google.cloud.texttospeech.v1beta1.TextToSpeech/ListVoices',
        request_serializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.ListVoicesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.ListVoicesResponse.FromString,
        )
    self.SynthesizeSpeech = channel.unary_unary(
        '/google.cloud.texttospeech.v1beta1.TextToSpeech/SynthesizeSpeech',
        request_serializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.SynthesizeSpeechRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.SynthesizeSpeechResponse.FromString,
        )


class TextToSpeechServicer(object):
  """Service that implements Google Cloud Text-to-Speech API.
  """

  def ListVoices(self, request, context):
    """Returns a list of Voice supported for synthesis.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SynthesizeSpeech(self, request, context):
    """Synthesizes speech synchronously: receive results after all text input
    has been processed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TextToSpeechServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListVoices': grpc.unary_unary_rpc_method_handler(
          servicer.ListVoices,
          request_deserializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.ListVoicesRequest.FromString,
          response_serializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.ListVoicesResponse.SerializeToString,
      ),
      'SynthesizeSpeech': grpc.unary_unary_rpc_method_handler(
          servicer.SynthesizeSpeech,
          request_deserializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.SynthesizeSpeechRequest.FromString,
          response_serializer=google_dot_cloud_dot_texttospeech_dot_v1beta1_dot_cloud__tts__pb2.SynthesizeSpeechResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.texttospeech.v1beta1.TextToSpeech', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
