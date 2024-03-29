# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/common/final_app_url.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.enums import app_url_operating_system_type_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_app__url__operating__system__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/common/final_app_url.proto',
  package='google.ads.googleads.v2.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v2.commonB\020FinalAppUrlProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Common\312\002\036Google\\Ads\\GoogleAds\\V2\\Common\352\002\"Google::Ads::GoogleAds::V2::Common',
  serialized_pb=b'\n2google/ads/googleads/v2/common/final_app_url.proto\x12\x1egoogle.ads.googleads.v2.common\x1a\x41google/ads/googleads/v2/enums/app_url_operating_system_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xa1\x01\n\x0b\x46inalAppUrl\x12g\n\x07os_type\x18\x01 \x01(\x0e\x32V.google.ads.googleads.v2.enums.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType\x12)\n\x03url\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xeb\x01\n\"com.google.ads.googleads.v2.commonB\x10\x46inalAppUrlProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Common\xea\x02\"Google::Ads::GoogleAds::V2::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_app__url__operating__system__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_FINALAPPURL = _descriptor.Descriptor(
  name='FinalAppUrl',
  full_name='google.ads.googleads.v2.common.FinalAppUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='os_type', full_name='google.ads.googleads.v2.common.FinalAppUrl.os_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.ads.googleads.v2.common.FinalAppUrl.url', index=1,
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
  serialized_start=216,
  serialized_end=377,
)

_FINALAPPURL.fields_by_name['os_type'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_app__url__operating__system__type__pb2._APPURLOPERATINGSYSTEMTYPEENUM_APPURLOPERATINGSYSTEMTYPE
_FINALAPPURL.fields_by_name['url'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['FinalAppUrl'] = _FINALAPPURL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FinalAppUrl = _reflection.GeneratedProtocolMessageType('FinalAppUrl', (_message.Message,), {
  'DESCRIPTOR' : _FINALAPPURL,
  '__module__' : 'google.ads.googleads.v2.common.final_app_url_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.FinalAppUrl)
  })
_sym_db.RegisterMessage(FinalAppUrl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
