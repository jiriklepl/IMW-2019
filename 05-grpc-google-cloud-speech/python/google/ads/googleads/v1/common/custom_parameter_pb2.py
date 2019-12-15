# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/common/custom_parameter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/common/custom_parameter.proto',
  package='google.ads.googleads.v1.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v1.commonB\024CustomParameterProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Common\312\002\036Google\\Ads\\GoogleAds\\V1\\Common\352\002\"Google::Ads::GoogleAds::V1::Common',
  serialized_pb=b'\n5google/ads/googleads/v1/common/custom_parameter.proto\x12\x1egoogle.ads.googleads.v1.common\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"i\n\x0f\x43ustomParameter\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xef\x01\n\"com.google.ads.googleads.v1.commonB\x14\x43ustomParameterProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Common\xea\x02\"Google::Ads::GoogleAds::V1::Commonb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CUSTOMPARAMETER = _descriptor.Descriptor(
  name='CustomParameter',
  full_name='google.ads.googleads.v1.common.CustomParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.ads.googleads.v1.common.CustomParameter.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.ads.googleads.v1.common.CustomParameter.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=151,
  serialized_end=256,
)

_CUSTOMPARAMETER.fields_by_name['key'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMPARAMETER.fields_by_name['value'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CustomParameter'] = _CUSTOMPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomParameter = _reflection.GeneratedProtocolMessageType('CustomParameter', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMPARAMETER,
  '__module__' : 'google.ads.googleads.v1.common.custom_parameter_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.CustomParameter)
  })
_sym_db.RegisterMessage(CustomParameter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)