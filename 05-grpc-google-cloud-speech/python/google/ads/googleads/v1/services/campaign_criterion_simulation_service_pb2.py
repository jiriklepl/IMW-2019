# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/campaign_criterion_simulation_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import campaign_criterion_simulation_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__criterion__simulation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/campaign_criterion_simulation_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\'CampaignCriterionSimulationServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\nLgoogle/ads/googleads/v1/services/campaign_criterion_simulation_service.proto\x12 google.ads.googleads.v1.services\x1a\x45google/ads/googleads/v1/resources/campaign_criterion_simulation.proto\x1a\x1cgoogle/api/annotations.proto\">\n%GetCampaignCriterionSimulationRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x98\x02\n\"CampaignCriterionSimulationService\x12\xf1\x01\n\x1eGetCampaignCriterionSimulation\x12G.google.ads.googleads.v1.services.GetCampaignCriterionSimulationRequest\x1a>.google.ads.googleads.v1.resources.CampaignCriterionSimulation\"F\x82\xd3\xe4\x93\x02@\x12>/v1/{resource_name=customers/*/campaignCriterionSimulations/*}B\x8e\x02\n$com.google.ads.googleads.v1.servicesB\'CampaignCriterionSimulationServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__criterion__simulation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETCAMPAIGNCRITERIONSIMULATIONREQUEST = _descriptor.Descriptor(
  name='GetCampaignCriterionSimulationRequest',
  full_name='google.ads.googleads.v1.services.GetCampaignCriterionSimulationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetCampaignCriterionSimulationRequest.resource_name', index=0,
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
  serialized_start=215,
  serialized_end=277,
)

DESCRIPTOR.message_types_by_name['GetCampaignCriterionSimulationRequest'] = _GETCAMPAIGNCRITERIONSIMULATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignCriterionSimulationRequest = _reflection.GeneratedProtocolMessageType('GetCampaignCriterionSimulationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNCRITERIONSIMULATIONREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.campaign_criterion_simulation_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetCampaignCriterionSimulationRequest)
  })
_sym_db.RegisterMessage(GetCampaignCriterionSimulationRequest)


DESCRIPTOR._options = None

_CAMPAIGNCRITERIONSIMULATIONSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignCriterionSimulationService',
  full_name='google.ads.googleads.v1.services.CampaignCriterionSimulationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=280,
  serialized_end=560,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaignCriterionSimulation',
    full_name='google.ads.googleads.v1.services.CampaignCriterionSimulationService.GetCampaignCriterionSimulation',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNCRITERIONSIMULATIONREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__criterion__simulation__pb2._CAMPAIGNCRITERIONSIMULATION,
    serialized_options=b'\202\323\344\223\002@\022>/v1/{resource_name=customers/*/campaignCriterionSimulations/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNCRITERIONSIMULATIONSERVICE)

DESCRIPTOR.services_by_name['CampaignCriterionSimulationService'] = _CAMPAIGNCRITERIONSIMULATIONSERVICE

# @@protoc_insertion_point(module_scope)
