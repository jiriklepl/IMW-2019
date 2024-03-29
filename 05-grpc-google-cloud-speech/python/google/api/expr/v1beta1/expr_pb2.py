# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1beta1/expr.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api.expr.v1beta1 import source_pb2 as google_dot_api_dot_expr_dot_v1beta1_dot_source__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/expr/v1beta1/expr.proto',
  package='google.api.expr.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\033com.google.api.expr.v1beta1B\tExprProtoP\001Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\370\001\001',
  serialized_pb=b'\n\"google/api/expr/v1beta1/expr.proto\x12\x17google.api.expr.v1beta1\x1a$google/api/expr/v1beta1/source.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x8b\x01\n\nParsedExpr\x12+\n\x04\x65xpr\x18\x02 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12\x38\n\x0bsource_info\x18\x03 \x01(\x0b\x32#.google.api.expr.v1beta1.SourceInfo\x12\x16\n\x0esyntax_version\x18\x04 \x01(\t\"\xab\n\n\x04\x45xpr\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x38\n\x0cliteral_expr\x18\x03 \x01(\x0b\x32 .google.api.expr.v1beta1.LiteralH\x00\x12\x39\n\nident_expr\x18\x04 \x01(\x0b\x32#.google.api.expr.v1beta1.Expr.IdentH\x00\x12;\n\x0bselect_expr\x18\x05 \x01(\x0b\x32$.google.api.expr.v1beta1.Expr.SelectH\x00\x12\x37\n\tcall_expr\x18\x06 \x01(\x0b\x32\".google.api.expr.v1beta1.Expr.CallH\x00\x12=\n\tlist_expr\x18\x07 \x01(\x0b\x32(.google.api.expr.v1beta1.Expr.CreateListH\x00\x12\x41\n\x0bstruct_expr\x18\x08 \x01(\x0b\x32*.google.api.expr.v1beta1.Expr.CreateStructH\x00\x12I\n\x12\x63omprehension_expr\x18\t \x01(\x0b\x32+.google.api.expr.v1beta1.Expr.ComprehensionH\x00\x1a\x15\n\x05Ident\x12\x0c\n\x04name\x18\x01 \x01(\t\x1aZ\n\x06Select\x12.\n\x07operand\x18\x01 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x11\n\ttest_only\x18\x03 \x01(\x08\x1at\n\x04\x43\x61ll\x12-\n\x06target\x18\x01 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12\x10\n\x08\x66unction\x18\x02 \x01(\t\x12+\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x1a=\n\nCreateList\x12/\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x1a\xf6\x01\n\x0c\x43reateStruct\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x41\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x30.google.api.expr.v1beta1.Expr.CreateStruct.Entry\x1a\x94\x01\n\x05\x45ntry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\tfield_key\x18\x02 \x01(\tH\x00\x12\x30\n\x07map_key\x18\x03 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.ExprH\x00\x12,\n\x05value\x18\x04 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.ExprB\n\n\x08key_kind\x1a\xb0\x02\n\rComprehension\x12\x10\n\x08iter_var\x18\x01 \x01(\t\x12\x31\n\niter_range\x18\x02 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12\x10\n\x08\x61\x63\x63u_var\x18\x03 \x01(\t\x12\x30\n\taccu_init\x18\x04 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12\x35\n\x0eloop_condition\x18\x05 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12\x30\n\tloop_step\x18\x06 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.Expr\x12-\n\x06result\x18\x07 \x01(\x0b\x32\x1d.google.api.expr.v1beta1.ExprB\x0b\n\texpr_kind\"\xd8\x01\n\x07Literal\x12\x30\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0cuint64_value\x18\x04 \x01(\x04H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00\x42\x0f\n\rconstant_kindBj\n\x1b\x63om.google.api.expr.v1beta1B\tExprProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_expr_dot_v1beta1_dot_source__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_PARSEDEXPR = _descriptor.Descriptor(
  name='ParsedExpr',
  full_name='google.api.expr.v1beta1.ParsedExpr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='expr', full_name='google.api.expr.v1beta1.ParsedExpr.expr', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_info', full_name='google.api.expr.v1beta1.ParsedExpr.source_info', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='syntax_version', full_name='google.api.expr.v1beta1.ParsedExpr.syntax_version', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=132,
  serialized_end=271,
)


_EXPR_IDENT = _descriptor.Descriptor(
  name='Ident',
  full_name='google.api.expr.v1beta1.Expr.Ident',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.api.expr.v1beta1.Expr.Ident.name', index=0,
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
  serialized_start=734,
  serialized_end=755,
)

_EXPR_SELECT = _descriptor.Descriptor(
  name='Select',
  full_name='google.api.expr.v1beta1.Expr.Select',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operand', full_name='google.api.expr.v1beta1.Expr.Select.operand', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='google.api.expr.v1beta1.Expr.Select.field', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_only', full_name='google.api.expr.v1beta1.Expr.Select.test_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=757,
  serialized_end=847,
)

_EXPR_CALL = _descriptor.Descriptor(
  name='Call',
  full_name='google.api.expr.v1beta1.Expr.Call',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='google.api.expr.v1beta1.Expr.Call.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function', full_name='google.api.expr.v1beta1.Expr.Call.function', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='google.api.expr.v1beta1.Expr.Call.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=849,
  serialized_end=965,
)

_EXPR_CREATELIST = _descriptor.Descriptor(
  name='CreateList',
  full_name='google.api.expr.v1beta1.Expr.CreateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='google.api.expr.v1beta1.Expr.CreateList.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=967,
  serialized_end=1028,
)

_EXPR_CREATESTRUCT_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='google.api.expr.v1beta1.Expr.CreateStruct.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.api.expr.v1beta1.Expr.CreateStruct.Entry.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_key', full_name='google.api.expr.v1beta1.Expr.CreateStruct.Entry.field_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_key', full_name='google.api.expr.v1beta1.Expr.CreateStruct.Entry.map_key', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.api.expr.v1beta1.Expr.CreateStruct.Entry.value', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='key_kind', full_name='google.api.expr.v1beta1.Expr.CreateStruct.Entry.key_kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1129,
  serialized_end=1277,
)

_EXPR_CREATESTRUCT = _descriptor.Descriptor(
  name='CreateStruct',
  full_name='google.api.expr.v1beta1.Expr.CreateStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.api.expr.v1beta1.Expr.CreateStruct.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='google.api.expr.v1beta1.Expr.CreateStruct.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXPR_CREATESTRUCT_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1031,
  serialized_end=1277,
)

_EXPR_COMPREHENSION = _descriptor.Descriptor(
  name='Comprehension',
  full_name='google.api.expr.v1beta1.Expr.Comprehension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iter_var', full_name='google.api.expr.v1beta1.Expr.Comprehension.iter_var', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iter_range', full_name='google.api.expr.v1beta1.Expr.Comprehension.iter_range', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accu_var', full_name='google.api.expr.v1beta1.Expr.Comprehension.accu_var', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accu_init', full_name='google.api.expr.v1beta1.Expr.Comprehension.accu_init', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loop_condition', full_name='google.api.expr.v1beta1.Expr.Comprehension.loop_condition', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loop_step', full_name='google.api.expr.v1beta1.Expr.Comprehension.loop_step', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='google.api.expr.v1beta1.Expr.Comprehension.result', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=1280,
  serialized_end=1584,
)

_EXPR = _descriptor.Descriptor(
  name='Expr',
  full_name='google.api.expr.v1beta1.Expr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.api.expr.v1beta1.Expr.id', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='literal_expr', full_name='google.api.expr.v1beta1.Expr.literal_expr', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ident_expr', full_name='google.api.expr.v1beta1.Expr.ident_expr', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='select_expr', full_name='google.api.expr.v1beta1.Expr.select_expr', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_expr', full_name='google.api.expr.v1beta1.Expr.call_expr', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_expr', full_name='google.api.expr.v1beta1.Expr.list_expr', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='struct_expr', full_name='google.api.expr.v1beta1.Expr.struct_expr', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comprehension_expr', full_name='google.api.expr.v1beta1.Expr.comprehension_expr', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXPR_IDENT, _EXPR_SELECT, _EXPR_CALL, _EXPR_CREATELIST, _EXPR_CREATESTRUCT, _EXPR_COMPREHENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='expr_kind', full_name='google.api.expr.v1beta1.Expr.expr_kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=274,
  serialized_end=1597,
)


_LITERAL = _descriptor.Descriptor(
  name='Literal',
  full_name='google.api.expr.v1beta1.Literal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='null_value', full_name='google.api.expr.v1beta1.Literal.null_value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='google.api.expr.v1beta1.Literal.bool_value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='google.api.expr.v1beta1.Literal.int64_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='google.api.expr.v1beta1.Literal.uint64_value', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='google.api.expr.v1beta1.Literal.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.api.expr.v1beta1.Literal.string_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='google.api.expr.v1beta1.Literal.bytes_value', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
    _descriptor.OneofDescriptor(
      name='constant_kind', full_name='google.api.expr.v1beta1.Literal.constant_kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1600,
  serialized_end=1816,
)

_PARSEDEXPR.fields_by_name['expr'].message_type = _EXPR
_PARSEDEXPR.fields_by_name['source_info'].message_type = google_dot_api_dot_expr_dot_v1beta1_dot_source__pb2._SOURCEINFO
_EXPR_IDENT.containing_type = _EXPR
_EXPR_SELECT.fields_by_name['operand'].message_type = _EXPR
_EXPR_SELECT.containing_type = _EXPR
_EXPR_CALL.fields_by_name['target'].message_type = _EXPR
_EXPR_CALL.fields_by_name['args'].message_type = _EXPR
_EXPR_CALL.containing_type = _EXPR
_EXPR_CREATELIST.fields_by_name['elements'].message_type = _EXPR
_EXPR_CREATELIST.containing_type = _EXPR
_EXPR_CREATESTRUCT_ENTRY.fields_by_name['map_key'].message_type = _EXPR
_EXPR_CREATESTRUCT_ENTRY.fields_by_name['value'].message_type = _EXPR
_EXPR_CREATESTRUCT_ENTRY.containing_type = _EXPR_CREATESTRUCT
_EXPR_CREATESTRUCT_ENTRY.oneofs_by_name['key_kind'].fields.append(
  _EXPR_CREATESTRUCT_ENTRY.fields_by_name['field_key'])
_EXPR_CREATESTRUCT_ENTRY.fields_by_name['field_key'].containing_oneof = _EXPR_CREATESTRUCT_ENTRY.oneofs_by_name['key_kind']
_EXPR_CREATESTRUCT_ENTRY.oneofs_by_name['key_kind'].fields.append(
  _EXPR_CREATESTRUCT_ENTRY.fields_by_name['map_key'])
_EXPR_CREATESTRUCT_ENTRY.fields_by_name['map_key'].containing_oneof = _EXPR_CREATESTRUCT_ENTRY.oneofs_by_name['key_kind']
_EXPR_CREATESTRUCT.fields_by_name['entries'].message_type = _EXPR_CREATESTRUCT_ENTRY
_EXPR_CREATESTRUCT.containing_type = _EXPR
_EXPR_COMPREHENSION.fields_by_name['iter_range'].message_type = _EXPR
_EXPR_COMPREHENSION.fields_by_name['accu_init'].message_type = _EXPR
_EXPR_COMPREHENSION.fields_by_name['loop_condition'].message_type = _EXPR
_EXPR_COMPREHENSION.fields_by_name['loop_step'].message_type = _EXPR
_EXPR_COMPREHENSION.fields_by_name['result'].message_type = _EXPR
_EXPR_COMPREHENSION.containing_type = _EXPR
_EXPR.fields_by_name['literal_expr'].message_type = _LITERAL
_EXPR.fields_by_name['ident_expr'].message_type = _EXPR_IDENT
_EXPR.fields_by_name['select_expr'].message_type = _EXPR_SELECT
_EXPR.fields_by_name['call_expr'].message_type = _EXPR_CALL
_EXPR.fields_by_name['list_expr'].message_type = _EXPR_CREATELIST
_EXPR.fields_by_name['struct_expr'].message_type = _EXPR_CREATESTRUCT
_EXPR.fields_by_name['comprehension_expr'].message_type = _EXPR_COMPREHENSION
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['literal_expr'])
_EXPR.fields_by_name['literal_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['ident_expr'])
_EXPR.fields_by_name['ident_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['select_expr'])
_EXPR.fields_by_name['select_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['call_expr'])
_EXPR.fields_by_name['call_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['list_expr'])
_EXPR.fields_by_name['list_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['struct_expr'])
_EXPR.fields_by_name['struct_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_EXPR.oneofs_by_name['expr_kind'].fields.append(
  _EXPR.fields_by_name['comprehension_expr'])
_EXPR.fields_by_name['comprehension_expr'].containing_oneof = _EXPR.oneofs_by_name['expr_kind']
_LITERAL.fields_by_name['null_value'].enum_type = google_dot_protobuf_dot_struct__pb2._NULLVALUE
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['null_value'])
_LITERAL.fields_by_name['null_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['bool_value'])
_LITERAL.fields_by_name['bool_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['int64_value'])
_LITERAL.fields_by_name['int64_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['uint64_value'])
_LITERAL.fields_by_name['uint64_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['double_value'])
_LITERAL.fields_by_name['double_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['string_value'])
_LITERAL.fields_by_name['string_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
_LITERAL.oneofs_by_name['constant_kind'].fields.append(
  _LITERAL.fields_by_name['bytes_value'])
_LITERAL.fields_by_name['bytes_value'].containing_oneof = _LITERAL.oneofs_by_name['constant_kind']
DESCRIPTOR.message_types_by_name['ParsedExpr'] = _PARSEDEXPR
DESCRIPTOR.message_types_by_name['Expr'] = _EXPR
DESCRIPTOR.message_types_by_name['Literal'] = _LITERAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParsedExpr = _reflection.GeneratedProtocolMessageType('ParsedExpr', (_message.Message,), {
  'DESCRIPTOR' : _PARSEDEXPR,
  '__module__' : 'google.api.expr.v1beta1.expr_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.ParsedExpr)
  })
_sym_db.RegisterMessage(ParsedExpr)

Expr = _reflection.GeneratedProtocolMessageType('Expr', (_message.Message,), {

  'Ident' : _reflection.GeneratedProtocolMessageType('Ident', (_message.Message,), {
    'DESCRIPTOR' : _EXPR_IDENT,
    '__module__' : 'google.api.expr.v1beta1.expr_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.Ident)
    })
  ,

  'Select' : _reflection.GeneratedProtocolMessageType('Select', (_message.Message,), {
    'DESCRIPTOR' : _EXPR_SELECT,
    '__module__' : 'google.api.expr.v1beta1.expr_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.Select)
    })
  ,

  'Call' : _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), {
    'DESCRIPTOR' : _EXPR_CALL,
    '__module__' : 'google.api.expr.v1beta1.expr_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.Call)
    })
  ,

  'CreateList' : _reflection.GeneratedProtocolMessageType('CreateList', (_message.Message,), {
    'DESCRIPTOR' : _EXPR_CREATELIST,
    '__module__' : 'google.api.expr.v1beta1.expr_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.CreateList)
    })
  ,

  'CreateStruct' : _reflection.GeneratedProtocolMessageType('CreateStruct', (_message.Message,), {

    'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
      'DESCRIPTOR' : _EXPR_CREATESTRUCT_ENTRY,
      '__module__' : 'google.api.expr.v1beta1.expr_pb2'
      # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.CreateStruct.Entry)
      })
    ,
    'DESCRIPTOR' : _EXPR_CREATESTRUCT,
    '__module__' : 'google.api.expr.v1beta1.expr_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.CreateStruct)
    })
  ,

  'Comprehension' : _reflection.GeneratedProtocolMessageType('Comprehension', (_message.Message,), {
    'DESCRIPTOR' : _EXPR_COMPREHENSION,
    '__module__' : 'google.api.expr.v1beta1.expr_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr.Comprehension)
    })
  ,
  'DESCRIPTOR' : _EXPR,
  '__module__' : 'google.api.expr.v1beta1.expr_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Expr)
  })
_sym_db.RegisterMessage(Expr)
_sym_db.RegisterMessage(Expr.Ident)
_sym_db.RegisterMessage(Expr.Select)
_sym_db.RegisterMessage(Expr.Call)
_sym_db.RegisterMessage(Expr.CreateList)
_sym_db.RegisterMessage(Expr.CreateStruct)
_sym_db.RegisterMessage(Expr.CreateStruct.Entry)
_sym_db.RegisterMessage(Expr.Comprehension)

Literal = _reflection.GeneratedProtocolMessageType('Literal', (_message.Message,), {
  'DESCRIPTOR' : _LITERAL,
  '__module__' : 'google.api.expr.v1beta1.expr_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.Literal)
  })
_sym_db.RegisterMessage(Literal)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
