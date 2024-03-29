# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/google_ads_field_category.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/google_ads_field_category.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB\033GoogleAdsFieldCategoryProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\n=google/ads/googleads/v2/enums/google_ads_field_category.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x8a\x01\n\x1aGoogleAdsFieldCategoryEnum\"l\n\x16GoogleAdsFieldCategory\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08RESOURCE\x10\x02\x12\r\n\tATTRIBUTE\x10\x03\x12\x0b\n\x07SEGMENT\x10\x05\x12\n\n\x06METRIC\x10\x06\x42\xf0\x01\n!com.google.ads.googleads.v2.enumsB\x1bGoogleAdsFieldCategoryProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_GOOGLEADSFIELDCATEGORYENUM_GOOGLEADSFIELDCATEGORY = _descriptor.EnumDescriptor(
  name='GoogleAdsFieldCategory',
  full_name='google.ads.googleads.v2.enums.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory',
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
      name='RESOURCE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTRIBUTE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEGMENT', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METRIC', index=5, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_GOOGLEADSFIELDCATEGORYENUM_GOOGLEADSFIELDCATEGORY)


_GOOGLEADSFIELDCATEGORYENUM = _descriptor.Descriptor(
  name='GoogleAdsFieldCategoryEnum',
  full_name='google.ads.googleads.v2.enums.GoogleAdsFieldCategoryEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GOOGLEADSFIELDCATEGORYENUM_GOOGLEADSFIELDCATEGORY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=265,
)

_GOOGLEADSFIELDCATEGORYENUM_GOOGLEADSFIELDCATEGORY.containing_type = _GOOGLEADSFIELDCATEGORYENUM
DESCRIPTOR.message_types_by_name['GoogleAdsFieldCategoryEnum'] = _GOOGLEADSFIELDCATEGORYENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GoogleAdsFieldCategoryEnum = _reflection.GeneratedProtocolMessageType('GoogleAdsFieldCategoryEnum', (_message.Message,), {
  'DESCRIPTOR' : _GOOGLEADSFIELDCATEGORYENUM,
  '__module__' : 'google.ads.googleads.v2.enums.google_ads_field_category_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.GoogleAdsFieldCategoryEnum)
  })
_sym_db.RegisterMessage(GoogleAdsFieldCategoryEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
