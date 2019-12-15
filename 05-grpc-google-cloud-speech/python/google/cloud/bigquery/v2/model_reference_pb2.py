# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/v2/model_reference.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/bigquery/v2/model_reference.proto',
  package='google.cloud.bigquery.v2',
  syntax='proto3',
  serialized_options=b'\n\034com.google.cloud.bigquery.v2B\023ModelReferenceProtoZ@google.golang.org/genproto/googleapis/cloud/bigquery/v2;bigquery',
  serialized_pb=b'\n.google/cloud/bigquery/v2/model_reference.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/api/annotations.proto\"Y\n\x0eModelReference\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\x08model_id\x18\x03 \x01(\tB\x03\xe0\x41\x02\x42u\n\x1c\x63om.google.cloud.bigquery.v2B\x13ModelReferenceProtoZ@google.golang.org/genproto/googleapis/cloud/bigquery/v2;bigqueryb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MODELREFERENCE = _descriptor.Descriptor(
  name='ModelReference',
  full_name='google.cloud.bigquery.v2.ModelReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.cloud.bigquery.v2.ModelReference.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.cloud.bigquery.v2.ModelReference.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='google.cloud.bigquery.v2.ModelReference.model_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=139,
  serialized_end=228,
)

DESCRIPTOR.message_types_by_name['ModelReference'] = _MODELREFERENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelReference = _reflection.GeneratedProtocolMessageType('ModelReference', (_message.Message,), {
  'DESCRIPTOR' : _MODELREFERENCE,
  '__module__' : 'google.cloud.bigquery.v2.model_reference_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.v2.ModelReference)
  })
_sym_db.RegisterMessage(ModelReference)


DESCRIPTOR._options = None
_MODELREFERENCE.fields_by_name['project_id']._options = None
_MODELREFERENCE.fields_by_name['dataset_id']._options = None
_MODELREFERENCE.fields_by_name['model_id']._options = None
# @@protoc_insertion_point(module_scope)
