# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/resources/ad_group_bid_modifier.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2
from google.ads.googleads.v1.enums import bid_modifier_source_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bid__modifier__source__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/resources/ad_group_bid_modifier.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v1.resourcesB\027AdGroupBidModifierProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources',
  serialized_pb=b'\n=google/ads/googleads/v1/resources/ad_group_bid_modifier.proto\x12!google.ads.googleads.v1.resources\x1a-google/ads/googleads/v1/common/criteria.proto\x1a\x37google/ads/googleads/v1/enums/bid_modifier_source.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xec\x06\n\x12\x41\x64GroupBidModifier\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12.\n\x08\x61\x64_group\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0c\x63riterion_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\x0c\x62id_modifier\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\rbase_ad_group\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x63\n\x13\x62id_modifier_source\x18\n \x01(\x0e\x32\x46.google.ads.googleads.v1.enums.BidModifierSourceEnum.BidModifierSource\x12_\n\x19hotel_date_selection_type\x18\x05 \x01(\x0b\x32:.google.ads.googleads.v1.common.HotelDateSelectionTypeInfoH\x00\x12\x65\n\x1chotel_advance_booking_window\x18\x06 \x01(\x0b\x32=.google.ads.googleads.v1.common.HotelAdvanceBookingWindowInfoH\x00\x12U\n\x14hotel_length_of_stay\x18\x07 \x01(\x0b\x32\x35.google.ads.googleads.v1.common.HotelLengthOfStayInfoH\x00\x12Q\n\x12hotel_check_in_day\x18\x08 \x01(\x0b\x32\x33.google.ads.googleads.v1.common.HotelCheckInDayInfoH\x00\x12<\n\x06\x64\x65vice\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v1.common.DeviceInfoH\x00\x12Q\n\x11preferred_content\x18\x0c \x01(\x0b\x32\x34.google.ads.googleads.v1.common.PreferredContentInfoH\x00\x42\x0b\n\tcriterionB\x84\x02\n%com.google.ads.googleads.v1.resourcesB\x17\x41\x64GroupBidModifierProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bid__modifier__source__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_ADGROUPBIDMODIFIER = _descriptor.Descriptor(
  name='AdGroupBidModifier',
  full_name='google.ads.googleads.v1.resources.AdGroupBidModifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.ad_group', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='criterion_id', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.criterion_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_modifier', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.bid_modifier', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_ad_group', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.base_ad_group', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_modifier_source', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.bid_modifier_source', index=5,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_date_selection_type', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.hotel_date_selection_type', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_advance_booking_window', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.hotel_advance_booking_window', index=7,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_length_of_stay', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.hotel_length_of_stay', index=8,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_check_in_day', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.hotel_check_in_day', index=9,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.device', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preferred_content', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.preferred_content', index=11,
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
      name='criterion', full_name='google.ads.googleads.v1.resources.AdGroupBidModifier.criterion',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=267,
  serialized_end=1143,
)

_ADGROUPBIDMODIFIER.fields_by_name['ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPBIDMODIFIER.fields_by_name['criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ADGROUPBIDMODIFIER.fields_by_name['bid_modifier'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_ADGROUPBIDMODIFIER.fields_by_name['base_ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPBIDMODIFIER.fields_by_name['bid_modifier_source'].enum_type = google_dot_ads_dot_googleads_dot_v1_dot_enums_dot_bid__modifier__source__pb2._BIDMODIFIERSOURCEENUM_BIDMODIFIERSOURCE
_ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._HOTELDATESELECTIONTYPEINFO
_ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._HOTELADVANCEBOOKINGWINDOWINFO
_ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._HOTELLENGTHOFSTAYINFO
_ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._HOTELCHECKINDAYINFO
_ADGROUPBIDMODIFIER.fields_by_name['device'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._DEVICEINFO
_ADGROUPBIDMODIFIER.fields_by_name['preferred_content'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_common_dot_criteria__pb2._PREFERREDCONTENTINFO
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['device'])
_ADGROUPBIDMODIFIER.fields_by_name['device'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['preferred_content'])
_ADGROUPBIDMODIFIER.fields_by_name['preferred_content'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
DESCRIPTOR.message_types_by_name['AdGroupBidModifier'] = _ADGROUPBIDMODIFIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupBidModifier = _reflection.GeneratedProtocolMessageType('AdGroupBidModifier', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPBIDMODIFIER,
  '__module__' : 'google.ads.googleads.v1.resources.ad_group_bid_modifier_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.AdGroupBidModifier)
  })
_sym_db.RegisterMessage(AdGroupBidModifier)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
