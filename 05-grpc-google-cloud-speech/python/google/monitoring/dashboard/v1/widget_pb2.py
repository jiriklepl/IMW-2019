# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/dashboard/v1/widget.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.monitoring.dashboard.v1 import scorecard_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_scorecard__pb2
from google.monitoring.dashboard.v1 import text_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_text__pb2
from google.monitoring.dashboard.v1 import xychart_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_xychart__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/dashboard/v1/widget.proto',
  package='google.monitoring.dashboard.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.monitoring.dashboard.v1B\013WidgetProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard',
  serialized_pb=b'\n+google/monitoring/dashboard/v1/widget.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/monitoring/dashboard/v1/scorecard.proto\x1a)google/monitoring/dashboard/v1/text.proto\x1a,google/monitoring/dashboard/v1/xychart.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x83\x02\n\x06Widget\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0\x41\x01\x12;\n\x08xy_chart\x18\x02 \x01(\x0b\x32\'.google.monitoring.dashboard.v1.XyChartH\x00\x12>\n\tscorecard\x18\x03 \x01(\x0b\x32).google.monitoring.dashboard.v1.ScorecardH\x00\x12\x34\n\x04text\x18\x04 \x01(\x0b\x32$.google.monitoring.dashboard.v1.TextH\x00\x12\'\n\x05\x62lank\x18\x05 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\t\n\x07\x63ontentB|\n\"com.google.monitoring.dashboard.v1B\x0bWidgetProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboardb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_monitoring_dot_dashboard_dot_v1_dot_scorecard__pb2.DESCRIPTOR,google_dot_monitoring_dot_dashboard_dot_v1_dot_text__pb2.DESCRIPTOR,google_dot_monitoring_dot_dashboard_dot_v1_dot_xychart__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_WIDGET = _descriptor.Descriptor(
  name='Widget',
  full_name='google.monitoring.dashboard.v1.Widget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='google.monitoring.dashboard.v1.Widget.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xy_chart', full_name='google.monitoring.dashboard.v1.Widget.xy_chart', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scorecard', full_name='google.monitoring.dashboard.v1.Widget.scorecard', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.monitoring.dashboard.v1.Widget.text', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blank', full_name='google.monitoring.dashboard.v1.Widget.blank', index=4,
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
    _descriptor.OneofDescriptor(
      name='content', full_name='google.monitoring.dashboard.v1.Widget.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=279,
  serialized_end=538,
)

_WIDGET.fields_by_name['xy_chart'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_xychart__pb2._XYCHART
_WIDGET.fields_by_name['scorecard'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_scorecard__pb2._SCORECARD
_WIDGET.fields_by_name['text'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_text__pb2._TEXT
_WIDGET.fields_by_name['blank'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_WIDGET.oneofs_by_name['content'].fields.append(
  _WIDGET.fields_by_name['xy_chart'])
_WIDGET.fields_by_name['xy_chart'].containing_oneof = _WIDGET.oneofs_by_name['content']
_WIDGET.oneofs_by_name['content'].fields.append(
  _WIDGET.fields_by_name['scorecard'])
_WIDGET.fields_by_name['scorecard'].containing_oneof = _WIDGET.oneofs_by_name['content']
_WIDGET.oneofs_by_name['content'].fields.append(
  _WIDGET.fields_by_name['text'])
_WIDGET.fields_by_name['text'].containing_oneof = _WIDGET.oneofs_by_name['content']
_WIDGET.oneofs_by_name['content'].fields.append(
  _WIDGET.fields_by_name['blank'])
_WIDGET.fields_by_name['blank'].containing_oneof = _WIDGET.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['Widget'] = _WIDGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Widget = _reflection.GeneratedProtocolMessageType('Widget', (_message.Message,), {
  'DESCRIPTOR' : _WIDGET,
  '__module__' : 'google.monitoring.dashboard.v1.widget_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Widget)
  })
_sym_db.RegisterMessage(Widget)


DESCRIPTOR._options = None
_WIDGET.fields_by_name['title']._options = None
# @@protoc_insertion_point(module_scope)
