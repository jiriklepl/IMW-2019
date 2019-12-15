# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/common/bidding.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.enums import page_one_promoted_strategy_goal_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_page__one__promoted__strategy__goal__pb2
from google.ads.googleads.v1.enums import target_impression_share_location_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_target__impression__share__location__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/common/bidding.proto',
  package='google.ads.googleads.v1.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v1.commonB\014BiddingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Common\312\002\036Google\\Ads\\GoogleAds\\V1\\Common\352\002\"Google::Ads::GoogleAds::V1::Common',
  serialized_pb=b'\n,google/ads/googleads/v1/common/bidding.proto\x12\x1egoogle.ads.googleads.v1.common\x1a\x43google/ads/googleads/v1/enums/page_one_promoted_strategy_goal.proto\x1a\x44google/ads/googleads/v1/enums/target_impression_share_location.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"I\n\nCommission\x12;\n\x16\x63ommission_rate_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\r\n\x0b\x45nhancedCpc\"E\n\tManualCpc\x12\x38\n\x14\x65nhanced_cpc_enabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x0b\n\tManualCpm\"\x0b\n\tManualCpv\"\x15\n\x13MaximizeConversions\"L\n\x17MaximizeConversionValue\x12\x31\n\x0btarget_roas\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"\xc6\x03\n\x0fPageOnePromoted\x12q\n\rstrategy_goal\x18\x01 \x01(\x0e\x32Z.google.ads.googleads.v1.enums.PageOnePromotedStrategyGoalEnum.PageOnePromotedStrategyGoal\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\x0c\x62id_modifier\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x37\n\x13only_raise_cpc_bids\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12I\n%raise_cpc_bid_when_budget_constrained\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12K\n\'raise_cpc_bid_when_quality_score_is_low\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xbb\x01\n\tTargetCpa\x12\x36\n\x11target_cpa_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x63pc_bid_floor_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x0b\n\tTargetCpm\"\x85\x02\n\x15TargetImpressionShare\x12p\n\x08location\x18\x01 \x01(\x0e\x32^.google.ads.googleads.v1.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocation\x12=\n\x18location_fraction_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xd2\x02\n\x12TargetOutrankShare\x12@\n\x1btarget_outrank_share_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x11\x63ompetitor_domain\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x13only_raise_cpc_bids\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12K\n\'raise_cpc_bid_when_quality_score_is_low\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xb7\x01\n\nTargetRoas\x12\x31\n\x0btarget_roas\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x63pc_bid_floor_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x84\x01\n\x0bTargetSpend\x12\x38\n\x13target_spend_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x83\x01\n\nPercentCpc\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x14\x65nhanced_cpc_enabled\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\xe7\x01\n\"com.google.ads.googleads.v1.commonB\x0c\x42iddingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Common\xea\x02\"Google::Ads::GoogleAds::V1::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_page__one__promoted__strategy__goal__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_target__impression__share__location__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_COMMISSION = _descriptor.Descriptor(
  name='Commission',
  full_name='google.ads.googleads.v1.common.Commission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commission_rate_micros', full_name='google.ads.googleads.v1.common.Commission.commission_rate_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=281,
  serialized_end=354,
)


_ENHANCEDCPC = _descriptor.Descriptor(
  name='EnhancedCpc',
  full_name='google.ads.googleads.v1.common.EnhancedCpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=356,
  serialized_end=369,
)


_MANUALCPC = _descriptor.Descriptor(
  name='ManualCpc',
  full_name='google.ads.googleads.v1.common.ManualCpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enhanced_cpc_enabled', full_name='google.ads.googleads.v1.common.ManualCpc.enhanced_cpc_enabled', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=371,
  serialized_end=440,
)


_MANUALCPM = _descriptor.Descriptor(
  name='ManualCpm',
  full_name='google.ads.googleads.v1.common.ManualCpm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=442,
  serialized_end=453,
)


_MANUALCPV = _descriptor.Descriptor(
  name='ManualCpv',
  full_name='google.ads.googleads.v1.common.ManualCpv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=455,
  serialized_end=466,
)


_MAXIMIZECONVERSIONS = _descriptor.Descriptor(
  name='MaximizeConversions',
  full_name='google.ads.googleads.v1.common.MaximizeConversions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=468,
  serialized_end=489,
)


_MAXIMIZECONVERSIONVALUE = _descriptor.Descriptor(
  name='MaximizeConversionValue',
  full_name='google.ads.googleads.v1.common.MaximizeConversionValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_roas', full_name='google.ads.googleads.v1.common.MaximizeConversionValue.target_roas', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=491,
  serialized_end=567,
)


_PAGEONEPROMOTED = _descriptor.Descriptor(
  name='PageOnePromoted',
  full_name='google.ads.googleads.v1.common.PageOnePromoted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy_goal', full_name='google.ads.googleads.v1.common.PageOnePromoted.strategy_goal', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.PageOnePromoted.cpc_bid_ceiling_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_modifier', full_name='google.ads.googleads.v1.common.PageOnePromoted.bid_modifier', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only_raise_cpc_bids', full_name='google.ads.googleads.v1.common.PageOnePromoted.only_raise_cpc_bids', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raise_cpc_bid_when_budget_constrained', full_name='google.ads.googleads.v1.common.PageOnePromoted.raise_cpc_bid_when_budget_constrained', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raise_cpc_bid_when_quality_score_is_low', full_name='google.ads.googleads.v1.common.PageOnePromoted.raise_cpc_bid_when_quality_score_is_low', index=5,
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
  serialized_start=570,
  serialized_end=1024,
)


_TARGETCPA = _descriptor.Descriptor(
  name='TargetCpa',
  full_name='google.ads.googleads.v1.common.TargetCpa',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_cpa_micros', full_name='google.ads.googleads.v1.common.TargetCpa.target_cpa_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.TargetCpa.cpc_bid_ceiling_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_floor_micros', full_name='google.ads.googleads.v1.common.TargetCpa.cpc_bid_floor_micros', index=2,
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
  serialized_start=1027,
  serialized_end=1214,
)


_TARGETCPM = _descriptor.Descriptor(
  name='TargetCpm',
  full_name='google.ads.googleads.v1.common.TargetCpm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1216,
  serialized_end=1227,
)


_TARGETIMPRESSIONSHARE = _descriptor.Descriptor(
  name='TargetImpressionShare',
  full_name='google.ads.googleads.v1.common.TargetImpressionShare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='google.ads.googleads.v1.common.TargetImpressionShare.location', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_fraction_micros', full_name='google.ads.googleads.v1.common.TargetImpressionShare.location_fraction_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.TargetImpressionShare.cpc_bid_ceiling_micros', index=2,
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
  serialized_start=1230,
  serialized_end=1491,
)


_TARGETOUTRANKSHARE = _descriptor.Descriptor(
  name='TargetOutrankShare',
  full_name='google.ads.googleads.v1.common.TargetOutrankShare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_outrank_share_micros', full_name='google.ads.googleads.v1.common.TargetOutrankShare.target_outrank_share_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='competitor_domain', full_name='google.ads.googleads.v1.common.TargetOutrankShare.competitor_domain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.TargetOutrankShare.cpc_bid_ceiling_micros', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only_raise_cpc_bids', full_name='google.ads.googleads.v1.common.TargetOutrankShare.only_raise_cpc_bids', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raise_cpc_bid_when_quality_score_is_low', full_name='google.ads.googleads.v1.common.TargetOutrankShare.raise_cpc_bid_when_quality_score_is_low', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=1494,
  serialized_end=1832,
)


_TARGETROAS = _descriptor.Descriptor(
  name='TargetRoas',
  full_name='google.ads.googleads.v1.common.TargetRoas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_roas', full_name='google.ads.googleads.v1.common.TargetRoas.target_roas', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.TargetRoas.cpc_bid_ceiling_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_floor_micros', full_name='google.ads.googleads.v1.common.TargetRoas.cpc_bid_floor_micros', index=2,
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
  serialized_start=1835,
  serialized_end=2018,
)


_TARGETSPEND = _descriptor.Descriptor(
  name='TargetSpend',
  full_name='google.ads.googleads.v1.common.TargetSpend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_spend_micros', full_name='google.ads.googleads.v1.common.TargetSpend.target_spend_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.TargetSpend.cpc_bid_ceiling_micros', index=1,
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
  serialized_start=2021,
  serialized_end=2153,
)


_PERCENTCPC = _descriptor.Descriptor(
  name='PercentCpc',
  full_name='google.ads.googleads.v1.common.PercentCpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v1.common.PercentCpc.cpc_bid_ceiling_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enhanced_cpc_enabled', full_name='google.ads.googleads.v1.common.PercentCpc.enhanced_cpc_enabled', index=1,
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
  serialized_start=2156,
  serialized_end=2287,
)

_COMMISSION.fields_by_name['commission_rate_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MANUALCPC.fields_by_name['enhanced_cpc_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MAXIMIZECONVERSIONVALUE.fields_by_name['target_roas'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_PAGEONEPROMOTED.fields_by_name['strategy_goal'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_page__one__promoted__strategy__goal__pb2._PAGEONEPROMOTEDSTRATEGYGOALENUM_PAGEONEPROMOTEDSTRATEGYGOAL
_PAGEONEPROMOTED.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PAGEONEPROMOTED.fields_by_name['bid_modifier'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_PAGEONEPROMOTED.fields_by_name['only_raise_cpc_bids'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_PAGEONEPROMOTED.fields_by_name['raise_cpc_bid_when_budget_constrained'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_PAGEONEPROMOTED.fields_by_name['raise_cpc_bid_when_quality_score_is_low'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TARGETCPA.fields_by_name['target_cpa_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETCPA.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETCPA.fields_by_name['cpc_bid_floor_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETIMPRESSIONSHARE.fields_by_name['location'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_target__impression__share__location__pb2._TARGETIMPRESSIONSHARELOCATIONENUM_TARGETIMPRESSIONSHARELOCATION
_TARGETIMPRESSIONSHARE.fields_by_name['location_fraction_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETIMPRESSIONSHARE.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETOUTRANKSHARE.fields_by_name['target_outrank_share_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_TARGETOUTRANKSHARE.fields_by_name['competitor_domain'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_TARGETOUTRANKSHARE.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETOUTRANKSHARE.fields_by_name['only_raise_cpc_bids'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TARGETOUTRANKSHARE.fields_by_name['raise_cpc_bid_when_quality_score_is_low'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TARGETROAS.fields_by_name['target_roas'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_TARGETROAS.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETROAS.fields_by_name['cpc_bid_floor_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETSPEND.fields_by_name['target_spend_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETSPEND.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PERCENTCPC.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PERCENTCPC.fields_by_name['enhanced_cpc_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['Commission'] = _COMMISSION
DESCRIPTOR.message_types_by_name['EnhancedCpc'] = _ENHANCEDCPC
DESCRIPTOR.message_types_by_name['ManualCpc'] = _MANUALCPC
DESCRIPTOR.message_types_by_name['ManualCpm'] = _MANUALCPM
DESCRIPTOR.message_types_by_name['ManualCpv'] = _MANUALCPV
DESCRIPTOR.message_types_by_name['MaximizeConversions'] = _MAXIMIZECONVERSIONS
DESCRIPTOR.message_types_by_name['MaximizeConversionValue'] = _MAXIMIZECONVERSIONVALUE
DESCRIPTOR.message_types_by_name['PageOnePromoted'] = _PAGEONEPROMOTED
DESCRIPTOR.message_types_by_name['TargetCpa'] = _TARGETCPA
DESCRIPTOR.message_types_by_name['TargetCpm'] = _TARGETCPM
DESCRIPTOR.message_types_by_name['TargetImpressionShare'] = _TARGETIMPRESSIONSHARE
DESCRIPTOR.message_types_by_name['TargetOutrankShare'] = _TARGETOUTRANKSHARE
DESCRIPTOR.message_types_by_name['TargetRoas'] = _TARGETROAS
DESCRIPTOR.message_types_by_name['TargetSpend'] = _TARGETSPEND
DESCRIPTOR.message_types_by_name['PercentCpc'] = _PERCENTCPC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Commission = _reflection.GeneratedProtocolMessageType('Commission', (_message.Message,), {
  'DESCRIPTOR' : _COMMISSION,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.Commission)
  })
_sym_db.RegisterMessage(Commission)

EnhancedCpc = _reflection.GeneratedProtocolMessageType('EnhancedCpc', (_message.Message,), {
  'DESCRIPTOR' : _ENHANCEDCPC,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.EnhancedCpc)
  })
_sym_db.RegisterMessage(EnhancedCpc)

ManualCpc = _reflection.GeneratedProtocolMessageType('ManualCpc', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCPC,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.ManualCpc)
  })
_sym_db.RegisterMessage(ManualCpc)

ManualCpm = _reflection.GeneratedProtocolMessageType('ManualCpm', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCPM,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.ManualCpm)
  })
_sym_db.RegisterMessage(ManualCpm)

ManualCpv = _reflection.GeneratedProtocolMessageType('ManualCpv', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCPV,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.ManualCpv)
  })
_sym_db.RegisterMessage(ManualCpv)

MaximizeConversions = _reflection.GeneratedProtocolMessageType('MaximizeConversions', (_message.Message,), {
  'DESCRIPTOR' : _MAXIMIZECONVERSIONS,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.MaximizeConversions)
  })
_sym_db.RegisterMessage(MaximizeConversions)

MaximizeConversionValue = _reflection.GeneratedProtocolMessageType('MaximizeConversionValue', (_message.Message,), {
  'DESCRIPTOR' : _MAXIMIZECONVERSIONVALUE,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.MaximizeConversionValue)
  })
_sym_db.RegisterMessage(MaximizeConversionValue)

PageOnePromoted = _reflection.GeneratedProtocolMessageType('PageOnePromoted', (_message.Message,), {
  'DESCRIPTOR' : _PAGEONEPROMOTED,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.PageOnePromoted)
  })
_sym_db.RegisterMessage(PageOnePromoted)

TargetCpa = _reflection.GeneratedProtocolMessageType('TargetCpa', (_message.Message,), {
  'DESCRIPTOR' : _TARGETCPA,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TargetCpa)
  })
_sym_db.RegisterMessage(TargetCpa)

TargetCpm = _reflection.GeneratedProtocolMessageType('TargetCpm', (_message.Message,), {
  'DESCRIPTOR' : _TARGETCPM,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TargetCpm)
  })
_sym_db.RegisterMessage(TargetCpm)

TargetImpressionShare = _reflection.GeneratedProtocolMessageType('TargetImpressionShare', (_message.Message,), {
  'DESCRIPTOR' : _TARGETIMPRESSIONSHARE,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TargetImpressionShare)
  })
_sym_db.RegisterMessage(TargetImpressionShare)

TargetOutrankShare = _reflection.GeneratedProtocolMessageType('TargetOutrankShare', (_message.Message,), {
  'DESCRIPTOR' : _TARGETOUTRANKSHARE,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TargetOutrankShare)
  })
_sym_db.RegisterMessage(TargetOutrankShare)

TargetRoas = _reflection.GeneratedProtocolMessageType('TargetRoas', (_message.Message,), {
  'DESCRIPTOR' : _TARGETROAS,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TargetRoas)
  })
_sym_db.RegisterMessage(TargetRoas)

TargetSpend = _reflection.GeneratedProtocolMessageType('TargetSpend', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSPEND,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TargetSpend)
  })
_sym_db.RegisterMessage(TargetSpend)

PercentCpc = _reflection.GeneratedProtocolMessageType('PercentCpc', (_message.Message,), {
  'DESCRIPTOR' : _PERCENTCPC,
  '__module__' : 'google.ads.googleads.v1.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.PercentCpc)
  })
_sym_db.RegisterMessage(PercentCpc)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
