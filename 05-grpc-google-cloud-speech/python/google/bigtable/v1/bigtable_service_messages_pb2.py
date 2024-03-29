# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/v1/bigtable_service_messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.bigtable.v1 import bigtable_data_pb2 as google_dot_bigtable_dot_v1_dot_bigtable__data__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bigtable/v1/bigtable_service_messages.proto',
  package='google.bigtable.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.google.bigtable.v1B\034BigtableServiceMessagesProtoP\001Z:google.golang.org/genproto/googleapis/bigtable/v1;bigtable',
  serialized_pb=b'\n2google/bigtable/v1/bigtable_service_messages.proto\x12\x12google.bigtable.v1\x1a&google/bigtable/v1/bigtable_data.proto\x1a\x17google/rpc/status.proto\"\x8b\x02\n\x0fReadRowsRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x11\n\x07row_key\x18\x02 \x01(\x0cH\x00\x12\x31\n\trow_range\x18\x03 \x01(\x0b\x32\x1c.google.bigtable.v1.RowRangeH\x00\x12-\n\x07row_set\x18\x08 \x01(\x0b\x32\x1a.google.bigtable.v1.RowSetH\x00\x12-\n\x06\x66ilter\x18\x05 \x01(\x0b\x32\x1d.google.bigtable.v1.RowFilter\x12\x1e\n\x16\x61llow_row_interleaving\x18\x06 \x01(\x08\x12\x16\n\x0enum_rows_limit\x18\x07 \x01(\x03\x42\x08\n\x06target\"\xd0\x01\n\x10ReadRowsResponse\x12\x0f\n\x07row_key\x18\x01 \x01(\x0c\x12:\n\x06\x63hunks\x18\x02 \x03(\x0b\x32*.google.bigtable.v1.ReadRowsResponse.Chunk\x1ao\n\x05\x43hunk\x12\x32\n\x0crow_contents\x18\x01 \x01(\x0b\x32\x1a.google.bigtable.v1.FamilyH\x00\x12\x13\n\treset_row\x18\x02 \x01(\x08H\x00\x12\x14\n\ncommit_row\x18\x03 \x01(\x08H\x00\x42\x07\n\x05\x63hunk\"*\n\x14SampleRowKeysRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\">\n\x15SampleRowKeysResponse\x12\x0f\n\x07row_key\x18\x01 \x01(\x0c\x12\x14\n\x0coffset_bytes\x18\x02 \x01(\x03\"h\n\x10MutateRowRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x0f\n\x07row_key\x18\x02 \x01(\x0c\x12/\n\tmutations\x18\x03 \x03(\x0b\x32\x1c.google.bigtable.v1.Mutation\"\xb0\x01\n\x11MutateRowsRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12<\n\x07\x65ntries\x18\x02 \x03(\x0b\x32+.google.bigtable.v1.MutateRowsRequest.Entry\x1aI\n\x05\x45ntry\x12\x0f\n\x07row_key\x18\x01 \x01(\x0c\x12/\n\tmutations\x18\x02 \x03(\x0b\x32\x1c.google.bigtable.v1.Mutation\":\n\x12MutateRowsResponse\x12$\n\x08statuses\x18\x01 \x03(\x0b\x32\x12.google.rpc.Status\"\xe5\x01\n\x18\x43heckAndMutateRowRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x0f\n\x07row_key\x18\x02 \x01(\x0c\x12\x37\n\x10predicate_filter\x18\x06 \x01(\x0b\x32\x1d.google.bigtable.v1.RowFilter\x12\x34\n\x0etrue_mutations\x18\x04 \x03(\x0b\x32\x1c.google.bigtable.v1.Mutation\x12\x35\n\x0f\x66\x61lse_mutations\x18\x05 \x03(\x0b\x32\x1c.google.bigtable.v1.Mutation\"6\n\x19\x43heckAndMutateRowResponse\x12\x19\n\x11predicate_matched\x18\x01 \x01(\x08\"x\n\x19ReadModifyWriteRowRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x0f\n\x07row_key\x18\x02 \x01(\x0c\x12\x36\n\x05rules\x18\x03 \x03(\x0b\x32\'.google.bigtable.v1.ReadModifyWriteRuleBt\n\x16\x63om.google.bigtable.v1B\x1c\x42igtableServiceMessagesProtoP\x01Z:google.golang.org/genproto/googleapis/bigtable/v1;bigtableb\x06proto3'
  ,
  dependencies=[google_dot_bigtable_dot_v1_dot_bigtable__data__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_READROWSREQUEST = _descriptor.Descriptor(
  name='ReadRowsRequest',
  full_name='google.bigtable.v1.ReadRowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='google.bigtable.v1.ReadRowsRequest.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.ReadRowsRequest.row_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_range', full_name='google.bigtable.v1.ReadRowsRequest.row_range', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_set', full_name='google.bigtable.v1.ReadRowsRequest.row_set', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.bigtable.v1.ReadRowsRequest.filter', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_row_interleaving', full_name='google.bigtable.v1.ReadRowsRequest.allow_row_interleaving', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_rows_limit', full_name='google.bigtable.v1.ReadRowsRequest.num_rows_limit', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
    _descriptor.OneofDescriptor(
      name='target', full_name='google.bigtable.v1.ReadRowsRequest.target',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=140,
  serialized_end=407,
)


_READROWSRESPONSE_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='google.bigtable.v1.ReadRowsResponse.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_contents', full_name='google.bigtable.v1.ReadRowsResponse.Chunk.row_contents', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_row', full_name='google.bigtable.v1.ReadRowsResponse.Chunk.reset_row', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_row', full_name='google.bigtable.v1.ReadRowsResponse.Chunk.commit_row', index=2,
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
    _descriptor.OneofDescriptor(
      name='chunk', full_name='google.bigtable.v1.ReadRowsResponse.Chunk.chunk',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=507,
  serialized_end=618,
)

_READROWSRESPONSE = _descriptor.Descriptor(
  name='ReadRowsResponse',
  full_name='google.bigtable.v1.ReadRowsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.ReadRowsResponse.row_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='google.bigtable.v1.ReadRowsResponse.chunks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_READROWSRESPONSE_CHUNK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=618,
)


_SAMPLEROWKEYSREQUEST = _descriptor.Descriptor(
  name='SampleRowKeysRequest',
  full_name='google.bigtable.v1.SampleRowKeysRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='google.bigtable.v1.SampleRowKeysRequest.table_name', index=0,
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
  serialized_start=620,
  serialized_end=662,
)


_SAMPLEROWKEYSRESPONSE = _descriptor.Descriptor(
  name='SampleRowKeysResponse',
  full_name='google.bigtable.v1.SampleRowKeysResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.SampleRowKeysResponse.row_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset_bytes', full_name='google.bigtable.v1.SampleRowKeysResponse.offset_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=664,
  serialized_end=726,
)


_MUTATEROWREQUEST = _descriptor.Descriptor(
  name='MutateRowRequest',
  full_name='google.bigtable.v1.MutateRowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='google.bigtable.v1.MutateRowRequest.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.MutateRowRequest.row_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutations', full_name='google.bigtable.v1.MutateRowRequest.mutations', index=2,
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
  serialized_start=728,
  serialized_end=832,
)


_MUTATEROWSREQUEST_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='google.bigtable.v1.MutateRowsRequest.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.MutateRowsRequest.Entry.row_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutations', full_name='google.bigtable.v1.MutateRowsRequest.Entry.mutations', index=1,
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
  serialized_start=938,
  serialized_end=1011,
)

_MUTATEROWSREQUEST = _descriptor.Descriptor(
  name='MutateRowsRequest',
  full_name='google.bigtable.v1.MutateRowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='google.bigtable.v1.MutateRowsRequest.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='google.bigtable.v1.MutateRowsRequest.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MUTATEROWSREQUEST_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=835,
  serialized_end=1011,
)


_MUTATEROWSRESPONSE = _descriptor.Descriptor(
  name='MutateRowsResponse',
  full_name='google.bigtable.v1.MutateRowsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statuses', full_name='google.bigtable.v1.MutateRowsResponse.statuses', index=0,
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
  serialized_start=1013,
  serialized_end=1071,
)


_CHECKANDMUTATEROWREQUEST = _descriptor.Descriptor(
  name='CheckAndMutateRowRequest',
  full_name='google.bigtable.v1.CheckAndMutateRowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='google.bigtable.v1.CheckAndMutateRowRequest.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.CheckAndMutateRowRequest.row_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predicate_filter', full_name='google.bigtable.v1.CheckAndMutateRowRequest.predicate_filter', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='true_mutations', full_name='google.bigtable.v1.CheckAndMutateRowRequest.true_mutations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='false_mutations', full_name='google.bigtable.v1.CheckAndMutateRowRequest.false_mutations', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=1074,
  serialized_end=1303,
)


_CHECKANDMUTATEROWRESPONSE = _descriptor.Descriptor(
  name='CheckAndMutateRowResponse',
  full_name='google.bigtable.v1.CheckAndMutateRowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicate_matched', full_name='google.bigtable.v1.CheckAndMutateRowResponse.predicate_matched', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=1305,
  serialized_end=1359,
)


_READMODIFYWRITEROWREQUEST = _descriptor.Descriptor(
  name='ReadModifyWriteRowRequest',
  full_name='google.bigtable.v1.ReadModifyWriteRowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='google.bigtable.v1.ReadModifyWriteRowRequest.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_key', full_name='google.bigtable.v1.ReadModifyWriteRowRequest.row_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='google.bigtable.v1.ReadModifyWriteRowRequest.rules', index=2,
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
  serialized_start=1361,
  serialized_end=1481,
)

_READROWSREQUEST.fields_by_name['row_range'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._ROWRANGE
_READROWSREQUEST.fields_by_name['row_set'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._ROWSET
_READROWSREQUEST.fields_by_name['filter'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._ROWFILTER
_READROWSREQUEST.oneofs_by_name['target'].fields.append(
  _READROWSREQUEST.fields_by_name['row_key'])
_READROWSREQUEST.fields_by_name['row_key'].containing_oneof = _READROWSREQUEST.oneofs_by_name['target']
_READROWSREQUEST.oneofs_by_name['target'].fields.append(
  _READROWSREQUEST.fields_by_name['row_range'])
_READROWSREQUEST.fields_by_name['row_range'].containing_oneof = _READROWSREQUEST.oneofs_by_name['target']
_READROWSREQUEST.oneofs_by_name['target'].fields.append(
  _READROWSREQUEST.fields_by_name['row_set'])
_READROWSREQUEST.fields_by_name['row_set'].containing_oneof = _READROWSREQUEST.oneofs_by_name['target']
_READROWSRESPONSE_CHUNK.fields_by_name['row_contents'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._FAMILY
_READROWSRESPONSE_CHUNK.containing_type = _READROWSRESPONSE
_READROWSRESPONSE_CHUNK.oneofs_by_name['chunk'].fields.append(
  _READROWSRESPONSE_CHUNK.fields_by_name['row_contents'])
_READROWSRESPONSE_CHUNK.fields_by_name['row_contents'].containing_oneof = _READROWSRESPONSE_CHUNK.oneofs_by_name['chunk']
_READROWSRESPONSE_CHUNK.oneofs_by_name['chunk'].fields.append(
  _READROWSRESPONSE_CHUNK.fields_by_name['reset_row'])
_READROWSRESPONSE_CHUNK.fields_by_name['reset_row'].containing_oneof = _READROWSRESPONSE_CHUNK.oneofs_by_name['chunk']
_READROWSRESPONSE_CHUNK.oneofs_by_name['chunk'].fields.append(
  _READROWSRESPONSE_CHUNK.fields_by_name['commit_row'])
_READROWSRESPONSE_CHUNK.fields_by_name['commit_row'].containing_oneof = _READROWSRESPONSE_CHUNK.oneofs_by_name['chunk']
_READROWSRESPONSE.fields_by_name['chunks'].message_type = _READROWSRESPONSE_CHUNK
_MUTATEROWREQUEST.fields_by_name['mutations'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._MUTATION
_MUTATEROWSREQUEST_ENTRY.fields_by_name['mutations'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._MUTATION
_MUTATEROWSREQUEST_ENTRY.containing_type = _MUTATEROWSREQUEST
_MUTATEROWSREQUEST.fields_by_name['entries'].message_type = _MUTATEROWSREQUEST_ENTRY
_MUTATEROWSRESPONSE.fields_by_name['statuses'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_CHECKANDMUTATEROWREQUEST.fields_by_name['predicate_filter'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._ROWFILTER
_CHECKANDMUTATEROWREQUEST.fields_by_name['true_mutations'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._MUTATION
_CHECKANDMUTATEROWREQUEST.fields_by_name['false_mutations'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._MUTATION
_READMODIFYWRITEROWREQUEST.fields_by_name['rules'].message_type = google_dot_bigtable_dot_v1_dot_bigtable__data__pb2._READMODIFYWRITERULE
DESCRIPTOR.message_types_by_name['ReadRowsRequest'] = _READROWSREQUEST
DESCRIPTOR.message_types_by_name['ReadRowsResponse'] = _READROWSRESPONSE
DESCRIPTOR.message_types_by_name['SampleRowKeysRequest'] = _SAMPLEROWKEYSREQUEST
DESCRIPTOR.message_types_by_name['SampleRowKeysResponse'] = _SAMPLEROWKEYSRESPONSE
DESCRIPTOR.message_types_by_name['MutateRowRequest'] = _MUTATEROWREQUEST
DESCRIPTOR.message_types_by_name['MutateRowsRequest'] = _MUTATEROWSREQUEST
DESCRIPTOR.message_types_by_name['MutateRowsResponse'] = _MUTATEROWSRESPONSE
DESCRIPTOR.message_types_by_name['CheckAndMutateRowRequest'] = _CHECKANDMUTATEROWREQUEST
DESCRIPTOR.message_types_by_name['CheckAndMutateRowResponse'] = _CHECKANDMUTATEROWRESPONSE
DESCRIPTOR.message_types_by_name['ReadModifyWriteRowRequest'] = _READMODIFYWRITEROWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadRowsRequest = _reflection.GeneratedProtocolMessageType('ReadRowsRequest', (_message.Message,), {
  'DESCRIPTOR' : _READROWSREQUEST,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.ReadRowsRequest)
  })
_sym_db.RegisterMessage(ReadRowsRequest)

ReadRowsResponse = _reflection.GeneratedProtocolMessageType('ReadRowsResponse', (_message.Message,), {

  'Chunk' : _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
    'DESCRIPTOR' : _READROWSRESPONSE_CHUNK,
    '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.v1.ReadRowsResponse.Chunk)
    })
  ,
  'DESCRIPTOR' : _READROWSRESPONSE,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.ReadRowsResponse)
  })
_sym_db.RegisterMessage(ReadRowsResponse)
_sym_db.RegisterMessage(ReadRowsResponse.Chunk)

SampleRowKeysRequest = _reflection.GeneratedProtocolMessageType('SampleRowKeysRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEROWKEYSREQUEST,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.SampleRowKeysRequest)
  })
_sym_db.RegisterMessage(SampleRowKeysRequest)

SampleRowKeysResponse = _reflection.GeneratedProtocolMessageType('SampleRowKeysResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEROWKEYSRESPONSE,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.SampleRowKeysResponse)
  })
_sym_db.RegisterMessage(SampleRowKeysResponse)

MutateRowRequest = _reflection.GeneratedProtocolMessageType('MutateRowRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEROWREQUEST,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.MutateRowRequest)
  })
_sym_db.RegisterMessage(MutateRowRequest)

MutateRowsRequest = _reflection.GeneratedProtocolMessageType('MutateRowsRequest', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _MUTATEROWSREQUEST_ENTRY,
    '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.v1.MutateRowsRequest.Entry)
    })
  ,
  'DESCRIPTOR' : _MUTATEROWSREQUEST,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.MutateRowsRequest)
  })
_sym_db.RegisterMessage(MutateRowsRequest)
_sym_db.RegisterMessage(MutateRowsRequest.Entry)

MutateRowsResponse = _reflection.GeneratedProtocolMessageType('MutateRowsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEROWSRESPONSE,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.MutateRowsResponse)
  })
_sym_db.RegisterMessage(MutateRowsResponse)

CheckAndMutateRowRequest = _reflection.GeneratedProtocolMessageType('CheckAndMutateRowRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKANDMUTATEROWREQUEST,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.CheckAndMutateRowRequest)
  })
_sym_db.RegisterMessage(CheckAndMutateRowRequest)

CheckAndMutateRowResponse = _reflection.GeneratedProtocolMessageType('CheckAndMutateRowResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKANDMUTATEROWRESPONSE,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.CheckAndMutateRowResponse)
  })
_sym_db.RegisterMessage(CheckAndMutateRowResponse)

ReadModifyWriteRowRequest = _reflection.GeneratedProtocolMessageType('ReadModifyWriteRowRequest', (_message.Message,), {
  'DESCRIPTOR' : _READMODIFYWRITEROWREQUEST,
  '__module__' : 'google.bigtable.v1.bigtable_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.v1.ReadModifyWriteRowRequest)
  })
_sym_db.RegisterMessage(ReadModifyWriteRowRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
