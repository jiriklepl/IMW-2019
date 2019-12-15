# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/resources/feed_item_target.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2
from google.ads.googleads.v1.enums import feed_item_target_device_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_feed__item__target__device__pb2
from google.ads.googleads.v1.enums import feed_item_target_type_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_feed__item__target__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/resources/feed_item_target.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v1.resourcesB\023FeedItemTargetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources',
  serialized_pb=b'\n8google/ads/googleads/v1/resources/feed_item_target.proto\x12!google.ads.googleads.v1.resources\x1a-google/ads/googleads/v1/common/criteria.proto\x1a;google/ads/googleads/v1/enums/feed_item_target_device.proto\x1a\x39google/ads/googleads/v1/enums/feed_item_target_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x8d\x05\n\x0e\x46\x65\x65\x64ItemTarget\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12/\n\tfeed_item\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12g\n\x15\x66\x65\x65\x64_item_target_type\x18\x03 \x01(\x0e\x32H.google.ads.googleads.v1.enums.FeedItemTargetTypeEnum.FeedItemTargetType\x12\x38\n\x13\x66\x65\x65\x64_item_target_id\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\x08\x63\x61mpaign\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12\x30\n\x08\x61\x64_group\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12>\n\x07keyword\x18\x07 \x01(\x0b\x32+.google.ads.googleads.v1.common.KeywordInfoH\x00\x12;\n\x13geo_target_constant\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12^\n\x06\x64\x65vice\x18\t \x01(\x0e\x32L.google.ads.googleads.v1.enums.FeedItemTargetDeviceEnum.FeedItemTargetDeviceH\x00\x12\x45\n\x0b\x61\x64_schedule\x18\n \x01(\x0b\x32..google.ads.googleads.v1.common.AdScheduleInfoH\x00\x42\x08\n\x06targetB\x80\x02\n%com.google.ads.googleads.v1.resourcesB\x13\x46\x65\x65\x64ItemTargetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_feed__item__target__device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_feed__item__target__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_FEEDITEMTARGET = _descriptor.Descriptor(
  name='FeedItemTarget',
  full_name='google.ads.googleads.v1.resources.FeedItemTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.FeedItemTarget.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed_item', full_name='google.ads.googleads.v1.resources.FeedItemTarget.feed_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed_item_target_type', full_name='google.ads.googleads.v1.resources.FeedItemTarget.feed_item_target_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed_item_target_id', full_name='google.ads.googleads.v1.resources.FeedItemTarget.feed_item_target_id', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v1.resources.FeedItemTarget.campaign', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v1.resources.FeedItemTarget.ad_group', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='google.ads.googleads.v1.resources.FeedItemTarget.keyword', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_target_constant', full_name='google.ads.googleads.v1.resources.FeedItemTarget.geo_target_constant', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v1.resources.FeedItemTarget.device', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_schedule', full_name='google.ads.googleads.v1.resources.FeedItemTarget.ad_schedule', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='target', full_name='google.ads.googleads.v1.resources.FeedItemTarget.target',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=325,
  serialized_end=978,
)

_FEEDITEMTARGET.fields_by_name['feed_item'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FEEDITEMTARGET.fields_by_name['feed_item_target_type'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_feed__item__target__type__pb2._FEEDITEMTARGETTYPEENUM_FEEDITEMTARGETTYPE
_FEEDITEMTARGET.fields_by_name['feed_item_target_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_FEEDITEMTARGET.fields_by_name['campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FEEDITEMTARGET.fields_by_name['ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FEEDITEMTARGET.fields_by_name['keyword'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._KEYWORDINFO
_FEEDITEMTARGET.fields_by_name['geo_target_constant'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FEEDITEMTARGET.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_feed__item__target__device__pb2._FEEDITEMTARGETDEVICEENUM_FEEDITEMTARGETDEVICE
_FEEDITEMTARGET.fields_by_name['ad_schedule'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._ADSCHEDULEINFO
_FEEDITEMTARGET.oneofs_by_name['target'].fields.append(
  _FEEDITEMTARGET.fields_by_name['campaign'])
_FEEDITEMTARGET.fields_by_name['campaign'].containing_oneof = _FEEDITEMTARGET.oneofs_by_name['target']
_FEEDITEMTARGET.oneofs_by_name['target'].fields.append(
  _FEEDITEMTARGET.fields_by_name['ad_group'])
_FEEDITEMTARGET.fields_by_name['ad_group'].containing_oneof = _FEEDITEMTARGET.oneofs_by_name['target']
_FEEDITEMTARGET.oneofs_by_name['target'].fields.append(
  _FEEDITEMTARGET.fields_by_name['keyword'])
_FEEDITEMTARGET.fields_by_name['keyword'].containing_oneof = _FEEDITEMTARGET.oneofs_by_name['target']
_FEEDITEMTARGET.oneofs_by_name['target'].fields.append(
  _FEEDITEMTARGET.fields_by_name['geo_target_constant'])
_FEEDITEMTARGET.fields_by_name['geo_target_constant'].containing_oneof = _FEEDITEMTARGET.oneofs_by_name['target']
_FEEDITEMTARGET.oneofs_by_name['target'].fields.append(
  _FEEDITEMTARGET.fields_by_name['device'])
_FEEDITEMTARGET.fields_by_name['device'].containing_oneof = _FEEDITEMTARGET.oneofs_by_name['target']
_FEEDITEMTARGET.oneofs_by_name['target'].fields.append(
  _FEEDITEMTARGET.fields_by_name['ad_schedule'])
_FEEDITEMTARGET.fields_by_name['ad_schedule'].containing_oneof = _FEEDITEMTARGET.oneofs_by_name['target']
DESCRIPTOR.message_types_by_name['FeedItemTarget'] = _FEEDITEMTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedItemTarget = _reflection.GeneratedProtocolMessageType('FeedItemTarget', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMTARGET,
  '__module__' : 'google.ads.googleads.v1.resources.feed_item_target_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.FeedItemTarget)
  })
_sym_db.RegisterMessage(FeedItemTarget)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
