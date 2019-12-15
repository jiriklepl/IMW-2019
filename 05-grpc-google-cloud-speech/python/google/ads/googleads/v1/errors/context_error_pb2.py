# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/errors/context_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/errors/context_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v1.errorsB\021ContextErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors',
  serialized_pb=b'\n2google/ads/googleads/v1/errors/context_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\x9c\x01\n\x10\x43ontextErrorEnum\"\x87\x01\n\x0c\x43ontextError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\'\n#OPERATION_NOT_PERMITTED_FOR_CONTEXT\x10\x02\x12\x30\n,OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE\x10\x03\x42\xec\x01\n\"com.google.ads.googleads.v1.errorsB\x11\x43ontextErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONTEXTERRORENUM_CONTEXTERROR = _descriptor.EnumDescriptor(
  name='ContextError',
  full_name='google.ads.googleads.v1.errors.ContextErrorEnum.ContextError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_NOT_PERMITTED_FOR_CONTEXT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=273,
)
_sym_db.RegisterEnumDescriptor(_CONTEXTERRORENUM_CONTEXTERROR)


_CONTEXTERRORENUM = _descriptor.Descriptor(
  name='ContextErrorEnum',
  full_name='google.ads.googleads.v1.errors.ContextErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTEXTERRORENUM_CONTEXTERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=273,
)

_CONTEXTERRORENUM_CONTEXTERROR.containing_type = _CONTEXTERRORENUM
DESCRIPTOR.message_types_by_name['ContextErrorEnum'] = _CONTEXTERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContextErrorEnum = _reflection.GeneratedProtocolMessageType('ContextErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXTERRORENUM,
  '__module__' : 'google.ads.googleads.v1.errors.context_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.ContextErrorEnum)
  })
_sym_db.RegisterMessage(ContextErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
