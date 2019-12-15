# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/clouderrorreporting/v1beta1/error_group_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.devtools.clouderrorreporting.v1beta1 import common_pb2 as google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/clouderrorreporting/v1beta1/error_group_service.proto',
  package='google.devtools.clouderrorreporting.v1beta1',
  syntax='proto3',
  serialized_options=b'\n/com.google.devtools.clouderrorreporting.v1beta1B\026ErrorGroupServiceProtoP\001Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\370\001\001\252\002#Google.Cloud.ErrorReporting.V1Beta1\312\002#Google\\Cloud\\ErrorReporting\\V1beta1',
  serialized_pb=b'\nEgoogle/devtools/clouderrorreporting/v1beta1/error_group_service.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x38google/devtools/clouderrorreporting/v1beta1/common.proto\"\\\n\x0fGetGroupRequest\x12I\n\ngroup_name\x18\x01 \x01(\tB5\xe0\x41\x02\xfa\x41/\n-clouderrorreporting.googleapis.com/ErrorGroup\"a\n\x12UpdateGroupRequest\x12K\n\x05group\x18\x01 \x01(\x0b\x32\x37.google.devtools.clouderrorreporting.v1beta1.ErrorGroupB\x03\xe0\x41\x02\x32\xfb\x03\n\x11\x45rrorGroupService\x12\xc1\x01\n\x08GetGroup\x12<.google.devtools.clouderrorreporting.v1beta1.GetGroupRequest\x1a\x37.google.devtools.clouderrorreporting.v1beta1.ErrorGroup\">\x82\xd3\xe4\x93\x02+\x12)/v1beta1/{group_name=projects/*/groups/*}\xda\x41\ngroup_name\x12\xc9\x01\n\x0bUpdateGroup\x12?.google.devtools.clouderrorreporting.v1beta1.UpdateGroupRequest\x1a\x37.google.devtools.clouderrorreporting.v1beta1.ErrorGroup\"@\x82\xd3\xe4\x93\x02\x32\x1a)/v1beta1/{group.name=projects/*/groups/*}:\x05group\xda\x41\x05group\x1aV\xca\x41\"clouderrorreporting.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xfa\x01\n/com.google.devtools.clouderrorreporting.v1beta1B\x16\x45rrorGroupServiceProtoP\x01Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2.DESCRIPTOR,])




_GETGROUPREQUEST = _descriptor.Descriptor(
  name='GetGroupRequest',
  full_name='google.devtools.clouderrorreporting.v1beta1.GetGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_name', full_name='google.devtools.clouderrorreporting.v1beta1.GetGroupRequest.group_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A/\n-clouderrorreporting.googleapis.com/ErrorGroup', file=DESCRIPTOR),
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
  serialized_start=291,
  serialized_end=383,
)


_UPDATEGROUPREQUEST = _descriptor.Descriptor(
  name='UpdateGroupRequest',
  full_name='google.devtools.clouderrorreporting.v1beta1.UpdateGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group', full_name='google.devtools.clouderrorreporting.v1beta1.UpdateGroupRequest.group', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
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
  serialized_start=385,
  serialized_end=482,
)

_UPDATEGROUPREQUEST.fields_by_name['group'].message_type = google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2._ERRORGROUP
DESCRIPTOR.message_types_by_name['GetGroupRequest'] = _GETGROUPREQUEST
DESCRIPTOR.message_types_by_name['UpdateGroupRequest'] = _UPDATEGROUPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGroupRequest = _reflection.GeneratedProtocolMessageType('GetGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPREQUEST,
  '__module__' : 'google.devtools.clouderrorreporting.v1beta1.error_group_service_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.GetGroupRequest)
  })
_sym_db.RegisterMessage(GetGroupRequest)

UpdateGroupRequest = _reflection.GeneratedProtocolMessageType('UpdateGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPREQUEST,
  '__module__' : 'google.devtools.clouderrorreporting.v1beta1.error_group_service_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.UpdateGroupRequest)
  })
_sym_db.RegisterMessage(UpdateGroupRequest)


DESCRIPTOR._options = None
_GETGROUPREQUEST.fields_by_name['group_name']._options = None
_UPDATEGROUPREQUEST.fields_by_name['group']._options = None

_ERRORGROUPSERVICE = _descriptor.ServiceDescriptor(
  name='ErrorGroupService',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroupService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\"clouderrorreporting.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  serialized_start=485,
  serialized_end=992,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGroup',
    full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.GetGroup',
    index=0,
    containing_service=None,
    input_type=_GETGROUPREQUEST,
    output_type=google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2._ERRORGROUP,
    serialized_options=b'\202\323\344\223\002+\022)/v1beta1/{group_name=projects/*/groups/*}\332A\ngroup_name',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGroup',
    full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.UpdateGroup',
    index=1,
    containing_service=None,
    input_type=_UPDATEGROUPREQUEST,
    output_type=google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2._ERRORGROUP,
    serialized_options=b'\202\323\344\223\0022\032)/v1beta1/{group.name=projects/*/groups/*}:\005group\332A\005group',
  ),
])
_sym_db.RegisterServiceDescriptor(_ERRORGROUPSERVICE)

DESCRIPTOR.services_by_name['ErrorGroupService'] = _ERRORGROUPSERVICE

# @@protoc_insertion_point(module_scope)
