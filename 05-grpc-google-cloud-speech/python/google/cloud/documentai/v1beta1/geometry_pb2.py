# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/documentai/v1beta1/geometry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/documentai/v1beta1/geometry.proto',
  package='google.cloud.documentai.v1beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.documentai.v1beta1B\rGeometryProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/documentai/v1beta1;documentai',
  serialized_pb=b'\n.google/cloud/documentai/v1beta1/geometry.proto\x12\x1fgoogle.cloud.documentai.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\x99\x01\n\x0c\x42oundingPoly\x12\x39\n\x08vertices\x18\x01 \x03(\x0b\x32\'.google.cloud.documentai.v1beta1.Vertex\x12N\n\x13normalized_vertices\x18\x02 \x03(\x0b\x32\x31.google.cloud.documentai.v1beta1.NormalizedVertexB\x81\x01\n#com.google.cloud.documentai.v1beta1B\rGeometryProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/documentai/v1beta1;documentaib\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_VERTEX = _descriptor.Descriptor(
  name='Vertex',
  full_name='google.cloud.documentai.v1beta1.Vertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='google.cloud.documentai.v1beta1.Vertex.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='google.cloud.documentai.v1beta1.Vertex.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=113,
  serialized_end=143,
)


_NORMALIZEDVERTEX = _descriptor.Descriptor(
  name='NormalizedVertex',
  full_name='google.cloud.documentai.v1beta1.NormalizedVertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='google.cloud.documentai.v1beta1.NormalizedVertex.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='google.cloud.documentai.v1beta1.NormalizedVertex.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=145,
  serialized_end=185,
)


_BOUNDINGPOLY = _descriptor.Descriptor(
  name='BoundingPoly',
  full_name='google.cloud.documentai.v1beta1.BoundingPoly',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='google.cloud.documentai.v1beta1.BoundingPoly.vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalized_vertices', full_name='google.cloud.documentai.v1beta1.BoundingPoly.normalized_vertices', index=1,
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
  serialized_start=188,
  serialized_end=341,
)

_BOUNDINGPOLY.fields_by_name['vertices'].message_type = _VERTEX
_BOUNDINGPOLY.fields_by_name['normalized_vertices'].message_type = _NORMALIZEDVERTEX
DESCRIPTOR.message_types_by_name['Vertex'] = _VERTEX
DESCRIPTOR.message_types_by_name['NormalizedVertex'] = _NORMALIZEDVERTEX
DESCRIPTOR.message_types_by_name['BoundingPoly'] = _BOUNDINGPOLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), {
  'DESCRIPTOR' : _VERTEX,
  '__module__' : 'google.cloud.documentai.v1beta1.geometry_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta1.Vertex)
  })
_sym_db.RegisterMessage(Vertex)

NormalizedVertex = _reflection.GeneratedProtocolMessageType('NormalizedVertex', (_message.Message,), {
  'DESCRIPTOR' : _NORMALIZEDVERTEX,
  '__module__' : 'google.cloud.documentai.v1beta1.geometry_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta1.NormalizedVertex)
  })
_sym_db.RegisterMessage(NormalizedVertex)

BoundingPoly = _reflection.GeneratedProtocolMessageType('BoundingPoly', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGPOLY,
  '__module__' : 'google.cloud.documentai.v1beta1.geometry_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta1.BoundingPoly)
  })
_sym_db.RegisterMessage(BoundingPoly)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
