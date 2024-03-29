# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling/v1beta1/annotation_spec_set.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datalabeling/v1beta1/annotation_spec_set.proto',
  package='google.cloud.datalabeling.v1beta1',
  syntax='proto3',
  serialized_options=b'\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling',
  serialized_pb=b'\n;google/cloud/datalabeling/v1beta1/annotation_spec_set.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\xb5\x01\n\x11\x41nnotationSpecSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12K\n\x10\x61nnotation_specs\x18\x04 \x03(\x0b\x32\x31.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12\x1a\n\x12\x62locking_resources\x18\x05 \x03(\t\";\n\x0e\x41nnotationSpec\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\tBx\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabelingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ANNOTATIONSPECSET = _descriptor.Descriptor(
  name='AnnotationSpecSet',
  full_name='google.cloud.datalabeling.v1beta1.AnnotationSpecSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpecSet.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpecSet.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpecSet.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation_specs', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpecSet.annotation_specs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocking_resources', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpecSet.blocking_resources', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=129,
  serialized_end=310,
)


_ANNOTATIONSPEC = _descriptor.Descriptor(
  name='AnnotationSpec',
  full_name='google.cloud.datalabeling.v1beta1.AnnotationSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpec.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.datalabeling.v1beta1.AnnotationSpec.description', index=1,
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
  ],
  serialized_start=312,
  serialized_end=371,
)

_ANNOTATIONSPECSET.fields_by_name['annotation_specs'].message_type = _ANNOTATIONSPEC
DESCRIPTOR.message_types_by_name['AnnotationSpecSet'] = _ANNOTATIONSPECSET
DESCRIPTOR.message_types_by_name['AnnotationSpec'] = _ANNOTATIONSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnnotationSpecSet = _reflection.GeneratedProtocolMessageType('AnnotationSpecSet', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATIONSPECSET,
  '__module__' : 'google.cloud.datalabeling.v1beta1.annotation_spec_set_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.AnnotationSpecSet)
  })
_sym_db.RegisterMessage(AnnotationSpecSet)

AnnotationSpec = _reflection.GeneratedProtocolMessageType('AnnotationSpec', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATIONSPEC,
  '__module__' : 'google.cloud.datalabeling.v1beta1.annotation_spec_set_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.AnnotationSpec)
  })
_sym_db.RegisterMessage(AnnotationSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
