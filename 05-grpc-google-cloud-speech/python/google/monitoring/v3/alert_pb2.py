# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/v3/alert.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
from google.monitoring.v3 import mutation_record_pb2 as google_dot_monitoring_dot_v3_dot_mutation__record__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/v3/alert.proto',
  package='google.monitoring.v3',
  syntax='proto3',
  serialized_options=b'\n\030com.google.monitoring.v3B\nAlertProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3',
  serialized_pb=b'\n google/monitoring/v3/alert.proto\x12\x14google.monitoring.v3\x1a!google/monitoring/v3/common.proto\x1a*google/monitoring/v3/mutation_record.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"\x83\r\n\x0b\x41lertPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x46\n\rdocumentation\x18\r \x01(\x0b\x32/.google.monitoring.v3.AlertPolicy.Documentation\x12\x46\n\x0buser_labels\x18\x10 \x03(\x0b\x32\x31.google.monitoring.v3.AlertPolicy.UserLabelsEntry\x12?\n\nconditions\x18\x0c \x03(\x0b\x32+.google.monitoring.v3.AlertPolicy.Condition\x12I\n\x08\x63ombiner\x18\x06 \x01(\x0e\x32\x37.google.monitoring.v3.AlertPolicy.ConditionCombinerType\x12+\n\x07\x65nabled\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12$\n\x08validity\x18\x12 \x01(\x0b\x32\x12.google.rpc.Status\x12\x1d\n\x15notification_channels\x18\x0e \x03(\t\x12=\n\x0f\x63reation_record\x18\n \x01(\x0b\x32$.google.monitoring.v3.MutationRecord\x12=\n\x0fmutation_record\x18\x0b \x01(\x0b\x32$.google.monitoring.v3.MutationRecord\x1a\x33\n\rDocumentation\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t\x1a\xf8\x06\n\tCondition\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x06 \x01(\t\x12Z\n\x13\x63ondition_threshold\x18\x01 \x01(\x0b\x32;.google.monitoring.v3.AlertPolicy.Condition.MetricThresholdH\x00\x12U\n\x10\x63ondition_absent\x18\x02 \x01(\x0b\x32\x39.google.monitoring.v3.AlertPolicy.Condition.MetricAbsenceH\x00\x1a\x35\n\x07Trigger\x12\x0f\n\x05\x63ount\x18\x01 \x01(\x05H\x00\x12\x11\n\x07percent\x18\x02 \x01(\x01H\x00\x42\x06\n\x04type\x1a\x81\x03\n\x0fMetricThreshold\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x37\n\x0c\x61ggregations\x18\x08 \x03(\x0b\x32!.google.monitoring.v3.Aggregation\x12\x1a\n\x12\x64\x65nominator_filter\x18\t \x01(\t\x12\x43\n\x18\x64\x65nominator_aggregations\x18\n \x03(\x0b\x32!.google.monitoring.v3.Aggregation\x12\x38\n\ncomparison\x18\x04 \x01(\x0e\x32$.google.monitoring.v3.ComparisonType\x12\x17\n\x0fthreshold_value\x18\x05 \x01(\x01\x12+\n\x08\x64uration\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x44\n\x07trigger\x18\x07 \x01(\x0b\x32\x33.google.monitoring.v3.AlertPolicy.Condition.Trigger\x1a\xcb\x01\n\rMetricAbsence\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x37\n\x0c\x61ggregations\x18\x05 \x03(\x0b\x32!.google.monitoring.v3.Aggregation\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x44\n\x07trigger\x18\x03 \x01(\x0b\x32\x33.google.monitoring.v3.AlertPolicy.Condition.TriggerB\x0b\n\tcondition\x1a\x31\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"a\n\x15\x43onditionCombinerType\x12\x17\n\x13\x43OMBINE_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41ND\x10\x01\x12\x06\n\x02OR\x10\x02\x12\x1e\n\x1a\x41ND_WITH_MATCHING_RESOURCE\x10\x03\x42\xa2\x01\n\x18\x63om.google.monitoring.v3B\nAlertProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3'
  ,
  dependencies=[google_dot_monitoring_dot_v3_dot_common__pb2.DESCRIPTOR,google_dot_monitoring_dot_v3_dot_mutation__record__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])



_ALERTPOLICY_CONDITIONCOMBINERTYPE = _descriptor.EnumDescriptor(
  name='ConditionCombinerType',
  full_name='google.monitoring.v3.AlertPolicy.ConditionCombinerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMBINE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AND_WITH_MATCHING_RESOURCE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1797,
  serialized_end=1894,
)
_sym_db.RegisterEnumDescriptor(_ALERTPOLICY_CONDITIONCOMBINERTYPE)


_ALERTPOLICY_DOCUMENTATION = _descriptor.Descriptor(
  name='Documentation',
  full_name='google.monitoring.v3.AlertPolicy.Documentation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='google.monitoring.v3.AlertPolicy.Documentation.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.monitoring.v3.AlertPolicy.Documentation.mime_type', index=1,
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
  serialized_start=802,
  serialized_end=853,
)

_ALERTPOLICY_CONDITION_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='google.monitoring.v3.AlertPolicy.Condition.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='google.monitoring.v3.AlertPolicy.Condition.Trigger.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent', full_name='google.monitoring.v3.AlertPolicy.Condition.Trigger.percent', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
      name='type', full_name='google.monitoring.v3.AlertPolicy.Condition.Trigger.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1084,
  serialized_end=1137,
)

_ALERTPOLICY_CONDITION_METRICTHRESHOLD = _descriptor.Descriptor(
  name='MetricThreshold',
  full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.filter', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregations', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.aggregations', index=1,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denominator_filter', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.denominator_filter', index=2,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denominator_aggregations', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.denominator_aggregations', index=3,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comparison', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.comparison', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold_value', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.threshold_value', index=5,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.duration', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.trigger', index=7,
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
  serialized_start=1140,
  serialized_end=1525,
)

_ALERTPOLICY_CONDITION_METRICABSENCE = _descriptor.Descriptor(
  name='MetricAbsence',
  full_name='google.monitoring.v3.AlertPolicy.Condition.MetricAbsence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricAbsence.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregations', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricAbsence.aggregations', index=1,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricAbsence.duration', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='google.monitoring.v3.AlertPolicy.Condition.MetricAbsence.trigger', index=3,
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
  ],
  serialized_start=1528,
  serialized_end=1731,
)

_ALERTPOLICY_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='google.monitoring.v3.AlertPolicy.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.monitoring.v3.AlertPolicy.Condition.name', index=0,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.monitoring.v3.AlertPolicy.Condition.display_name', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition_threshold', full_name='google.monitoring.v3.AlertPolicy.Condition.condition_threshold', index=2,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition_absent', full_name='google.monitoring.v3.AlertPolicy.Condition.condition_absent', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTPOLICY_CONDITION_TRIGGER, _ALERTPOLICY_CONDITION_METRICTHRESHOLD, _ALERTPOLICY_CONDITION_METRICABSENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='condition', full_name='google.monitoring.v3.AlertPolicy.Condition.condition',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=856,
  serialized_end=1744,
)

_ALERTPOLICY_USERLABELSENTRY = _descriptor.Descriptor(
  name='UserLabelsEntry',
  full_name='google.monitoring.v3.AlertPolicy.UserLabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.monitoring.v3.AlertPolicy.UserLabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.monitoring.v3.AlertPolicy.UserLabelsEntry.value', index=1,
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
  serialized_start=1746,
  serialized_end=1795,
)

_ALERTPOLICY = _descriptor.Descriptor(
  name='AlertPolicy',
  full_name='google.monitoring.v3.AlertPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.monitoring.v3.AlertPolicy.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.monitoring.v3.AlertPolicy.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='documentation', full_name='google.monitoring.v3.AlertPolicy.documentation', index=2,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_labels', full_name='google.monitoring.v3.AlertPolicy.user_labels', index=3,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='google.monitoring.v3.AlertPolicy.conditions', index=4,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combiner', full_name='google.monitoring.v3.AlertPolicy.combiner', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='google.monitoring.v3.AlertPolicy.enabled', index=6,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validity', full_name='google.monitoring.v3.AlertPolicy.validity', index=7,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notification_channels', full_name='google.monitoring.v3.AlertPolicy.notification_channels', index=8,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_record', full_name='google.monitoring.v3.AlertPolicy.creation_record', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutation_record', full_name='google.monitoring.v3.AlertPolicy.mutation_record', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTPOLICY_DOCUMENTATION, _ALERTPOLICY_CONDITION, _ALERTPOLICY_USERLABELSENTRY, ],
  enum_types=[
    _ALERTPOLICY_CONDITIONCOMBINERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=1894,
)

_ALERTPOLICY_DOCUMENTATION.containing_type = _ALERTPOLICY
_ALERTPOLICY_CONDITION_TRIGGER.containing_type = _ALERTPOLICY_CONDITION
_ALERTPOLICY_CONDITION_TRIGGER.oneofs_by_name['type'].fields.append(
  _ALERTPOLICY_CONDITION_TRIGGER.fields_by_name['count'])
_ALERTPOLICY_CONDITION_TRIGGER.fields_by_name['count'].containing_oneof = _ALERTPOLICY_CONDITION_TRIGGER.oneofs_by_name['type']
_ALERTPOLICY_CONDITION_TRIGGER.oneofs_by_name['type'].fields.append(
  _ALERTPOLICY_CONDITION_TRIGGER.fields_by_name['percent'])
_ALERTPOLICY_CONDITION_TRIGGER.fields_by_name['percent'].containing_oneof = _ALERTPOLICY_CONDITION_TRIGGER.oneofs_by_name['type']
_ALERTPOLICY_CONDITION_METRICTHRESHOLD.fields_by_name['aggregations'].message_type = google_dot_monitoring_dot_v3_dot_common__pb2._AGGREGATION
_ALERTPOLICY_CONDITION_METRICTHRESHOLD.fields_by_name['denominator_aggregations'].message_type = google_dot_monitoring_dot_v3_dot_common__pb2._AGGREGATION
_ALERTPOLICY_CONDITION_METRICTHRESHOLD.fields_by_name['comparison'].enum_type = google_dot_monitoring_dot_v3_dot_common__pb2._COMPARISONTYPE
_ALERTPOLICY_CONDITION_METRICTHRESHOLD.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_ALERTPOLICY_CONDITION_METRICTHRESHOLD.fields_by_name['trigger'].message_type = _ALERTPOLICY_CONDITION_TRIGGER
_ALERTPOLICY_CONDITION_METRICTHRESHOLD.containing_type = _ALERTPOLICY_CONDITION
_ALERTPOLICY_CONDITION_METRICABSENCE.fields_by_name['aggregations'].message_type = google_dot_monitoring_dot_v3_dot_common__pb2._AGGREGATION
_ALERTPOLICY_CONDITION_METRICABSENCE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_ALERTPOLICY_CONDITION_METRICABSENCE.fields_by_name['trigger'].message_type = _ALERTPOLICY_CONDITION_TRIGGER
_ALERTPOLICY_CONDITION_METRICABSENCE.containing_type = _ALERTPOLICY_CONDITION
_ALERTPOLICY_CONDITION.fields_by_name['condition_threshold'].message_type = _ALERTPOLICY_CONDITION_METRICTHRESHOLD
_ALERTPOLICY_CONDITION.fields_by_name['condition_absent'].message_type = _ALERTPOLICY_CONDITION_METRICABSENCE
_ALERTPOLICY_CONDITION.containing_type = _ALERTPOLICY
_ALERTPOLICY_CONDITION.oneofs_by_name['condition'].fields.append(
  _ALERTPOLICY_CONDITION.fields_by_name['condition_threshold'])
_ALERTPOLICY_CONDITION.fields_by_name['condition_threshold'].containing_oneof = _ALERTPOLICY_CONDITION.oneofs_by_name['condition']
_ALERTPOLICY_CONDITION.oneofs_by_name['condition'].fields.append(
  _ALERTPOLICY_CONDITION.fields_by_name['condition_absent'])
_ALERTPOLICY_CONDITION.fields_by_name['condition_absent'].containing_oneof = _ALERTPOLICY_CONDITION.oneofs_by_name['condition']
_ALERTPOLICY_USERLABELSENTRY.containing_type = _ALERTPOLICY
_ALERTPOLICY.fields_by_name['documentation'].message_type = _ALERTPOLICY_DOCUMENTATION
_ALERTPOLICY.fields_by_name['user_labels'].message_type = _ALERTPOLICY_USERLABELSENTRY
_ALERTPOLICY.fields_by_name['conditions'].message_type = _ALERTPOLICY_CONDITION
_ALERTPOLICY.fields_by_name['combiner'].enum_type = _ALERTPOLICY_CONDITIONCOMBINERTYPE
_ALERTPOLICY.fields_by_name['enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_ALERTPOLICY.fields_by_name['validity'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_ALERTPOLICY.fields_by_name['creation_record'].message_type = google_dot_monitoring_dot_v3_dot_mutation__record__pb2._MUTATIONRECORD
_ALERTPOLICY.fields_by_name['mutation_record'].message_type = google_dot_monitoring_dot_v3_dot_mutation__record__pb2._MUTATIONRECORD
_ALERTPOLICY_CONDITIONCOMBINERTYPE.containing_type = _ALERTPOLICY
DESCRIPTOR.message_types_by_name['AlertPolicy'] = _ALERTPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertPolicy = _reflection.GeneratedProtocolMessageType('AlertPolicy', (_message.Message,), {

  'Documentation' : _reflection.GeneratedProtocolMessageType('Documentation', (_message.Message,), {
    'DESCRIPTOR' : _ALERTPOLICY_DOCUMENTATION,
    '__module__' : 'google.monitoring.v3.alert_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy.Documentation)
    })
  ,

  'Condition' : _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {

    'Trigger' : _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
      'DESCRIPTOR' : _ALERTPOLICY_CONDITION_TRIGGER,
      '__module__' : 'google.monitoring.v3.alert_pb2'
      # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy.Condition.Trigger)
      })
    ,

    'MetricThreshold' : _reflection.GeneratedProtocolMessageType('MetricThreshold', (_message.Message,), {
      'DESCRIPTOR' : _ALERTPOLICY_CONDITION_METRICTHRESHOLD,
      '__module__' : 'google.monitoring.v3.alert_pb2'
      # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy.Condition.MetricThreshold)
      })
    ,

    'MetricAbsence' : _reflection.GeneratedProtocolMessageType('MetricAbsence', (_message.Message,), {
      'DESCRIPTOR' : _ALERTPOLICY_CONDITION_METRICABSENCE,
      '__module__' : 'google.monitoring.v3.alert_pb2'
      # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy.Condition.MetricAbsence)
      })
    ,
    'DESCRIPTOR' : _ALERTPOLICY_CONDITION,
    '__module__' : 'google.monitoring.v3.alert_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy.Condition)
    })
  ,

  'UserLabelsEntry' : _reflection.GeneratedProtocolMessageType('UserLabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALERTPOLICY_USERLABELSENTRY,
    '__module__' : 'google.monitoring.v3.alert_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy.UserLabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ALERTPOLICY,
  '__module__' : 'google.monitoring.v3.alert_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.v3.AlertPolicy)
  })
_sym_db.RegisterMessage(AlertPolicy)
_sym_db.RegisterMessage(AlertPolicy.Documentation)
_sym_db.RegisterMessage(AlertPolicy.Condition)
_sym_db.RegisterMessage(AlertPolicy.Condition.Trigger)
_sym_db.RegisterMessage(AlertPolicy.Condition.MetricThreshold)
_sym_db.RegisterMessage(AlertPolicy.Condition.MetricAbsence)
_sym_db.RegisterMessage(AlertPolicy.UserLabelsEntry)


DESCRIPTOR._options = None
_ALERTPOLICY_USERLABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
