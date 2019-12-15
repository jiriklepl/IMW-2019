# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/readalignment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.genomics.v1 import cigar_pb2 as google_dot_genomics_dot_v1_dot_cigar__pb2
from google.genomics.v1 import position_pb2 as google_dot_genomics_dot_v1_dot_position__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/genomics/v1/readalignment.proto',
  package='google.genomics.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.google.genomics.v1B\022ReadAlignmentProtoP\001Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\370\001\001',
  serialized_pb=b'\n&google/genomics/v1/readalignment.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/genomics/v1/cigar.proto\x1a!google/genomics/v1/position.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x88\x01\n\x0fLinearAlignment\x12.\n\x08position\x18\x01 \x01(\x0b\x32\x1c.google.genomics.v1.Position\x12\x17\n\x0fmapping_quality\x18\x02 \x01(\x05\x12,\n\x05\x63igar\x18\x03 \x03(\x0b\x32\x1d.google.genomics.v1.CigarUnit\"\xd9\x04\n\x04Read\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rread_group_id\x18\x02 \x01(\t\x12\x19\n\x11read_group_set_id\x18\x03 \x01(\t\x12\x15\n\rfragment_name\x18\x04 \x01(\t\x12\x18\n\x10proper_placement\x18\x05 \x01(\x08\x12\x1a\n\x12\x64uplicate_fragment\x18\x06 \x01(\x08\x12\x17\n\x0f\x66ragment_length\x18\x07 \x01(\x05\x12\x13\n\x0bread_number\x18\x08 \x01(\x05\x12\x14\n\x0cnumber_reads\x18\t \x01(\x05\x12$\n\x1c\x66\x61iled_vendor_quality_checks\x18\n \x01(\x08\x12\x36\n\talignment\x18\x0b \x01(\x0b\x32#.google.genomics.v1.LinearAlignment\x12\x1b\n\x13secondary_alignment\x18\x0c \x01(\x08\x12\x1f\n\x17supplementary_alignment\x18\r \x01(\x08\x12\x18\n\x10\x61ligned_sequence\x18\x0e \x01(\t\x12\x17\n\x0f\x61ligned_quality\x18\x0f \x03(\x05\x12\x38\n\x12next_mate_position\x18\x10 \x01(\x0b\x32\x1c.google.genomics.v1.Position\x12\x30\n\x04info\x18\x11 \x03(\x0b\x32\".google.genomics.v1.Read.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x42m\n\x16\x63om.google.genomics.v1B\x12ReadAlignmentProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_genomics_dot_v1_dot_cigar__pb2.DESCRIPTOR,google_dot_genomics_dot_v1_dot_position__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LINEARALIGNMENT = _descriptor.Descriptor(
  name='LinearAlignment',
  full_name='google.genomics.v1.LinearAlignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='google.genomics.v1.LinearAlignment.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapping_quality', full_name='google.genomics.v1.LinearAlignment.mapping_quality', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cigar', full_name='google.genomics.v1.LinearAlignment.cigar', index=2,
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
  serialized_start=190,
  serialized_end=326,
)


_READ_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='google.genomics.v1.Read.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.genomics.v1.Read.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.genomics.v1.Read.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=930,
)

_READ = _descriptor.Descriptor(
  name='Read',
  full_name='google.genomics.v1.Read',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.genomics.v1.Read.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_group_id', full_name='google.genomics.v1.Read.read_group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_group_set_id', full_name='google.genomics.v1.Read.read_group_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fragment_name', full_name='google.genomics.v1.Read.fragment_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proper_placement', full_name='google.genomics.v1.Read.proper_placement', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duplicate_fragment', full_name='google.genomics.v1.Read.duplicate_fragment', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fragment_length', full_name='google.genomics.v1.Read.fragment_length', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_number', full_name='google.genomics.v1.Read.read_number', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_reads', full_name='google.genomics.v1.Read.number_reads', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed_vendor_quality_checks', full_name='google.genomics.v1.Read.failed_vendor_quality_checks', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alignment', full_name='google.genomics.v1.Read.alignment', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_alignment', full_name='google.genomics.v1.Read.secondary_alignment', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supplementary_alignment', full_name='google.genomics.v1.Read.supplementary_alignment', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aligned_sequence', full_name='google.genomics.v1.Read.aligned_sequence', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aligned_quality', full_name='google.genomics.v1.Read.aligned_quality', index=14,
      number=15, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_mate_position', full_name='google.genomics.v1.Read.next_mate_position', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='google.genomics.v1.Read.info', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_READ_INFOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=930,
)

_LINEARALIGNMENT.fields_by_name['position'].message_type = google_dot_genomics_dot_v1_dot_position__pb2._POSITION
_LINEARALIGNMENT.fields_by_name['cigar'].message_type = google_dot_genomics_dot_v1_dot_cigar__pb2._CIGARUNIT
_READ_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_READ_INFOENTRY.containing_type = _READ
_READ.fields_by_name['alignment'].message_type = _LINEARALIGNMENT
_READ.fields_by_name['next_mate_position'].message_type = google_dot_genomics_dot_v1_dot_position__pb2._POSITION
_READ.fields_by_name['info'].message_type = _READ_INFOENTRY
DESCRIPTOR.message_types_by_name['LinearAlignment'] = _LINEARALIGNMENT
DESCRIPTOR.message_types_by_name['Read'] = _READ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinearAlignment = _reflection.GeneratedProtocolMessageType('LinearAlignment', (_message.Message,), {
  'DESCRIPTOR' : _LINEARALIGNMENT,
  '__module__' : 'google.genomics.v1.readalignment_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.LinearAlignment)
  })
_sym_db.RegisterMessage(LinearAlignment)

Read = _reflection.GeneratedProtocolMessageType('Read', (_message.Message,), {

  'InfoEntry' : _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), {
    'DESCRIPTOR' : _READ_INFOENTRY,
    '__module__' : 'google.genomics.v1.readalignment_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.Read.InfoEntry)
    })
  ,
  'DESCRIPTOR' : _READ,
  '__module__' : 'google.genomics.v1.readalignment_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.Read)
  })
_sym_db.RegisterMessage(Read)
_sym_db.RegisterMessage(Read.InfoEntry)


DESCRIPTOR._options = None
_READ_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)