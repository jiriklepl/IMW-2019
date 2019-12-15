# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/enums/keyword_plan_forecast_interval.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/enums/keyword_plan_forecast_interval.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v1.enumsB KeywordPlanForecastIntervalProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums',
  serialized_pb=b'\nBgoogle/ads/googleads/v1/enums/keyword_plan_forecast_interval.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\x8f\x01\n\x1fKeywordPlanForecastIntervalEnum\"l\n\x1bKeywordPlanForecastInterval\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\r\n\tNEXT_WEEK\x10\x03\x12\x0e\n\nNEXT_MONTH\x10\x04\x12\x10\n\x0cNEXT_QUARTER\x10\x05\x42\xf5\x01\n!com.google.ads.googleads.v1.enumsB KeywordPlanForecastIntervalProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_KEYWORDPLANFORECASTINTERVALENUM_KEYWORDPLANFORECASTINTERVAL = _descriptor.EnumDescriptor(
  name='KeywordPlanForecastInterval',
  full_name='google.ads.googleads.v1.enums.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval',
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
      name='NEXT_WEEK', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_MONTH', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_QUARTER', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=275,
)
_sym_db.RegisterEnumDescriptor(_KEYWORDPLANFORECASTINTERVALENUM_KEYWORDPLANFORECASTINTERVAL)


_KEYWORDPLANFORECASTINTERVALENUM = _descriptor.Descriptor(
  name='KeywordPlanForecastIntervalEnum',
  full_name='google.ads.googleads.v1.enums.KeywordPlanForecastIntervalEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEYWORDPLANFORECASTINTERVALENUM_KEYWORDPLANFORECASTINTERVAL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=275,
)

_KEYWORDPLANFORECASTINTERVALENUM_KEYWORDPLANFORECASTINTERVAL.containing_type = _KEYWORDPLANFORECASTINTERVALENUM
DESCRIPTOR.message_types_by_name['KeywordPlanForecastIntervalEnum'] = _KEYWORDPLANFORECASTINTERVALENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanForecastIntervalEnum = _reflection.GeneratedProtocolMessageType('KeywordPlanForecastIntervalEnum', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANFORECASTINTERVALENUM,
  '__module__' : 'google.ads.googleads.v1.enums.keyword_plan_forecast_interval_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.KeywordPlanForecastIntervalEnum)
  })
_sym_db.RegisterMessage(KeywordPlanForecastIntervalEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
