# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.webrisk.v1beta1 import webrisk_pb2 as google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2


class WebRiskServiceV1Beta1Stub(object):
  """Web Risk v1beta1 API defines an interface to detect malicious URLs on your
  website and in client applications.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ComputeThreatListDiff = channel.unary_unary(
        '/google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1/ComputeThreatListDiff',
        request_serializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.ComputeThreatListDiffRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.ComputeThreatListDiffResponse.FromString,
        )
    self.SearchUris = channel.unary_unary(
        '/google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1/SearchUris',
        request_serializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchUrisRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchUrisResponse.FromString,
        )
    self.SearchHashes = channel.unary_unary(
        '/google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1/SearchHashes',
        request_serializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchHashesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchHashesResponse.FromString,
        )


class WebRiskServiceV1Beta1Servicer(object):
  """Web Risk v1beta1 API defines an interface to detect malicious URLs on your
  website and in client applications.
  """

  def ComputeThreatListDiff(self, request, context):
    """Gets the most recent threat list diffs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchUris(self, request, context):
    """This method is used to check whether a URI is on a given threatList.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchHashes(self, request, context):
    """Gets the full hashes that match the requested hash prefix.
    This is used after a hash prefix is looked up in a threatList
    and there is a match. The client side threatList only holds partial hashes
    so the client must query this method to determine if there is a full
    hash match of a threat.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WebRiskServiceV1Beta1Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ComputeThreatListDiff': grpc.unary_unary_rpc_method_handler(
          servicer.ComputeThreatListDiff,
          request_deserializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.ComputeThreatListDiffRequest.FromString,
          response_serializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.ComputeThreatListDiffResponse.SerializeToString,
      ),
      'SearchUris': grpc.unary_unary_rpc_method_handler(
          servicer.SearchUris,
          request_deserializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchUrisRequest.FromString,
          response_serializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchUrisResponse.SerializeToString,
      ),
      'SearchHashes': grpc.unary_unary_rpc_method_handler(
          servicer.SearchHashes,
          request_deserializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchHashesRequest.FromString,
          response_serializer=google_dot_cloud_dot_webrisk_dot_v1beta1_dot_webrisk__pb2.SearchHashesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
