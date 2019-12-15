# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/ad_group_criterion_label_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.resources import ad_group_criterion_label_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__criterion__label__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/ad_group_criterion_label_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB!AdGroupCriterionLabelServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\nGgoogle/ads/googleads/v2/services/ad_group_criterion_label_service.proto\x12 google.ads.googleads.v2.services\x1a@google/ads/googleads/v2/resources/ad_group_criterion_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto\"8\n\x1fGetAdGroupCriterionLabelRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xc0\x01\n#MutateAdGroupCriterionLabelsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12T\n\noperations\x18\x02 \x03(\x0b\x32@.google.ads.googleads.v2.services.AdGroupCriterionLabelOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x8b\x01\n\x1e\x41\x64GroupCriterionLabelOperation\x12J\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x38.google.ads.googleads.v2.resources.AdGroupCriterionLabelH\x00\x12\x10\n\x06remove\x18\x02 \x01(\tH\x00\x42\x0b\n\toperation\"\xaf\x01\n$MutateAdGroupCriterionLabelsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12T\n\x07results\x18\x02 \x03(\x0b\x32\x43.google.ads.googleads.v2.services.MutateAdGroupCriterionLabelResult\":\n!MutateAdGroupCriterionLabelResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x8f\x04\n\x1c\x41\x64GroupCriterionLabelService\x12\xd9\x01\n\x18GetAdGroupCriterionLabel\x12\x41.google.ads.googleads.v2.services.GetAdGroupCriterionLabelRequest\x1a\x38.google.ads.googleads.v2.resources.AdGroupCriterionLabel\"@\x82\xd3\xe4\x93\x02:\x12\x38/v2/{resource_name=customers/*/adGroupCriterionLabels/*}\x12\xf5\x01\n\x1cMutateAdGroupCriterionLabels\x12\x45.google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest\x1a\x46.google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsResponse\"F\x82\xd3\xe4\x93\x02@\";/v2/customers/{customer_id=*}/adGroupCriterionLabels:mutate:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x88\x02\n$com.google.ads.googleads.v2.servicesB!AdGroupCriterionLabelServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__criterion__label__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GETADGROUPCRITERIONLABELREQUEST = _descriptor.Descriptor(
  name='GetAdGroupCriterionLabelRequest',
  full_name='google.ads.googleads.v2.services.GetAdGroupCriterionLabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetAdGroupCriterionLabelRequest.resource_name', index=0,
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
  serialized_start=255,
  serialized_end=311,
)


_MUTATEADGROUPCRITERIONLABELSREQUEST = _descriptor.Descriptor(
  name='MutateAdGroupCriterionLabelsRequest',
  full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest.validate_only', index=3,
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
  serialized_start=314,
  serialized_end=506,
)


_ADGROUPCRITERIONLABELOPERATION = _descriptor.Descriptor(
  name='AdGroupCriterionLabelOperation',
  full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelOperation.remove', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
      name='operation', full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=509,
  serialized_end=648,
)


_MUTATEADGROUPCRITERIONLABELSRESPONSE = _descriptor.Descriptor(
  name='MutateAdGroupCriterionLabelsResponse',
  full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsResponse.results', index=1,
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
  serialized_start=651,
  serialized_end=826,
)


_MUTATEADGROUPCRITERIONLABELRESULT = _descriptor.Descriptor(
  name='MutateAdGroupCriterionLabelResult',
  full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.MutateAdGroupCriterionLabelResult.resource_name', index=0,
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
  serialized_start=828,
  serialized_end=886,
)

_MUTATEADGROUPCRITERIONLABELSREQUEST.fields_by_name['operations'].message_type = _ADGROUPCRITERIONLABELOPERATION
_ADGROUPCRITERIONLABELOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__criterion__label__pb2._ADGROUPCRITERIONLABEL
_ADGROUPCRITERIONLABELOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPCRITERIONLABELOPERATION.fields_by_name['create'])
_ADGROUPCRITERIONLABELOPERATION.fields_by_name['create'].containing_oneof = _ADGROUPCRITERIONLABELOPERATION.oneofs_by_name['operation']
_ADGROUPCRITERIONLABELOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPCRITERIONLABELOPERATION.fields_by_name['remove'])
_ADGROUPCRITERIONLABELOPERATION.fields_by_name['remove'].containing_oneof = _ADGROUPCRITERIONLABELOPERATION.oneofs_by_name['operation']
_MUTATEADGROUPCRITERIONLABELSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEADGROUPCRITERIONLABELSRESPONSE.fields_by_name['results'].message_type = _MUTATEADGROUPCRITERIONLABELRESULT
DESCRIPTOR.message_types_by_name['GetAdGroupCriterionLabelRequest'] = _GETADGROUPCRITERIONLABELREQUEST
DESCRIPTOR.message_types_by_name['MutateAdGroupCriterionLabelsRequest'] = _MUTATEADGROUPCRITERIONLABELSREQUEST
DESCRIPTOR.message_types_by_name['AdGroupCriterionLabelOperation'] = _ADGROUPCRITERIONLABELOPERATION
DESCRIPTOR.message_types_by_name['MutateAdGroupCriterionLabelsResponse'] = _MUTATEADGROUPCRITERIONLABELSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAdGroupCriterionLabelResult'] = _MUTATEADGROUPCRITERIONLABELRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdGroupCriterionLabelRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupCriterionLabelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADGROUPCRITERIONLABELREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.ad_group_criterion_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetAdGroupCriterionLabelRequest)
  })
_sym_db.RegisterMessage(GetAdGroupCriterionLabelRequest)

MutateAdGroupCriterionLabelsRequest = _reflection.GeneratedProtocolMessageType('MutateAdGroupCriterionLabelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADGROUPCRITERIONLABELSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.ad_group_criterion_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsRequest)
  })
_sym_db.RegisterMessage(MutateAdGroupCriterionLabelsRequest)

AdGroupCriterionLabelOperation = _reflection.GeneratedProtocolMessageType('AdGroupCriterionLabelOperation', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPCRITERIONLABELOPERATION,
  '__module__' : 'google.ads.googleads.v2.services.ad_group_criterion_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.AdGroupCriterionLabelOperation)
  })
_sym_db.RegisterMessage(AdGroupCriterionLabelOperation)

MutateAdGroupCriterionLabelsResponse = _reflection.GeneratedProtocolMessageType('MutateAdGroupCriterionLabelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADGROUPCRITERIONLABELSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.ad_group_criterion_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateAdGroupCriterionLabelsResponse)
  })
_sym_db.RegisterMessage(MutateAdGroupCriterionLabelsResponse)

MutateAdGroupCriterionLabelResult = _reflection.GeneratedProtocolMessageType('MutateAdGroupCriterionLabelResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADGROUPCRITERIONLABELRESULT,
  '__module__' : 'google.ads.googleads.v2.services.ad_group_criterion_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateAdGroupCriterionLabelResult)
  })
_sym_db.RegisterMessage(MutateAdGroupCriterionLabelResult)


DESCRIPTOR._options = None

_ADGROUPCRITERIONLABELSERVICE = _descriptor.ServiceDescriptor(
  name='AdGroupCriterionLabelService',
  full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=889,
  serialized_end=1416,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdGroupCriterionLabel',
    full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelService.GetAdGroupCriterionLabel',
    index=0,
    containing_service=None,
    input_type=_GETADGROUPCRITERIONLABELREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_ad__group__criterion__label__pb2._ADGROUPCRITERIONLABEL,
    serialized_options=b'\202\323\344\223\002:\0228/v2/{resource_name=customers/*/adGroupCriterionLabels/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateAdGroupCriterionLabels',
    full_name='google.ads.googleads.v2.services.AdGroupCriterionLabelService.MutateAdGroupCriterionLabels',
    index=1,
    containing_service=None,
    input_type=_MUTATEADGROUPCRITERIONLABELSREQUEST,
    output_type=_MUTATEADGROUPCRITERIONLABELSRESPONSE,
    serialized_options=b'\202\323\344\223\002@\";/v2/customers/{customer_id=*}/adGroupCriterionLabels:mutate:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_ADGROUPCRITERIONLABELSERVICE)

DESCRIPTOR.services_by_name['AdGroupCriterionLabelService'] = _ADGROUPCRITERIONLABELSERVICE

# @@protoc_insertion_point(module_scope)