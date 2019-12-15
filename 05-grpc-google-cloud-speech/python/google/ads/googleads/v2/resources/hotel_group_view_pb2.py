# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/resources/hotel_group_view.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/resources/hotel_group_view.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v2.resourcesB\023HotelGroupViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources',
  serialized_pb=b'\n8google/ads/googleads/v2/resources/hotel_group_view.proto\x12!google.ads.googleads.v2.resources\x1a\x1cgoogle/api/annotations.proto\"\'\n\x0eHotelGroupView\x12\x15\n\rresource_name\x18\x01 \x01(\tB\x80\x02\n%com.google.ads.googleads.v2.resourcesB\x13HotelGroupViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_HOTELGROUPVIEW = _descriptor.Descriptor(
  name='HotelGroupView',
  full_name='google.ads.googleads.v2.resources.HotelGroupView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.HotelGroupView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['HotelGroupView'] = _HOTELGROUPVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotelGroupView = _reflection.GeneratedProtocolMessageType('HotelGroupView', (_message.Message,), {
  'DESCRIPTOR' : _HOTELGROUPVIEW,
  '__module__' : 'google.ads.googleads.v2.resources.hotel_group_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.HotelGroupView)
  })
_sym_db.RegisterMessage(HotelGroupView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
