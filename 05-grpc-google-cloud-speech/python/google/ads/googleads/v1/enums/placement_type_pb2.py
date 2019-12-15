# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/enums/placement_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/enums/placement_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v1.enumsB\022PlacementTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums',
  serialized_pb=b'\n2google/ads/googleads/v1/enums/placement_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xa9\x01\n\x11PlacementTypeEnum\"\x93\x01\n\rPlacementType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07WEBSITE\x10\x02\x12\x17\n\x13MOBILE_APP_CATEGORY\x10\x03\x12\x16\n\x12MOBILE_APPLICATION\x10\x04\x12\x11\n\rYOUTUBE_VIDEO\x10\x05\x12\x13\n\x0fYOUTUBE_CHANNEL\x10\x06\x42\xe7\x01\n!com.google.ads.googleads.v1.enumsB\x12PlacementTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PLACEMENTTYPEENUM_PLACEMENTTYPE = _descriptor.EnumDescriptor(
  name='PlacementType',
  full_name='google.ads.googleads.v1.enums.PlacementTypeEnum.PlacementType',
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
      name='WEBSITE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILE_APP_CATEGORY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILE_APPLICATION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_VIDEO', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_CHANNEL', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_PLACEMENTTYPEENUM_PLACEMENTTYPE)


_PLACEMENTTYPEENUM = _descriptor.Descriptor(
  name='PlacementTypeEnum',
  full_name='google.ads.googleads.v1.enums.PlacementTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PLACEMENTTYPEENUM_PLACEMENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=285,
)

_PLACEMENTTYPEENUM_PLACEMENTTYPE.containing_type = _PLACEMENTTYPEENUM
DESCRIPTOR.message_types_by_name['PlacementTypeEnum'] = _PLACEMENTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlacementTypeEnum = _reflection.GeneratedProtocolMessageType('PlacementTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _PLACEMENTTYPEENUM,
  '__module__' : 'google.ads.googleads.v1.enums.placement_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.PlacementTypeEnum)
  })
_sym_db.RegisterMessage(PlacementTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
