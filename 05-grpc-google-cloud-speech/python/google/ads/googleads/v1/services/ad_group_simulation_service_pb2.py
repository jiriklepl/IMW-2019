# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/ad_group_simulation_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import ad_group_simulation_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__group__simulation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/ad_group_simulation_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\035AdGroupSimulationServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\nBgoogle/ads/googleads/v1/services/ad_group_simulation_service.proto\x12 google.ads.googleads.v1.services\x1a;google/ads/googleads/v1/resources/ad_group_simulation.proto\x1a\x1cgoogle/api/annotations.proto\"4\n\x1bGetAdGroupSimulationRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xe6\x01\n\x18\x41\x64GroupSimulationService\x12\xc9\x01\n\x14GetAdGroupSimulation\x12=.google.ads.googleads.v1.services.GetAdGroupSimulationRequest\x1a\x34.google.ads.googleads.v1.resources.AdGroupSimulation\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/v1/{resource_name=customers/*/adGroupSimulations/*}B\x84\x02\n$com.google.ads.googleads.v1.servicesB\x1d\x41\x64GroupSimulationServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__group__simulation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETADGROUPSIMULATIONREQUEST = _descriptor.Descriptor(
  name='GetAdGroupSimulationRequest',
  full_name='google.ads.googleads.v1.services.GetAdGroupSimulationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetAdGroupSimulationRequest.resource_name', index=0,
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
  serialized_start=195,
  serialized_end=247,
)

DESCRIPTOR.message_types_by_name['GetAdGroupSimulationRequest'] = _GETADGROUPSIMULATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdGroupSimulationRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupSimulationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADGROUPSIMULATIONREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.ad_group_simulation_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetAdGroupSimulationRequest)
  })
_sym_db.RegisterMessage(GetAdGroupSimulationRequest)


DESCRIPTOR._options = None

_ADGROUPSIMULATIONSERVICE = _descriptor.ServiceDescriptor(
  name='AdGroupSimulationService',
  full_name='google.ads.googleads.v1.services.AdGroupSimulationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=250,
  serialized_end=480,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdGroupSimulation',
    full_name='google.ads.googleads.v1.services.AdGroupSimulationService.GetAdGroupSimulation',
    index=0,
    containing_service=None,
    input_type=_GETADGROUPSIMULATIONREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_ad__group__simulation__pb2._ADGROUPSIMULATION,
    serialized_options=b'\202\323\344\223\0026\0224/v1/{resource_name=customers/*/adGroupSimulations/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_ADGROUPSIMULATIONSERVICE)

DESCRIPTOR.services_by_name['AdGroupSimulationService'] = _ADGROUPSIMULATIONSERVICE

# @@protoc_insertion_point(module_scope)