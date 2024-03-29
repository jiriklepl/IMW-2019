# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/campaign_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import campaign_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/campaign_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\024CampaignServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\n7google/ads/googleads/v1/services/campaign_service.proto\x12 google.ads.googleads.v1.services\x1a\x30google/ads/googleads/v1/resources/campaign.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"+\n\x12GetCampaignRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xa6\x01\n\x16MutateCampaignsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12G\n\noperations\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v1.services.CampaignOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xe1\x01\n\x11\x43\x61mpaignOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12=\n\x06\x63reate\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v1.resources.CampaignH\x00\x12=\n\x06update\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v1.resources.CampaignH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x95\x01\n\x17MutateCampaignsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12G\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v1.services.MutateCampaignResult\"-\n\x14MutateCampaignResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xfd\x02\n\x0f\x43\x61mpaignService\x12\xa5\x01\n\x0bGetCampaign\x12\x34.google.ads.googleads.v1.services.GetCampaignRequest\x1a+.google.ads.googleads.v1.resources.Campaign\"3\x82\xd3\xe4\x93\x02-\x12+/v1/{resource_name=customers/*/campaigns/*}\x12\xc1\x01\n\x0fMutateCampaigns\x12\x38.google.ads.googleads.v1.services.MutateCampaignsRequest\x1a\x39.google.ads.googleads.v1.services.MutateCampaignsResponse\"9\x82\xd3\xe4\x93\x02\x33\"./v1/customers/{customer_id=*}/campaigns:mutate:\x01*B\xfb\x01\n$com.google.ads.googleads.v1.servicesB\x14\x43\x61mpaignServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCAMPAIGNREQUEST = _descriptor.Descriptor(
  name='GetCampaignRequest',
  full_name='google.ads.googleads.v1.services.GetCampaignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetCampaignRequest.resource_name', index=0,
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
  serialized_start=264,
  serialized_end=307,
)


_MUTATECAMPAIGNSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignsRequest',
  full_name='google.ads.googleads.v1.services.MutateCampaignsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateCampaignsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateCampaignsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v1.services.MutateCampaignsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v1.services.MutateCampaignsRequest.validate_only', index=3,
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
  serialized_start=310,
  serialized_end=476,
)


_CAMPAIGNOPERATION = _descriptor.Descriptor(
  name='CampaignOperation',
  full_name='google.ads.googleads.v1.services.CampaignOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v1.services.CampaignOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.CampaignOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v1.services.CampaignOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.CampaignOperation.remove', index=3,
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
      name='operation', full_name='google.ads.googleads.v1.services.CampaignOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=479,
  serialized_end=704,
)


_MUTATECAMPAIGNSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignsResponse',
  full_name='google.ads.googleads.v1.services.MutateCampaignsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v1.services.MutateCampaignsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateCampaignsResponse.results', index=1,
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
  serialized_start=707,
  serialized_end=856,
)


_MUTATECAMPAIGNRESULT = _descriptor.Descriptor(
  name='MutateCampaignResult',
  full_name='google.ads.googleads.v1.services.MutateCampaignResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateCampaignResult.resource_name', index=0,
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
  serialized_start=858,
  serialized_end=903,
)

_MUTATECAMPAIGNSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNOPERATION
_CAMPAIGNOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__pb2._CAMPAIGN
_CAMPAIGNOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__pb2._CAMPAIGN
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['create'])
_CAMPAIGNOPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['update'])
_CAMPAIGNOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['remove'])
_CAMPAIGNOPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECAMPAIGNSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNRESULT
DESCRIPTOR.message_types_by_name['GetCampaignRequest'] = _GETCAMPAIGNREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignsRequest'] = _MUTATECAMPAIGNSREQUEST
DESCRIPTOR.message_types_by_name['CampaignOperation'] = _CAMPAIGNOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignsResponse'] = _MUTATECAMPAIGNSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignResult'] = _MUTATECAMPAIGNRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignRequest = _reflection.GeneratedProtocolMessageType('GetCampaignRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.campaign_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetCampaignRequest)
  })
_sym_db.RegisterMessage(GetCampaignRequest)

MutateCampaignsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNSREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.campaign_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignsRequest)
  })
_sym_db.RegisterMessage(MutateCampaignsRequest)

CampaignOperation = _reflection.GeneratedProtocolMessageType('CampaignOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNOPERATION,
  '__module__' : 'google.ads.googleads.v1.services.campaign_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.CampaignOperation)
  })
_sym_db.RegisterMessage(CampaignOperation)

MutateCampaignsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNSRESPONSE,
  '__module__' : 'google.ads.googleads.v1.services.campaign_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignsResponse)
  })
_sym_db.RegisterMessage(MutateCampaignsResponse)

MutateCampaignResult = _reflection.GeneratedProtocolMessageType('MutateCampaignResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNRESULT,
  '__module__' : 'google.ads.googleads.v1.services.campaign_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignResult)
  })
_sym_db.RegisterMessage(MutateCampaignResult)


DESCRIPTOR._options = None

_CAMPAIGNSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignService',
  full_name='google.ads.googleads.v1.services.CampaignService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=906,
  serialized_end=1287,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaign',
    full_name='google.ads.googleads.v1.services.CampaignService.GetCampaign',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__pb2._CAMPAIGN,
    serialized_options=b'\202\323\344\223\002-\022+/v1/{resource_name=customers/*/campaigns/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaigns',
    full_name='google.ads.googleads.v1.services.CampaignService.MutateCampaigns',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNSREQUEST,
    output_type=_MUTATECAMPAIGNSRESPONSE,
    serialized_options=b'\202\323\344\223\0023\"./v1/customers/{customer_id=*}/campaigns:mutate:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNSERVICE)

DESCRIPTOR.services_by_name['CampaignService'] = _CAMPAIGNSERVICE

# @@protoc_insertion_point(module_scope)
