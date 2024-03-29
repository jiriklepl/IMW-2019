# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/keyword_plan_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.common import keyword_plan_common_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_common_dot_keyword__plan__common__pb2
from google.ads.googleads.v2.resources import keyword_plan_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/keyword_plan_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB\027KeywordPlanServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\n;google/ads/googleads/v2/services/keyword_plan_service.proto\x12 google.ads.googleads.v2.services\x1a\x38google/ads/googleads/v2/common/keyword_plan_common.proto\x1a\x34google/ads/googleads/v2/resources/keyword_plan.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto\".\n\x15GetKeywordPlanRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xac\x01\n\x19MutateKeywordPlansRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12J\n\noperations\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v2.services.KeywordPlanOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xea\x01\n\x14KeywordPlanOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12@\n\x06\x63reate\x18\x01 \x01(\x0b\x32..google.ads.googleads.v2.resources.KeywordPlanH\x00\x12@\n\x06update\x18\x02 \x01(\x0b\x32..google.ads.googleads.v2.resources.KeywordPlanH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x9c\x01\n\x1aMutateKeywordPlansResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12K\n\x07results\x18\x02 \x03(\x0b\x32:.google.ads.googleads.v2.services.MutateKeywordPlansResult\"1\n\x18MutateKeywordPlansResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\"6\n\x1eGenerateForecastMetricsRequest\x12\x14\n\x0ckeyword_plan\x18\x01 \x01(\t\"\xaf\x02\n\x1fGenerateForecastMetricsResponse\x12Y\n\x12\x63\x61mpaign_forecasts\x18\x01 \x03(\x0b\x32=.google.ads.googleads.v2.services.KeywordPlanCampaignForecast\x12X\n\x12\x61\x64_group_forecasts\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v2.services.KeywordPlanAdGroupForecast\x12W\n\x11keyword_forecasts\x18\x03 \x03(\x0b\x32<.google.ads.googleads.v2.services.KeywordPlanKeywordForecast\"\xa8\x01\n\x1bKeywordPlanCampaignForecast\x12;\n\x15keyword_plan_campaign\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12L\n\x11\x63\x61mpaign_forecast\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v2.services.ForecastMetrics\"\xa7\x01\n\x1aKeywordPlanAdGroupForecast\x12;\n\x15keyword_plan_ad_group\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12L\n\x11\x61\x64_group_forecast\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v2.services.ForecastMetrics\"\xae\x01\n\x1aKeywordPlanKeywordForecast\x12\x43\n\x1dkeyword_plan_ad_group_keyword\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x10keyword_forecast\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v2.services.ForecastMetrics\"\x81\x02\n\x0f\x46orecastMetrics\x12\x31\n\x0bimpressions\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12)\n\x03\x63tr\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\x0b\x61verage_cpc\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12,\n\x06\x63licks\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\x0b\x63ost_micros\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"8\n GenerateHistoricalMetricsRequest\x12\x14\n\x0ckeyword_plan\x18\x01 \x01(\t\"{\n!GenerateHistoricalMetricsResponse\x12V\n\x07metrics\x18\x01 \x03(\x0b\x32\x45.google.ads.googleads.v2.services.KeywordPlanKeywordHistoricalMetrics\"\xb0\x01\n#KeywordPlanKeywordHistoricalMetrics\x12\x32\n\x0csearch_query\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12U\n\x0fkeyword_metrics\x18\x02 \x01(\x0b\x32<.google.ads.googleads.v2.common.KeywordPlanHistoricalMetrics2\xa3\x07\n\x12KeywordPlanService\x12\xb1\x01\n\x0eGetKeywordPlan\x12\x37.google.ads.googleads.v2.services.GetKeywordPlanRequest\x1a..google.ads.googleads.v2.resources.KeywordPlan\"6\x82\xd3\xe4\x93\x02\x30\x12./v2/{resource_name=customers/*/keywordPlans/*}\x12\xcd\x01\n\x12MutateKeywordPlans\x12;.google.ads.googleads.v2.services.MutateKeywordPlansRequest\x1a<.google.ads.googleads.v2.services.MutateKeywordPlansResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/v2/customers/{customer_id=*}/keywordPlans:mutate:\x01*\x12\xf0\x01\n\x17GenerateForecastMetrics\x12@.google.ads.googleads.v2.services.GenerateForecastMetricsRequest\x1a\x41.google.ads.googleads.v2.services.GenerateForecastMetricsResponse\"P\x82\xd3\xe4\x93\x02J\"E/v2/{keyword_plan=customers/*/keywordPlans/*}:generateForecastMetrics:\x01*\x12\xf8\x01\n\x19GenerateHistoricalMetrics\x12\x42.google.ads.googleads.v2.services.GenerateHistoricalMetricsRequest\x1a\x43.google.ads.googleads.v2.services.GenerateHistoricalMetricsResponse\"R\x82\xd3\xe4\x93\x02L\"G/v2/{keyword_plan=customers/*/keywordPlans/*}:generateHistoricalMetrics:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xfe\x01\n$com.google.ads.googleads.v2.servicesB\x17KeywordPlanServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_common_dot_keyword__plan__common__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GETKEYWORDPLANREQUEST = _descriptor.Descriptor(
  name='GetKeywordPlanRequest',
  full_name='google.ads.googleads.v2.services.GetKeywordPlanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetKeywordPlanRequest.resource_name', index=0,
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
  serialized_start=355,
  serialized_end=401,
)


_MUTATEKEYWORDPLANSREQUEST = _descriptor.Descriptor(
  name='MutateKeywordPlansRequest',
  full_name='google.ads.googleads.v2.services.MutateKeywordPlansRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.MutateKeywordPlansRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v2.services.MutateKeywordPlansRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v2.services.MutateKeywordPlansRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v2.services.MutateKeywordPlansRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=404,
  serialized_end=576,
)


_KEYWORDPLANOPERATION = _descriptor.Descriptor(
  name='KeywordPlanOperation',
  full_name='google.ads.googleads.v2.services.KeywordPlanOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v2.services.KeywordPlanOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v2.services.KeywordPlanOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v2.services.KeywordPlanOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v2.services.KeywordPlanOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v2.services.KeywordPlanOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=579,
  serialized_end=813,
)


_MUTATEKEYWORDPLANSRESPONSE = _descriptor.Descriptor(
  name='MutateKeywordPlansResponse',
  full_name='google.ads.googleads.v2.services.MutateKeywordPlansResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v2.services.MutateKeywordPlansResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.MutateKeywordPlansResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=816,
  serialized_end=972,
)


_MUTATEKEYWORDPLANSRESULT = _descriptor.Descriptor(
  name='MutateKeywordPlansResult',
  full_name='google.ads.googleads.v2.services.MutateKeywordPlansResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.MutateKeywordPlansResult.resource_name', index=0,
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
  serialized_start=974,
  serialized_end=1023,
)


_GENERATEFORECASTMETRICSREQUEST = _descriptor.Descriptor(
  name='GenerateForecastMetricsRequest',
  full_name='google.ads.googleads.v2.services.GenerateForecastMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword_plan', full_name='google.ads.googleads.v2.services.GenerateForecastMetricsRequest.keyword_plan', index=0,
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
  serialized_start=1025,
  serialized_end=1079,
)


_GENERATEFORECASTMETRICSRESPONSE = _descriptor.Descriptor(
  name='GenerateForecastMetricsResponse',
  full_name='google.ads.googleads.v2.services.GenerateForecastMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='campaign_forecasts', full_name='google.ads.googleads.v2.services.GenerateForecastMetricsResponse.campaign_forecasts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_forecasts', full_name='google.ads.googleads.v2.services.GenerateForecastMetricsResponse.ad_group_forecasts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_forecasts', full_name='google.ads.googleads.v2.services.GenerateForecastMetricsResponse.keyword_forecasts', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1082,
  serialized_end=1385,
)


_KEYWORDPLANCAMPAIGNFORECAST = _descriptor.Descriptor(
  name='KeywordPlanCampaignForecast',
  full_name='google.ads.googleads.v2.services.KeywordPlanCampaignForecast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword_plan_campaign', full_name='google.ads.googleads.v2.services.KeywordPlanCampaignForecast.keyword_plan_campaign', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_forecast', full_name='google.ads.googleads.v2.services.KeywordPlanCampaignForecast.campaign_forecast', index=1,
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
  serialized_start=1388,
  serialized_end=1556,
)


_KEYWORDPLANADGROUPFORECAST = _descriptor.Descriptor(
  name='KeywordPlanAdGroupForecast',
  full_name='google.ads.googleads.v2.services.KeywordPlanAdGroupForecast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword_plan_ad_group', full_name='google.ads.googleads.v2.services.KeywordPlanAdGroupForecast.keyword_plan_ad_group', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_forecast', full_name='google.ads.googleads.v2.services.KeywordPlanAdGroupForecast.ad_group_forecast', index=1,
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
  serialized_start=1559,
  serialized_end=1726,
)


_KEYWORDPLANKEYWORDFORECAST = _descriptor.Descriptor(
  name='KeywordPlanKeywordForecast',
  full_name='google.ads.googleads.v2.services.KeywordPlanKeywordForecast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword_plan_ad_group_keyword', full_name='google.ads.googleads.v2.services.KeywordPlanKeywordForecast.keyword_plan_ad_group_keyword', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_forecast', full_name='google.ads.googleads.v2.services.KeywordPlanKeywordForecast.keyword_forecast', index=1,
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
  serialized_start=1729,
  serialized_end=1903,
)


_FORECASTMETRICS = _descriptor.Descriptor(
  name='ForecastMetrics',
  full_name='google.ads.googleads.v2.services.ForecastMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='impressions', full_name='google.ads.googleads.v2.services.ForecastMetrics.impressions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctr', full_name='google.ads.googleads.v2.services.ForecastMetrics.ctr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_cpc', full_name='google.ads.googleads.v2.services.ForecastMetrics.average_cpc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clicks', full_name='google.ads.googleads.v2.services.ForecastMetrics.clicks', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_micros', full_name='google.ads.googleads.v2.services.ForecastMetrics.cost_micros', index=4,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1906,
  serialized_end=2163,
)


_GENERATEHISTORICALMETRICSREQUEST = _descriptor.Descriptor(
  name='GenerateHistoricalMetricsRequest',
  full_name='google.ads.googleads.v2.services.GenerateHistoricalMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword_plan', full_name='google.ads.googleads.v2.services.GenerateHistoricalMetricsRequest.keyword_plan', index=0,
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
  serialized_start=2165,
  serialized_end=2221,
)


_GENERATEHISTORICALMETRICSRESPONSE = _descriptor.Descriptor(
  name='GenerateHistoricalMetricsResponse',
  full_name='google.ads.googleads.v2.services.GenerateHistoricalMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='google.ads.googleads.v2.services.GenerateHistoricalMetricsResponse.metrics', index=0,
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
  serialized_start=2223,
  serialized_end=2346,
)


_KEYWORDPLANKEYWORDHISTORICALMETRICS = _descriptor.Descriptor(
  name='KeywordPlanKeywordHistoricalMetrics',
  full_name='google.ads.googleads.v2.services.KeywordPlanKeywordHistoricalMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='search_query', full_name='google.ads.googleads.v2.services.KeywordPlanKeywordHistoricalMetrics.search_query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_metrics', full_name='google.ads.googleads.v2.services.KeywordPlanKeywordHistoricalMetrics.keyword_metrics', index=1,
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
  serialized_start=2349,
  serialized_end=2525,
)

_MUTATEKEYWORDPLANSREQUEST.fields_by_name['operations'].message_type = _KEYWORDPLANOPERATION
_KEYWORDPLANOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_KEYWORDPLANOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__pb2._KEYWORDPLAN
_KEYWORDPLANOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__pb2._KEYWORDPLAN
_KEYWORDPLANOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANOPERATION.fields_by_name['create'])
_KEYWORDPLANOPERATION.fields_by_name['create'].containing_oneof = _KEYWORDPLANOPERATION.oneofs_by_name['operation']
_KEYWORDPLANOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANOPERATION.fields_by_name['update'])
_KEYWORDPLANOPERATION.fields_by_name['update'].containing_oneof = _KEYWORDPLANOPERATION.oneofs_by_name['operation']
_KEYWORDPLANOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANOPERATION.fields_by_name['remove'])
_KEYWORDPLANOPERATION.fields_by_name['remove'].containing_oneof = _KEYWORDPLANOPERATION.oneofs_by_name['operation']
_MUTATEKEYWORDPLANSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEKEYWORDPLANSRESPONSE.fields_by_name['results'].message_type = _MUTATEKEYWORDPLANSRESULT
_GENERATEFORECASTMETRICSRESPONSE.fields_by_name['campaign_forecasts'].message_type = _KEYWORDPLANCAMPAIGNFORECAST
_GENERATEFORECASTMETRICSRESPONSE.fields_by_name['ad_group_forecasts'].message_type = _KEYWORDPLANADGROUPFORECAST
_GENERATEFORECASTMETRICSRESPONSE.fields_by_name['keyword_forecasts'].message_type = _KEYWORDPLANKEYWORDFORECAST
_KEYWORDPLANCAMPAIGNFORECAST.fields_by_name['keyword_plan_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANCAMPAIGNFORECAST.fields_by_name['campaign_forecast'].message_type = _FORECASTMETRICS
_KEYWORDPLANADGROUPFORECAST.fields_by_name['keyword_plan_ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANADGROUPFORECAST.fields_by_name['ad_group_forecast'].message_type = _FORECASTMETRICS
_KEYWORDPLANKEYWORDFORECAST.fields_by_name['keyword_plan_ad_group_keyword'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANKEYWORDFORECAST.fields_by_name['keyword_forecast'].message_type = _FORECASTMETRICS
_FORECASTMETRICS.fields_by_name['impressions'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_FORECASTMETRICS.fields_by_name['ctr'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_FORECASTMETRICS.fields_by_name['average_cpc'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_FORECASTMETRICS.fields_by_name['clicks'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_FORECASTMETRICS.fields_by_name['cost_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GENERATEHISTORICALMETRICSRESPONSE.fields_by_name['metrics'].message_type = _KEYWORDPLANKEYWORDHISTORICALMETRICS
_KEYWORDPLANKEYWORDHISTORICALMETRICS.fields_by_name['search_query'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANKEYWORDHISTORICALMETRICS.fields_by_name['keyword_metrics'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_keyword__plan__common__pb2._KEYWORDPLANHISTORICALMETRICS
DESCRIPTOR.message_types_by_name['GetKeywordPlanRequest'] = _GETKEYWORDPLANREQUEST
DESCRIPTOR.message_types_by_name['MutateKeywordPlansRequest'] = _MUTATEKEYWORDPLANSREQUEST
DESCRIPTOR.message_types_by_name['KeywordPlanOperation'] = _KEYWORDPLANOPERATION
DESCRIPTOR.message_types_by_name['MutateKeywordPlansResponse'] = _MUTATEKEYWORDPLANSRESPONSE
DESCRIPTOR.message_types_by_name['MutateKeywordPlansResult'] = _MUTATEKEYWORDPLANSRESULT
DESCRIPTOR.message_types_by_name['GenerateForecastMetricsRequest'] = _GENERATEFORECASTMETRICSREQUEST
DESCRIPTOR.message_types_by_name['GenerateForecastMetricsResponse'] = _GENERATEFORECASTMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['KeywordPlanCampaignForecast'] = _KEYWORDPLANCAMPAIGNFORECAST
DESCRIPTOR.message_types_by_name['KeywordPlanAdGroupForecast'] = _KEYWORDPLANADGROUPFORECAST
DESCRIPTOR.message_types_by_name['KeywordPlanKeywordForecast'] = _KEYWORDPLANKEYWORDFORECAST
DESCRIPTOR.message_types_by_name['ForecastMetrics'] = _FORECASTMETRICS
DESCRIPTOR.message_types_by_name['GenerateHistoricalMetricsRequest'] = _GENERATEHISTORICALMETRICSREQUEST
DESCRIPTOR.message_types_by_name['GenerateHistoricalMetricsResponse'] = _GENERATEHISTORICALMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['KeywordPlanKeywordHistoricalMetrics'] = _KEYWORDPLANKEYWORDHISTORICALMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKeywordPlanRequest = _reflection.GeneratedProtocolMessageType('GetKeywordPlanRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETKEYWORDPLANREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetKeywordPlanRequest)
  })
_sym_db.RegisterMessage(GetKeywordPlanRequest)

MutateKeywordPlansRequest = _reflection.GeneratedProtocolMessageType('MutateKeywordPlansRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEKEYWORDPLANSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateKeywordPlansRequest)
  })
_sym_db.RegisterMessage(MutateKeywordPlansRequest)

KeywordPlanOperation = _reflection.GeneratedProtocolMessageType('KeywordPlanOperation', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANOPERATION,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.KeywordPlanOperation)
  })
_sym_db.RegisterMessage(KeywordPlanOperation)

MutateKeywordPlansResponse = _reflection.GeneratedProtocolMessageType('MutateKeywordPlansResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEKEYWORDPLANSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateKeywordPlansResponse)
  })
_sym_db.RegisterMessage(MutateKeywordPlansResponse)

MutateKeywordPlansResult = _reflection.GeneratedProtocolMessageType('MutateKeywordPlansResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEKEYWORDPLANSRESULT,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateKeywordPlansResult)
  })
_sym_db.RegisterMessage(MutateKeywordPlansResult)

GenerateForecastMetricsRequest = _reflection.GeneratedProtocolMessageType('GenerateForecastMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFORECASTMETRICSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GenerateForecastMetricsRequest)
  })
_sym_db.RegisterMessage(GenerateForecastMetricsRequest)

GenerateForecastMetricsResponse = _reflection.GeneratedProtocolMessageType('GenerateForecastMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFORECASTMETRICSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GenerateForecastMetricsResponse)
  })
_sym_db.RegisterMessage(GenerateForecastMetricsResponse)

KeywordPlanCampaignForecast = _reflection.GeneratedProtocolMessageType('KeywordPlanCampaignForecast', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANCAMPAIGNFORECAST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.KeywordPlanCampaignForecast)
  })
_sym_db.RegisterMessage(KeywordPlanCampaignForecast)

KeywordPlanAdGroupForecast = _reflection.GeneratedProtocolMessageType('KeywordPlanAdGroupForecast', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANADGROUPFORECAST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.KeywordPlanAdGroupForecast)
  })
_sym_db.RegisterMessage(KeywordPlanAdGroupForecast)

KeywordPlanKeywordForecast = _reflection.GeneratedProtocolMessageType('KeywordPlanKeywordForecast', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANKEYWORDFORECAST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.KeywordPlanKeywordForecast)
  })
_sym_db.RegisterMessage(KeywordPlanKeywordForecast)

ForecastMetrics = _reflection.GeneratedProtocolMessageType('ForecastMetrics', (_message.Message,), {
  'DESCRIPTOR' : _FORECASTMETRICS,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ForecastMetrics)
  })
_sym_db.RegisterMessage(ForecastMetrics)

GenerateHistoricalMetricsRequest = _reflection.GeneratedProtocolMessageType('GenerateHistoricalMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEHISTORICALMETRICSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GenerateHistoricalMetricsRequest)
  })
_sym_db.RegisterMessage(GenerateHistoricalMetricsRequest)

GenerateHistoricalMetricsResponse = _reflection.GeneratedProtocolMessageType('GenerateHistoricalMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEHISTORICALMETRICSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GenerateHistoricalMetricsResponse)
  })
_sym_db.RegisterMessage(GenerateHistoricalMetricsResponse)

KeywordPlanKeywordHistoricalMetrics = _reflection.GeneratedProtocolMessageType('KeywordPlanKeywordHistoricalMetrics', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANKEYWORDHISTORICALMETRICS,
  '__module__' : 'google.ads.googleads.v2.services.keyword_plan_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.KeywordPlanKeywordHistoricalMetrics)
  })
_sym_db.RegisterMessage(KeywordPlanKeywordHistoricalMetrics)


DESCRIPTOR._options = None

_KEYWORDPLANSERVICE = _descriptor.ServiceDescriptor(
  name='KeywordPlanService',
  full_name='google.ads.googleads.v2.services.KeywordPlanService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=2528,
  serialized_end=3459,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetKeywordPlan',
    full_name='google.ads.googleads.v2.services.KeywordPlanService.GetKeywordPlan',
    index=0,
    containing_service=None,
    input_type=_GETKEYWORDPLANREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_keyword__plan__pb2._KEYWORDPLAN,
    serialized_options=b'\202\323\344\223\0020\022./v2/{resource_name=customers/*/keywordPlans/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateKeywordPlans',
    full_name='google.ads.googleads.v2.services.KeywordPlanService.MutateKeywordPlans',
    index=1,
    containing_service=None,
    input_type=_MUTATEKEYWORDPLANSREQUEST,
    output_type=_MUTATEKEYWORDPLANSRESPONSE,
    serialized_options=b'\202\323\344\223\0026\"1/v2/customers/{customer_id=*}/keywordPlans:mutate:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GenerateForecastMetrics',
    full_name='google.ads.googleads.v2.services.KeywordPlanService.GenerateForecastMetrics',
    index=2,
    containing_service=None,
    input_type=_GENERATEFORECASTMETRICSREQUEST,
    output_type=_GENERATEFORECASTMETRICSRESPONSE,
    serialized_options=b'\202\323\344\223\002J\"E/v2/{keyword_plan=customers/*/keywordPlans/*}:generateForecastMetrics:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GenerateHistoricalMetrics',
    full_name='google.ads.googleads.v2.services.KeywordPlanService.GenerateHistoricalMetrics',
    index=3,
    containing_service=None,
    input_type=_GENERATEHISTORICALMETRICSREQUEST,
    output_type=_GENERATEHISTORICALMETRICSRESPONSE,
    serialized_options=b'\202\323\344\223\002L\"G/v2/{keyword_plan=customers/*/keywordPlans/*}:generateHistoricalMetrics:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYWORDPLANSERVICE)

DESCRIPTOR.services_by_name['KeywordPlanService'] = _KEYWORDPLANSERVICE

# @@protoc_insertion_point(module_scope)
