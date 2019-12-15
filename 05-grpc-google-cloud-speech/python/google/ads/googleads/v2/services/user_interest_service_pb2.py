# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/user_interest_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.resources import user_interest_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_user__interest__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/user_interest_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB\030UserInterestServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\n<google/ads/googleads/v2/services/user_interest_service.proto\x12 google.ads.googleads.v2.services\x1a\x35google/ads/googleads/v2/resources/user_interest.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\"/\n\x16GetUserInterestRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xea\x01\n\x13UserInterestService\x12\xb5\x01\n\x0fGetUserInterest\x12\x38.google.ads.googleads.v2.services.GetUserInterestRequest\x1a/.google.ads.googleads.v2.resources.UserInterest\"7\x82\xd3\xe4\x93\x02\x31\x12//v2/{resource_name=customers/*/userInterests/*}\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xff\x01\n$com.google.ads.googleads.v2.servicesB\x18UserInterestServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_user__interest__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GETUSERINTERESTREQUEST = _descriptor.Descriptor(
  name='GetUserInterestRequest',
  full_name='google.ads.googleads.v2.services.GetUserInterestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetUserInterestRequest.resource_name', index=0,
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
  serialized_start=208,
  serialized_end=255,
)

DESCRIPTOR.message_types_by_name['GetUserInterestRequest'] = _GETUSERINTERESTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserInterestRequest = _reflection.GeneratedProtocolMessageType('GetUserInterestRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERINTERESTREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.user_interest_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetUserInterestRequest)
  })
_sym_db.RegisterMessage(GetUserInterestRequest)


DESCRIPTOR._options = None

_USERINTERESTSERVICE = _descriptor.ServiceDescriptor(
  name='UserInterestService',
  full_name='google.ads.googleads.v2.services.UserInterestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=258,
  serialized_end=492,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserInterest',
    full_name='google.ads.googleads.v2.services.UserInterestService.GetUserInterest',
    index=0,
    containing_service=None,
    input_type=_GETUSERINTERESTREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_user__interest__pb2._USERINTEREST,
    serialized_options=b'\202\323\344\223\0021\022//v2/{resource_name=customers/*/userInterests/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_USERINTERESTSERVICE)

DESCRIPTOR.services_by_name['UserInterestService'] = _USERINTERESTSERVICE

# @@protoc_insertion_point(module_scope)