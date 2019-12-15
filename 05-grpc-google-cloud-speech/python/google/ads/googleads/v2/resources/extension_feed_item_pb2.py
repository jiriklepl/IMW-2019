# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/resources/extension_feed_item.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_common_dot_criteria__pb2
from google.ads.googleads.v2.common import extensions_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2
from google.ads.googleads.v2.enums import extension_type_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_extension__type__pb2
from google.ads.googleads.v2.enums import feed_item_status_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_feed__item__status__pb2
from google.ads.googleads.v2.enums import feed_item_target_device_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_feed__item__target__device__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/resources/extension_feed_item.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v2.resourcesB\026ExtensionFeedItemProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources',
  serialized_pb=b'\n;google/ads/googleads/v2/resources/extension_feed_item.proto\x12!google.ads.googleads.v2.resources\x1a-google/ads/googleads/v2/common/criteria.proto\x1a/google/ads/googleads/v2/common/extensions.proto\x1a\x32google/ads/googleads/v2/enums/extension_type.proto\x1a\x34google/ads/googleads/v2/enums/feed_item_status.proto\x1a;google/ads/googleads/v2/enums/feed_item_target_device.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xc7\r\n\x11\x45xtensionFeedItem\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12V\n\x0e\x65xtension_type\x18\r \x01(\x0e\x32>.google.ads.googleads.v2.enums.ExtensionTypeEnum.ExtensionType\x12\x35\n\x0fstart_date_time\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rend_date_time\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x44\n\x0c\x61\x64_schedules\x18\x10 \x03(\x0b\x32..google.ads.googleads.v2.common.AdScheduleInfo\x12\\\n\x06\x64\x65vice\x18\x11 \x01(\x0e\x32L.google.ads.googleads.v2.enums.FeedItemTargetDeviceEnum.FeedItemTargetDevice\x12\x42\n\x1ctargeted_geo_target_constant\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x45\n\x10targeted_keyword\x18\x16 \x01(\x0b\x32+.google.ads.googleads.v2.common.KeywordInfo\x12P\n\x06status\x18\x04 \x01(\x0e\x32@.google.ads.googleads.v2.enums.FeedItemStatusEnum.FeedItemStatus\x12N\n\x12sitelink_feed_item\x18\x02 \x01(\x0b\x32\x30.google.ads.googleads.v2.common.SitelinkFeedItemH\x00\x12\x61\n\x1cstructured_snippet_feed_item\x18\x03 \x01(\x0b\x32\x39.google.ads.googleads.v2.common.StructuredSnippetFeedItemH\x00\x12\x44\n\rapp_feed_item\x18\x07 \x01(\x0b\x32+.google.ads.googleads.v2.common.AppFeedItemH\x00\x12\x46\n\x0e\x63\x61ll_feed_item\x18\x08 \x01(\x0b\x32,.google.ads.googleads.v2.common.CallFeedItemH\x00\x12L\n\x11\x63\x61llout_feed_item\x18\t \x01(\x0b\x32/.google.ads.googleads.v2.common.CalloutFeedItemH\x00\x12U\n\x16text_message_feed_item\x18\n \x01(\x0b\x32\x33.google.ads.googleads.v2.common.TextMessageFeedItemH\x00\x12H\n\x0fprice_feed_item\x18\x0b \x01(\x0b\x32-.google.ads.googleads.v2.common.PriceFeedItemH\x00\x12P\n\x13promotion_feed_item\x18\x0c \x01(\x0b\x32\x31.google.ads.googleads.v2.common.PromotionFeedItemH\x00\x12N\n\x12location_feed_item\x18\x0e \x01(\x0b\x32\x30.google.ads.googleads.v2.common.LocationFeedItemH\x00\x12\x61\n\x1c\x61\x66\x66iliate_location_feed_item\x18\x0f \x01(\x0b\x32\x39.google.ads.googleads.v2.common.AffiliateLocationFeedItemH\x00\x12W\n\x17hotel_callout_feed_item\x18\x17 \x01(\x0b\x32\x34.google.ads.googleads.v2.common.HotelCalloutFeedItemH\x00\x12\x39\n\x11targeted_campaign\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x12\x39\n\x11targeted_ad_group\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x42\x0b\n\textensionB\x1c\n\x1aserving_resource_targetingB\x83\x02\n%com.google.ads.googleads.v2.resourcesB\x16\x45xtensionFeedItemProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_common_dot_criteria__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_extension__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_feed__item__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_feed__item__target__device__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_EXTENSIONFEEDITEM = _descriptor.Descriptor(
  name='ExtensionFeedItem',
  full_name='google.ads.googleads.v2.resources.ExtensionFeedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.id', index=1,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_type', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.extension_type', index=2,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date_time', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.start_date_time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date_time', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.end_date_time', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_schedules', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.ad_schedules', index=5,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.device', index=6,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeted_geo_target_constant', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.targeted_geo_target_constant', index=7,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeted_keyword', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.targeted_keyword', index=8,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.status', index=9,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sitelink_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.sitelink_feed_item', index=10,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='structured_snippet_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.structured_snippet_feed_item', index=11,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.app_feed_item', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.call_feed_item', index=13,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callout_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.callout_feed_item', index=14,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_message_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.text_message_feed_item', index=15,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.price_feed_item', index=16,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='promotion_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.promotion_feed_item', index=17,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.location_feed_item', index=18,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='affiliate_location_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.affiliate_location_feed_item', index=19,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_callout_feed_item', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.hotel_callout_feed_item', index=20,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeted_campaign', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.targeted_campaign', index=21,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeted_ad_group', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.targeted_ad_group', index=22,
      number=19, type=11, cpp_type=10, label=1,
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
      name='extension', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.extension',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='serving_resource_targeting', full_name='google.ads.googleads.v2.resources.ExtensionFeedItem.serving_resource_targeting',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=424,
  serialized_end=2159,
)

_EXTENSIONFEEDITEM.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_EXTENSIONFEEDITEM.fields_by_name['extension_type'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_extension__type__pb2._EXTENSIONTYPEENUM_EXTENSIONTYPE
_EXTENSIONFEEDITEM.fields_by_name['start_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EXTENSIONFEEDITEM.fields_by_name['end_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EXTENSIONFEEDITEM.fields_by_name['ad_schedules'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_criteria__pb2._ADSCHEDULEINFO
_EXTENSIONFEEDITEM.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_feed__item__target__device__pb2._FEEDITEMTARGETDEVICEENUM_FEEDITEMTARGETDEVICE
_EXTENSIONFEEDITEM.fields_by_name['targeted_geo_target_constant'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EXTENSIONFEEDITEM.fields_by_name['targeted_keyword'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_criteria__pb2._KEYWORDINFO
_EXTENSIONFEEDITEM.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_feed__item__status__pb2._FEEDITEMSTATUSENUM_FEEDITEMSTATUS
_EXTENSIONFEEDITEM.fields_by_name['sitelink_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._SITELINKFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['structured_snippet_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._STRUCTUREDSNIPPETFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['app_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._APPFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['call_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._CALLFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['callout_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._CALLOUTFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['text_message_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._TEXTMESSAGEFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['price_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._PRICEFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['promotion_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._PROMOTIONFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['location_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._LOCATIONFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['affiliate_location_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._AFFILIATELOCATIONFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['hotel_callout_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_extensions__pb2._HOTELCALLOUTFEEDITEM
_EXTENSIONFEEDITEM.fields_by_name['targeted_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EXTENSIONFEEDITEM.fields_by_name['targeted_ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['sitelink_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['sitelink_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['structured_snippet_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['structured_snippet_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['app_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['app_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['call_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['call_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['callout_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['callout_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['text_message_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['text_message_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['price_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['price_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['promotion_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['promotion_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['location_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['location_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['affiliate_location_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['affiliate_location_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['extension'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['hotel_callout_feed_item'])
_EXTENSIONFEEDITEM.fields_by_name['hotel_callout_feed_item'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['extension']
_EXTENSIONFEEDITEM.oneofs_by_name['serving_resource_targeting'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['targeted_campaign'])
_EXTENSIONFEEDITEM.fields_by_name['targeted_campaign'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['serving_resource_targeting']
_EXTENSIONFEEDITEM.oneofs_by_name['serving_resource_targeting'].fields.append(
  _EXTENSIONFEEDITEM.fields_by_name['targeted_ad_group'])
_EXTENSIONFEEDITEM.fields_by_name['targeted_ad_group'].containing_oneof = _EXTENSIONFEEDITEM.oneofs_by_name['serving_resource_targeting']
DESCRIPTOR.message_types_by_name['ExtensionFeedItem'] = _EXTENSIONFEEDITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtensionFeedItem = _reflection.GeneratedProtocolMessageType('ExtensionFeedItem', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONFEEDITEM,
  '__module__' : 'google.ads.googleads.v2.resources.extension_feed_item_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.ExtensionFeedItem)
  })
_sym_db.RegisterMessage(ExtensionFeedItem)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
