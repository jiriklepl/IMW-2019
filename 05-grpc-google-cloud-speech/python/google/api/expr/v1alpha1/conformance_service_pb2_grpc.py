# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.api.expr.v1alpha1 import conformance_service_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2


class ConformanceServiceStub(object):
  """Access a CEL implementation from another process or machine.
  A CEL implementation is decomposed as a parser, a static checker,
  and an evaluator.  Every CEL implementation is expected to provide
  a server for this API.  The API will be used for conformance testing
  and other utilities.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Parse = channel.unary_unary(
        '/google.api.expr.v1alpha1.ConformanceService/Parse',
        request_serializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.ParseRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.ParseResponse.FromString,
        )
    self.Check = channel.unary_unary(
        '/google.api.expr.v1alpha1.ConformanceService/Check',
        request_serializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.CheckRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.CheckResponse.FromString,
        )
    self.Eval = channel.unary_unary(
        '/google.api.expr.v1alpha1.ConformanceService/Eval',
        request_serializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.EvalRequest.SerializeToString,
        response_deserializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.EvalResponse.FromString,
        )


class ConformanceServiceServicer(object):
  """Access a CEL implementation from another process or machine.
  A CEL implementation is decomposed as a parser, a static checker,
  and an evaluator.  Every CEL implementation is expected to provide
  a server for this API.  The API will be used for conformance testing
  and other utilities.
  """

  def Parse(self, request, context):
    """Transforms CEL source text into a parsed representation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Check(self, request, context):
    """Runs static checks on a parsed CEL representation and return
    an annotated representation, or a set of issues.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Eval(self, request, context):
    """Evaluates a parsed or annotation CEL representation given
    values of external bindings.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConformanceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Parse': grpc.unary_unary_rpc_method_handler(
          servicer.Parse,
          request_deserializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.ParseRequest.FromString,
          response_serializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.ParseResponse.SerializeToString,
      ),
      'Check': grpc.unary_unary_rpc_method_handler(
          servicer.Check,
          request_deserializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.CheckRequest.FromString,
          response_serializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.CheckResponse.SerializeToString,
      ),
      'Eval': grpc.unary_unary_rpc_method_handler(
          servicer.Eval,
          request_deserializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.EvalRequest.FromString,
          response_serializer=google_dot_api_dot_expr_dot_v1alpha1_dot_conformance__service__pb2.EvalResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.api.expr.v1alpha1.ConformanceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
