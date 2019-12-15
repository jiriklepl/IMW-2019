# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/location_placeholder_field.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/location_placeholder_field.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB\035LocationPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\n>google/ads/googleads/v2/enums/location_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\xe1\x01\n\x1cLocationPlaceholderFieldEnum\"\xc0\x01\n\x18LocationPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rBUSINESS_NAME\x10\x02\x12\x12\n\x0e\x41\x44\x44RESS_LINE_1\x10\x03\x12\x12\n\x0e\x41\x44\x44RESS_LINE_2\x10\x04\x12\x08\n\x04\x43ITY\x10\x05\x12\x0c\n\x08PROVINCE\x10\x06\x12\x0f\n\x0bPOSTAL_CODE\x10\x07\x12\x10\n\x0c\x43OUNTRY_CODE\x10\x08\x12\x10\n\x0cPHONE_NUMBER\x10\tB\xf2\x01\n!com.google.ads.googleads.v2.enumsB\x1dLocationPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LOCATIONPLACEHOLDERFIELDENUM_LOCATIONPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='LocationPlaceholderField',
  full_name='google.ads.googleads.v2.enums.LocationPlaceholderFieldEnum.LocationPlaceholderField',
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
      name='BUSINESS_NAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_LINE_1', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_LINE_2', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROVINCE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTRY_CODE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=353,
)
_sym_db.RegisterEnumDescriptor(_LOCATIONPLACEHOLDERFIELDENUM_LOCATIONPLACEHOLDERFIELD)


_LOCATIONPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='LocationPlaceholderFieldEnum',
  full_name='google.ads.googleads.v2.enums.LocationPlaceholderFieldEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOCATIONPLACEHOLDERFIELDENUM_LOCATIONPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=353,
)

_LOCATIONPLACEHOLDERFIELDENUM_LOCATIONPLACEHOLDERFIELD.containing_type = _LOCATIONPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['LocationPlaceholderFieldEnum'] = _LOCATIONPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('LocationPlaceholderFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONPLACEHOLDERFIELDENUM,
  '__module__' : 'google.ads.googleads.v2.enums.location_placeholder_field_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.LocationPlaceholderFieldEnum)
  })
_sym_db.RegisterMessage(LocationPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
