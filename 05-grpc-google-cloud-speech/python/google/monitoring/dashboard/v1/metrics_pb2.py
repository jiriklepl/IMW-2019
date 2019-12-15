# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/dashboard/v1/metrics.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.monitoring.dashboard.v1 import common_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/dashboard/v1/metrics.proto',
  package='google.monitoring.dashboard.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.monitoring.dashboard.v1B\014MetricsProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard',
  serialized_pb=b'\n,google/monitoring/dashboard/v1/metrics.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/monitoring/dashboard/v1/common.proto\"\xdd\x01\n\x0fTimeSeriesQuery\x12N\n\x12time_series_filter\x18\x01 \x01(\x0b\x32\x30.google.monitoring.dashboard.v1.TimeSeriesFilterH\x00\x12Y\n\x18time_series_filter_ratio\x18\x02 \x01(\x0b\x32\x35.google.monitoring.dashboard.v1.TimeSeriesFilterRatioH\x00\x12\x15\n\runit_override\x18\x05 \x01(\tB\x08\n\x06source\"\xba\x02\n\x10TimeSeriesFilter\x12\x13\n\x06\x66ilter\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12@\n\x0b\x61ggregation\x18\x02 \x01(\x0b\x32+.google.monitoring.dashboard.v1.Aggregation\x12W\n\x17pick_time_series_filter\x18\x04 \x01(\x0b\x32\x34.google.monitoring.dashboard.v1.PickTimeSeriesFilterH\x00\x12\x65\n\x1estatistical_time_series_filter\x18\x05 \x01(\x0b\x32;.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterH\x00\x42\x0f\n\routput_filter\"\xc2\x04\n\x15TimeSeriesFilterRatio\x12R\n\tnumerator\x18\x01 \x01(\x0b\x32?.google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart\x12T\n\x0b\x64\x65nominator\x18\x02 \x01(\x0b\x32?.google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart\x12J\n\x15secondary_aggregation\x18\x03 \x01(\x0b\x32+.google.monitoring.dashboard.v1.Aggregation\x12W\n\x17pick_time_series_filter\x18\x04 \x01(\x0b\x32\x34.google.monitoring.dashboard.v1.PickTimeSeriesFilterH\x00\x12\x65\n\x1estatistical_time_series_filter\x18\x05 \x01(\x0b\x32;.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterH\x00\x1a\x62\n\tRatioPart\x12\x13\n\x06\x66ilter\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12@\n\x0b\x61ggregation\x18\x02 \x01(\x0b\x32+.google.monitoring.dashboard.v1.AggregationB\x0f\n\routput_filter\"\xa4\x02\n\tThreshold\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12>\n\x05\x63olor\x18\x03 \x01(\x0e\x32/.google.monitoring.dashboard.v1.Threshold.Color\x12\x46\n\tdirection\x18\x04 \x01(\x0e\x32\x33.google.monitoring.dashboard.v1.Threshold.Direction\"3\n\x05\x43olor\x12\x15\n\x11\x43OLOR_UNSPECIFIED\x10\x00\x12\n\n\x06YELLOW\x10\x04\x12\x07\n\x03RED\x10\x06\"<\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\t\n\x05\x41\x42OVE\x10\x01\x12\t\n\x05\x42\x45LOW\x10\x02*Q\n\x0eSparkChartType\x12 \n\x1cSPARK_CHART_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSPARK_LINE\x10\x01\x12\r\n\tSPARK_BAR\x10\x02\x42}\n\"com.google.monitoring.dashboard.v1B\x0cMetricsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboardb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2.DESCRIPTOR,])

_SPARKCHARTTYPE = _descriptor.EnumDescriptor(
  name='SparkChartType',
  full_name='google.monitoring.dashboard.v1.SparkChartType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPARK_CHART_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPARK_LINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPARK_BAR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1575,
  serialized_end=1656,
)
_sym_db.RegisterEnumDescriptor(_SPARKCHARTTYPE)

SparkChartType = enum_type_wrapper.EnumTypeWrapper(_SPARKCHARTTYPE)
SPARK_CHART_TYPE_UNSPECIFIED = 0
SPARK_LINE = 1
SPARK_BAR = 2


_THRESHOLD_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='google.monitoring.dashboard.v1.Threshold.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=1, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=2, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1460,
  serialized_end=1511,
)
_sym_db.RegisterEnumDescriptor(_THRESHOLD_COLOR)

_THRESHOLD_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='google.monitoring.dashboard.v1.Threshold.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABOVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BELOW', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1513,
  serialized_end=1573,
)
_sym_db.RegisterEnumDescriptor(_THRESHOLD_DIRECTION)


_TIMESERIESQUERY = _descriptor.Descriptor(
  name='TimeSeriesQuery',
  full_name='google.monitoring.dashboard.v1.TimeSeriesQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_series_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesQuery.time_series_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_series_filter_ratio', full_name='google.monitoring.dashboard.v1.TimeSeriesQuery.time_series_filter_ratio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit_override', full_name='google.monitoring.dashboard.v1.TimeSeriesQuery.unit_override', index=2,
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
      name='source', full_name='google.monitoring.dashboard.v1.TimeSeriesQuery.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=159,
  serialized_end=380,
)


_TIMESERIESFILTER = _descriptor.Descriptor(
  name='TimeSeriesFilter',
  full_name='google.monitoring.dashboard.v1.TimeSeriesFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilter.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='google.monitoring.dashboard.v1.TimeSeriesFilter.aggregation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pick_time_series_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilter.pick_time_series_filter', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statistical_time_series_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilter.statistical_time_series_filter', index=3,
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
      name='output_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilter.output_filter',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=383,
  serialized_end=697,
)


_TIMESERIESFILTERRATIO_RATIOPART = _descriptor.Descriptor(
  name='RatioPart',
  full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart.aggregation', index=1,
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
  serialized_start=1163,
  serialized_end=1261,
)

_TIMESERIESFILTERRATIO = _descriptor.Descriptor(
  name='TimeSeriesFilterRatio',
  full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numerator', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.numerator', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denominator', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.denominator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_aggregation', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.secondary_aggregation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pick_time_series_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.pick_time_series_filter', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statistical_time_series_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.statistical_time_series_filter', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIMESERIESFILTERRATIO_RATIOPART, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='output_filter', full_name='google.monitoring.dashboard.v1.TimeSeriesFilterRatio.output_filter',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=700,
  serialized_end=1278,
)


_THRESHOLD = _descriptor.Descriptor(
  name='Threshold',
  full_name='google.monitoring.dashboard.v1.Threshold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='google.monitoring.dashboard.v1.Threshold.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.monitoring.dashboard.v1.Threshold.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='google.monitoring.dashboard.v1.Threshold.color', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='google.monitoring.dashboard.v1.Threshold.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _THRESHOLD_COLOR,
    _THRESHOLD_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1281,
  serialized_end=1573,
)

_TIMESERIESQUERY.fields_by_name['time_series_filter'].message_type = _TIMESERIESFILTER
_TIMESERIESQUERY.fields_by_name['time_series_filter_ratio'].message_type = _TIMESERIESFILTERRATIO
_TIMESERIESQUERY.oneofs_by_name['source'].fields.append(
  _TIMESERIESQUERY.fields_by_name['time_series_filter'])
_TIMESERIESQUERY.fields_by_name['time_series_filter'].containing_oneof = _TIMESERIESQUERY.oneofs_by_name['source']
_TIMESERIESQUERY.oneofs_by_name['source'].fields.append(
  _TIMESERIESQUERY.fields_by_name['time_series_filter_ratio'])
_TIMESERIESQUERY.fields_by_name['time_series_filter_ratio'].containing_oneof = _TIMESERIESQUERY.oneofs_by_name['source']
_TIMESERIESFILTER.fields_by_name['aggregation'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._AGGREGATION
_TIMESERIESFILTER.fields_by_name['pick_time_series_filter'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._PICKTIMESERIESFILTER
_TIMESERIESFILTER.fields_by_name['statistical_time_series_filter'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._STATISTICALTIMESERIESFILTER
_TIMESERIESFILTER.oneofs_by_name['output_filter'].fields.append(
  _TIMESERIESFILTER.fields_by_name['pick_time_series_filter'])
_TIMESERIESFILTER.fields_by_name['pick_time_series_filter'].containing_oneof = _TIMESERIESFILTER.oneofs_by_name['output_filter']
_TIMESERIESFILTER.oneofs_by_name['output_filter'].fields.append(
  _TIMESERIESFILTER.fields_by_name['statistical_time_series_filter'])
_TIMESERIESFILTER.fields_by_name['statistical_time_series_filter'].containing_oneof = _TIMESERIESFILTER.oneofs_by_name['output_filter']
_TIMESERIESFILTERRATIO_RATIOPART.fields_by_name['aggregation'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._AGGREGATION
_TIMESERIESFILTERRATIO_RATIOPART.containing_type = _TIMESERIESFILTERRATIO
_TIMESERIESFILTERRATIO.fields_by_name['numerator'].message_type = _TIMESERIESFILTERRATIO_RATIOPART
_TIMESERIESFILTERRATIO.fields_by_name['denominator'].message_type = _TIMESERIESFILTERRATIO_RATIOPART
_TIMESERIESFILTERRATIO.fields_by_name['secondary_aggregation'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._AGGREGATION
_TIMESERIESFILTERRATIO.fields_by_name['pick_time_series_filter'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._PICKTIMESERIESFILTER
_TIMESERIESFILTERRATIO.fields_by_name['statistical_time_series_filter'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2._STATISTICALTIMESERIESFILTER
_TIMESERIESFILTERRATIO.oneofs_by_name['output_filter'].fields.append(
  _TIMESERIESFILTERRATIO.fields_by_name['pick_time_series_filter'])
_TIMESERIESFILTERRATIO.fields_by_name['pick_time_series_filter'].containing_oneof = _TIMESERIESFILTERRATIO.oneofs_by_name['output_filter']
_TIMESERIESFILTERRATIO.oneofs_by_name['output_filter'].fields.append(
  _TIMESERIESFILTERRATIO.fields_by_name['statistical_time_series_filter'])
_TIMESERIESFILTERRATIO.fields_by_name['statistical_time_series_filter'].containing_oneof = _TIMESERIESFILTERRATIO.oneofs_by_name['output_filter']
_THRESHOLD.fields_by_name['color'].enum_type = _THRESHOLD_COLOR
_THRESHOLD.fields_by_name['direction'].enum_type = _THRESHOLD_DIRECTION
_THRESHOLD_COLOR.containing_type = _THRESHOLD
_THRESHOLD_DIRECTION.containing_type = _THRESHOLD
DESCRIPTOR.message_types_by_name['TimeSeriesQuery'] = _TIMESERIESQUERY
DESCRIPTOR.message_types_by_name['TimeSeriesFilter'] = _TIMESERIESFILTER
DESCRIPTOR.message_types_by_name['TimeSeriesFilterRatio'] = _TIMESERIESFILTERRATIO
DESCRIPTOR.message_types_by_name['Threshold'] = _THRESHOLD
DESCRIPTOR.enum_types_by_name['SparkChartType'] = _SPARKCHARTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeSeriesQuery = _reflection.GeneratedProtocolMessageType('TimeSeriesQuery', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIESQUERY,
  '__module__' : 'google.monitoring.dashboard.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesQuery)
  })
_sym_db.RegisterMessage(TimeSeriesQuery)

TimeSeriesFilter = _reflection.GeneratedProtocolMessageType('TimeSeriesFilter', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIESFILTER,
  '__module__' : 'google.monitoring.dashboard.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesFilter)
  })
_sym_db.RegisterMessage(TimeSeriesFilter)

TimeSeriesFilterRatio = _reflection.GeneratedProtocolMessageType('TimeSeriesFilterRatio', (_message.Message,), {

  'RatioPart' : _reflection.GeneratedProtocolMessageType('RatioPart', (_message.Message,), {
    'DESCRIPTOR' : _TIMESERIESFILTERRATIO_RATIOPART,
    '__module__' : 'google.monitoring.dashboard.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart)
    })
  ,
  'DESCRIPTOR' : _TIMESERIESFILTERRATIO,
  '__module__' : 'google.monitoring.dashboard.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesFilterRatio)
  })
_sym_db.RegisterMessage(TimeSeriesFilterRatio)
_sym_db.RegisterMessage(TimeSeriesFilterRatio.RatioPart)

Threshold = _reflection.GeneratedProtocolMessageType('Threshold', (_message.Message,), {
  'DESCRIPTOR' : _THRESHOLD,
  '__module__' : 'google.monitoring.dashboard.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Threshold)
  })
_sym_db.RegisterMessage(Threshold)


DESCRIPTOR._options = None
_TIMESERIESFILTER.fields_by_name['filter']._options = None
_TIMESERIESFILTERRATIO_RATIOPART.fields_by_name['filter']._options = None
# @@protoc_insertion_point(module_scope)