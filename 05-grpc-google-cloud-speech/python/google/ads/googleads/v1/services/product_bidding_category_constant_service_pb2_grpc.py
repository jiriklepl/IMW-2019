# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.googleads.v1.resources import product_bidding_category_constant_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_product__bidding__category__constant__pb2
from google.ads.googleads.v1.services import product_bidding_category_constant_service_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_services_dot_product__bidding__category__constant__service__pb2


class ProductBiddingCategoryConstantServiceStub(object):
  """Proto file describing the Product Bidding Category constant service

  Service to fetch Product Bidding Categories.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetProductBiddingCategoryConstant = channel.unary_unary(
        '/google.ads.googleads.v1.services.ProductBiddingCategoryConstantService/GetProductBiddingCategoryConstant',
        request_serializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_product__bidding__category__constant__service__pb2.GetProductBiddingCategoryConstantRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_product__bidding__category__constant__pb2.ProductBiddingCategoryConstant.FromString,
        )


class ProductBiddingCategoryConstantServiceServicer(object):
  """Proto file describing the Product Bidding Category constant service

  Service to fetch Product Bidding Categories.
  """

  def GetProductBiddingCategoryConstant(self, request, context):
    """Returns the requested Product Bidding Category in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProductBiddingCategoryConstantServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetProductBiddingCategoryConstant': grpc.unary_unary_rpc_method_handler(
          servicer.GetProductBiddingCategoryConstant,
          request_deserializer=google_dot_ads_dot_googleads_dot_v1_dot_services_dot_product__bidding__category__constant__service__pb2.GetProductBiddingCategoryConstantRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_product__bidding__category__constant__pb2.ProductBiddingCategoryConstant.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.ProductBiddingCategoryConstantService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
