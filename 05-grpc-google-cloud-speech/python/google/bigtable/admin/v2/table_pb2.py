# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/admin/v2/table.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bigtable/admin/v2/table.proto',
  package='google.bigtable.admin.v2',
  syntax='proto3',
  serialized_options=b'\n\034com.google.bigtable.admin.v2B\nTableProtoP\001Z=google.golang.org/genproto/googleapis/bigtable/admin/v2;admin\252\002\036Google.Cloud.Bigtable.Admin.V2\312\002\036Google\\Cloud\\Bigtable\\Admin\\V2',
  serialized_pb=b'\n$google/bigtable/admin/v2/table.proto\x12\x18google.bigtable.admin.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcb\x06\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12J\n\x0e\x63luster_states\x18\x02 \x03(\x0b\x32\x32.google.bigtable.admin.v2.Table.ClusterStatesEntry\x12L\n\x0f\x63olumn_families\x18\x03 \x03(\x0b\x32\x33.google.bigtable.admin.v2.Table.ColumnFamiliesEntry\x12I\n\x0bgranularity\x18\x04 \x01(\x0e\x32\x34.google.bigtable.admin.v2.Table.TimestampGranularity\x1a\xe2\x01\n\x0c\x43lusterState\x12X\n\x11replication_state\x18\x01 \x01(\x0e\x32=.google.bigtable.admin.v2.Table.ClusterState.ReplicationState\"x\n\x10ReplicationState\x12\x13\n\x0fSTATE_NOT_KNOWN\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x17\n\x13PLANNED_MAINTENANCE\x10\x02\x12\x19\n\x15UNPLANNED_MAINTENANCE\x10\x03\x12\t\n\x05READY\x10\x04\x1a\x62\n\x12\x43lusterStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.google.bigtable.admin.v2.Table.ClusterState:\x02\x38\x01\x1a]\n\x13\x43olumnFamiliesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.google.bigtable.admin.v2.ColumnFamily:\x02\x38\x01\"I\n\x14TimestampGranularity\x12%\n!TIMESTAMP_GRANULARITY_UNSPECIFIED\x10\x00\x12\n\n\x06MILLIS\x10\x01\"\\\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\r\n\tNAME_ONLY\x10\x01\x12\x0f\n\x0bSCHEMA_VIEW\x10\x02\x12\x14\n\x10REPLICATION_VIEW\x10\x03\x12\x08\n\x04\x46ULL\x10\x04\"A\n\x0c\x43olumnFamily\x12\x31\n\x07gc_rule\x18\x01 \x01(\x0b\x32 .google.bigtable.admin.v2.GcRule\"\xd5\x02\n\x06GcRule\x12\x1a\n\x10max_num_versions\x18\x01 \x01(\x05H\x00\x12,\n\x07max_age\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x45\n\x0cintersection\x18\x03 \x01(\x0b\x32-.google.bigtable.admin.v2.GcRule.IntersectionH\x00\x12\x37\n\x05union\x18\x04 \x01(\x0b\x32&.google.bigtable.admin.v2.GcRule.UnionH\x00\x1a?\n\x0cIntersection\x12/\n\x05rules\x18\x01 \x03(\x0b\x32 .google.bigtable.admin.v2.GcRule\x1a\x38\n\x05Union\x12/\n\x05rules\x18\x01 \x03(\x0b\x32 .google.bigtable.admin.v2.GcRuleB\x06\n\x04rule\"\xcf\x02\n\x08Snapshot\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x0csource_table\x18\x02 \x01(\x0b\x32\x1f.google.bigtable.admin.v2.Table\x12\x17\n\x0f\x64\x61ta_size_bytes\x18\x03 \x01(\x03\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x64\x65lete_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x05state\x18\x06 \x01(\x0e\x32(.google.bigtable.admin.v2.Snapshot.State\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\"5\n\x05State\x12\x13\n\x0fSTATE_NOT_KNOWN\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08\x43REATING\x10\x02\x42\xad\x01\n\x1c\x63om.google.bigtable.admin.v2B\nTableProtoP\x01Z=google.golang.org/genproto/googleapis/bigtable/admin/v2;admin\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_TABLE_CLUSTERSTATE_REPLICATIONSTATE = _descriptor.EnumDescriptor(
  name='ReplicationState',
  full_name='google.bigtable.admin.v2.Table.ClusterState.ReplicationState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_NOT_KNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANNED_MAINTENANCE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNPLANNED_MAINTENANCE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=521,
  serialized_end=641,
)
_sym_db.RegisterEnumDescriptor(_TABLE_CLUSTERSTATE_REPLICATIONSTATE)

_TABLE_TIMESTAMPGRANULARITY = _descriptor.EnumDescriptor(
  name='TimestampGranularity',
  full_name='google.bigtable.admin.v2.Table.TimestampGranularity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP_GRANULARITY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLIS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=838,
  serialized_end=911,
)
_sym_db.RegisterEnumDescriptor(_TABLE_TIMESTAMPGRANULARITY)

_TABLE_VIEW = _descriptor.EnumDescriptor(
  name='View',
  full_name='google.bigtable.admin.v2.Table.View',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_ONLY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCHEMA_VIEW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLICATION_VIEW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=913,
  serialized_end=1005,
)
_sym_db.RegisterEnumDescriptor(_TABLE_VIEW)

_SNAPSHOT_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.bigtable.admin.v2.Snapshot.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_NOT_KNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1701,
  serialized_end=1754,
)
_sym_db.RegisterEnumDescriptor(_SNAPSHOT_STATE)


_TABLE_CLUSTERSTATE = _descriptor.Descriptor(
  name='ClusterState',
  full_name='google.bigtable.admin.v2.Table.ClusterState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replication_state', full_name='google.bigtable.admin.v2.Table.ClusterState.replication_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TABLE_CLUSTERSTATE_REPLICATIONSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=641,
)

_TABLE_CLUSTERSTATESENTRY = _descriptor.Descriptor(
  name='ClusterStatesEntry',
  full_name='google.bigtable.admin.v2.Table.ClusterStatesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.bigtable.admin.v2.Table.ClusterStatesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.bigtable.admin.v2.Table.ClusterStatesEntry.value', index=1,
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
  serialized_start=643,
  serialized_end=741,
)

_TABLE_COLUMNFAMILIESENTRY = _descriptor.Descriptor(
  name='ColumnFamiliesEntry',
  full_name='google.bigtable.admin.v2.Table.ColumnFamiliesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.bigtable.admin.v2.Table.ColumnFamiliesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.bigtable.admin.v2.Table.ColumnFamiliesEntry.value', index=1,
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
  serialized_start=743,
  serialized_end=836,
)

_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='google.bigtable.admin.v2.Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.Table.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_states', full_name='google.bigtable.admin.v2.Table.cluster_states', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_families', full_name='google.bigtable.admin.v2.Table.column_families', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='google.bigtable.admin.v2.Table.granularity', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TABLE_CLUSTERSTATE, _TABLE_CLUSTERSTATESENTRY, _TABLE_COLUMNFAMILIESENTRY, ],
  enum_types=[
    _TABLE_TIMESTAMPGRANULARITY,
    _TABLE_VIEW,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=1005,
)


_COLUMNFAMILY = _descriptor.Descriptor(
  name='ColumnFamily',
  full_name='google.bigtable.admin.v2.ColumnFamily',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gc_rule', full_name='google.bigtable.admin.v2.ColumnFamily.gc_rule', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1007,
  serialized_end=1072,
)


_GCRULE_INTERSECTION = _descriptor.Descriptor(
  name='Intersection',
  full_name='google.bigtable.admin.v2.GcRule.Intersection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='google.bigtable.admin.v2.GcRule.Intersection.rules', index=0,
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
  serialized_start=1287,
  serialized_end=1350,
)

_GCRULE_UNION = _descriptor.Descriptor(
  name='Union',
  full_name='google.bigtable.admin.v2.GcRule.Union',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='google.bigtable.admin.v2.GcRule.Union.rules', index=0,
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
  serialized_start=1352,
  serialized_end=1408,
)

_GCRULE = _descriptor.Descriptor(
  name='GcRule',
  full_name='google.bigtable.admin.v2.GcRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_num_versions', full_name='google.bigtable.admin.v2.GcRule.max_num_versions', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_age', full_name='google.bigtable.admin.v2.GcRule.max_age', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intersection', full_name='google.bigtable.admin.v2.GcRule.intersection', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union', full_name='google.bigtable.admin.v2.GcRule.union', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GCRULE_INTERSECTION, _GCRULE_UNION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='rule', full_name='google.bigtable.admin.v2.GcRule.rule',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1075,
  serialized_end=1416,
)


_SNAPSHOT = _descriptor.Descriptor(
  name='Snapshot',
  full_name='google.bigtable.admin.v2.Snapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.Snapshot.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_table', full_name='google.bigtable.admin.v2.Snapshot.source_table', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_size_bytes', full_name='google.bigtable.admin.v2.Snapshot.data_size_bytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.bigtable.admin.v2.Snapshot.create_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_time', full_name='google.bigtable.admin.v2.Snapshot.delete_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.bigtable.admin.v2.Snapshot.state', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.bigtable.admin.v2.Snapshot.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SNAPSHOT_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1419,
  serialized_end=1754,
)

_TABLE_CLUSTERSTATE.fields_by_name['replication_state'].enum_type = _TABLE_CLUSTERSTATE_REPLICATIONSTATE
_TABLE_CLUSTERSTATE.containing_type = _TABLE
_TABLE_CLUSTERSTATE_REPLICATIONSTATE.containing_type = _TABLE_CLUSTERSTATE
_TABLE_CLUSTERSTATESENTRY.fields_by_name['value'].message_type = _TABLE_CLUSTERSTATE
_TABLE_CLUSTERSTATESENTRY.containing_type = _TABLE
_TABLE_COLUMNFAMILIESENTRY.fields_by_name['value'].message_type = _COLUMNFAMILY
_TABLE_COLUMNFAMILIESENTRY.containing_type = _TABLE
_TABLE.fields_by_name['cluster_states'].message_type = _TABLE_CLUSTERSTATESENTRY
_TABLE.fields_by_name['column_families'].message_type = _TABLE_COLUMNFAMILIESENTRY
_TABLE.fields_by_name['granularity'].enum_type = _TABLE_TIMESTAMPGRANULARITY
_TABLE_TIMESTAMPGRANULARITY.containing_type = _TABLE
_TABLE_VIEW.containing_type = _TABLE
_COLUMNFAMILY.fields_by_name['gc_rule'].message_type = _GCRULE
_GCRULE_INTERSECTION.fields_by_name['rules'].message_type = _GCRULE
_GCRULE_INTERSECTION.containing_type = _GCRULE
_GCRULE_UNION.fields_by_name['rules'].message_type = _GCRULE
_GCRULE_UNION.containing_type = _GCRULE
_GCRULE.fields_by_name['max_age'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GCRULE.fields_by_name['intersection'].message_type = _GCRULE_INTERSECTION
_GCRULE.fields_by_name['union'].message_type = _GCRULE_UNION
_GCRULE.oneofs_by_name['rule'].fields.append(
  _GCRULE.fields_by_name['max_num_versions'])
_GCRULE.fields_by_name['max_num_versions'].containing_oneof = _GCRULE.oneofs_by_name['rule']
_GCRULE.oneofs_by_name['rule'].fields.append(
  _GCRULE.fields_by_name['max_age'])
_GCRULE.fields_by_name['max_age'].containing_oneof = _GCRULE.oneofs_by_name['rule']
_GCRULE.oneofs_by_name['rule'].fields.append(
  _GCRULE.fields_by_name['intersection'])
_GCRULE.fields_by_name['intersection'].containing_oneof = _GCRULE.oneofs_by_name['rule']
_GCRULE.oneofs_by_name['rule'].fields.append(
  _GCRULE.fields_by_name['union'])
_GCRULE.fields_by_name['union'].containing_oneof = _GCRULE.oneofs_by_name['rule']
_SNAPSHOT.fields_by_name['source_table'].message_type = _TABLE
_SNAPSHOT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SNAPSHOT.fields_by_name['delete_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SNAPSHOT.fields_by_name['state'].enum_type = _SNAPSHOT_STATE
_SNAPSHOT_STATE.containing_type = _SNAPSHOT
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['ColumnFamily'] = _COLUMNFAMILY
DESCRIPTOR.message_types_by_name['GcRule'] = _GCRULE
DESCRIPTOR.message_types_by_name['Snapshot'] = _SNAPSHOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {

  'ClusterState' : _reflection.GeneratedProtocolMessageType('ClusterState', (_message.Message,), {
    'DESCRIPTOR' : _TABLE_CLUSTERSTATE,
    '__module__' : 'google.bigtable.admin.v2.table_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Table.ClusterState)
    })
  ,

  'ClusterStatesEntry' : _reflection.GeneratedProtocolMessageType('ClusterStatesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TABLE_CLUSTERSTATESENTRY,
    '__module__' : 'google.bigtable.admin.v2.table_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Table.ClusterStatesEntry)
    })
  ,

  'ColumnFamiliesEntry' : _reflection.GeneratedProtocolMessageType('ColumnFamiliesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TABLE_COLUMNFAMILIESENTRY,
    '__module__' : 'google.bigtable.admin.v2.table_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Table.ColumnFamiliesEntry)
    })
  ,
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'google.bigtable.admin.v2.table_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Table)
  })
_sym_db.RegisterMessage(Table)
_sym_db.RegisterMessage(Table.ClusterState)
_sym_db.RegisterMessage(Table.ClusterStatesEntry)
_sym_db.RegisterMessage(Table.ColumnFamiliesEntry)

ColumnFamily = _reflection.GeneratedProtocolMessageType('ColumnFamily', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNFAMILY,
  '__module__' : 'google.bigtable.admin.v2.table_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.ColumnFamily)
  })
_sym_db.RegisterMessage(ColumnFamily)

GcRule = _reflection.GeneratedProtocolMessageType('GcRule', (_message.Message,), {

  'Intersection' : _reflection.GeneratedProtocolMessageType('Intersection', (_message.Message,), {
    'DESCRIPTOR' : _GCRULE_INTERSECTION,
    '__module__' : 'google.bigtable.admin.v2.table_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.GcRule.Intersection)
    })
  ,

  'Union' : _reflection.GeneratedProtocolMessageType('Union', (_message.Message,), {
    'DESCRIPTOR' : _GCRULE_UNION,
    '__module__' : 'google.bigtable.admin.v2.table_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.GcRule.Union)
    })
  ,
  'DESCRIPTOR' : _GCRULE,
  '__module__' : 'google.bigtable.admin.v2.table_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.GcRule)
  })
_sym_db.RegisterMessage(GcRule)
_sym_db.RegisterMessage(GcRule.Intersection)
_sym_db.RegisterMessage(GcRule.Union)

Snapshot = _reflection.GeneratedProtocolMessageType('Snapshot', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOT,
  '__module__' : 'google.bigtable.admin.v2.table_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Snapshot)
  })
_sym_db.RegisterMessage(Snapshot)


DESCRIPTOR._options = None
_TABLE_CLUSTERSTATESENTRY._options = None
_TABLE_COLUMNFAMILIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
