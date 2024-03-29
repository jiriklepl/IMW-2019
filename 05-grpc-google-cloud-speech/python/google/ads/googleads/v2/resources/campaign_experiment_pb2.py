# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/resources/campaign_experiment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.enums import campaign_experiment_status_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_campaign__experiment__status__pb2
from google.ads.googleads.v2.enums import campaign_experiment_traffic_split_type_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_campaign__experiment__traffic__split__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/resources/campaign_experiment.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v2.resourcesB\027CampaignExperimentProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources',
  serialized_pb=b'\n;google/ads/googleads/v2/resources/campaign_experiment.proto\x12!google.ads.googleads.v2.resources\x1a>google/ads/googleads/v2/enums/campaign_experiment_status.proto\x1aJgoogle/ads/googleads/v2/enums/campaign_experiment_traffic_split_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xed\x05\n\x12\x43\x61mpaignExperiment\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0e\x63\x61mpaign_draft\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x15traffic_split_percent\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x84\x01\n\x12traffic_split_type\x18\x07 \x01(\x0e\x32h.google.ads.googleads.v2.enums.CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType\x12\x39\n\x13\x65xperiment_campaign\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x64\n\x06status\x18\t \x01(\x0e\x32T.google.ads.googleads.v2.enums.CampaignExperimentStatusEnum.CampaignExperimentStatus\x12<\n\x16long_running_operation\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nstart_date\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x65nd_date\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x84\x02\n%com.google.ads.googleads.v2.resourcesB\x17\x43\x61mpaignExperimentProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_campaign__experiment__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_campaign__experiment__traffic__split__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNEXPERIMENT = _descriptor.Descriptor(
  name='CampaignExperiment',
  full_name='google.ads.googleads.v2.resources.CampaignExperiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.CampaignExperiment.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v2.resources.CampaignExperiment.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_draft', full_name='google.ads.googleads.v2.resources.CampaignExperiment.campaign_draft', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v2.resources.CampaignExperiment.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.ads.googleads.v2.resources.CampaignExperiment.description', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_split_percent', full_name='google.ads.googleads.v2.resources.CampaignExperiment.traffic_split_percent', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_split_type', full_name='google.ads.googleads.v2.resources.CampaignExperiment.traffic_split_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_campaign', full_name='google.ads.googleads.v2.resources.CampaignExperiment.experiment_campaign', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v2.resources.CampaignExperiment.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_running_operation', full_name='google.ads.googleads.v2.resources.CampaignExperiment.long_running_operation', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='google.ads.googleads.v2.resources.CampaignExperiment.start_date', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='google.ads.googleads.v2.resources.CampaignExperiment.end_date', index=11,
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
  ],
  serialized_start=301,
  serialized_end=1050,
)

_CAMPAIGNEXPERIMENT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNEXPERIMENT.fields_by_name['campaign_draft'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXPERIMENT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXPERIMENT.fields_by_name['description'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXPERIMENT.fields_by_name['traffic_split_percent'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNEXPERIMENT.fields_by_name['traffic_split_type'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_campaign__experiment__traffic__split__type__pb2._CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPE
_CAMPAIGNEXPERIMENT.fields_by_name['experiment_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXPERIMENT.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_campaign__experiment__status__pb2._CAMPAIGNEXPERIMENTSTATUSENUM_CAMPAIGNEXPERIMENTSTATUS
_CAMPAIGNEXPERIMENT.fields_by_name['long_running_operation'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXPERIMENT.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXPERIMENT.fields_by_name['end_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CampaignExperiment'] = _CAMPAIGNEXPERIMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignExperiment = _reflection.GeneratedProtocolMessageType('CampaignExperiment', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNEXPERIMENT,
  '__module__' : 'google.ads.googleads.v2.resources.campaign_experiment_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.CampaignExperiment)
  })
_sym_db.RegisterMessage(CampaignExperiment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
