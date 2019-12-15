# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/campaign_bid_modifier_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import campaign_bid_modifier_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__bid__modifier__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/campaign_bid_modifier_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\037CampaignBidModifierServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\nDgoogle/ads/googleads/v1/services/campaign_bid_modifier_service.proto\x12 google.ads.googleads.v1.services\x1a=google/ads/googleads/v1/resources/campaign_bid_modifier.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"6\n\x1dGetCampaignBidModifierRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xbc\x01\n!MutateCampaignBidModifiersRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12R\n\noperations\x18\x02 \x03(\x0b\x32>.google.ads.googleads.v1.services.CampaignBidModifierOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x82\x02\n\x1c\x43\x61mpaignBidModifierOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12H\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x36.google.ads.googleads.v1.resources.CampaignBidModifierH\x00\x12H\n\x06update\x18\x02 \x01(\x0b\x32\x36.google.ads.googleads.v1.resources.CampaignBidModifierH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\xab\x01\n\"MutateCampaignBidModifiersResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12R\n\x07results\x18\x02 \x03(\x0b\x32\x41.google.ads.googleads.v1.services.MutateCampaignBidModifierResult\"8\n\x1fMutateCampaignBidModifierResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xe0\x03\n\x1a\x43\x61mpaignBidModifierService\x12\xd1\x01\n\x16GetCampaignBidModifier\x12?.google.ads.googleads.v1.services.GetCampaignBidModifierRequest\x1a\x36.google.ads.googleads.v1.resources.CampaignBidModifier\">\x82\xd3\xe4\x93\x02\x38\x12\x36/v1/{resource_name=customers/*/campaignBidModifiers/*}\x12\xed\x01\n\x1aMutateCampaignBidModifiers\x12\x43.google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest\x1a\x44.google.ads.googleads.v1.services.MutateCampaignBidModifiersResponse\"D\x82\xd3\xe4\x93\x02>\"9/v1/customers/{customer_id=*}/campaignBidModifiers:mutate:\x01*B\x86\x02\n$com.google.ads.googleads.v1.servicesB\x1f\x43\x61mpaignBidModifierServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__bid__modifier__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCAMPAIGNBIDMODIFIERREQUEST = _descriptor.Descriptor(
  name='GetCampaignBidModifierRequest',
  full_name='google.ads.googleads.v1.services.GetCampaignBidModifierRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetCampaignBidModifierRequest.resource_name', index=0,
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
  serialized_start=290,
  serialized_end=344,
)


_MUTATECAMPAIGNBIDMODIFIERSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignBidModifiersRequest',
  full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest.validate_only', index=3,
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
  serialized_start=347,
  serialized_end=535,
)


_CAMPAIGNBIDMODIFIEROPERATION = _descriptor.Descriptor(
  name='CampaignBidModifierOperation',
  full_name='google.ads.googleads.v1.services.CampaignBidModifierOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v1.services.CampaignBidModifierOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.CampaignBidModifierOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v1.services.CampaignBidModifierOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.CampaignBidModifierOperation.remove', index=3,
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
      name='operation', full_name='google.ads.googleads.v1.services.CampaignBidModifierOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=538,
  serialized_end=796,
)


_MUTATECAMPAIGNBIDMODIFIERSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignBidModifiersResponse',
  full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifiersResponse.results', index=1,
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
  serialized_start=799,
  serialized_end=970,
)


_MUTATECAMPAIGNBIDMODIFIERRESULT = _descriptor.Descriptor(
  name='MutateCampaignBidModifierResult',
  full_name='google.ads.googleads.v1.services.MutateCampaignBidModifierResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateCampaignBidModifierResult.resource_name', index=0,
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
  serialized_start=972,
  serialized_end=1028,
)

_MUTATECAMPAIGNBIDMODIFIERSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNBIDMODIFIEROPERATION
_CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__bid__modifier__pb2._CAMPAIGNBIDMODIFIER
_CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__bid__modifier__pb2._CAMPAIGNBIDMODIFIER
_CAMPAIGNBIDMODIFIEROPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['create'])
_CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNBIDMODIFIEROPERATION.oneofs_by_name['operation']
_CAMPAIGNBIDMODIFIEROPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['update'])
_CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNBIDMODIFIEROPERATION.oneofs_by_name['operation']
_CAMPAIGNBIDMODIFIEROPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['remove'])
_CAMPAIGNBIDMODIFIEROPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNBIDMODIFIEROPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNBIDMODIFIERSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECAMPAIGNBIDMODIFIERSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNBIDMODIFIERRESULT
DESCRIPTOR.message_types_by_name['GetCampaignBidModifierRequest'] = _GETCAMPAIGNBIDMODIFIERREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignBidModifiersRequest'] = _MUTATECAMPAIGNBIDMODIFIERSREQUEST
DESCRIPTOR.message_types_by_name['CampaignBidModifierOperation'] = _CAMPAIGNBIDMODIFIEROPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignBidModifiersResponse'] = _MUTATECAMPAIGNBIDMODIFIERSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignBidModifierResult'] = _MUTATECAMPAIGNBIDMODIFIERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignBidModifierRequest = _reflection.GeneratedProtocolMessageType('GetCampaignBidModifierRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNBIDMODIFIERREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetCampaignBidModifierRequest)
  })
_sym_db.RegisterMessage(GetCampaignBidModifierRequest)

MutateCampaignBidModifiersRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignBidModifiersRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNBIDMODIFIERSREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignBidModifiersRequest)
  })
_sym_db.RegisterMessage(MutateCampaignBidModifiersRequest)

CampaignBidModifierOperation = _reflection.GeneratedProtocolMessageType('CampaignBidModifierOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNBIDMODIFIEROPERATION,
  '__module__' : 'google.ads.googleads.v1.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.CampaignBidModifierOperation)
  })
_sym_db.RegisterMessage(CampaignBidModifierOperation)

MutateCampaignBidModifiersResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignBidModifiersResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNBIDMODIFIERSRESPONSE,
  '__module__' : 'google.ads.googleads.v1.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignBidModifiersResponse)
  })
_sym_db.RegisterMessage(MutateCampaignBidModifiersResponse)

MutateCampaignBidModifierResult = _reflection.GeneratedProtocolMessageType('MutateCampaignBidModifierResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNBIDMODIFIERRESULT,
  '__module__' : 'google.ads.googleads.v1.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignBidModifierResult)
  })
_sym_db.RegisterMessage(MutateCampaignBidModifierResult)


DESCRIPTOR._options = None

_CAMPAIGNBIDMODIFIERSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignBidModifierService',
  full_name='google.ads.googleads.v1.services.CampaignBidModifierService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1031,
  serialized_end=1511,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaignBidModifier',
    full_name='google.ads.googleads.v1.services.CampaignBidModifierService.GetCampaignBidModifier',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNBIDMODIFIERREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_campaign__bid__modifier__pb2._CAMPAIGNBIDMODIFIER,
    serialized_options=b'\202\323\344\223\0028\0226/v1/{resource_name=customers/*/campaignBidModifiers/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaignBidModifiers',
    full_name='google.ads.googleads.v1.services.CampaignBidModifierService.MutateCampaignBidModifiers',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNBIDMODIFIERSREQUEST,
    output_type=_MUTATECAMPAIGNBIDMODIFIERSRESPONSE,
    serialized_options=b'\202\323\344\223\002>\"9/v1/customers/{customer_id=*}/campaignBidModifiers:mutate:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNBIDMODIFIERSERVICE)

DESCRIPTOR.services_by_name['CampaignBidModifierService'] = _CAMPAIGNBIDMODIFIERSERVICE

# @@protoc_insertion_point(module_scope)
