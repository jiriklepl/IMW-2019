# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/enums/negative_geo_target_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/enums/negative_geo_target_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v1.enumsB\032NegativeGeoTargetTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums',
  serialized_pb=b'\n<google/ads/googleads/v1/enums/negative_geo_target_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"{\n\x19NegativeGeoTargetTypeEnum\"^\n\x15NegativeGeoTargetType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\r\n\tDONT_CARE\x10\x02\x12\x18\n\x14LOCATION_OF_PRESENCE\x10\x03\x42\xef\x01\n!com.google.ads.googleads.v1.enumsB\x1aNegativeGeoTargetTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_NEGATIVEGEOTARGETTYPEENUM_NEGATIVEGEOTARGETTYPE = _descriptor.EnumDescriptor(
  name='NegativeGeoTargetType',
  full_name='google.ads.googleads.v1.enums.NegativeGeoTargetTypeEnum.NegativeGeoTargetType',
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
      name='DONT_CARE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_OF_PRESENCE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_NEGATIVEGEOTARGETTYPEENUM_NEGATIVEGEOTARGETTYPE)


_NEGATIVEGEOTARGETTYPEENUM = _descriptor.Descriptor(
  name='NegativeGeoTargetTypeEnum',
  full_name='google.ads.googleads.v1.enums.NegativeGeoTargetTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NEGATIVEGEOTARGETTYPEENUM_NEGATIVEGEOTARGETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=248,
)

_NEGATIVEGEOTARGETTYPEENUM_NEGATIVEGEOTARGETTYPE.containing_type = _NEGATIVEGEOTARGETTYPEENUM
DESCRIPTOR.message_types_by_name['NegativeGeoTargetTypeEnum'] = _NEGATIVEGEOTARGETTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NegativeGeoTargetTypeEnum = _reflection.GeneratedProtocolMessageType('NegativeGeoTargetTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _NEGATIVEGEOTARGETTYPEENUM,
  '__module__' : 'google.ads.googleads.v1.enums.negative_geo_target_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.NegativeGeoTargetTypeEnum)
  })
_sym_db.RegisterMessage(NegativeGeoTargetTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
