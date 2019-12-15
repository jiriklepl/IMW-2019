# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/errors/internal_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/errors/internal_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v1.errorsB\022InternalErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors',
  serialized_pb=b'\n3google/ads/googleads/v1/errors/internal_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\x89\x01\n\x11InternalErrorEnum\"t\n\rInternalError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x1c\n\x18\x45RROR_CODE_NOT_PUBLISHED\x10\x03\x12\x13\n\x0fTRANSIENT_ERROR\x10\x04\x42\xed\x01\n\"com.google.ads.googleads.v1.errorsB\x12InternalErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_INTERNALERRORENUM_INTERNALERROR = _descriptor.EnumDescriptor(
  name='InternalError',
  full_name='google.ads.googleads.v1.errors.InternalErrorEnum.InternalError',
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
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CODE_NOT_PUBLISHED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSIENT_ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=139,
  serialized_end=255,
)
_sym_db.RegisterEnumDescriptor(_INTERNALERRORENUM_INTERNALERROR)


_INTERNALERRORENUM = _descriptor.Descriptor(
  name='InternalErrorEnum',
  full_name='google.ads.googleads.v1.errors.InternalErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INTERNALERRORENUM_INTERNALERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=255,
)

_INTERNALERRORENUM_INTERNALERROR.containing_type = _INTERNALERRORENUM
DESCRIPTOR.message_types_by_name['InternalErrorEnum'] = _INTERNALERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InternalErrorEnum = _reflection.GeneratedProtocolMessageType('InternalErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _INTERNALERRORENUM,
  '__module__' : 'google.ads.googleads.v1.errors.internal_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.InternalErrorEnum)
  })
_sym_db.RegisterMessage(InternalErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
