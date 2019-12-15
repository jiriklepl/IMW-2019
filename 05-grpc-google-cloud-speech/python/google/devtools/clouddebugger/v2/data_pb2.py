# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/clouddebugger/v2/data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.devtools.source.v1 import source_context_pb2 as google_dot_devtools_dot_source_dot_v1_dot_source__context__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/clouddebugger/v2/data.proto',
  package='google.devtools.clouddebugger.v2',
  syntax='proto3',
  serialized_options=b'\n$com.google.devtools.clouddebugger.v2B\tDataProtoP\001ZMgoogle.golang.org/genproto/googleapis/devtools/clouddebugger/v2;clouddebugger\370\001\001\252\002\030Google.Cloud.Debugger.V2\312\002\030Google\\Cloud\\Debugger\\V2',
  serialized_pb=b'\n+google/devtools/clouddebugger/v2/data.proto\x12 google.devtools.clouddebugger.v2\x1a.google/devtools/source/v1/source_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"3\n\rFormatMessage\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\x12\x12\n\nparameters\x18\x02 \x03(\t\"\xe4\x02\n\rStatusMessage\x12\x10\n\x08is_error\x18\x01 \x01(\x08\x12L\n\trefers_to\x18\x02 \x01(\x0e\x32\x39.google.devtools.clouddebugger.v2.StatusMessage.Reference\x12\x44\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32/.google.devtools.clouddebugger.v2.FormatMessage\"\xac\x01\n\tReference\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x1e\n\x1a\x42REAKPOINT_SOURCE_LOCATION\x10\x03\x12\x18\n\x14\x42REAKPOINT_CONDITION\x10\x04\x12\x19\n\x15\x42REAKPOINT_EXPRESSION\x10\x07\x12\x12\n\x0e\x42REAKPOINT_AGE\x10\x08\x12\x11\n\rVARIABLE_NAME\x10\x05\x12\x12\n\x0eVARIABLE_VALUE\x10\x06\"<\n\x0eSourceLocation\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x03 \x01(\x05\"\xe9\x01\n\x08Variable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12;\n\x07members\x18\x03 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.Variable\x12\x34\n\x0fvar_table_index\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12?\n\x06status\x18\x05 \x01(\x0b\x32/.google.devtools.clouddebugger.v2.StatusMessage\"\xdd\x01\n\nStackFrame\x12\x10\n\x08\x66unction\x18\x01 \x01(\t\x12\x42\n\x08location\x18\x02 \x01(\x0b\x32\x30.google.devtools.clouddebugger.v2.SourceLocation\x12=\n\targuments\x18\x03 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.Variable\x12:\n\x06locals\x18\x04 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.Variable\"\x97\x07\n\nBreakpoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x43\n\x06\x61\x63tion\x18\r \x01(\x0e\x32\x33.google.devtools.clouddebugger.v2.Breakpoint.Action\x12\x42\n\x08location\x18\x02 \x01(\x0b\x32\x30.google.devtools.clouddebugger.v2.SourceLocation\x12\x11\n\tcondition\x18\x03 \x01(\t\x12\x13\n\x0b\x65xpressions\x18\x04 \x03(\t\x12\x1a\n\x12log_message_format\x18\x0e \x01(\t\x12H\n\tlog_level\x18\x0f \x01(\x0e\x32\x35.google.devtools.clouddebugger.v2.Breakpoint.LogLevel\x12\x16\n\x0eis_final_state\x18\x05 \x01(\x08\x12/\n\x0b\x63reate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nfinal_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nuser_email\x18\x10 \x01(\t\x12?\n\x06status\x18\n \x01(\x0b\x32/.google.devtools.clouddebugger.v2.StatusMessage\x12\x42\n\x0cstack_frames\x18\x07 \x03(\x0b\x32,.google.devtools.clouddebugger.v2.StackFrame\x12I\n\x15\x65valuated_expressions\x18\x08 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.Variable\x12\x42\n\x0evariable_table\x18\t \x03(\x0b\x32*.google.devtools.clouddebugger.v2.Variable\x12H\n\x06labels\x18\x11 \x03(\x0b\x32\x38.google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1e\n\x06\x41\x63tion\x12\x0b\n\x07\x43\x41PTURE\x10\x00\x12\x07\n\x03LOG\x10\x01\",\n\x08LogLevel\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\xdf\x03\n\x08\x44\x65\x62uggee\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x12\n\nuniquifier\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bis_inactive\x18\x05 \x01(\x08\x12\x15\n\ragent_version\x18\x06 \x01(\t\x12\x13\n\x0bis_disabled\x18\x07 \x01(\x08\x12?\n\x06status\x18\x08 \x01(\x0b\x32/.google.devtools.clouddebugger.v2.StatusMessage\x12\x41\n\x0fsource_contexts\x18\t \x03(\x0b\x32(.google.devtools.source.v1.SourceContext\x12Q\n\x13\x65xt_source_contexts\x18\r \x03(\x0b\x32\x30.google.devtools.source.v1.ExtendedSourceContextB\x02\x18\x01\x12\x46\n\x06labels\x18\x0b \x03(\x0b\x32\x36.google.devtools.clouddebugger.v2.Debuggee.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\xbb\x01\n$com.google.devtools.clouddebugger.v2B\tDataProtoP\x01ZMgoogle.golang.org/genproto/googleapis/devtools/clouddebugger/v2;clouddebugger\xf8\x01\x01\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2b\x06proto3'
  ,
  dependencies=[google_dot_devtools_dot_source_dot_v1_dot_source__context__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_STATUSMESSAGE_REFERENCE = _descriptor.EnumDescriptor(
  name='Reference',
  full_name='google.devtools.clouddebugger.v2.StatusMessage.Reference',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKPOINT_SOURCE_LOCATION', index=1, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKPOINT_CONDITION', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKPOINT_EXPRESSION', index=3, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKPOINT_AGE', index=4, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARIABLE_NAME', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARIABLE_VALUE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=462,
  serialized_end=634,
)
_sym_db.RegisterEnumDescriptor(_STATUSMESSAGE_REFERENCE)

_BREAKPOINT_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='google.devtools.clouddebugger.v2.Breakpoint.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CAPTURE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2002,
  serialized_end=2032,
)
_sym_db.RegisterEnumDescriptor(_BREAKPOINT_ACTION)

_BREAKPOINT_LOGLEVEL = _descriptor.EnumDescriptor(
  name='LogLevel',
  full_name='google.devtools.clouddebugger.v2.Breakpoint.LogLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2034,
  serialized_end=2078,
)
_sym_db.RegisterEnumDescriptor(_BREAKPOINT_LOGLEVEL)


_FORMATMESSAGE = _descriptor.Descriptor(
  name='FormatMessage',
  full_name='google.devtools.clouddebugger.v2.FormatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='google.devtools.clouddebugger.v2.FormatMessage.format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='google.devtools.clouddebugger.v2.FormatMessage.parameters', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=224,
  serialized_end=275,
)


_STATUSMESSAGE = _descriptor.Descriptor(
  name='StatusMessage',
  full_name='google.devtools.clouddebugger.v2.StatusMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_error', full_name='google.devtools.clouddebugger.v2.StatusMessage.is_error', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refers_to', full_name='google.devtools.clouddebugger.v2.StatusMessage.refers_to', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.devtools.clouddebugger.v2.StatusMessage.description', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUSMESSAGE_REFERENCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=634,
)


_SOURCELOCATION = _descriptor.Descriptor(
  name='SourceLocation',
  full_name='google.devtools.clouddebugger.v2.SourceLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='google.devtools.clouddebugger.v2.SourceLocation.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='google.devtools.clouddebugger.v2.SourceLocation.line', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column', full_name='google.devtools.clouddebugger.v2.SourceLocation.column', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=636,
  serialized_end=696,
)


_VARIABLE = _descriptor.Descriptor(
  name='Variable',
  full_name='google.devtools.clouddebugger.v2.Variable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.clouddebugger.v2.Variable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.clouddebugger.v2.Variable.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.devtools.clouddebugger.v2.Variable.type', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='members', full_name='google.devtools.clouddebugger.v2.Variable.members', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='var_table_index', full_name='google.devtools.clouddebugger.v2.Variable.var_table_index', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.devtools.clouddebugger.v2.Variable.status', index=5,
      number=5, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=699,
  serialized_end=932,
)


_STACKFRAME = _descriptor.Descriptor(
  name='StackFrame',
  full_name='google.devtools.clouddebugger.v2.StackFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function', full_name='google.devtools.clouddebugger.v2.StackFrame.function', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='google.devtools.clouddebugger.v2.StackFrame.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='google.devtools.clouddebugger.v2.StackFrame.arguments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locals', full_name='google.devtools.clouddebugger.v2.StackFrame.locals', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=935,
  serialized_end=1156,
)


_BREAKPOINT_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry.value', index=1,
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
  serialized_start=1955,
  serialized_end=2000,
)

_BREAKPOINT = _descriptor.Descriptor(
  name='Breakpoint',
  full_name='google.devtools.clouddebugger.v2.Breakpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.clouddebugger.v2.Breakpoint.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='google.devtools.clouddebugger.v2.Breakpoint.action', index=1,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='google.devtools.clouddebugger.v2.Breakpoint.location', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='google.devtools.clouddebugger.v2.Breakpoint.condition', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expressions', full_name='google.devtools.clouddebugger.v2.Breakpoint.expressions', index=4,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_message_format', full_name='google.devtools.clouddebugger.v2.Breakpoint.log_message_format', index=5,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='google.devtools.clouddebugger.v2.Breakpoint.log_level', index=6,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_final_state', full_name='google.devtools.clouddebugger.v2.Breakpoint.is_final_state', index=7,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.devtools.clouddebugger.v2.Breakpoint.create_time', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='final_time', full_name='google.devtools.clouddebugger.v2.Breakpoint.final_time', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='google.devtools.clouddebugger.v2.Breakpoint.user_email', index=10,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.devtools.clouddebugger.v2.Breakpoint.status', index=11,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_frames', full_name='google.devtools.clouddebugger.v2.Breakpoint.stack_frames', index=12,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evaluated_expressions', full_name='google.devtools.clouddebugger.v2.Breakpoint.evaluated_expressions', index=13,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variable_table', full_name='google.devtools.clouddebugger.v2.Breakpoint.variable_table', index=14,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.devtools.clouddebugger.v2.Breakpoint.labels', index=15,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BREAKPOINT_LABELSENTRY, ],
  enum_types=[
    _BREAKPOINT_ACTION,
    _BREAKPOINT_LOGLEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1159,
  serialized_end=2078,
)


_DEBUGGEE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.devtools.clouddebugger.v2.Debuggee.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.clouddebugger.v2.Debuggee.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.clouddebugger.v2.Debuggee.LabelsEntry.value', index=1,
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
  serialized_start=1955,
  serialized_end=2000,
)

_DEBUGGEE = _descriptor.Descriptor(
  name='Debuggee',
  full_name='google.devtools.clouddebugger.v2.Debuggee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.clouddebugger.v2.Debuggee.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='google.devtools.clouddebugger.v2.Debuggee.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniquifier', full_name='google.devtools.clouddebugger.v2.Debuggee.uniquifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.devtools.clouddebugger.v2.Debuggee.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_inactive', full_name='google.devtools.clouddebugger.v2.Debuggee.is_inactive', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_version', full_name='google.devtools.clouddebugger.v2.Debuggee.agent_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_disabled', full_name='google.devtools.clouddebugger.v2.Debuggee.is_disabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.devtools.clouddebugger.v2.Debuggee.status', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_contexts', full_name='google.devtools.clouddebugger.v2.Debuggee.source_contexts', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ext_source_contexts', full_name='google.devtools.clouddebugger.v2.Debuggee.ext_source_contexts', index=9,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.devtools.clouddebugger.v2.Debuggee.labels', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGGEE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2081,
  serialized_end=2560,
)

_STATUSMESSAGE.fields_by_name['refers_to'].enum_type = _STATUSMESSAGE_REFERENCE
_STATUSMESSAGE.fields_by_name['description'].message_type = _FORMATMESSAGE
_STATUSMESSAGE_REFERENCE.containing_type = _STATUSMESSAGE
_VARIABLE.fields_by_name['members'].message_type = _VARIABLE
_VARIABLE.fields_by_name['var_table_index'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_VARIABLE.fields_by_name['status'].message_type = _STATUSMESSAGE
_STACKFRAME.fields_by_name['location'].message_type = _SOURCELOCATION
_STACKFRAME.fields_by_name['arguments'].message_type = _VARIABLE
_STACKFRAME.fields_by_name['locals'].message_type = _VARIABLE
_BREAKPOINT_LABELSENTRY.containing_type = _BREAKPOINT
_BREAKPOINT.fields_by_name['action'].enum_type = _BREAKPOINT_ACTION
_BREAKPOINT.fields_by_name['location'].message_type = _SOURCELOCATION
_BREAKPOINT.fields_by_name['log_level'].enum_type = _BREAKPOINT_LOGLEVEL
_BREAKPOINT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BREAKPOINT.fields_by_name['final_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BREAKPOINT.fields_by_name['status'].message_type = _STATUSMESSAGE
_BREAKPOINT.fields_by_name['stack_frames'].message_type = _STACKFRAME
_BREAKPOINT.fields_by_name['evaluated_expressions'].message_type = _VARIABLE
_BREAKPOINT.fields_by_name['variable_table'].message_type = _VARIABLE
_BREAKPOINT.fields_by_name['labels'].message_type = _BREAKPOINT_LABELSENTRY
_BREAKPOINT_ACTION.containing_type = _BREAKPOINT
_BREAKPOINT_LOGLEVEL.containing_type = _BREAKPOINT
_DEBUGGEE_LABELSENTRY.containing_type = _DEBUGGEE
_DEBUGGEE.fields_by_name['status'].message_type = _STATUSMESSAGE
_DEBUGGEE.fields_by_name['source_contexts'].message_type = google_dot_devtools_dot_source_dot_v1_dot_source__context__pb2._SOURCECONTEXT
_DEBUGGEE.fields_by_name['ext_source_contexts'].message_type = google_dot_devtools_dot_source_dot_v1_dot_source__context__pb2._EXTENDEDSOURCECONTEXT
_DEBUGGEE.fields_by_name['labels'].message_type = _DEBUGGEE_LABELSENTRY
DESCRIPTOR.message_types_by_name['FormatMessage'] = _FORMATMESSAGE
DESCRIPTOR.message_types_by_name['StatusMessage'] = _STATUSMESSAGE
DESCRIPTOR.message_types_by_name['SourceLocation'] = _SOURCELOCATION
DESCRIPTOR.message_types_by_name['Variable'] = _VARIABLE
DESCRIPTOR.message_types_by_name['StackFrame'] = _STACKFRAME
DESCRIPTOR.message_types_by_name['Breakpoint'] = _BREAKPOINT
DESCRIPTOR.message_types_by_name['Debuggee'] = _DEBUGGEE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FormatMessage = _reflection.GeneratedProtocolMessageType('FormatMessage', (_message.Message,), {
  'DESCRIPTOR' : _FORMATMESSAGE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.FormatMessage)
  })
_sym_db.RegisterMessage(FormatMessage)

StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)

SourceLocation = _reflection.GeneratedProtocolMessageType('SourceLocation', (_message.Message,), {
  'DESCRIPTOR' : _SOURCELOCATION,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.SourceLocation)
  })
_sym_db.RegisterMessage(SourceLocation)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Variable)
  })
_sym_db.RegisterMessage(Variable)

StackFrame = _reflection.GeneratedProtocolMessageType('StackFrame', (_message.Message,), {
  'DESCRIPTOR' : _STACKFRAME,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.StackFrame)
  })
_sym_db.RegisterMessage(StackFrame)

Breakpoint = _reflection.GeneratedProtocolMessageType('Breakpoint', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BREAKPOINT_LABELSENTRY,
    '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _BREAKPOINT,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Breakpoint)
  })
_sym_db.RegisterMessage(Breakpoint)
_sym_db.RegisterMessage(Breakpoint.LabelsEntry)

Debuggee = _reflection.GeneratedProtocolMessageType('Debuggee', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEBUGGEE_LABELSENTRY,
    '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Debuggee.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DEBUGGEE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Debuggee)
  })
_sym_db.RegisterMessage(Debuggee)
_sym_db.RegisterMessage(Debuggee.LabelsEntry)


DESCRIPTOR._options = None
_BREAKPOINT_LABELSENTRY._options = None
_DEBUGGEE_LABELSENTRY._options = None
_DEBUGGEE.fields_by_name['ext_source_contexts']._options = None
# @@protoc_insertion_point(module_scope)