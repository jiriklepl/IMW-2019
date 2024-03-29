# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/ad_group_ad_asset_view_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.resources import ad_group_ad_asset_view_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__ad__asset__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/ad_group_ad_asset_view_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB\036AdGroupAdAssetViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\nEgoogle/ads/googleads/v2/services/ad_group_ad_asset_view_service.proto\x12 google.ads.googleads.v2.services\x1a>google/ads/googleads/v2/resources/ad_group_ad_asset_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\"5\n\x1cGetAdGroupAdAssetViewRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x88\x02\n\x19\x41\x64GroupAdAssetViewService\x12\xcd\x01\n\x15GetAdGroupAdAssetView\x12>.google.ads.googleads.v2.services.GetAdGroupAdAssetViewRequest\x1a\x35.google.ads.googleads.v2.resources.AdGroupAdAssetView\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v2/{resource_name=customers/*/adGroupAdAssetViews/*}\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x85\x02\n$com.google.ads.googleads.v2.servicesB\x1e\x41\x64GroupAdAssetViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__ad__asset__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GETADGROUPADASSETVIEWREQUEST = _descriptor.Descriptor(
  name='GetAdGroupAdAssetViewRequest',
  full_name='google.ads.googleads.v2.services.GetAdGroupAdAssetViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetAdGroupAdAssetViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=279,
)

DESCRIPTOR.message_types_by_name['GetAdGroupAdAssetViewRequest'] = _GETADGROUPADASSETVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdGroupAdAssetViewRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupAdAssetViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADGROUPADASSETVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.ad_group_ad_asset_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetAdGroupAdAssetViewRequest)
  })
_sym_db.RegisterMessage(GetAdGroupAdAssetViewRequest)


DESCRIPTOR._options = None

_ADGROUPADASSETVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='AdGroupAdAssetViewService',
  full_name='google.ads.googleads.v2.services.AdGroupAdAssetViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=282,
  serialized_end=546,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdGroupAdAssetView',
    full_name='google.ads.googleads.v2.services.AdGroupAdAssetViewService.GetAdGroupAdAssetView',
    index=0,
    containing_service=None,
    input_type=_GETADGROUPADASSETVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__ad__asset__view__pb2._ADGROUPADASSETVIEW,
    serialized_options=b'\202\323\344\223\0027\0225/v2/{resource_name=customers/*/adGroupAdAssetViews/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_ADGROUPADASSETVIEWSERVICE)

DESCRIPTOR.services_by_name['AdGroupAdAssetViewService'] = _ADGROUPADASSETVIEWSERVICE

# @@protoc_insertion_point(module_scope)
