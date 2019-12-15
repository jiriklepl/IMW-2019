# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/resources/user_location_view.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/resources/user_location_view.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v2.resourcesB\025UserLocationViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources',
  serialized_pb=b'\n:google/ads/googleads/v2/resources/user_location_view.proto\x12!google.ads.googleads.v2.resources\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x9c\x01\n\x10UserLocationView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x39\n\x14\x63ountry_criterion_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x12targeting_location\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x82\x02\n%com.google.ads.googleads.v2.resourcesB\x15UserLocationViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_USERLOCATIONVIEW = _descriptor.Descriptor(
  name='UserLocationView',
  full_name='google.ads.googleads.v2.resources.UserLocationView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.UserLocationView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_criterion_id', full_name='google.ads.googleads.v2.resources.UserLocationView.country_criterion_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeting_location', full_name='google.ads.googleads.v2.resources.UserLocationView.targeting_location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=160,
  serialized_end=316,
)

_USERLOCATIONVIEW.fields_by_name['country_criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_USERLOCATIONVIEW.fields_by_name['targeting_location'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['UserLocationView'] = _USERLOCATIONVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserLocationView = _reflection.GeneratedProtocolMessageType('UserLocationView', (_message.Message,), {
  'DESCRIPTOR' : _USERLOCATIONVIEW,
  '__module__' : 'google.ads.googleads.v2.resources.user_location_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.UserLocationView)
  })
_sym_db.RegisterMessage(UserLocationView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
