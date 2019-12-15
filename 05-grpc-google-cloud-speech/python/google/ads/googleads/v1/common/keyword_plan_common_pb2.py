# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/common/keyword_plan_common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.enums import keyword_plan_competition_level_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_keyword__plan__competition__level__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/common/keyword_plan_common.proto',
  package='google.ads.googleads.v1.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v1.commonB\026KeywordPlanCommonProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Common\312\002\036Google\\Ads\\GoogleAds\\V1\\Common\352\002\"Google::Ads::GoogleAds::V1::Common',
  serialized_pb=b'\n8google/ads/googleads/v1/common/keyword_plan_common.proto\x12\x1egoogle.ads.googleads.v1.common\x1a\x42google/ads/googleads/v1/enums/keyword_plan_competition_level.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xca\x01\n\x1cKeywordPlanHistoricalMetrics\x12\x39\n\x14\x61vg_monthly_searches\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12o\n\x0b\x63ompetition\x18\x02 \x01(\x0e\x32Z.google.ads.googleads.v1.enums.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevelB\xf1\x01\n\"com.google.ads.googleads.v1.commonB\x16KeywordPlanCommonProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Common\xea\x02\"Google::Ads::GoogleAds::V1::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_keyword__plan__competition__level__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_KEYWORDPLANHISTORICALMETRICS = _descriptor.Descriptor(
  name='KeywordPlanHistoricalMetrics',
  full_name='google.ads.googleads.v1.common.KeywordPlanHistoricalMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avg_monthly_searches', full_name='google.ads.googleads.v1.common.KeywordPlanHistoricalMetrics.avg_monthly_searches', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='competition', full_name='google.ads.googleads.v1.common.KeywordPlanHistoricalMetrics.competition', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=223,
  serialized_end=425,
)

_KEYWORDPLANHISTORICALMETRICS.fields_by_name['avg_monthly_searches'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANHISTORICALMETRICS.fields_by_name['competition'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_keyword__plan__competition__level__pb2._KEYWORDPLANCOMPETITIONLEVELENUM_KEYWORDPLANCOMPETITIONLEVEL
DESCRIPTOR.message_types_by_name['KeywordPlanHistoricalMetrics'] = _KEYWORDPLANHISTORICALMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanHistoricalMetrics = _reflection.GeneratedProtocolMessageType('KeywordPlanHistoricalMetrics', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANHISTORICALMETRICS,
  '__module__' : 'google.ads.googleads.v1.common.keyword_plan_common_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.KeywordPlanHistoricalMetrics)
  })
_sym_db.RegisterMessage(KeywordPlanHistoricalMetrics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
