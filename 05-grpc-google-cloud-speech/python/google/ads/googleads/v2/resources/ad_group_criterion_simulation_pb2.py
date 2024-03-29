# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/resources/ad_group_criterion_simulation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.common import simulation_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_common_dot_simulation__pb2
from google.ads.googleads.v2.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_simulation__modification__method__pb2
from google.ads.googleads.v2.enums import simulation_type_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_simulation__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/resources/ad_group_criterion_simulation.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v2.resourcesB\037AdGroupCriterionSimulationProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources',
  serialized_pb=b'\nEgoogle/ads/googleads/v2/resources/ad_group_criterion_simulation.proto\x12!google.ads.googleads.v2.resources\x1a/google/ads/googleads/v2/common/simulation.proto\x1a\x42google/ads/googleads/v2/enums/simulation_modification_method.proto\x1a\x33google/ads/googleads/v2/enums/simulation_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xac\x04\n\x1a\x41\x64GroupCriterionSimulation\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x30\n\x0b\x61\x64_group_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0c\x63riterion_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12N\n\x04type\x18\x04 \x01(\x0e\x32@.google.ads.googleads.v2.enums.SimulationTypeEnum.SimulationType\x12y\n\x13modification_method\x18\x05 \x01(\x0e\x32\\.google.ads.googleads.v2.enums.SimulationModificationMethodEnum.SimulationModificationMethod\x12\x30\n\nstart_date\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x65nd_date\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12W\n\x12\x63pc_bid_point_list\x18\x08 \x01(\x0b\x32\x39.google.ads.googleads.v2.common.CpcBidSimulationPointListH\x00\x42\x0c\n\npoint_listB\x8c\x02\n%com.google.ads.googleads.v2.resourcesB\x1f\x41\x64GroupCriterionSimulationProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_common_dot_simulation__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_simulation__modification__method__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_simulation__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPCRITERIONSIMULATION = _descriptor.Descriptor(
  name='AdGroupCriterionSimulation',
  full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_id', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.ad_group_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='criterion_id', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.criterion_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modification_method', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.modification_method', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.start_date', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.end_date', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_point_list', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.cpc_bid_point_list', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
      name='point_list', full_name='google.ads.googleads.v2.resources.AdGroupCriterionSimulation.point_list',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=341,
  serialized_end=897,
)

_ADGROUPCRITERIONSIMULATION.fields_by_name['ad_group_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ADGROUPCRITERIONSIMULATION.fields_by_name['criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ADGROUPCRITERIONSIMULATION.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_simulation__type__pb2._SIMULATIONTYPEENUM_SIMULATIONTYPE
_ADGROUPCRITERIONSIMULATION.fields_by_name['modification_method'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_simulation__modification__method__pb2._SIMULATIONMODIFICATIONMETHODENUM_SIMULATIONMODIFICATIONMETHOD
_ADGROUPCRITERIONSIMULATION.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPCRITERIONSIMULATION.fields_by_name['end_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPCRITERIONSIMULATION.fields_by_name['cpc_bid_point_list'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_common_dot_simulation__pb2._CPCBIDSIMULATIONPOINTLIST
_ADGROUPCRITERIONSIMULATION.oneofs_by_name['point_list'].fields.append(
  _ADGROUPCRITERIONSIMULATION.fields_by_name['cpc_bid_point_list'])
_ADGROUPCRITERIONSIMULATION.fields_by_name['cpc_bid_point_list'].containing_oneof = _ADGROUPCRITERIONSIMULATION.oneofs_by_name['point_list']
DESCRIPTOR.message_types_by_name['AdGroupCriterionSimulation'] = _ADGROUPCRITERIONSIMULATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupCriterionSimulation = _reflection.GeneratedProtocolMessageType('AdGroupCriterionSimulation', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPCRITERIONSIMULATION,
  '__module__' : 'google.ads.googleads.v2.resources.ad_group_criterion_simulation_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.AdGroupCriterionSimulation)
  })
_sym_db.RegisterMessage(AdGroupCriterionSimulation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
