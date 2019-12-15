# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1beta1/data_stats.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl/v1beta1/data_stats.proto',
  package='google.cloud.automl.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1',
  serialized_pb=b'\n,google/cloud/automl/v1beta1/data_stats.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\xfd\x03\n\tDataStats\x12\x42\n\rfloat64_stats\x18\x03 \x01(\x0b\x32).google.cloud.automl.v1beta1.Float64StatsH\x00\x12@\n\x0cstring_stats\x18\x04 \x01(\x0b\x32(.google.cloud.automl.v1beta1.StringStatsH\x00\x12\x46\n\x0ftimestamp_stats\x18\x05 \x01(\x0b\x32+.google.cloud.automl.v1beta1.TimestampStatsH\x00\x12>\n\x0b\x61rray_stats\x18\x06 \x01(\x0b\x32\'.google.cloud.automl.v1beta1.ArrayStatsH\x00\x12@\n\x0cstruct_stats\x18\x07 \x01(\x0b\x32(.google.cloud.automl.v1beta1.StructStatsH\x00\x12\x44\n\x0e\x63\x61tegory_stats\x18\x08 \x01(\x0b\x32*.google.cloud.automl.v1beta1.CategoryStatsH\x00\x12\x1c\n\x14\x64istinct_value_count\x18\x01 \x01(\x03\x12\x18\n\x10null_value_count\x18\x02 \x01(\x03\x12\x19\n\x11valid_value_count\x18\t \x01(\x03\x42\x07\n\x05stats\"\xdd\x01\n\x0c\x46loat64Stats\x12\x0c\n\x04mean\x18\x01 \x01(\x01\x12\x1a\n\x12standard_deviation\x18\x02 \x01(\x01\x12\x11\n\tquantiles\x18\x03 \x03(\x01\x12T\n\x11histogram_buckets\x18\x04 \x03(\x0b\x32\x39.google.cloud.automl.v1beta1.Float64Stats.HistogramBucket\x1a:\n\x0fHistogramBucket\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"\x8d\x01\n\x0bStringStats\x12P\n\x11top_unigram_stats\x18\x01 \x03(\x0b\x32\x35.google.cloud.automl.v1beta1.StringStats.UnigramStats\x1a,\n\x0cUnigramStats\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"\xf4\x02\n\x0eTimestampStats\x12V\n\x0egranular_stats\x18\x01 \x03(\x0b\x32>.google.cloud.automl.v1beta1.TimestampStats.GranularStatsEntry\x1a\x98\x01\n\rGranularStats\x12W\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\x46.google.cloud.automl.v1beta1.TimestampStats.GranularStats.BucketsEntry\x1a.\n\x0c\x42ucketsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1ao\n\x12GranularStatsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12H\n\x05value\x18\x02 \x01(\x0b\x32\x39.google.cloud.automl.v1beta1.TimestampStats.GranularStats:\x02\x38\x01\"J\n\nArrayStats\x12<\n\x0cmember_stats\x18\x02 \x01(\x0b\x32&.google.cloud.automl.v1beta1.DataStats\"\xb7\x01\n\x0bStructStats\x12M\n\x0b\x66ield_stats\x18\x01 \x03(\x0b\x32\x38.google.cloud.automl.v1beta1.StructStats.FieldStatsEntry\x1aY\n\x0f\x46ieldStatsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.google.cloud.automl.v1beta1.DataStats:\x02\x38\x01\"\xa0\x01\n\rCategoryStats\x12Z\n\x12top_category_stats\x18\x01 \x03(\x0b\x32>.google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats\x1a\x33\n\x13SingleCategoryStats\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"%\n\x10\x43orrelationStats\x12\x11\n\tcramers_v\x18\x01 \x01(\x01\x42\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DATASTATS = _descriptor.Descriptor(
  name='DataStats',
  full_name='google.cloud.automl.v1beta1.DataStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='float64_stats', full_name='google.cloud.automl.v1beta1.DataStats.float64_stats', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_stats', full_name='google.cloud.automl.v1beta1.DataStats.string_stats', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_stats', full_name='google.cloud.automl.v1beta1.DataStats.timestamp_stats', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array_stats', full_name='google.cloud.automl.v1beta1.DataStats.array_stats', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='struct_stats', full_name='google.cloud.automl.v1beta1.DataStats.struct_stats', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_stats', full_name='google.cloud.automl.v1beta1.DataStats.category_stats', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distinct_value_count', full_name='google.cloud.automl.v1beta1.DataStats.distinct_value_count', index=6,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='null_value_count', full_name='google.cloud.automl.v1beta1.DataStats.null_value_count', index=7,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_value_count', full_name='google.cloud.automl.v1beta1.DataStats.valid_value_count', index=8,
      number=9, type=3, cpp_type=2, label=1,
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
      name='stats', full_name='google.cloud.automl.v1beta1.DataStats.stats',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=108,
  serialized_end=617,
)


_FLOAT64STATS_HISTOGRAMBUCKET = _descriptor.Descriptor(
  name='HistogramBucket',
  full_name='google.cloud.automl.v1beta1.Float64Stats.HistogramBucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='google.cloud.automl.v1beta1.Float64Stats.HistogramBucket.min', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='google.cloud.automl.v1beta1.Float64Stats.HistogramBucket.max', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='google.cloud.automl.v1beta1.Float64Stats.HistogramBucket.count', index=2,
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
  serialized_start=783,
  serialized_end=841,
)

_FLOAT64STATS = _descriptor.Descriptor(
  name='Float64Stats',
  full_name='google.cloud.automl.v1beta1.Float64Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='google.cloud.automl.v1beta1.Float64Stats.mean', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='standard_deviation', full_name='google.cloud.automl.v1beta1.Float64Stats.standard_deviation', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantiles', full_name='google.cloud.automl.v1beta1.Float64Stats.quantiles', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='histogram_buckets', full_name='google.cloud.automl.v1beta1.Float64Stats.histogram_buckets', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOAT64STATS_HISTOGRAMBUCKET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=841,
)


_STRINGSTATS_UNIGRAMSTATS = _descriptor.Descriptor(
  name='UnigramStats',
  full_name='google.cloud.automl.v1beta1.StringStats.UnigramStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.StringStats.UnigramStats.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='google.cloud.automl.v1beta1.StringStats.UnigramStats.count', index=1,
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
  serialized_start=941,
  serialized_end=985,
)

_STRINGSTATS = _descriptor.Descriptor(
  name='StringStats',
  full_name='google.cloud.automl.v1beta1.StringStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='top_unigram_stats', full_name='google.cloud.automl.v1beta1.StringStats.top_unigram_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STRINGSTATS_UNIGRAMSTATS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=985,
)


_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY = _descriptor.Descriptor(
  name='BucketsEntry',
  full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStats.BucketsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStats.BucketsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStats.BucketsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1201,
  serialized_end=1247,
)

_TIMESTAMPSTATS_GRANULARSTATS = _descriptor.Descriptor(
  name='GranularStats',
  full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buckets', full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStats.buckets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1095,
  serialized_end=1247,
)

_TIMESTAMPSTATS_GRANULARSTATSENTRY = _descriptor.Descriptor(
  name='GranularStatsEntry',
  full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStatsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStatsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.TimestampStats.GranularStatsEntry.value', index=1,
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
  serialized_start=1249,
  serialized_end=1360,
)

_TIMESTAMPSTATS = _descriptor.Descriptor(
  name='TimestampStats',
  full_name='google.cloud.automl.v1beta1.TimestampStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='granular_stats', full_name='google.cloud.automl.v1beta1.TimestampStats.granular_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIMESTAMPSTATS_GRANULARSTATS, _TIMESTAMPSTATS_GRANULARSTATSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=988,
  serialized_end=1360,
)


_ARRAYSTATS = _descriptor.Descriptor(
  name='ArrayStats',
  full_name='google.cloud.automl.v1beta1.ArrayStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member_stats', full_name='google.cloud.automl.v1beta1.ArrayStats.member_stats', index=0,
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
  serialized_start=1362,
  serialized_end=1436,
)


_STRUCTSTATS_FIELDSTATSENTRY = _descriptor.Descriptor(
  name='FieldStatsEntry',
  full_name='google.cloud.automl.v1beta1.StructStats.FieldStatsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.StructStats.FieldStatsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.StructStats.FieldStatsEntry.value', index=1,
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
  serialized_start=1533,
  serialized_end=1622,
)

_STRUCTSTATS = _descriptor.Descriptor(
  name='StructStats',
  full_name='google.cloud.automl.v1beta1.StructStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_stats', full_name='google.cloud.automl.v1beta1.StructStats.field_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STRUCTSTATS_FIELDSTATSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1439,
  serialized_end=1622,
)


_CATEGORYSTATS_SINGLECATEGORYSTATS = _descriptor.Descriptor(
  name='SingleCategoryStats',
  full_name='google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats.count', index=1,
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
  serialized_start=1734,
  serialized_end=1785,
)

_CATEGORYSTATS = _descriptor.Descriptor(
  name='CategoryStats',
  full_name='google.cloud.automl.v1beta1.CategoryStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='top_category_stats', full_name='google.cloud.automl.v1beta1.CategoryStats.top_category_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CATEGORYSTATS_SINGLECATEGORYSTATS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1625,
  serialized_end=1785,
)


_CORRELATIONSTATS = _descriptor.Descriptor(
  name='CorrelationStats',
  full_name='google.cloud.automl.v1beta1.CorrelationStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cramers_v', full_name='google.cloud.automl.v1beta1.CorrelationStats.cramers_v', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=1787,
  serialized_end=1824,
)

_DATASTATS.fields_by_name['float64_stats'].message_type = _FLOAT64STATS
_DATASTATS.fields_by_name['string_stats'].message_type = _STRINGSTATS
_DATASTATS.fields_by_name['timestamp_stats'].message_type = _TIMESTAMPSTATS
_DATASTATS.fields_by_name['array_stats'].message_type = _ARRAYSTATS
_DATASTATS.fields_by_name['struct_stats'].message_type = _STRUCTSTATS
_DATASTATS.fields_by_name['category_stats'].message_type = _CATEGORYSTATS
_DATASTATS.oneofs_by_name['stats'].fields.append(
  _DATASTATS.fields_by_name['float64_stats'])
_DATASTATS.fields_by_name['float64_stats'].containing_oneof = _DATASTATS.oneofs_by_name['stats']
_DATASTATS.oneofs_by_name['stats'].fields.append(
  _DATASTATS.fields_by_name['string_stats'])
_DATASTATS.fields_by_name['string_stats'].containing_oneof = _DATASTATS.oneofs_by_name['stats']
_DATASTATS.oneofs_by_name['stats'].fields.append(
  _DATASTATS.fields_by_name['timestamp_stats'])
_DATASTATS.fields_by_name['timestamp_stats'].containing_oneof = _DATASTATS.oneofs_by_name['stats']
_DATASTATS.oneofs_by_name['stats'].fields.append(
  _DATASTATS.fields_by_name['array_stats'])
_DATASTATS.fields_by_name['array_stats'].containing_oneof = _DATASTATS.oneofs_by_name['stats']
_DATASTATS.oneofs_by_name['stats'].fields.append(
  _DATASTATS.fields_by_name['struct_stats'])
_DATASTATS.fields_by_name['struct_stats'].containing_oneof = _DATASTATS.oneofs_by_name['stats']
_DATASTATS.oneofs_by_name['stats'].fields.append(
  _DATASTATS.fields_by_name['category_stats'])
_DATASTATS.fields_by_name['category_stats'].containing_oneof = _DATASTATS.oneofs_by_name['stats']
_FLOAT64STATS_HISTOGRAMBUCKET.containing_type = _FLOAT64STATS
_FLOAT64STATS.fields_by_name['histogram_buckets'].message_type = _FLOAT64STATS_HISTOGRAMBUCKET
_STRINGSTATS_UNIGRAMSTATS.containing_type = _STRINGSTATS
_STRINGSTATS.fields_by_name['top_unigram_stats'].message_type = _STRINGSTATS_UNIGRAMSTATS
_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY.containing_type = _TIMESTAMPSTATS_GRANULARSTATS
_TIMESTAMPSTATS_GRANULARSTATS.fields_by_name['buckets'].message_type = _TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY
_TIMESTAMPSTATS_GRANULARSTATS.containing_type = _TIMESTAMPSTATS
_TIMESTAMPSTATS_GRANULARSTATSENTRY.fields_by_name['value'].message_type = _TIMESTAMPSTATS_GRANULARSTATS
_TIMESTAMPSTATS_GRANULARSTATSENTRY.containing_type = _TIMESTAMPSTATS
_TIMESTAMPSTATS.fields_by_name['granular_stats'].message_type = _TIMESTAMPSTATS_GRANULARSTATSENTRY
_ARRAYSTATS.fields_by_name['member_stats'].message_type = _DATASTATS
_STRUCTSTATS_FIELDSTATSENTRY.fields_by_name['value'].message_type = _DATASTATS
_STRUCTSTATS_FIELDSTATSENTRY.containing_type = _STRUCTSTATS
_STRUCTSTATS.fields_by_name['field_stats'].message_type = _STRUCTSTATS_FIELDSTATSENTRY
_CATEGORYSTATS_SINGLECATEGORYSTATS.containing_type = _CATEGORYSTATS
_CATEGORYSTATS.fields_by_name['top_category_stats'].message_type = _CATEGORYSTATS_SINGLECATEGORYSTATS
DESCRIPTOR.message_types_by_name['DataStats'] = _DATASTATS
DESCRIPTOR.message_types_by_name['Float64Stats'] = _FLOAT64STATS
DESCRIPTOR.message_types_by_name['StringStats'] = _STRINGSTATS
DESCRIPTOR.message_types_by_name['TimestampStats'] = _TIMESTAMPSTATS
DESCRIPTOR.message_types_by_name['ArrayStats'] = _ARRAYSTATS
DESCRIPTOR.message_types_by_name['StructStats'] = _STRUCTSTATS
DESCRIPTOR.message_types_by_name['CategoryStats'] = _CATEGORYSTATS
DESCRIPTOR.message_types_by_name['CorrelationStats'] = _CORRELATIONSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataStats = _reflection.GeneratedProtocolMessageType('DataStats', (_message.Message,), {
  'DESCRIPTOR' : _DATASTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.DataStats)
  })
_sym_db.RegisterMessage(DataStats)

Float64Stats = _reflection.GeneratedProtocolMessageType('Float64Stats', (_message.Message,), {

  'HistogramBucket' : _reflection.GeneratedProtocolMessageType('HistogramBucket', (_message.Message,), {
    'DESCRIPTOR' : _FLOAT64STATS_HISTOGRAMBUCKET,
    '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.Float64Stats.HistogramBucket)
    })
  ,
  'DESCRIPTOR' : _FLOAT64STATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.Float64Stats)
  })
_sym_db.RegisterMessage(Float64Stats)
_sym_db.RegisterMessage(Float64Stats.HistogramBucket)

StringStats = _reflection.GeneratedProtocolMessageType('StringStats', (_message.Message,), {

  'UnigramStats' : _reflection.GeneratedProtocolMessageType('UnigramStats', (_message.Message,), {
    'DESCRIPTOR' : _STRINGSTATS_UNIGRAMSTATS,
    '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.StringStats.UnigramStats)
    })
  ,
  'DESCRIPTOR' : _STRINGSTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.StringStats)
  })
_sym_db.RegisterMessage(StringStats)
_sym_db.RegisterMessage(StringStats.UnigramStats)

TimestampStats = _reflection.GeneratedProtocolMessageType('TimestampStats', (_message.Message,), {

  'GranularStats' : _reflection.GeneratedProtocolMessageType('GranularStats', (_message.Message,), {

    'BucketsEntry' : _reflection.GeneratedProtocolMessageType('BucketsEntry', (_message.Message,), {
      'DESCRIPTOR' : _TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY,
      '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TimestampStats.GranularStats.BucketsEntry)
      })
    ,
    'DESCRIPTOR' : _TIMESTAMPSTATS_GRANULARSTATS,
    '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TimestampStats.GranularStats)
    })
  ,

  'GranularStatsEntry' : _reflection.GeneratedProtocolMessageType('GranularStatsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TIMESTAMPSTATS_GRANULARSTATSENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TimestampStats.GranularStatsEntry)
    })
  ,
  'DESCRIPTOR' : _TIMESTAMPSTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TimestampStats)
  })
_sym_db.RegisterMessage(TimestampStats)
_sym_db.RegisterMessage(TimestampStats.GranularStats)
_sym_db.RegisterMessage(TimestampStats.GranularStats.BucketsEntry)
_sym_db.RegisterMessage(TimestampStats.GranularStatsEntry)

ArrayStats = _reflection.GeneratedProtocolMessageType('ArrayStats', (_message.Message,), {
  'DESCRIPTOR' : _ARRAYSTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ArrayStats)
  })
_sym_db.RegisterMessage(ArrayStats)

StructStats = _reflection.GeneratedProtocolMessageType('StructStats', (_message.Message,), {

  'FieldStatsEntry' : _reflection.GeneratedProtocolMessageType('FieldStatsEntry', (_message.Message,), {
    'DESCRIPTOR' : _STRUCTSTATS_FIELDSTATSENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.StructStats.FieldStatsEntry)
    })
  ,
  'DESCRIPTOR' : _STRUCTSTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.StructStats)
  })
_sym_db.RegisterMessage(StructStats)
_sym_db.RegisterMessage(StructStats.FieldStatsEntry)

CategoryStats = _reflection.GeneratedProtocolMessageType('CategoryStats', (_message.Message,), {

  'SingleCategoryStats' : _reflection.GeneratedProtocolMessageType('SingleCategoryStats', (_message.Message,), {
    'DESCRIPTOR' : _CATEGORYSTATS_SINGLECATEGORYSTATS,
    '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats)
    })
  ,
  'DESCRIPTOR' : _CATEGORYSTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.CategoryStats)
  })
_sym_db.RegisterMessage(CategoryStats)
_sym_db.RegisterMessage(CategoryStats.SingleCategoryStats)

CorrelationStats = _reflection.GeneratedProtocolMessageType('CorrelationStats', (_message.Message,), {
  'DESCRIPTOR' : _CORRELATIONSTATS,
  '__module__' : 'google.cloud.automl.v1beta1.data_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.CorrelationStats)
  })
_sym_db.RegisterMessage(CorrelationStats)


DESCRIPTOR._options = None
_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY._options = None
_TIMESTAMPSTATS_GRANULARSTATSENTRY._options = None
_STRUCTSTATS_FIELDSTATSENTRY._options = None
# @@protoc_insertion_point(module_scope)
