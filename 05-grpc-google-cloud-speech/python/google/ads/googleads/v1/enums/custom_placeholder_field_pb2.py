# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/enums/custom_placeholder_field.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/enums/custom_placeholder_field.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v1.enumsB\033CustomPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums',
  serialized_pb=b'\n<google/ads/googleads/v1/enums/custom_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xbe\x03\n\x1a\x43ustomPlaceholderFieldEnum\"\x9f\x03\n\x16\x43ustomPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x07\n\x03ID2\x10\x03\x12\x0e\n\nITEM_TITLE\x10\x04\x12\x11\n\rITEM_SUBTITLE\x10\x05\x12\x14\n\x10ITEM_DESCRIPTION\x10\x06\x12\x10\n\x0cITEM_ADDRESS\x10\x07\x12\t\n\x05PRICE\x10\x08\x12\x13\n\x0f\x46ORMATTED_PRICE\x10\t\x12\x0e\n\nSALE_PRICE\x10\n\x12\x18\n\x14\x46ORMATTED_SALE_PRICE\x10\x0b\x12\r\n\tIMAGE_URL\x10\x0c\x12\x11\n\rITEM_CATEGORY\x10\r\x12\x0e\n\nFINAL_URLS\x10\x0e\x12\x15\n\x11\x46INAL_MOBILE_URLS\x10\x0f\x12\x10\n\x0cTRACKING_URL\x10\x10\x12\x17\n\x13\x43ONTEXTUAL_KEYWORDS\x10\x11\x12\x14\n\x10\x41NDROID_APP_LINK\x10\x12\x12\x0f\n\x0bSIMILAR_IDS\x10\x13\x12\x10\n\x0cIOS_APP_LINK\x10\x14\x12\x14\n\x10IOS_APP_STORE_ID\x10\x15\x42\xf0\x01\n!com.google.ads.googleads.v1.enumsB\x1b\x43ustomPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CUSTOMPLACEHOLDERFIELDENUM_CUSTOMPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='CustomPlaceholderField',
  full_name='google.ads.googleads.v1.enums.CustomPlaceholderFieldEnum.CustomPlaceholderField',
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
      name='ID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID2', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TITLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SUBTITLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_DESCRIPTION', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ADDRESS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMATTED_PRICE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALE_PRICE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMATTED_SALE_PRICE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_URL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URLS', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTEXTUAL_KEYWORDS', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_APP_LINK', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR_IDS', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_LINK', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_STORE_ID', index=21, number=21,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=572,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMPLACEHOLDERFIELDENUM_CUSTOMPLACEHOLDERFIELD)


_CUSTOMPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='CustomPlaceholderFieldEnum',
  full_name='google.ads.googleads.v1.enums.CustomPlaceholderFieldEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMPLACEHOLDERFIELDENUM_CUSTOMPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=572,
)

_CUSTOMPLACEHOLDERFIELDENUM_CUSTOMPLACEHOLDERFIELD.containing_type = _CUSTOMPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['CustomPlaceholderFieldEnum'] = _CUSTOMPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('CustomPlaceholderFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMPLACEHOLDERFIELDENUM,
  '__module__' : 'google.ads.googleads.v1.enums.custom_placeholder_field_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.CustomPlaceholderFieldEnum)
  })
_sym_db.RegisterMessage(CustomPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)