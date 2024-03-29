# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/containeranalysis/v1beta1/common/common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/containeranalysis/v1beta1/common/common.proto',
  package='grafeas.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\031io.grafeas.v1beta1.commonP\001ZVgoogle.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1/common;common\242\002\003GRA',
  serialized_pb=b'\n=google/devtools/containeranalysis/v1beta1/common/common.proto\x12\x0fgrafeas.v1beta1\"(\n\nRelatedUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t*\x8b\x01\n\x08NoteKind\x12\x19\n\x15NOTE_KIND_UNSPECIFIED\x10\x00\x12\x11\n\rVULNERABILITY\x10\x01\x12\t\n\x05\x42UILD\x10\x02\x12\t\n\x05IMAGE\x10\x03\x12\x0b\n\x07PACKAGE\x10\x04\x12\x0e\n\nDEPLOYMENT\x10\x05\x12\r\n\tDISCOVERY\x10\x06\x12\x0f\n\x0b\x41TTESTATION\x10\x07\x42{\n\x19io.grafeas.v1beta1.commonP\x01ZVgoogle.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1/common;common\xa2\x02\x03GRAb\x06proto3'
)

_NOTEKIND = _descriptor.EnumDescriptor(
  name='NoteKind',
  full_name='grafeas.v1beta1.NoteKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTE_KIND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VULNERABILITY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUILD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPLOYMENT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOVERY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTESTATION', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=125,
  serialized_end=264,
)
_sym_db.RegisterEnumDescriptor(_NOTEKIND)

NoteKind = enum_type_wrapper.EnumTypeWrapper(_NOTEKIND)
NOTE_KIND_UNSPECIFIED = 0
VULNERABILITY = 1
BUILD = 2
IMAGE = 3
PACKAGE = 4
DEPLOYMENT = 5
DISCOVERY = 6
ATTESTATION = 7



_RELATEDURL = _descriptor.Descriptor(
  name='RelatedUrl',
  full_name='grafeas.v1beta1.RelatedUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='grafeas.v1beta1.RelatedUrl.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='grafeas.v1beta1.RelatedUrl.label', index=1,
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
  serialized_start=82,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['RelatedUrl'] = _RELATEDURL
DESCRIPTOR.enum_types_by_name['NoteKind'] = _NOTEKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RelatedUrl = _reflection.GeneratedProtocolMessageType('RelatedUrl', (_message.Message,), {
  'DESCRIPTOR' : _RELATEDURL,
  '__module__' : 'google.devtools.containeranalysis.v1beta1.common.common_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.RelatedUrl)
  })
_sym_db.RegisterMessage(RelatedUrl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
