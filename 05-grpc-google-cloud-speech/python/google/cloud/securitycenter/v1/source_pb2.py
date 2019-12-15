# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter/v1/source.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/securitycenter/v1/source.proto',
  package='google.cloud.securitycenter.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.cloud.securitycenter.v1P\001ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\252\002\036Google.Cloud.SecurityCenter.V1\312\002\036Google\\Cloud\\SecurityCenter\\V1\352\002!Google::Cloud::SecurityCenter::V1',
  serialized_pb=b'\n+google/cloud/securitycenter/v1/source.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\"\x9b\x01\n\x06Source\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t:X\xea\x41U\n$securitycenter.googleapis.com/Source\x12-organizations/{organization}/sources/{source}B\xda\x01\n\"com.google.cloud.securitycenter.v1P\x01ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='google.cloud.securitycenter.v1.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.securitycenter.v1.Source.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.securitycenter.v1.Source.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.securitycenter.v1.Source.description', index=2,
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
  serialized_options=b'\352AU\n$securitycenter.googleapis.com/Source\022-organizations/{organization}/sources/{source}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=292,
)

DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'google.cloud.securitycenter.v1.source_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Source)
  })
_sym_db.RegisterMessage(Source)


DESCRIPTOR._options = None
_SOURCE._options = None
# @@protoc_insertion_point(module_scope)