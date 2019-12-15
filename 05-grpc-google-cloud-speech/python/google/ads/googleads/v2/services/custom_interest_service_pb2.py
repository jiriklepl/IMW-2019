# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/custom_interest_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.resources import custom_interest_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_custom__interest__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/custom_interest_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB\032CustomInterestServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\n>google/ads/googleads/v2/services/custom_interest_service.proto\x12 google.ads.googleads.v2.services\x1a\x37google/ads/googleads/v2/resources/custom_interest.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto\"1\n\x18GetCustomInterestRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x99\x01\n\x1cMutateCustomInterestsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12M\n\noperations\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v2.services.CustomInterestOperation\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xe1\x01\n\x17\x43ustomInterestOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x43\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x31.google.ads.googleads.v2.resources.CustomInterestH\x00\x12\x43\n\x06update\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v2.resources.CustomInterestH\x00\x42\x0b\n\toperation\"n\n\x1dMutateCustomInterestsResponse\x12M\n\x07results\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v2.services.MutateCustomInterestResult\"3\n\x1aMutateCustomInterestResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xd0\x03\n\x15\x43ustomInterestService\x12\xbd\x01\n\x11GetCustomInterest\x12:.google.ads.googleads.v2.services.GetCustomInterestRequest\x1a\x31.google.ads.googleads.v2.resources.CustomInterest\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{resource_name=customers/*/customInterests/*}\x12\xd9\x01\n\x15MutateCustomInterests\x12>.google.ads.googleads.v2.services.MutateCustomInterestsRequest\x1a?.google.ads.googleads.v2.services.MutateCustomInterestsResponse\"?\x82\xd3\xe4\x93\x02\x39\"4/v2/customers/{customer_id=*}/customInterests:mutate:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x81\x02\n$com.google.ads.googleads.v2.servicesB\x1a\x43ustomInterestServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_custom__interest__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GETCUSTOMINTERESTREQUEST = _descriptor.Descriptor(
  name='GetCustomInterestRequest',
  full_name='google.ads.googleads.v2.services.GetCustomInterestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetCustomInterestRequest.resource_name', index=0,
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
  serialized_start=246,
  serialized_end=295,
)


_MUTATECUSTOMINTERESTSREQUEST = _descriptor.Descriptor(
  name='MutateCustomInterestsRequest',
  full_name='google.ads.googleads.v2.services.MutateCustomInterestsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.MutateCustomInterestsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v2.services.MutateCustomInterestsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v2.services.MutateCustomInterestsRequest.validate_only', index=2,
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
  serialized_start=298,
  serialized_end=451,
)


_CUSTOMINTERESTOPERATION = _descriptor.Descriptor(
  name='CustomInterestOperation',
  full_name='google.ads.googleads.v2.services.CustomInterestOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v2.services.CustomInterestOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v2.services.CustomInterestOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v2.services.CustomInterestOperation.update', index=2,
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v2.services.CustomInterestOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=454,
  serialized_end=679,
)


_MUTATECUSTOMINTERESTSRESPONSE = _descriptor.Descriptor(
  name='MutateCustomInterestsResponse',
  full_name='google.ads.googleads.v2.services.MutateCustomInterestsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.MutateCustomInterestsResponse.results', index=0,
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
  serialized_start=681,
  serialized_end=791,
)


_MUTATECUSTOMINTERESTRESULT = _descriptor.Descriptor(
  name='MutateCustomInterestResult',
  full_name='google.ads.googleads.v2.services.MutateCustomInterestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.MutateCustomInterestResult.resource_name', index=0,
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
  serialized_start=793,
  serialized_end=844,
)

_MUTATECUSTOMINTERESTSREQUEST.fields_by_name['operations'].message_type = _CUSTOMINTERESTOPERATION
_CUSTOMINTERESTOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CUSTOMINTERESTOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_custom__interest__pb2._CUSTOMINTEREST
_CUSTOMINTERESTOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_custom__interest__pb2._CUSTOMINTEREST
_CUSTOMINTERESTOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMINTERESTOPERATION.fields_by_name['create'])
_CUSTOMINTERESTOPERATION.fields_by_name['create'].containing_oneof = _CUSTOMINTERESTOPERATION.oneofs_by_name['operation']
_CUSTOMINTERESTOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMINTERESTOPERATION.fields_by_name['update'])
_CUSTOMINTERESTOPERATION.fields_by_name['update'].containing_oneof = _CUSTOMINTERESTOPERATION.oneofs_by_name['operation']
_MUTATECUSTOMINTERESTSRESPONSE.fields_by_name['results'].message_type = _MUTATECUSTOMINTERESTRESULT
DESCRIPTOR.message_types_by_name['GetCustomInterestRequest'] = _GETCUSTOMINTERESTREQUEST
DESCRIPTOR.message_types_by_name['MutateCustomInterestsRequest'] = _MUTATECUSTOMINTERESTSREQUEST
DESCRIPTOR.message_types_by_name['CustomInterestOperation'] = _CUSTOMINTERESTOPERATION
DESCRIPTOR.message_types_by_name['MutateCustomInterestsResponse'] = _MUTATECUSTOMINTERESTSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomInterestResult'] = _MUTATECUSTOMINTERESTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomInterestRequest = _reflection.GeneratedProtocolMessageType('GetCustomInterestRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMINTERESTREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.custom_interest_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetCustomInterestRequest)
  })
_sym_db.RegisterMessage(GetCustomInterestRequest)

MutateCustomInterestsRequest = _reflection.GeneratedProtocolMessageType('MutateCustomInterestsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMINTERESTSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.custom_interest_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateCustomInterestsRequest)
  })
_sym_db.RegisterMessage(MutateCustomInterestsRequest)

CustomInterestOperation = _reflection.GeneratedProtocolMessageType('CustomInterestOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMINTERESTOPERATION,
  '__module__' : 'google.ads.googleads.v2.services.custom_interest_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.CustomInterestOperation)
  })
_sym_db.RegisterMessage(CustomInterestOperation)

MutateCustomInterestsResponse = _reflection.GeneratedProtocolMessageType('MutateCustomInterestsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMINTERESTSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.custom_interest_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateCustomInterestsResponse)
  })
_sym_db.RegisterMessage(MutateCustomInterestsResponse)

MutateCustomInterestResult = _reflection.GeneratedProtocolMessageType('MutateCustomInterestResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMINTERESTRESULT,
  '__module__' : 'google.ads.googleads.v2.services.custom_interest_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateCustomInterestResult)
  })
_sym_db.RegisterMessage(MutateCustomInterestResult)


DESCRIPTOR._options = None

_CUSTOMINTERESTSERVICE = _descriptor.ServiceDescriptor(
  name='CustomInterestService',
  full_name='google.ads.googleads.v2.services.CustomInterestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=847,
  serialized_end=1311,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomInterest',
    full_name='google.ads.googleads.v2.services.CustomInterestService.GetCustomInterest',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMINTERESTREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_custom__interest__pb2._CUSTOMINTEREST,
    serialized_options=b'\202\323\344\223\0023\0221/v2/{resource_name=customers/*/customInterests/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateCustomInterests',
    full_name='google.ads.googleads.v2.services.CustomInterestService.MutateCustomInterests',
    index=1,
    containing_service=None,
    input_type=_MUTATECUSTOMINTERESTSREQUEST,
    output_type=_MUTATECUSTOMINTERESTSRESPONSE,
    serialized_options=b'\202\323\344\223\0029\"4/v2/customers/{customer_id=*}/customInterests:mutate:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMINTERESTSERVICE)

DESCRIPTOR.services_by_name['CustomInterestService'] = _CUSTOMINTERESTSERVICE

# @@protoc_insertion_point(module_scope)
