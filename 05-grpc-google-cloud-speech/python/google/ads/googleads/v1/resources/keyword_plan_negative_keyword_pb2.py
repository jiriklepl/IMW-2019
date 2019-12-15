# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/resources/keyword_plan_negative_keyword.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_keyword__match__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/resources/keyword_plan_negative_keyword.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v1.resourcesB\037KeywordPlanNegativeKeywordProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources',
  serialized_pb=b'\nEgoogle/ads/googleads/v1/resources/keyword_plan_negative_keyword.proto\x12!google.ads.googleads.v1.resources\x1a\x36google/ads/googleads/v1/enums/keyword_match_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x9f\x02\n\x1aKeywordPlanNegativeKeyword\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12;\n\x15keyword_plan_campaign\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04text\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\nmatch_type\x18\x05 \x01(\x0e\x32\x44.google.ads.googleads.v1.enums.KeywordMatchTypeEnum.KeywordMatchTypeB\x8c\x02\n%com.google.ads.googleads.v1.resourcesB\x1fKeywordPlanNegativeKeywordProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_keyword__match__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_KEYWORDPLANNEGATIVEKEYWORD = _descriptor.Descriptor(
  name='KeywordPlanNegativeKeyword',
  full_name='google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_plan_campaign', full_name='google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword.keyword_plan_campaign', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword.id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword.text', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match_type', full_name='google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword.match_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=227,
  serialized_end=514,
)

_KEYWORDPLANNEGATIVEKEYWORD.fields_by_name['keyword_plan_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANNEGATIVEKEYWORD.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANNEGATIVEKEYWORD.fields_by_name['text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANNEGATIVEKEYWORD.fields_by_name['match_type'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_keyword__match__type__pb2._KEYWORDMATCHTYPEENUM_KEYWORDMATCHTYPE
DESCRIPTOR.message_types_by_name['KeywordPlanNegativeKeyword'] = _KEYWORDPLANNEGATIVEKEYWORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanNegativeKeyword = _reflection.GeneratedProtocolMessageType('KeywordPlanNegativeKeyword', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANNEGATIVEKEYWORD,
  '__module__' : 'google.ads.googleads.v1.resources.keyword_plan_negative_keyword_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword)
  })
_sym_db.RegisterMessage(KeywordPlanNegativeKeyword)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
