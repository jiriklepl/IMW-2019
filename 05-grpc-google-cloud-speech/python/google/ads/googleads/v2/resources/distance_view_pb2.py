# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/resources/distance_view.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.enums import distance_bucket_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_distance__bucket__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/resources/distance_view.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v2.resourcesB\021DistanceViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources',
  serialized_pb=b'\n5google/ads/googleads/v2/resources/distance_view.proto\x12!google.ads.googleads.v2.resources\x1a\x33google/ads/googleads/v2/enums/distance_bucket.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xb3\x01\n\x0c\x44istanceView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12Y\n\x0f\x64istance_bucket\x18\x02 \x01(\x0e\x32@.google.ads.googleads.v2.enums.DistanceBucketEnum.DistanceBucket\x12\x31\n\rmetric_system\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\xfe\x01\n%com.google.ads.googleads.v2.resourcesB\x11\x44istanceViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_distance__bucket__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DISTANCEVIEW = _descriptor.Descriptor(
  name='DistanceView',
  full_name='google.ads.googleads.v2.resources.DistanceView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.DistanceView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance_bucket', full_name='google.ads.googleads.v2.resources.DistanceView.distance_bucket', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_system', full_name='google.ads.googleads.v2.resources.DistanceView.metric_system', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=208,
  serialized_end=387,
)

_DISTANCEVIEW.fields_by_name['distance_bucket'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_distance__bucket__pb2._DISTANCEBUCKETENUM_DISTANCEBUCKET
_DISTANCEVIEW.fields_by_name['metric_system'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['DistanceView'] = _DISTANCEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DistanceView = _reflection.GeneratedProtocolMessageType('DistanceView', (_message.Message,), {
  'DESCRIPTOR' : _DISTANCEVIEW,
  '__module__' : 'google.ads.googleads.v2.resources.distance_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.DistanceView)
  })
_sym_db.RegisterMessage(DistanceView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
