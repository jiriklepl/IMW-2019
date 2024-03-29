# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/resources/customer_client.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/resources/customer_client.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v1.resourcesB\023CustomerClientProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources',
  serialized_pb=b'\n7google/ads/googleads/v1/resources/customer_client.proto\x12!google.ads.googleads.v1.resources\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xb6\x01\n\x0e\x43ustomerClient\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x35\n\x0f\x63lient_customer\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x06hidden\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x05level\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x80\x02\n%com.google.ads.googleads.v1.resourcesB\x13\x43ustomerClientProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CUSTOMERCLIENT = _descriptor.Descriptor(
  name='CustomerClient',
  full_name='google.ads.googleads.v1.resources.CustomerClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.CustomerClient.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_customer', full_name='google.ads.googleads.v1.resources.CustomerClient.client_customer', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='google.ads.googleads.v1.resources.CustomerClient.hidden', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='google.ads.googleads.v1.resources.CustomerClient.level', index=3,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=157,
  serialized_end=339,
)

_CUSTOMERCLIENT.fields_by_name['client_customer'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERCLIENT.fields_by_name['hidden'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMERCLIENT.fields_by_name['level'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['CustomerClient'] = _CUSTOMERCLIENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerClient = _reflection.GeneratedProtocolMessageType('CustomerClient', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERCLIENT,
  '__module__' : 'google.ads.googleads.v1.resources.customer_client_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.CustomerClient)
  })
_sym_db.RegisterMessage(CustomerClient)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
