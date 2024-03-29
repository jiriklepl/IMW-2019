# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/managed_placement_view_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import managed_placement_view_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_managed__placement__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/managed_placement_view_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB ManagedPlacementViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\nEgoogle/ads/googleads/v1/services/managed_placement_view_service.proto\x12 google.ads.googleads.v1.services\x1a>google/ads/googleads/v1/resources/managed_placement_view.proto\x1a\x1cgoogle/api/annotations.proto\"7\n\x1eGetManagedPlacementViewRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xf5\x01\n\x1bManagedPlacementViewService\x12\xd5\x01\n\x17GetManagedPlacementView\x12@.google.ads.googleads.v1.services.GetManagedPlacementViewRequest\x1a\x37.google.ads.googleads.v1.resources.ManagedPlacementView\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/{resource_name=customers/*/managedPlacementViews/*}B\x87\x02\n$com.google.ads.googleads.v1.servicesB ManagedPlacementViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_managed__placement__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETMANAGEDPLACEMENTVIEWREQUEST = _descriptor.Descriptor(
  name='GetManagedPlacementViewRequest',
  full_name='google.ads.googleads.v1.services.GetManagedPlacementViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetManagedPlacementViewRequest.resource_name', index=0,
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
  serialized_start=201,
  serialized_end=256,
)

DESCRIPTOR.message_types_by_name['GetManagedPlacementViewRequest'] = _GETMANAGEDPLACEMENTVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetManagedPlacementViewRequest = _reflection.GeneratedProtocolMessageType('GetManagedPlacementViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMANAGEDPLACEMENTVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.managed_placement_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetManagedPlacementViewRequest)
  })
_sym_db.RegisterMessage(GetManagedPlacementViewRequest)


DESCRIPTOR._options = None

_MANAGEDPLACEMENTVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='ManagedPlacementViewService',
  full_name='google.ads.googleads.v1.services.ManagedPlacementViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=259,
  serialized_end=504,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetManagedPlacementView',
    full_name='google.ads.googleads.v1.services.ManagedPlacementViewService.GetManagedPlacementView',
    index=0,
    containing_service=None,
    input_type=_GETMANAGEDPLACEMENTVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_managed__placement__view__pb2._MANAGEDPLACEMENTVIEW,
    serialized_options=b'\202\323\344\223\0029\0227/v1/{resource_name=customers/*/managedPlacementViews/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGEDPLACEMENTVIEWSERVICE)

DESCRIPTOR.services_by_name['ManagedPlacementViewService'] = _MANAGEDPLACEMENTVIEWSERVICE

# @@protoc_insertion_point(module_scope)
