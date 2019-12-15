# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/common/targeting_setting.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.enums import targeting_dimension_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_targeting__dimension__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/common/targeting_setting.proto',
  package='google.ads.googleads.v2.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v2.commonB\025TargetingSettingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Common\312\002\036Google\\Ads\\GoogleAds\\V2\\Common\352\002\"Google::Ads::GoogleAds::V2::Common',
  serialized_pb=b'\n6google/ads/googleads/v2/common/targeting_setting.proto\x12\x1egoogle.ads.googleads.v2.common\x1a\x37google/ads/googleads/v2/enums/targeting_dimension.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"b\n\x10TargetingSetting\x12N\n\x13target_restrictions\x18\x01 \x03(\x0b\x32\x31.google.ads.googleads.v2.common.TargetRestriction\"\xa8\x01\n\x11TargetRestriction\x12\x65\n\x13targeting_dimension\x18\x01 \x01(\x0e\x32H.google.ads.googleads.v2.enums.TargetingDimensionEnum.TargetingDimension\x12,\n\x08\x62id_only\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\xf0\x01\n\"com.google.ads.googleads.v2.commonB\x15TargetingSettingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Common\xea\x02\"Google::Ads::GoogleAds::V2::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_targeting__dimension__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_TARGETINGSETTING = _descriptor.Descriptor(
  name='TargetingSetting',
  full_name='google.ads.googleads.v2.common.TargetingSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_restrictions', full_name='google.ads.googleads.v2.common.TargetingSetting.target_restrictions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=209,
  serialized_end=307,
)


_TARGETRESTRICTION = _descriptor.Descriptor(
  name='TargetRestriction',
  full_name='google.ads.googleads.v2.common.TargetRestriction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targeting_dimension', full_name='google.ads.googleads.v2.common.TargetRestriction.targeting_dimension', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_only', full_name='google.ads.googleads.v2.common.TargetRestriction.bid_only', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=310,
  serialized_end=478,
)

_TARGETINGSETTING.fields_by_name['target_restrictions'].message_type = _TARGETRESTRICTION
_TARGETRESTRICTION.fields_by_name['targeting_dimension'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_targeting__dimension__pb2._TARGETINGDIMENSIONENUM_TARGETINGDIMENSION
_TARGETRESTRICTION.fields_by_name['bid_only'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['TargetingSetting'] = _TARGETINGSETTING
DESCRIPTOR.message_types_by_name['TargetRestriction'] = _TARGETRESTRICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetingSetting = _reflection.GeneratedProtocolMessageType('TargetingSetting', (_message.Message,), {
  'DESCRIPTOR' : _TARGETINGSETTING,
  '__module__' : 'google.ads.googleads.v2.common.targeting_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.TargetingSetting)
  })
_sym_db.RegisterMessage(TargetingSetting)

TargetRestriction = _reflection.GeneratedProtocolMessageType('TargetRestriction', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRESTRICTION,
  '__module__' : 'google.ads.googleads.v2.common.targeting_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.TargetRestriction)
  })
_sym_db.RegisterMessage(TargetRestriction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
