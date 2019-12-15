# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/containeranalysis/v1alpha1/provenance.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.devtools.containeranalysis.v1alpha1 import source_context_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_source__context__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/containeranalysis/v1alpha1/provenance.proto',
  package='google.devtools.containeranalysis.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n%com.google.containeranalysis.v1alpha1P\001Z[google.golang.org/genproto/googleapis/devtools/containeranalysis/v1alpha1;containeranalysis\242\002\003GCA',
  serialized_pb=b'\n;google/devtools/containeranalysis/v1alpha1/provenance.proto\x12*google.devtools.containeranalysis.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a?google/devtools/containeranalysis/v1alpha1/source_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x96\x05\n\x0f\x42uildProvenance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x45\n\x08\x63ommands\x18\x05 \x03(\x0b\x32\x33.google.devtools.containeranalysis.v1alpha1.Command\x12M\n\x0f\x62uilt_artifacts\x18\x06 \x03(\x0b\x32\x34.google.devtools.containeranalysis.v1alpha1.Artifact\x12/\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x63reator\x18\x0b \x01(\t\x12\x13\n\x0blogs_bucket\x18\r \x01(\t\x12M\n\x11source_provenance\x18\x0e \x01(\x0b\x32\x32.google.devtools.containeranalysis.v1alpha1.Source\x12\x12\n\ntrigger_id\x18\x0f \x01(\t\x12\x64\n\rbuild_options\x18\x10 \x03(\x0b\x32M.google.devtools.containeranalysis.v1alpha1.BuildProvenance.BuildOptionsEntry\x12\x17\n\x0f\x62uilder_version\x18\x11 \x01(\t\x1a\x33\n\x11\x42uildOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfa\x04\n\x06Source\x12S\n\x0estorage_source\x18\x01 \x01(\x0b\x32\x39.google.devtools.containeranalysis.v1alpha1.StorageSourceH\x00\x12M\n\x0brepo_source\x18\x02 \x01(\x0b\x32\x36.google.devtools.containeranalysis.v1alpha1.RepoSourceH\x00\x12Z\n\x17\x61rtifact_storage_source\x18\x04 \x01(\x0b\x32\x39.google.devtools.containeranalysis.v1alpha1.StorageSource\x12W\n\x0b\x66ile_hashes\x18\x03 \x03(\x0b\x32\x42.google.devtools.containeranalysis.v1alpha1.Source.FileHashesEntry\x12J\n\x07\x63ontext\x18\x07 \x01(\x0b\x32\x39.google.devtools.containeranalysis.v1alpha1.SourceContext\x12V\n\x13\x61\x64\x64itional_contexts\x18\x08 \x03(\x0b\x32\x39.google.devtools.containeranalysis.v1alpha1.SourceContext\x1ai\n\x0f\x46ileHashesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.google.devtools.containeranalysis.v1alpha1.FileHashes:\x02\x38\x01\x42\x08\n\x06source\"Q\n\nFileHashes\x12\x43\n\tfile_hash\x18\x01 \x03(\x0b\x32\x30.google.devtools.containeranalysis.v1alpha1.Hash\"\x80\x01\n\x04Hash\x12G\n\x04type\x18\x01 \x01(\x0e\x32\x39.google.devtools.containeranalysis.v1alpha1.Hash.HashType\x12\r\n\x05value\x18\x02 \x01(\x0c\" \n\x08HashType\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SHA256\x10\x01\"C\n\rStorageSource\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x12\n\ngeneration\x18\x03 \x01(\x03\"\x80\x01\n\nRepoSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\trepo_name\x18\x02 \x01(\t\x12\x15\n\x0b\x62ranch_name\x18\x03 \x01(\tH\x00\x12\x12\n\x08tag_name\x18\x04 \x01(\tH\x00\x12\x14\n\ncommit_sha\x18\x05 \x01(\tH\x00\x42\n\n\x08revision\"]\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x65nv\x18\x02 \x03(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0b\n\x03\x64ir\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x10\n\x08wait_for\x18\x06 \x03(\t\"E\n\x08\x41rtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05names\x18\x04 \x03(\tB\x8c\x01\n%com.google.containeranalysis.v1alpha1P\x01Z[google.golang.org/genproto/googleapis/devtools/containeranalysis/v1alpha1;containeranalysis\xa2\x02\x03GCAb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_source__context__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_HASH_HASHTYPE = _descriptor.EnumDescriptor(
  name='HashType',
  full_name='google.devtools.containeranalysis.v1alpha1.Hash.HashType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHA256', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1717,
  serialized_end=1749,
)
_sym_db.RegisterEnumDescriptor(_HASH_HASHTYPE)


_BUILDPROVENANCE_BUILDOPTIONSENTRY = _descriptor.Descriptor(
  name='BuildOptionsEntry',
  full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.BuildOptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.BuildOptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.BuildOptionsEntry.value', index=1,
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
  serialized_start=847,
  serialized_end=898,
)

_BUILDPROVENANCE = _descriptor.Descriptor(
  name='BuildProvenance',
  full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.project_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commands', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.commands', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='built_artifacts', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.built_artifacts', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.create_time', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.start_time', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish_time', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.finish_time', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.creator', index=7,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs_bucket', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.logs_bucket', index=8,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_provenance', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.source_provenance', index=9,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.trigger_id', index=10,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_options', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.build_options', index=11,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='builder_version', full_name='google.devtools.containeranalysis.v1alpha1.BuildProvenance.builder_version', index=12,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILDPROVENANCE_BUILDOPTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=898,
)


_SOURCE_FILEHASHESENTRY = _descriptor.Descriptor(
  name='FileHashesEntry',
  full_name='google.devtools.containeranalysis.v1alpha1.Source.FileHashesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.containeranalysis.v1alpha1.Source.FileHashesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.containeranalysis.v1alpha1.Source.FileHashesEntry.value', index=1,
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
  serialized_start=1420,
  serialized_end=1525,
)

_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='google.devtools.containeranalysis.v1alpha1.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storage_source', full_name='google.devtools.containeranalysis.v1alpha1.Source.storage_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_source', full_name='google.devtools.containeranalysis.v1alpha1.Source.repo_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_storage_source', full_name='google.devtools.containeranalysis.v1alpha1.Source.artifact_storage_source', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_hashes', full_name='google.devtools.containeranalysis.v1alpha1.Source.file_hashes', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='google.devtools.containeranalysis.v1alpha1.Source.context', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additional_contexts', full_name='google.devtools.containeranalysis.v1alpha1.Source.additional_contexts', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SOURCE_FILEHASHESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='google.devtools.containeranalysis.v1alpha1.Source.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=901,
  serialized_end=1535,
)


_FILEHASHES = _descriptor.Descriptor(
  name='FileHashes',
  full_name='google.devtools.containeranalysis.v1alpha1.FileHashes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_hash', full_name='google.devtools.containeranalysis.v1alpha1.FileHashes.file_hash', index=0,
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
  serialized_start=1537,
  serialized_end=1618,
)


_HASH = _descriptor.Descriptor(
  name='Hash',
  full_name='google.devtools.containeranalysis.v1alpha1.Hash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.devtools.containeranalysis.v1alpha1.Hash.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.containeranalysis.v1alpha1.Hash.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HASH_HASHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1621,
  serialized_end=1749,
)


_STORAGESOURCE = _descriptor.Descriptor(
  name='StorageSource',
  full_name='google.devtools.containeranalysis.v1alpha1.StorageSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='google.devtools.containeranalysis.v1alpha1.StorageSource.bucket', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='google.devtools.containeranalysis.v1alpha1.StorageSource.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation', full_name='google.devtools.containeranalysis.v1alpha1.StorageSource.generation', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=1751,
  serialized_end=1818,
)


_REPOSOURCE = _descriptor.Descriptor(
  name='RepoSource',
  full_name='google.devtools.containeranalysis.v1alpha1.RepoSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.containeranalysis.v1alpha1.RepoSource.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='google.devtools.containeranalysis.v1alpha1.RepoSource.repo_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branch_name', full_name='google.devtools.containeranalysis.v1alpha1.RepoSource.branch_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name', full_name='google.devtools.containeranalysis.v1alpha1.RepoSource.tag_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_sha', full_name='google.devtools.containeranalysis.v1alpha1.RepoSource.commit_sha', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='revision', full_name='google.devtools.containeranalysis.v1alpha1.RepoSource.revision',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1821,
  serialized_end=1949,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='google.devtools.containeranalysis.v1alpha1.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.containeranalysis.v1alpha1.Command.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='google.devtools.containeranalysis.v1alpha1.Command.env', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='google.devtools.containeranalysis.v1alpha1.Command.args', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dir', full_name='google.devtools.containeranalysis.v1alpha1.Command.dir', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.containeranalysis.v1alpha1.Command.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wait_for', full_name='google.devtools.containeranalysis.v1alpha1.Command.wait_for', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=1951,
  serialized_end=2044,
)


_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='google.devtools.containeranalysis.v1alpha1.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.containeranalysis.v1alpha1.Artifact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='google.devtools.containeranalysis.v1alpha1.Artifact.checksum', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.containeranalysis.v1alpha1.Artifact.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='names', full_name='google.devtools.containeranalysis.v1alpha1.Artifact.names', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=2046,
  serialized_end=2115,
)

_BUILDPROVENANCE_BUILDOPTIONSENTRY.containing_type = _BUILDPROVENANCE
_BUILDPROVENANCE.fields_by_name['commands'].message_type = _COMMAND
_BUILDPROVENANCE.fields_by_name['built_artifacts'].message_type = _ARTIFACT
_BUILDPROVENANCE.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILDPROVENANCE.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILDPROVENANCE.fields_by_name['finish_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILDPROVENANCE.fields_by_name['source_provenance'].message_type = _SOURCE
_BUILDPROVENANCE.fields_by_name['build_options'].message_type = _BUILDPROVENANCE_BUILDOPTIONSENTRY
_SOURCE_FILEHASHESENTRY.fields_by_name['value'].message_type = _FILEHASHES
_SOURCE_FILEHASHESENTRY.containing_type = _SOURCE
_SOURCE.fields_by_name['storage_source'].message_type = _STORAGESOURCE
_SOURCE.fields_by_name['repo_source'].message_type = _REPOSOURCE
_SOURCE.fields_by_name['artifact_storage_source'].message_type = _STORAGESOURCE
_SOURCE.fields_by_name['file_hashes'].message_type = _SOURCE_FILEHASHESENTRY
_SOURCE.fields_by_name['context'].message_type = google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_source__context__pb2._SOURCECONTEXT
_SOURCE.fields_by_name['additional_contexts'].message_type = google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_source__context__pb2._SOURCECONTEXT
_SOURCE.oneofs_by_name['source'].fields.append(
  _SOURCE.fields_by_name['storage_source'])
_SOURCE.fields_by_name['storage_source'].containing_oneof = _SOURCE.oneofs_by_name['source']
_SOURCE.oneofs_by_name['source'].fields.append(
  _SOURCE.fields_by_name['repo_source'])
_SOURCE.fields_by_name['repo_source'].containing_oneof = _SOURCE.oneofs_by_name['source']
_FILEHASHES.fields_by_name['file_hash'].message_type = _HASH
_HASH.fields_by_name['type'].enum_type = _HASH_HASHTYPE
_HASH_HASHTYPE.containing_type = _HASH
_REPOSOURCE.oneofs_by_name['revision'].fields.append(
  _REPOSOURCE.fields_by_name['branch_name'])
_REPOSOURCE.fields_by_name['branch_name'].containing_oneof = _REPOSOURCE.oneofs_by_name['revision']
_REPOSOURCE.oneofs_by_name['revision'].fields.append(
  _REPOSOURCE.fields_by_name['tag_name'])
_REPOSOURCE.fields_by_name['tag_name'].containing_oneof = _REPOSOURCE.oneofs_by_name['revision']
_REPOSOURCE.oneofs_by_name['revision'].fields.append(
  _REPOSOURCE.fields_by_name['commit_sha'])
_REPOSOURCE.fields_by_name['commit_sha'].containing_oneof = _REPOSOURCE.oneofs_by_name['revision']
DESCRIPTOR.message_types_by_name['BuildProvenance'] = _BUILDPROVENANCE
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['FileHashes'] = _FILEHASHES
DESCRIPTOR.message_types_by_name['Hash'] = _HASH
DESCRIPTOR.message_types_by_name['StorageSource'] = _STORAGESOURCE
DESCRIPTOR.message_types_by_name['RepoSource'] = _REPOSOURCE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildProvenance = _reflection.GeneratedProtocolMessageType('BuildProvenance', (_message.Message,), {

  'BuildOptionsEntry' : _reflection.GeneratedProtocolMessageType('BuildOptionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BUILDPROVENANCE_BUILDOPTIONSENTRY,
    '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.BuildProvenance.BuildOptionsEntry)
    })
  ,
  'DESCRIPTOR' : _BUILDPROVENANCE,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.BuildProvenance)
  })
_sym_db.RegisterMessage(BuildProvenance)
_sym_db.RegisterMessage(BuildProvenance.BuildOptionsEntry)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {

  'FileHashesEntry' : _reflection.GeneratedProtocolMessageType('FileHashesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SOURCE_FILEHASHESENTRY,
    '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.Source.FileHashesEntry)
    })
  ,
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.Source)
  })
_sym_db.RegisterMessage(Source)
_sym_db.RegisterMessage(Source.FileHashesEntry)

FileHashes = _reflection.GeneratedProtocolMessageType('FileHashes', (_message.Message,), {
  'DESCRIPTOR' : _FILEHASHES,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.FileHashes)
  })
_sym_db.RegisterMessage(FileHashes)

Hash = _reflection.GeneratedProtocolMessageType('Hash', (_message.Message,), {
  'DESCRIPTOR' : _HASH,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.Hash)
  })
_sym_db.RegisterMessage(Hash)

StorageSource = _reflection.GeneratedProtocolMessageType('StorageSource', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESOURCE,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.StorageSource)
  })
_sym_db.RegisterMessage(StorageSource)

RepoSource = _reflection.GeneratedProtocolMessageType('RepoSource', (_message.Message,), {
  'DESCRIPTOR' : _REPOSOURCE,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.RepoSource)
  })
_sym_db.RegisterMessage(RepoSource)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.Command)
  })
_sym_db.RegisterMessage(Command)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.provenance_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.Artifact)
  })
_sym_db.RegisterMessage(Artifact)


DESCRIPTOR._options = None
_BUILDPROVENANCE_BUILDOPTIONSENTRY._options = None
_SOURCE_FILEHASHESENTRY._options = None
# @@protoc_insertion_point(module_scope)
