# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/errors/conversion_action_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/errors/conversion_action_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v2.errorsB\032ConversionActionErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors',
  serialized_pb=b'\n<google/ads/googleads/v2/errors/conversion_action_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"\xef\x02\n\x19\x43onversionActionErrorEnum\"\xd1\x02\n\x15\x43onversionActionError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x02\x12\x14\n\x10\x44UPLICATE_APP_ID\x10\x03\x12\x37\n3TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD\x10\x04\x12\x31\n-BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION\x10\x05\x12)\n%DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED\x10\x06\x12\x1d\n\x19\x44\x41TA_DRIVEN_MODEL_EXPIRED\x10\x07\x12\x1b\n\x17\x44\x41TA_DRIVEN_MODEL_STALE\x10\x08\x12\x1d\n\x19\x44\x41TA_DRIVEN_MODEL_UNKNOWN\x10\tB\xf5\x01\n\"com.google.ads.googleads.v2.errorsB\x1a\x43onversionActionErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONVERSIONACTIONERRORENUM_CONVERSIONACTIONERROR = _descriptor.EnumDescriptor(
  name='ConversionActionError',
  full_name='google.ads.googleads.v2.errors.ConversionActionErrorEnum.ConversionActionError',
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
      name='DUPLICATE_NAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_APP_ID', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_DRIVEN_MODEL_EXPIRED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_DRIVEN_MODEL_STALE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_DRIVEN_MODEL_UNKNOWN', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_CONVERSIONACTIONERRORENUM_CONVERSIONACTIONERROR)


_CONVERSIONACTIONERRORENUM = _descriptor.Descriptor(
  name='ConversionActionErrorEnum',
  full_name='google.ads.googleads.v2.errors.ConversionActionErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVERSIONACTIONERRORENUM_CONVERSIONACTIONERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=494,
)

_CONVERSIONACTIONERRORENUM_CONVERSIONACTIONERROR.containing_type = _CONVERSIONACTIONERRORENUM
DESCRIPTOR.message_types_by_name['ConversionActionErrorEnum'] = _CONVERSIONACTIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionActionErrorEnum = _reflection.GeneratedProtocolMessageType('ConversionActionErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONACTIONERRORENUM,
  '__module__' : 'google.ads.googleads.v2.errors.conversion_action_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.ConversionActionErrorEnum)
  })
_sym_db.RegisterMessage(ConversionActionErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
