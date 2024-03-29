# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/containeranalysis/v1alpha1/source_context.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/containeranalysis/v1alpha1/source_context.proto',
  package='google.devtools.containeranalysis.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n%com.google.containeranalysis.v1alpha1P\001Z[google.golang.org/genproto/googleapis/devtools/containeranalysis/v1alpha1;containeranalysis\242\002\003GCA',
  serialized_pb=b'\n?google/devtools/containeranalysis/v1alpha1/source_context.proto\x12*google.devtools.containeranalysis.v1alpha1\x1a\x1cgoogle/api/annotations.proto\"\x9a\x03\n\rSourceContext\x12X\n\ncloud_repo\x18\x01 \x01(\x0b\x32\x42.google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContextH\x00\x12Q\n\x06gerrit\x18\x02 \x01(\x0b\x32?.google.devtools.containeranalysis.v1alpha1.GerritSourceContextH\x00\x12K\n\x03git\x18\x03 \x01(\x0b\x32<.google.devtools.containeranalysis.v1alpha1.GitSourceContextH\x00\x12U\n\x06labels\x18\x04 \x03(\x0b\x32\x45.google.devtools.containeranalysis.v1alpha1.SourceContext.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07\x63ontext\"\xaa\x01\n\x0c\x41liasContext\x12K\n\x04kind\x18\x01 \x01(\x0e\x32=.google.devtools.containeranalysis.v1alpha1.AliasContext.Kind\x12\x0c\n\x04name\x18\x02 \x01(\t\"?\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\t\n\x05\x46IXED\x10\x01\x12\x0b\n\x07MOVABLE\x10\x02\x12\t\n\x05OTHER\x10\x04\"\xd3\x01\n\x16\x43loudRepoSourceContext\x12\x43\n\x07repo_id\x18\x01 \x01(\x0b\x32\x32.google.devtools.containeranalysis.v1alpha1.RepoId\x12\x15\n\x0brevision_id\x18\x02 \x01(\tH\x00\x12Q\n\ralias_context\x18\x03 \x01(\x0b\x32\x38.google.devtools.containeranalysis.v1alpha1.AliasContextH\x00\x42\n\n\x08revision\"\xb5\x01\n\x13GerritSourceContext\x12\x10\n\x08host_uri\x18\x01 \x01(\t\x12\x16\n\x0egerrit_project\x18\x02 \x01(\t\x12\x15\n\x0brevision_id\x18\x03 \x01(\tH\x00\x12Q\n\ralias_context\x18\x04 \x01(\x0b\x32\x38.google.devtools.containeranalysis.v1alpha1.AliasContextH\x00\x42\n\n\x08revision\"4\n\x10GitSourceContext\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0brevision_id\x18\x02 \x01(\t\"s\n\x06RepoId\x12T\n\x0fproject_repo_id\x18\x01 \x01(\x0b\x32\x39.google.devtools.containeranalysis.v1alpha1.ProjectRepoIdH\x00\x12\r\n\x03uid\x18\x02 \x01(\tH\x00\x42\x04\n\x02id\"6\n\rProjectRepoId\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\trepo_name\x18\x02 \x01(\tB\x8c\x01\n%com.google.containeranalysis.v1alpha1P\x01Z[google.golang.org/genproto/googleapis/devtools/containeranalysis/v1alpha1;containeranalysis\xa2\x02\x03GCAb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ALIASCONTEXT_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='google.devtools.containeranalysis.v1alpha1.AliasContext.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KIND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIXED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVABLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=662,
  serialized_end=725,
)
_sym_db.RegisterEnumDescriptor(_ALIASCONTEXT_KIND)


_SOURCECONTEXT_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.LabelsEntry.value', index=1,
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
  serialized_start=496,
  serialized_end=541,
)

_SOURCECONTEXT = _descriptor.Descriptor(
  name='SourceContext',
  full_name='google.devtools.containeranalysis.v1alpha1.SourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_repo', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.cloud_repo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gerrit', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.gerrit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.git', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SOURCECONTEXT_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='context', full_name='google.devtools.containeranalysis.v1alpha1.SourceContext.context',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=142,
  serialized_end=552,
)


_ALIASCONTEXT = _descriptor.Descriptor(
  name='AliasContext',
  full_name='google.devtools.containeranalysis.v1alpha1.AliasContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.devtools.containeranalysis.v1alpha1.AliasContext.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.containeranalysis.v1alpha1.AliasContext.name', index=1,
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
    _ALIASCONTEXT_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=725,
)


_CLOUDREPOSOURCECONTEXT = _descriptor.Descriptor(
  name='CloudRepoSourceContext',
  full_name='google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_id', full_name='google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContext.repo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContext.revision_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias_context', full_name='google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContext.alias_context', index=2,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='revision', full_name='google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContext.revision',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=728,
  serialized_end=939,
)


_GERRITSOURCECONTEXT = _descriptor.Descriptor(
  name='GerritSourceContext',
  full_name='google.devtools.containeranalysis.v1alpha1.GerritSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_uri', full_name='google.devtools.containeranalysis.v1alpha1.GerritSourceContext.host_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gerrit_project', full_name='google.devtools.containeranalysis.v1alpha1.GerritSourceContext.gerrit_project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.devtools.containeranalysis.v1alpha1.GerritSourceContext.revision_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias_context', full_name='google.devtools.containeranalysis.v1alpha1.GerritSourceContext.alias_context', index=3,
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
      name='revision', full_name='google.devtools.containeranalysis.v1alpha1.GerritSourceContext.revision',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=942,
  serialized_end=1123,
)


_GITSOURCECONTEXT = _descriptor.Descriptor(
  name='GitSourceContext',
  full_name='google.devtools.containeranalysis.v1alpha1.GitSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.devtools.containeranalysis.v1alpha1.GitSourceContext.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.devtools.containeranalysis.v1alpha1.GitSourceContext.revision_id', index=1,
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
  serialized_start=1125,
  serialized_end=1177,
)


_REPOID = _descriptor.Descriptor(
  name='RepoId',
  full_name='google.devtools.containeranalysis.v1alpha1.RepoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_repo_id', full_name='google.devtools.containeranalysis.v1alpha1.RepoId.project_repo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='google.devtools.containeranalysis.v1alpha1.RepoId.uid', index=1,
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
    _descriptor.OneofDescriptor(
      name='id', full_name='google.devtools.containeranalysis.v1alpha1.RepoId.id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1179,
  serialized_end=1294,
)


_PROJECTREPOID = _descriptor.Descriptor(
  name='ProjectRepoId',
  full_name='google.devtools.containeranalysis.v1alpha1.ProjectRepoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.containeranalysis.v1alpha1.ProjectRepoId.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='google.devtools.containeranalysis.v1alpha1.ProjectRepoId.repo_name', index=1,
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
  serialized_start=1296,
  serialized_end=1350,
)

_SOURCECONTEXT_LABELSENTRY.containing_type = _SOURCECONTEXT
_SOURCECONTEXT.fields_by_name['cloud_repo'].message_type = _CLOUDREPOSOURCECONTEXT
_SOURCECONTEXT.fields_by_name['gerrit'].message_type = _GERRITSOURCECONTEXT
_SOURCECONTEXT.fields_by_name['git'].message_type = _GITSOURCECONTEXT
_SOURCECONTEXT.fields_by_name['labels'].message_type = _SOURCECONTEXT_LABELSENTRY
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['cloud_repo'])
_SOURCECONTEXT.fields_by_name['cloud_repo'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['gerrit'])
_SOURCECONTEXT.fields_by_name['gerrit'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['git'])
_SOURCECONTEXT.fields_by_name['git'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_ALIASCONTEXT.fields_by_name['kind'].enum_type = _ALIASCONTEXT_KIND
_ALIASCONTEXT_KIND.containing_type = _ALIASCONTEXT
_CLOUDREPOSOURCECONTEXT.fields_by_name['repo_id'].message_type = _REPOID
_CLOUDREPOSOURCECONTEXT.fields_by_name['alias_context'].message_type = _ALIASCONTEXT
_CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _CLOUDREPOSOURCECONTEXT.fields_by_name['revision_id'])
_CLOUDREPOSOURCECONTEXT.fields_by_name['revision_id'].containing_oneof = _CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision']
_CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _CLOUDREPOSOURCECONTEXT.fields_by_name['alias_context'])
_CLOUDREPOSOURCECONTEXT.fields_by_name['alias_context'].containing_oneof = _CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision']
_GERRITSOURCECONTEXT.fields_by_name['alias_context'].message_type = _ALIASCONTEXT
_GERRITSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _GERRITSOURCECONTEXT.fields_by_name['revision_id'])
_GERRITSOURCECONTEXT.fields_by_name['revision_id'].containing_oneof = _GERRITSOURCECONTEXT.oneofs_by_name['revision']
_GERRITSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _GERRITSOURCECONTEXT.fields_by_name['alias_context'])
_GERRITSOURCECONTEXT.fields_by_name['alias_context'].containing_oneof = _GERRITSOURCECONTEXT.oneofs_by_name['revision']
_REPOID.fields_by_name['project_repo_id'].message_type = _PROJECTREPOID
_REPOID.oneofs_by_name['id'].fields.append(
  _REPOID.fields_by_name['project_repo_id'])
_REPOID.fields_by_name['project_repo_id'].containing_oneof = _REPOID.oneofs_by_name['id']
_REPOID.oneofs_by_name['id'].fields.append(
  _REPOID.fields_by_name['uid'])
_REPOID.fields_by_name['uid'].containing_oneof = _REPOID.oneofs_by_name['id']
DESCRIPTOR.message_types_by_name['SourceContext'] = _SOURCECONTEXT
DESCRIPTOR.message_types_by_name['AliasContext'] = _ALIASCONTEXT
DESCRIPTOR.message_types_by_name['CloudRepoSourceContext'] = _CLOUDREPOSOURCECONTEXT
DESCRIPTOR.message_types_by_name['GerritSourceContext'] = _GERRITSOURCECONTEXT
DESCRIPTOR.message_types_by_name['GitSourceContext'] = _GITSOURCECONTEXT
DESCRIPTOR.message_types_by_name['RepoId'] = _REPOID
DESCRIPTOR.message_types_by_name['ProjectRepoId'] = _PROJECTREPOID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SourceContext = _reflection.GeneratedProtocolMessageType('SourceContext', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SOURCECONTEXT_LABELSENTRY,
    '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.SourceContext.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SOURCECONTEXT,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.SourceContext)
  })
_sym_db.RegisterMessage(SourceContext)
_sym_db.RegisterMessage(SourceContext.LabelsEntry)

AliasContext = _reflection.GeneratedProtocolMessageType('AliasContext', (_message.Message,), {
  'DESCRIPTOR' : _ALIASCONTEXT,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.AliasContext)
  })
_sym_db.RegisterMessage(AliasContext)

CloudRepoSourceContext = _reflection.GeneratedProtocolMessageType('CloudRepoSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDREPOSOURCECONTEXT,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.CloudRepoSourceContext)
  })
_sym_db.RegisterMessage(CloudRepoSourceContext)

GerritSourceContext = _reflection.GeneratedProtocolMessageType('GerritSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _GERRITSOURCECONTEXT,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.GerritSourceContext)
  })
_sym_db.RegisterMessage(GerritSourceContext)

GitSourceContext = _reflection.GeneratedProtocolMessageType('GitSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _GITSOURCECONTEXT,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.GitSourceContext)
  })
_sym_db.RegisterMessage(GitSourceContext)

RepoId = _reflection.GeneratedProtocolMessageType('RepoId', (_message.Message,), {
  'DESCRIPTOR' : _REPOID,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.RepoId)
  })
_sym_db.RegisterMessage(RepoId)

ProjectRepoId = _reflection.GeneratedProtocolMessageType('ProjectRepoId', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTREPOID,
  '__module__' : 'google.devtools.containeranalysis.v1alpha1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.containeranalysis.v1alpha1.ProjectRepoId)
  })
_sym_db.RegisterMessage(ProjectRepoId)


DESCRIPTOR._options = None
_SOURCECONTEXT_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
