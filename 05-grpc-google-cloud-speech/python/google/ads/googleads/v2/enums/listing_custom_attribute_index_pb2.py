# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/listing_custom_attribute_index.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/listing_custom_attribute_index.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB ListingCustomAttributeIndexProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\nBgoogle/ads/googleads/v2/enums/listing_custom_attribute_index.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x9a\x01\n\x1fListingCustomAttributeIndexEnum\"w\n\x1bListingCustomAttributeIndex\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06INDEX0\x10\x07\x12\n\n\x06INDEX1\x10\x08\x12\n\n\x06INDEX2\x10\t\x12\n\n\x06INDEX3\x10\n\x12\n\n\x06INDEX4\x10\x0b\x42\xf5\x01\n!com.google.ads.googleads.v2.enumsB ListingCustomAttributeIndexProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX = _descriptor.EnumDescriptor(
  name='ListingCustomAttributeIndex',
  full_name='google.ads.googleads.v2.enums.ListingCustomAttributeIndexEnum.ListingCustomAttributeIndex',
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
      name='INDEX0', index=2, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX1', index=3, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX2', index=4, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX3', index=5, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX4', index=6, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=286,
)
_sym_db.RegisterEnumDescriptor(_LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX)


_LISTINGCUSTOMATTRIBUTEINDEXENUM = _descriptor.Descriptor(
  name='ListingCustomAttributeIndexEnum',
  full_name='google.ads.googleads.v2.enums.ListingCustomAttributeIndexEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=286,
)

_LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX.containing_type = _LISTINGCUSTOMATTRIBUTEINDEXENUM
DESCRIPTOR.message_types_by_name['ListingCustomAttributeIndexEnum'] = _LISTINGCUSTOMATTRIBUTEINDEXENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListingCustomAttributeIndexEnum = _reflection.GeneratedProtocolMessageType('ListingCustomAttributeIndexEnum', (_message.Message,), {
  'DESCRIPTOR' : _LISTINGCUSTOMATTRIBUTEINDEXENUM,
  '__module__' : 'google.ads.googleads.v2.enums.listing_custom_attribute_index_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.ListingCustomAttributeIndexEnum)
  })
_sym_db.RegisterMessage(ListingCustomAttributeIndexEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
