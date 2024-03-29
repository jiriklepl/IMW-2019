# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/advertising_channel_sub_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/advertising_channel_sub_type.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB\036AdvertisingChannelSubTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\n@google/ads/googleads/v2/enums/advertising_channel_sub_type.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x95\x03\n\x1d\x41\x64vertisingChannelSubTypeEnum\"\xf3\x02\n\x19\x41\x64vertisingChannelSubType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11SEARCH_MOBILE_APP\x10\x02\x12\x16\n\x12\x44ISPLAY_MOBILE_APP\x10\x03\x12\x12\n\x0eSEARCH_EXPRESS\x10\x04\x12\x13\n\x0f\x44ISPLAY_EXPRESS\x10\x05\x12\x16\n\x12SHOPPING_SMART_ADS\x10\x06\x12\x14\n\x10\x44ISPLAY_GMAIL_AD\x10\x07\x12\x1a\n\x16\x44ISPLAY_SMART_CAMPAIGN\x10\x08\x12\x13\n\x0fVIDEO_OUTSTREAM\x10\t\x12\x10\n\x0cVIDEO_ACTION\x10\n\x12\x17\n\x13VIDEO_NON_SKIPPABLE\x10\x0b\x12\x10\n\x0c\x41PP_CAMPAIGN\x10\x0c\x12\x1f\n\x1b\x41PP_CAMPAIGN_FOR_ENGAGEMENT\x10\r\x12#\n\x1fSHOPPING_COMPARISON_LISTING_ADS\x10\x0f\x42\xf3\x01\n!com.google.ads.googleads.v2.enumsB\x1e\x41\x64vertisingChannelSubTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADVERTISINGCHANNELSUBTYPEENUM_ADVERTISINGCHANNELSUBTYPE = _descriptor.EnumDescriptor(
  name='AdvertisingChannelSubType',
  full_name='google.ads.googleads.v2.enums.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType',
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
      name='SEARCH_MOBILE_APP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_MOBILE_APP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_EXPRESS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_EXPRESS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_SMART_ADS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_GMAIL_AD', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_SMART_CAMPAIGN', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_OUTSTREAM', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_ACTION', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_NON_SKIPPABLE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_CAMPAIGN', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_CAMPAIGN_FOR_ENGAGEMENT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_COMPARISON_LISTING_ADS', index=14, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=164,
  serialized_end=535,
)
_sym_db.RegisterEnumDescriptor(_ADVERTISINGCHANNELSUBTYPEENUM_ADVERTISINGCHANNELSUBTYPE)


_ADVERTISINGCHANNELSUBTYPEENUM = _descriptor.Descriptor(
  name='AdvertisingChannelSubTypeEnum',
  full_name='google.ads.googleads.v2.enums.AdvertisingChannelSubTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADVERTISINGCHANNELSUBTYPEENUM_ADVERTISINGCHANNELSUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=535,
)

_ADVERTISINGCHANNELSUBTYPEENUM_ADVERTISINGCHANNELSUBTYPE.containing_type = _ADVERTISINGCHANNELSUBTYPEENUM
DESCRIPTOR.message_types_by_name['AdvertisingChannelSubTypeEnum'] = _ADVERTISINGCHANNELSUBTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdvertisingChannelSubTypeEnum = _reflection.GeneratedProtocolMessageType('AdvertisingChannelSubTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADVERTISINGCHANNELSUBTYPEENUM,
  '__module__' : 'google.ads.googleads.v2.enums.advertising_channel_sub_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.AdvertisingChannelSubTypeEnum)
  })
_sym_db.RegisterMessage(AdvertisingChannelSubTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
