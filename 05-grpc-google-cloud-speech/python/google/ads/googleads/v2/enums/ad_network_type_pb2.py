# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/ad_network_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/ad_network_type.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB\022AdNetworkTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\n3google/ads/googleads/v2/enums/ad_network_type.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\xa3\x01\n\x11\x41\x64NetworkTypeEnum\"\x8d\x01\n\rAdNetworkType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06SEARCH\x10\x02\x12\x13\n\x0fSEARCH_PARTNERS\x10\x03\x12\x0b\n\x07\x43ONTENT\x10\x04\x12\x12\n\x0eYOUTUBE_SEARCH\x10\x05\x12\x11\n\rYOUTUBE_WATCH\x10\x06\x12\t\n\x05MIXED\x10\x07\x42\xe7\x01\n!com.google.ads.googleads.v2.enumsB\x12\x41\x64NetworkTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADNETWORKTYPEENUM_ADNETWORKTYPE = _descriptor.EnumDescriptor(
  name='AdNetworkType',
  full_name='google.ads.googleads.v2.enums.AdNetworkTypeEnum.AdNetworkType',
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
      name='SEARCH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_PARTNERS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_SEARCH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_WATCH', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIXED', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=139,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_ADNETWORKTYPEENUM_ADNETWORKTYPE)


_ADNETWORKTYPEENUM = _descriptor.Descriptor(
  name='AdNetworkTypeEnum',
  full_name='google.ads.googleads.v2.enums.AdNetworkTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADNETWORKTYPEENUM_ADNETWORKTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=280,
)

_ADNETWORKTYPEENUM_ADNETWORKTYPE.containing_type = _ADNETWORKTYPEENUM
DESCRIPTOR.message_types_by_name['AdNetworkTypeEnum'] = _ADNETWORKTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdNetworkTypeEnum = _reflection.GeneratedProtocolMessageType('AdNetworkTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADNETWORKTYPEENUM,
  '__module__' : 'google.ads.googleads.v2.enums.ad_network_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.AdNetworkTypeEnum)
  })
_sym_db.RegisterMessage(AdNetworkTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
