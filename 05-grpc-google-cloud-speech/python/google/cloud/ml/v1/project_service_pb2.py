# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/ml/v1/project_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/ml/v1/project_service.proto',
  package='google.cloud.ml.v1',
  syntax='proto3',
  serialized_options=b'\n\032com.google.cloud.ml.api.v1B\023ProjectServiceProtoP\001Z4google.golang.org/genproto/googleapis/cloud/ml/v1;ml',
  serialized_pb=b'\n(google/cloud/ml/v1/project_service.proto\x12\x12google.cloud.ml.v1\x1a\x1cgoogle/api/annotations.proto\" \n\x10GetConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"M\n\x11GetConfigResponse\x12\x17\n\x0fservice_account\x18\x01 \x01(\t\x12\x1f\n\x17service_account_project\x18\x02 \x01(\x03\x32\x9e\x01\n\x18ProjectManagementService\x12\x81\x01\n\tGetConfig\x12$.google.cloud.ml.v1.GetConfigRequest\x1a%.google.cloud.ml.v1.GetConfigResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=projects/*}:getConfigBi\n\x1a\x63om.google.cloud.ml.api.v1B\x13ProjectServiceProtoP\x01Z4google.golang.org/genproto/googleapis/cloud/ml/v1;mlb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETCONFIGREQUEST = _descriptor.Descriptor(
  name='GetConfigRequest',
  full_name='google.cloud.ml.v1.GetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.ml.v1.GetConfigRequest.name', index=0,
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
  serialized_start=94,
  serialized_end=126,
)


_GETCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetConfigResponse',
  full_name='google.cloud.ml.v1.GetConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account', full_name='google.cloud.ml.v1.GetConfigResponse.service_account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_project', full_name='google.cloud.ml.v1.GetConfigResponse.service_account_project', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=128,
  serialized_end=205,
)

DESCRIPTOR.message_types_by_name['GetConfigRequest'] = _GETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetConfigResponse'] = _GETCONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetConfigRequest = _reflection.GeneratedProtocolMessageType('GetConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGREQUEST,
  '__module__' : 'google.cloud.ml.v1.project_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.ml.v1.GetConfigRequest)
  })
_sym_db.RegisterMessage(GetConfigRequest)

GetConfigResponse = _reflection.GeneratedProtocolMessageType('GetConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGRESPONSE,
  '__module__' : 'google.cloud.ml.v1.project_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.ml.v1.GetConfigResponse)
  })
_sym_db.RegisterMessage(GetConfigResponse)


DESCRIPTOR._options = None

_PROJECTMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='ProjectManagementService',
  full_name='google.cloud.ml.v1.ProjectManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=208,
  serialized_end=366,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='google.cloud.ml.v1.ProjectManagementService.GetConfig',
    index=0,
    containing_service=None,
    input_type=_GETCONFIGREQUEST,
    output_type=_GETCONFIGRESPONSE,
    serialized_options=b'\202\323\344\223\002!\022\037/v1/{name=projects/*}:getConfig',
  ),
])
_sym_db.RegisterServiceDescriptor(_PROJECTMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['ProjectManagementService'] = _PROJECTMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
