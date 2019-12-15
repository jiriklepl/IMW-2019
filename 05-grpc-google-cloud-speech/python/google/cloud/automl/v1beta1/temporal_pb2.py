# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1beta1/temporal.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl/v1beta1/temporal.proto',
  package='google.cloud.automl.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1',
  serialized_pb=b'\n*google/cloud/automl/v1beta1/temporal.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\"w\n\x0bTimeSegment\x12\x34\n\x11start_time_offset\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x32\n\x0f\x65nd_time_offset\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_TIMESEGMENT = _descriptor.Descriptor(
  name='TimeSegment',
  full_name='google.cloud.automl.v1beta1.TimeSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time_offset', full_name='google.cloud.automl.v1beta1.TimeSegment.start_time_offset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time_offset', full_name='google.cloud.automl.v1beta1.TimeSegment.end_time_offset', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=256,
)

_TIMESEGMENT.fields_by_name['start_time_offset'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TIMESEGMENT.fields_by_name['end_time_offset'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['TimeSegment'] = _TIMESEGMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeSegment = _reflection.GeneratedProtocolMessageType('TimeSegment', (_message.Message,), {
  'DESCRIPTOR' : _TIMESEGMENT,
  '__module__' : 'google.cloud.automl.v1beta1.temporal_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TimeSegment)
  })
_sym_db.RegisterMessage(TimeSegment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
