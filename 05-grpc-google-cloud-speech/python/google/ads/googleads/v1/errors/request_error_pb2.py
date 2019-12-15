# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/errors/request_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/errors/request_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v1.errorsB\021RequestErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors',
  serialized_pb=b'\n2google/ads/googleads/v1/errors/request_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\xcd\x04\n\x10RequestErrorEnum\"\xb8\x04\n\x0cRequestError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x19\n\x15RESOURCE_NAME_MISSING\x10\x03\x12\x1b\n\x17RESOURCE_NAME_MALFORMED\x10\x04\x12\x13\n\x0f\x42\x41\x44_RESOURCE_ID\x10\x11\x12\x17\n\x13INVALID_CUSTOMER_ID\x10\x10\x12\x16\n\x12OPERATION_REQUIRED\x10\x05\x12\x16\n\x12RESOURCE_NOT_FOUND\x10\x06\x12\x16\n\x12INVALID_PAGE_TOKEN\x10\x07\x12\x16\n\x12\x45XPIRED_PAGE_TOKEN\x10\x08\x12\x15\n\x11INVALID_PAGE_SIZE\x10\x16\x12\x1a\n\x16REQUIRED_FIELD_MISSING\x10\t\x12\x13\n\x0fIMMUTABLE_FIELD\x10\x0b\x12\x1e\n\x1aTOO_MANY_MUTATE_OPERATIONS\x10\r\x12)\n%CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT\x10\x0e\x12\x1f\n\x1b\x43\x41NNOT_MODIFY_FOREIGN_FIELD\x10\x0f\x12\x16\n\x12INVALID_ENUM_VALUE\x10\x12\x12%\n!DEVELOPER_TOKEN_PARAMETER_MISSING\x10\x13\x12\'\n#LOGIN_CUSTOMER_ID_PARAMETER_MISSING\x10\x14\x12(\n$VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN\x10\x15\x42\xec\x01\n\"com.google.ads.googleads.v1.errorsB\x11RequestErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_REQUESTERRORENUM_REQUESTERROR = _descriptor.EnumDescriptor(
  name='RequestError',
  full_name='google.ads.googleads.v1.errors.RequestErrorEnum.RequestError',
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
      name='RESOURCE_NAME_MISSING', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_NAME_MALFORMED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_RESOURCE_ID', index=4, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CUSTOMER_ID', index=5, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_REQUIRED', index=6, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_NOT_FOUND', index=7, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAGE_TOKEN', index=8, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED_PAGE_TOKEN', index=9, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAGE_SIZE', index=10, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRED_FIELD_MISSING', index=11, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMMUTABLE_FIELD', index=12, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_MUTATE_OPERATIONS', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_FOREIGN_FIELD', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ENUM_VALUE', index=16, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVELOPER_TOKEN_PARAMETER_MISSING', index=17, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_CUSTOMER_ID_PARAMETER_MISSING', index=18, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN', index=19, number=21,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=706,
)
_sym_db.RegisterEnumDescriptor(_REQUESTERRORENUM_REQUESTERROR)


_REQUESTERRORENUM = _descriptor.Descriptor(
  name='RequestErrorEnum',
  full_name='google.ads.googleads.v1.errors.RequestErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTERRORENUM_REQUESTERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=706,
)

_REQUESTERRORENUM_REQUESTERROR.containing_type = _REQUESTERRORENUM
DESCRIPTOR.message_types_by_name['RequestErrorEnum'] = _REQUESTERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestErrorEnum = _reflection.GeneratedProtocolMessageType('RequestErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTERRORENUM,
  '__module__' : 'google.ads.googleads.v1.errors.request_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.RequestErrorEnum)
  })
_sym_db.RegisterMessage(RequestErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
