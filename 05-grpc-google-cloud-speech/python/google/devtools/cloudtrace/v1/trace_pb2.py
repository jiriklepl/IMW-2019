# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/cloudtrace/v1/trace.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/cloudtrace/v1/trace.proto',
  package='google.devtools.cloudtrace.v1',
  syntax='proto3',
  serialized_options=b'\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\001ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v1;cloudtrace\252\002\025Google.Cloud.Trace.V1\312\002\025Google\\Cloud\\Trace\\V1',
  serialized_pb=b'\n)google/devtools/cloudtrace/v1/trace.proto\x12\x1dgoogle.devtools.cloudtrace.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"f\n\x05Trace\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08trace_id\x18\x02 \x01(\t\x12\x37\n\x05spans\x18\x03 \x03(\x0b\x32(.google.devtools.cloudtrace.v1.TraceSpan\">\n\x06Traces\x12\x34\n\x06traces\x18\x01 \x03(\x0b\x32$.google.devtools.cloudtrace.v1.Trace\"\xa2\x03\n\tTraceSpan\x12\x0f\n\x07span_id\x18\x01 \x01(\x06\x12?\n\x04kind\x18\x02 \x01(\x0e\x32\x31.google.devtools.cloudtrace.v1.TraceSpan.SpanKind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x0eparent_span_id\x18\x06 \x01(\x06\x42\x03\xe0\x41\x01\x12\x44\n\x06labels\x18\x07 \x03(\x0b\x32\x34.google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x0e\n\nRPC_SERVER\x10\x01\x12\x0e\n\nRPC_CLIENT\x10\x02\"\x80\x03\n\x11ListTracesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12L\n\x04view\x18\x02 \x01(\x0e\x32\x39.google.devtools.cloudtrace.v1.ListTracesRequest.ViewTypeB\x03\xe0\x41\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01\x12\x12\n\npage_token\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x06\x66ilter\x18\x07 \x01(\tB\x03\xe0\x41\x01\x12\x15\n\x08order_by\x18\x08 \x01(\tB\x03\xe0\x41\x01\"N\n\x08ViewType\x12\x19\n\x15VIEW_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MINIMAL\x10\x01\x12\x0c\n\x08ROOTSPAN\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\"c\n\x12ListTracesResponse\x12\x34\n\x06traces\x18\x01 \x03(\x0b\x32$.google.devtools.cloudtrace.v1.Trace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"A\n\x0fGetTraceRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\x08trace_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\"i\n\x12PatchTracesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12:\n\x06traces\x18\x02 \x01(\x0b\x32%.google.devtools.cloudtrace.v1.TracesB\x03\xe0\x41\x02\x32\xb5\x05\n\x0cTraceService\x12\xa8\x01\n\nListTraces\x12\x30.google.devtools.cloudtrace.v1.ListTracesRequest\x1a\x31.google.devtools.cloudtrace.v1.ListTracesResponse\"5\x82\xd3\xe4\x93\x02\"\x12 /v1/projects/{project_id}/traces\xda\x41\nproject_id\x12\xab\x01\n\x08GetTrace\x12..google.devtools.cloudtrace.v1.GetTraceRequest\x1a$.google.devtools.cloudtrace.v1.Trace\"I\x82\xd3\xe4\x93\x02-\x12+/v1/projects/{project_id}/traces/{trace_id}\xda\x41\x13project_id,trace_id\x12\x9e\x01\n\x0bPatchTraces\x12\x31.google.devtools.cloudtrace.v1.PatchTracesRequest\x1a\x16.google.protobuf.Empty\"D\x82\xd3\xe4\x93\x02*2 /v1/projects/{project_id}/traces:\x06traces\xda\x41\x11project_id,traces\x1a\xaa\x01\xca\x41\x19\x63loudtrace.googleapis.com\xd2\x41\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/trace.readonlyB\xaa\x01\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v1;cloudtrace\xaa\x02\x15Google.Cloud.Trace.V1\xca\x02\x15Google\\Cloud\\Trace\\V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_TRACESPAN_SPANKIND = _descriptor.EnumDescriptor(
  name='SpanKind',
  full_name='google.devtools.cloudtrace.v1.TraceSpan.SpanKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RPC_SERVER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RPC_CLIENT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=771,
  serialized_end=840,
)
_sym_db.RegisterEnumDescriptor(_TRACESPAN_SPANKIND)

_LISTTRACESREQUEST_VIEWTYPE = _descriptor.EnumDescriptor(
  name='ViewType',
  full_name='google.devtools.cloudtrace.v1.ListTracesRequest.ViewType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINIMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOTSPAN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1149,
  serialized_end=1227,
)
_sym_db.RegisterEnumDescriptor(_LISTTRACESREQUEST_VIEWTYPE)


_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='google.devtools.cloudtrace.v1.Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.Trace.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='google.devtools.cloudtrace.v1.Trace.trace_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spans', full_name='google.devtools.cloudtrace.v1.Trace.spans', index=2,
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
  serialized_start=253,
  serialized_end=355,
)


_TRACES = _descriptor.Descriptor(
  name='Traces',
  full_name='google.devtools.cloudtrace.v1.Traces',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traces', full_name='google.devtools.cloudtrace.v1.Traces.traces', index=0,
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
  serialized_start=357,
  serialized_end=419,
)


_TRACESPAN_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry.value', index=1,
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
  serialized_start=724,
  serialized_end=769,
)

_TRACESPAN = _descriptor.Descriptor(
  name='TraceSpan',
  full_name='google.devtools.cloudtrace.v1.TraceSpan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='span_id', full_name='google.devtools.cloudtrace.v1.TraceSpan.span_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.devtools.cloudtrace.v1.TraceSpan.kind', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.cloudtrace.v1.TraceSpan.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.devtools.cloudtrace.v1.TraceSpan.start_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.devtools.cloudtrace.v1.TraceSpan.end_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_span_id', full_name='google.devtools.cloudtrace.v1.TraceSpan.parent_span_id', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.devtools.cloudtrace.v1.TraceSpan.labels', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACESPAN_LABELSENTRY, ],
  enum_types=[
    _TRACESPAN_SPANKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=840,
)


_LISTTRACESREQUEST = _descriptor.Descriptor(
  name='ListTracesRequest',
  full_name='google.devtools.cloudtrace.v1.ListTracesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.start_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.end_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.filter', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='google.devtools.cloudtrace.v1.ListTracesRequest.order_by', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTTRACESREQUEST_VIEWTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=843,
  serialized_end=1227,
)


_LISTTRACESRESPONSE = _descriptor.Descriptor(
  name='ListTracesResponse',
  full_name='google.devtools.cloudtrace.v1.ListTracesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traces', full_name='google.devtools.cloudtrace.v1.ListTracesResponse.traces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.devtools.cloudtrace.v1.ListTracesResponse.next_page_token', index=1,
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
  serialized_start=1229,
  serialized_end=1328,
)


_GETTRACEREQUEST = _descriptor.Descriptor(
  name='GetTraceRequest',
  full_name='google.devtools.cloudtrace.v1.GetTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.GetTraceRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='google.devtools.cloudtrace.v1.GetTraceRequest.trace_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
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
  serialized_start=1330,
  serialized_end=1395,
)


_PATCHTRACESREQUEST = _descriptor.Descriptor(
  name='PatchTracesRequest',
  full_name='google.devtools.cloudtrace.v1.PatchTracesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.cloudtrace.v1.PatchTracesRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traces', full_name='google.devtools.cloudtrace.v1.PatchTracesRequest.traces', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
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
  serialized_start=1397,
  serialized_end=1502,
)

_TRACE.fields_by_name['spans'].message_type = _TRACESPAN
_TRACES.fields_by_name['traces'].message_type = _TRACE
_TRACESPAN_LABELSENTRY.containing_type = _TRACESPAN
_TRACESPAN.fields_by_name['kind'].enum_type = _TRACESPAN_SPANKIND
_TRACESPAN.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACESPAN.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACESPAN.fields_by_name['labels'].message_type = _TRACESPAN_LABELSENTRY
_TRACESPAN_SPANKIND.containing_type = _TRACESPAN
_LISTTRACESREQUEST.fields_by_name['view'].enum_type = _LISTTRACESREQUEST_VIEWTYPE
_LISTTRACESREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTRACESREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTRACESREQUEST_VIEWTYPE.containing_type = _LISTTRACESREQUEST
_LISTTRACESRESPONSE.fields_by_name['traces'].message_type = _TRACE
_PATCHTRACESREQUEST.fields_by_name['traces'].message_type = _TRACES
DESCRIPTOR.message_types_by_name['Trace'] = _TRACE
DESCRIPTOR.message_types_by_name['Traces'] = _TRACES
DESCRIPTOR.message_types_by_name['TraceSpan'] = _TRACESPAN
DESCRIPTOR.message_types_by_name['ListTracesRequest'] = _LISTTRACESREQUEST
DESCRIPTOR.message_types_by_name['ListTracesResponse'] = _LISTTRACESRESPONSE
DESCRIPTOR.message_types_by_name['GetTraceRequest'] = _GETTRACEREQUEST
DESCRIPTOR.message_types_by_name['PatchTracesRequest'] = _PATCHTRACESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.Trace)
  })
_sym_db.RegisterMessage(Trace)

Traces = _reflection.GeneratedProtocolMessageType('Traces', (_message.Message,), {
  'DESCRIPTOR' : _TRACES,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.Traces)
  })
_sym_db.RegisterMessage(Traces)

TraceSpan = _reflection.GeneratedProtocolMessageType('TraceSpan', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_LABELSENTRY,
    '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _TRACESPAN,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.TraceSpan)
  })
_sym_db.RegisterMessage(TraceSpan)
_sym_db.RegisterMessage(TraceSpan.LabelsEntry)

ListTracesRequest = _reflection.GeneratedProtocolMessageType('ListTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRACESREQUEST,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.ListTracesRequest)
  })
_sym_db.RegisterMessage(ListTracesRequest)

ListTracesResponse = _reflection.GeneratedProtocolMessageType('ListTracesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRACESRESPONSE,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.ListTracesResponse)
  })
_sym_db.RegisterMessage(ListTracesResponse)

GetTraceRequest = _reflection.GeneratedProtocolMessageType('GetTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRACEREQUEST,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.GetTraceRequest)
  })
_sym_db.RegisterMessage(GetTraceRequest)

PatchTracesRequest = _reflection.GeneratedProtocolMessageType('PatchTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _PATCHTRACESREQUEST,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.PatchTracesRequest)
  })
_sym_db.RegisterMessage(PatchTracesRequest)


DESCRIPTOR._options = None
_TRACESPAN_LABELSENTRY._options = None
_TRACESPAN.fields_by_name['parent_span_id']._options = None
_LISTTRACESREQUEST.fields_by_name['project_id']._options = None
_LISTTRACESREQUEST.fields_by_name['view']._options = None
_LISTTRACESREQUEST.fields_by_name['page_size']._options = None
_LISTTRACESREQUEST.fields_by_name['filter']._options = None
_LISTTRACESREQUEST.fields_by_name['order_by']._options = None
_GETTRACEREQUEST.fields_by_name['project_id']._options = None
_GETTRACEREQUEST.fields_by_name['trace_id']._options = None
_PATCHTRACESREQUEST.fields_by_name['project_id']._options = None
_PATCHTRACESREQUEST.fields_by_name['traces']._options = None

_TRACESERVICE = _descriptor.ServiceDescriptor(
  name='TraceService',
  full_name='google.devtools.cloudtrace.v1.TraceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\031cloudtrace.googleapis.com\322A\212\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/trace.readonly',
  serialized_start=1505,
  serialized_end=2198,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTraces',
    full_name='google.devtools.cloudtrace.v1.TraceService.ListTraces',
    index=0,
    containing_service=None,
    input_type=_LISTTRACESREQUEST,
    output_type=_LISTTRACESRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\022 /v1/projects/{project_id}/traces\332A\nproject_id',
  ),
  _descriptor.MethodDescriptor(
    name='GetTrace',
    full_name='google.devtools.cloudtrace.v1.TraceService.GetTrace',
    index=1,
    containing_service=None,
    input_type=_GETTRACEREQUEST,
    output_type=_TRACE,
    serialized_options=b'\202\323\344\223\002-\022+/v1/projects/{project_id}/traces/{trace_id}\332A\023project_id,trace_id',
  ),
  _descriptor.MethodDescriptor(
    name='PatchTraces',
    full_name='google.devtools.cloudtrace.v1.TraceService.PatchTraces',
    index=2,
    containing_service=None,
    input_type=_PATCHTRACESREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002*2 /v1/projects/{project_id}/traces:\006traces\332A\021project_id,traces',
  ),
])
_sym_db.RegisterServiceDescriptor(_TRACESERVICE)

DESCRIPTOR.services_by_name['TraceService'] = _TRACESERVICE

# @@protoc_insertion_point(module_scope)