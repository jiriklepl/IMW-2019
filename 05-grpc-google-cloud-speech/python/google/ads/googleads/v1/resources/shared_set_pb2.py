# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/resources/shared_set.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.enums import shared_set_status_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_shared__set__status__pb2
from google.ads.googleads.v1.enums import shared_set_type_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_shared__set__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/resources/shared_set.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v1.resourcesB\016SharedSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources',
  serialized_pb=b'\n2google/ads/googleads/v1/resources/shared_set.proto\x12!google.ads.googleads.v1.resources\x1a\x35google/ads/googleads/v1/enums/shared_set_status.proto\x1a\x33google/ads/googleads/v1/enums/shared_set_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x82\x03\n\tSharedSet\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12L\n\x04type\x18\x03 \x01(\x0e\x32>.google.ads.googleads.v1.enums.SharedSetTypeEnum.SharedSetType\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12R\n\x06status\x18\x05 \x01(\x0e\x32\x42.google.ads.googleads.v1.enums.SharedSetStatusEnum.SharedSetStatus\x12\x31\n\x0cmember_count\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0freference_count\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\xfb\x01\n%com.google.ads.googleads.v1.resourcesB\x0eSharedSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_shared__set__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_shared__set__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SHAREDSET = _descriptor.Descriptor(
  name='SharedSet',
  full_name='google.ads.googleads.v1.resources.SharedSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.SharedSet.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.SharedSet.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v1.resources.SharedSet.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.SharedSet.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v1.resources.SharedSet.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_count', full_name='google.ads.googleads.v1.resources.SharedSet.member_count', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_count', full_name='google.ads.googleads.v1.resources.SharedSet.reference_count', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=260,
  serialized_end=646,
)

_SHAREDSET.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SHAREDSET.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_shared__set__type__pb2._SHAREDSETTYPEENUM_SHAREDSETTYPE
_SHAREDSET.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SHAREDSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_shared__set__status__pb2._SHAREDSETSTATUSENUM_SHAREDSETSTATUS
_SHAREDSET.fields_by_name['member_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SHAREDSET.fields_by_name['reference_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['SharedSet'] = _SHAREDSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedSet = _reflection.GeneratedProtocolMessageType('SharedSet', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDSET,
  '__module__' : 'google.ads.googleads.v1.resources.shared_set_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.SharedSet)
  })
_sym_db.RegisterMessage(SharedSet)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
