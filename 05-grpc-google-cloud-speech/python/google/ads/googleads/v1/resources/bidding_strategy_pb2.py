# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/resources/bidding_strategy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.common import bidding_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2
from google.ads.googleads.v1.enums import bidding_strategy_status_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bidding__strategy__status__pb2
from google.ads.googleads.v1.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bidding__strategy__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/resources/bidding_strategy.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v1.resourcesB\024BiddingStrategyProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources',
  serialized_pb=b'\n8google/ads/googleads/v1/resources/bidding_strategy.proto\x12!google.ads.googleads.v1.resources\x1a,google/ads/googleads/v1/common/bidding.proto\x1a;google/ads/googleads/v1/enums/bidding_strategy_status.proto\x1a\x39google/ads/googleads/v1/enums/bidding_strategy_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xc1\x07\n\x0f\x42iddingStrategy\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12^\n\x06status\x18\x0f \x01(\x0e\x32N.google.ads.googleads.v1.enums.BiddingStrategyStatusEnum.BiddingStrategyStatus\x12X\n\x04type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v1.enums.BiddingStrategyTypeEnum.BiddingStrategyType\x12\x33\n\x0e\x63\x61mpaign_count\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1anon_removed_campaign_count\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x43\n\x0c\x65nhanced_cpc\x18\x07 \x01(\x0b\x32+.google.ads.googleads.v1.common.EnhancedCpcH\x00\x12L\n\x11page_one_promoted\x18\x08 \x01(\x0b\x32/.google.ads.googleads.v1.common.PageOnePromotedH\x00\x12?\n\ntarget_cpa\x18\t \x01(\x0b\x32).google.ads.googleads.v1.common.TargetCpaH\x00\x12X\n\x17target_impression_share\x18\x30 \x01(\x0b\x32\x35.google.ads.googleads.v1.common.TargetImpressionShareH\x00\x12R\n\x14target_outrank_share\x18\n \x01(\x0b\x32\x32.google.ads.googleads.v1.common.TargetOutrankShareH\x00\x12\x41\n\x0btarget_roas\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v1.common.TargetRoasH\x00\x12\x43\n\x0ctarget_spend\x18\x0c \x01(\x0b\x32+.google.ads.googleads.v1.common.TargetSpendH\x00\x42\x08\n\x06schemeB\x81\x02\n%com.google.ads.googleads.v1.resourcesB\x14\x42iddingStrategyProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bidding__strategy__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bidding__strategy__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_BIDDINGSTRATEGY = _descriptor.Descriptor(
  name='BiddingStrategy',
  full_name='google.ads.googleads.v1.resources.BiddingStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.BiddingStrategy.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.BiddingStrategy.id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.BiddingStrategy.name', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v1.resources.BiddingStrategy.status', index=3,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v1.resources.BiddingStrategy.type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_count', full_name='google.ads.googleads.v1.resources.BiddingStrategy.campaign_count', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='non_removed_campaign_count', full_name='google.ads.googleads.v1.resources.BiddingStrategy.non_removed_campaign_count', index=6,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enhanced_cpc', full_name='google.ads.googleads.v1.resources.BiddingStrategy.enhanced_cpc', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_one_promoted', full_name='google.ads.googleads.v1.resources.BiddingStrategy.page_one_promoted', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_cpa', full_name='google.ads.googleads.v1.resources.BiddingStrategy.target_cpa', index=9,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_impression_share', full_name='google.ads.googleads.v1.resources.BiddingStrategy.target_impression_share', index=10,
      number=48, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_outrank_share', full_name='google.ads.googleads.v1.resources.BiddingStrategy.target_outrank_share', index=11,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_roas', full_name='google.ads.googleads.v1.resources.BiddingStrategy.target_roas', index=12,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_spend', full_name='google.ads.googleads.v1.resources.BiddingStrategy.target_spend', index=13,
      number=12, type=11, cpp_type=10, label=1,
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
      name='scheme', full_name='google.ads.googleads.v1.resources.BiddingStrategy.scheme',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=324,
  serialized_end=1285,
)

_BIDDINGSTRATEGY.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BIDDINGSTRATEGY.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BIDDINGSTRATEGY.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bidding__strategy__status__pb2._BIDDINGSTRATEGYSTATUSENUM_BIDDINGSTRATEGYSTATUS
_BIDDINGSTRATEGY.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bidding__strategy__type__pb2._BIDDINGSTRATEGYTYPEENUM_BIDDINGSTRATEGYTYPE
_BIDDINGSTRATEGY.fields_by_name['campaign_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BIDDINGSTRATEGY.fields_by_name['non_removed_campaign_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BIDDINGSTRATEGY.fields_by_name['enhanced_cpc'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._ENHANCEDCPC
_BIDDINGSTRATEGY.fields_by_name['page_one_promoted'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._PAGEONEPROMOTED
_BIDDINGSTRATEGY.fields_by_name['target_cpa'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._TARGETCPA
_BIDDINGSTRATEGY.fields_by_name['target_impression_share'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._TARGETIMPRESSIONSHARE
_BIDDINGSTRATEGY.fields_by_name['target_outrank_share'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._TARGETOUTRANKSHARE
_BIDDINGSTRATEGY.fields_by_name['target_roas'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._TARGETROAS
_BIDDINGSTRATEGY.fields_by_name['target_spend'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_bidding__pb2._TARGETSPEND
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['enhanced_cpc'])
_BIDDINGSTRATEGY.fields_by_name['enhanced_cpc'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['page_one_promoted'])
_BIDDINGSTRATEGY.fields_by_name['page_one_promoted'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_cpa'])
_BIDDINGSTRATEGY.fields_by_name['target_cpa'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_impression_share'])
_BIDDINGSTRATEGY.fields_by_name['target_impression_share'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_outrank_share'])
_BIDDINGSTRATEGY.fields_by_name['target_outrank_share'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_roas'])
_BIDDINGSTRATEGY.fields_by_name['target_roas'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_spend'])
_BIDDINGSTRATEGY.fields_by_name['target_spend'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
DESCRIPTOR.message_types_by_name['BiddingStrategy'] = _BIDDINGSTRATEGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingStrategy = _reflection.GeneratedProtocolMessageType('BiddingStrategy', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGSTRATEGY,
  '__module__' : 'google.ads.googleads.v1.resources.bidding_strategy_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.BiddingStrategy)
  })
_sym_db.RegisterMessage(BiddingStrategy)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
