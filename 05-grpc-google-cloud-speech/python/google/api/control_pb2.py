# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/control.proto',
  package='google.api',
  syntax='proto3',
  serialized_options=b'\n\016com.google.apiB\014ControlProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI',
  serialized_pb=b'\n\x18google/api/control.proto\x12\ngoogle.api\"\x1e\n\x07\x43ontrol\x12\x13\n\x0b\x65nvironment\x18\x01 \x01(\tBn\n\x0e\x63om.google.apiB\x0c\x43ontrolProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3'
)




_CONTROL = _descriptor.Descriptor(
  name='Control',
  full_name='google.api.Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='environment', full_name='google.api.Control.environment', index=0,
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
  serialized_start=40,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['Control'] = _CONTROL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Control = _reflection.GeneratedProtocolMessageType('Control', (_message.Message,), {
  'DESCRIPTOR' : _CONTROL,
  '__module__' : 'google.api.control_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Control)
  })
_sym_db.RegisterMessage(Control)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
