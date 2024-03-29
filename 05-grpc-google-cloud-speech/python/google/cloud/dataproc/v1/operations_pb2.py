# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataproc/v1/operations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dataproc/v1/operations.proto',
  package='google.cloud.dataproc.v1',
  syntax='proto3',
  serialized_options=b'\n\034com.google.cloud.dataproc.v1B\017OperationsProtoP\001Z@google.golang.org/genproto/googleapis/cloud/dataproc/v1;dataproc',
  serialized_pb=b'\n)google/cloud/dataproc/v1/operations.proto\x12\x18google.cloud.dataproc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x89\x02\n\x16\x43lusterOperationStatus\x12J\n\x05state\x18\x01 \x01(\x0e\x32\x36.google.cloud.dataproc.v1.ClusterOperationStatus.StateB\x03\xe0\x41\x03\x12\x18\n\x0binner_state\x18\x02 \x01(\tB\x03\xe0\x41\x03\x12\x14\n\x07\x64\x65tails\x18\x03 \x01(\tB\x03\xe0\x41\x03\x12\x39\n\x10state_start_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\"8\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\"\xb8\x03\n\x18\x43lusterOperationMetadata\x12\x19\n\x0c\x63luster_name\x18\x07 \x01(\tB\x03\xe0\x41\x03\x12\x19\n\x0c\x63luster_uuid\x18\x08 \x01(\tB\x03\xe0\x41\x03\x12\x45\n\x06status\x18\t \x01(\x0b\x32\x30.google.cloud.dataproc.v1.ClusterOperationStatusB\x03\xe0\x41\x03\x12M\n\x0estatus_history\x18\n \x03(\x0b\x32\x30.google.cloud.dataproc.v1.ClusterOperationStatusB\x03\xe0\x41\x03\x12\x1b\n\x0eoperation_type\x18\x0b \x01(\tB\x03\xe0\x41\x03\x12\x18\n\x0b\x64\x65scription\x18\x0c \x01(\tB\x03\xe0\x41\x03\x12S\n\x06labels\x18\r \x03(\x0b\x32>.google.cloud.dataproc.v1.ClusterOperationMetadata.LabelsEntryB\x03\xe0\x41\x03\x12\x15\n\x08warnings\x18\x0e \x03(\tB\x03\xe0\x41\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42s\n\x1c\x63om.google.cloud.dataproc.v1B\x0fOperationsProtoP\x01Z@google.golang.org/genproto/googleapis/cloud/dataproc/v1;dataprocb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CLUSTEROPERATIONSTATUS_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.dataproc.v1.ClusterOperationStatus.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=377,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_CLUSTEROPERATIONSTATUS_STATE)


_CLUSTEROPERATIONSTATUS = _descriptor.Descriptor(
  name='ClusterOperationStatus',
  full_name='google.cloud.dataproc.v1.ClusterOperationStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.dataproc.v1.ClusterOperationStatus.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inner_state', full_name='google.cloud.dataproc.v1.ClusterOperationStatus.inner_state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='google.cloud.dataproc.v1.ClusterOperationStatus.details', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_start_time', full_name='google.cloud.dataproc.v1.ClusterOperationStatus.state_start_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLUSTEROPERATIONSTATUS_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=433,
)


_CLUSTEROPERATIONMETADATA_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=831,
  serialized_end=876,
)

_CLUSTEROPERATIONMETADATA = _descriptor.Descriptor(
  name='ClusterOperationMetadata',
  full_name='google.cloud.dataproc.v1.ClusterOperationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_name', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.cluster_name', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_uuid', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.cluster_uuid', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.status', index=2,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_history', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.status_history', index=3,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation_type', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.operation_type', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.description', index=5,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.labels', index=6,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warnings', full_name='google.cloud.dataproc.v1.ClusterOperationMetadata.warnings', index=7,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTEROPERATIONMETADATA_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=876,
)

_CLUSTEROPERATIONSTATUS.fields_by_name['state'].enum_type = _CLUSTEROPERATIONSTATUS_STATE
_CLUSTEROPERATIONSTATUS.fields_by_name['state_start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLUSTEROPERATIONSTATUS_STATE.containing_type = _CLUSTEROPERATIONSTATUS
_CLUSTEROPERATIONMETADATA_LABELSENTRY.containing_type = _CLUSTEROPERATIONMETADATA
_CLUSTEROPERATIONMETADATA.fields_by_name['status'].message_type = _CLUSTEROPERATIONSTATUS
_CLUSTEROPERATIONMETADATA.fields_by_name['status_history'].message_type = _CLUSTEROPERATIONSTATUS
_CLUSTEROPERATIONMETADATA.fields_by_name['labels'].message_type = _CLUSTEROPERATIONMETADATA_LABELSENTRY
DESCRIPTOR.message_types_by_name['ClusterOperationStatus'] = _CLUSTEROPERATIONSTATUS
DESCRIPTOR.message_types_by_name['ClusterOperationMetadata'] = _CLUSTEROPERATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClusterOperationStatus = _reflection.GeneratedProtocolMessageType('ClusterOperationStatus', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTEROPERATIONSTATUS,
  '__module__' : 'google.cloud.dataproc.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.ClusterOperationStatus)
  })
_sym_db.RegisterMessage(ClusterOperationStatus)

ClusterOperationMetadata = _reflection.GeneratedProtocolMessageType('ClusterOperationMetadata', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTEROPERATIONMETADATA_LABELSENTRY,
    '__module__' : 'google.cloud.dataproc.v1.operations_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.ClusterOperationMetadata.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLUSTEROPERATIONMETADATA,
  '__module__' : 'google.cloud.dataproc.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.ClusterOperationMetadata)
  })
_sym_db.RegisterMessage(ClusterOperationMetadata)
_sym_db.RegisterMessage(ClusterOperationMetadata.LabelsEntry)


DESCRIPTOR._options = None
_CLUSTEROPERATIONSTATUS.fields_by_name['state']._options = None
_CLUSTEROPERATIONSTATUS.fields_by_name['inner_state']._options = None
_CLUSTEROPERATIONSTATUS.fields_by_name['details']._options = None
_CLUSTEROPERATIONSTATUS.fields_by_name['state_start_time']._options = None
_CLUSTEROPERATIONMETADATA_LABELSENTRY._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['cluster_name']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['cluster_uuid']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['status']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['status_history']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['operation_type']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['description']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['labels']._options = None
_CLUSTEROPERATIONMETADATA.fields_by_name['warnings']._options = None
# @@protoc_insertion_point(module_scope)
