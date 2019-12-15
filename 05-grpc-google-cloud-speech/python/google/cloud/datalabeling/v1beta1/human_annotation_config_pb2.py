# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling/v1beta1/human_annotation_config.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datalabeling/v1beta1/human_annotation_config.proto',
  package='google.cloud.datalabeling.v1beta1',
  syntax='proto3',
  serialized_options=b'\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling',
  serialized_pb=b'\n?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\"\xac\x02\n\x15HumanAnnotationConfig\x12\x13\n\x0binstruction\x18\x01 \x01(\t\x12&\n\x1e\x61nnotated_dataset_display_name\x18\x02 \x01(\t\x12%\n\x1d\x61nnotated_dataset_description\x18\x03 \x01(\t\x12\x13\n\x0blabel_group\x18\x04 \x01(\t\x12\x15\n\rlanguage_code\x18\x05 \x01(\t\x12\x15\n\rreplica_count\x18\x06 \x01(\x05\x12\x34\n\x11question_duration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1a\n\x12\x63ontributor_emails\x18\t \x03(\t\x12\x1a\n\x12user_email_address\x18\n \x01(\t\"\xae\x01\n\x19ImageClassificationConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\x12\x19\n\x11\x61llow_multi_label\x18\x02 \x01(\x08\x12Y\n\x17\x61nswer_aggregation_type\x18\x03 \x01(\x0e\x32\x38.google.cloud.datalabeling.v1beta1.StringAggregationType\"N\n\x12\x42oundingPolyConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\x12\x1b\n\x13instruction_message\x18\x02 \x01(\t\"J\n\x0ePolylineConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\x12\x1b\n\x13instruction_message\x18\x02 \x01(\t\"N\n\x12SegmentationConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\x12\x1b\n\x13instruction_message\x18\x02 \x01(\t\"\x87\x02\n\x19VideoClassificationConfig\x12y\n\x1b\x61nnotation_spec_set_configs\x18\x01 \x03(\x0b\x32T.google.cloud.datalabeling.v1beta1.VideoClassificationConfig.AnnotationSpecSetConfig\x12\x1c\n\x14\x61pply_shot_detection\x18\x02 \x01(\x08\x1aQ\n\x17\x41nnotationSpecSetConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\x12\x19\n\x11\x61llow_multi_label\x18\x02 \x01(\x08\"S\n\x15ObjectDetectionConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\x12\x1d\n\x15\x65xtraction_frame_rate\x18\x03 \x01(\x01\"3\n\x14ObjectTrackingConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t\"+\n\x0b\x45ventConfig\x12\x1c\n\x14\x61nnotation_spec_sets\x18\x01 \x03(\t\"\xa0\x01\n\x18TextClassificationConfig\x12\x19\n\x11\x61llow_multi_label\x18\x01 \x01(\x08\x12\x1b\n\x13\x61nnotation_spec_set\x18\x02 \x01(\t\x12L\n\x10sentiment_config\x18\x03 \x01(\x0b\x32\x32.google.cloud.datalabeling.v1beta1.SentimentConfig\";\n\x0fSentimentConfig\x12(\n enable_label_sentiment_selection\x18\x01 \x01(\x08\"9\n\x1aTextEntityExtractionConfig\x12\x1b\n\x13\x61nnotation_spec_set\x18\x01 \x01(\t*{\n\x15StringAggregationType\x12\'\n#STRING_AGGREGATION_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMAJORITY_VOTE\x10\x01\x12\x12\n\x0eUNANIMOUS_VOTE\x10\x02\x12\x12\n\x0eNO_AGGREGATION\x10\x03\x42x\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabelingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_STRINGAGGREGATIONTYPE = _descriptor.EnumDescriptor(
  name='StringAggregationType',
  full_name='google.cloud.datalabeling.v1beta1.StringAggregationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING_AGGREGATION_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAJORITY_VOTE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNANIMOUS_VOTE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_AGGREGATION', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1612,
  serialized_end=1735,
)
_sym_db.RegisterEnumDescriptor(_STRINGAGGREGATIONTYPE)

StringAggregationType = enum_type_wrapper.EnumTypeWrapper(_STRINGAGGREGATIONTYPE)
STRING_AGGREGATION_TYPE_UNSPECIFIED = 0
MAJORITY_VOTE = 1
UNANIMOUS_VOTE = 2
NO_AGGREGATION = 3



_HUMANANNOTATIONCONFIG = _descriptor.Descriptor(
  name='HumanAnnotationConfig',
  full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instruction', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.instruction', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotated_dataset_display_name', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.annotated_dataset_display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotated_dataset_description', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.annotated_dataset_description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_group', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.label_group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.language_code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replica_count', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.replica_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='question_duration', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.question_duration', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contributor_emails', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.contributor_emails', index=7,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_email_address', full_name='google.cloud.datalabeling.v1beta1.HumanAnnotationConfig.user_email_address', index=8,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=165,
  serialized_end=465,
)


_IMAGECLASSIFICATIONCONFIG = _descriptor.Descriptor(
  name='ImageClassificationConfig',
  full_name='google.cloud.datalabeling.v1beta1.ImageClassificationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.ImageClassificationConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_multi_label', full_name='google.cloud.datalabeling.v1beta1.ImageClassificationConfig.allow_multi_label', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer_aggregation_type', full_name='google.cloud.datalabeling.v1beta1.ImageClassificationConfig.answer_aggregation_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=468,
  serialized_end=642,
)


_BOUNDINGPOLYCONFIG = _descriptor.Descriptor(
  name='BoundingPolyConfig',
  full_name='google.cloud.datalabeling.v1beta1.BoundingPolyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.BoundingPolyConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instruction_message', full_name='google.cloud.datalabeling.v1beta1.BoundingPolyConfig.instruction_message', index=1,
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
  serialized_start=644,
  serialized_end=722,
)


_POLYLINECONFIG = _descriptor.Descriptor(
  name='PolylineConfig',
  full_name='google.cloud.datalabeling.v1beta1.PolylineConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.PolylineConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instruction_message', full_name='google.cloud.datalabeling.v1beta1.PolylineConfig.instruction_message', index=1,
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
  serialized_start=724,
  serialized_end=798,
)


_SEGMENTATIONCONFIG = _descriptor.Descriptor(
  name='SegmentationConfig',
  full_name='google.cloud.datalabeling.v1beta1.SegmentationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.SegmentationConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instruction_message', full_name='google.cloud.datalabeling.v1beta1.SegmentationConfig.instruction_message', index=1,
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
  serialized_start=800,
  serialized_end=878,
)


_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG = _descriptor.Descriptor(
  name='AnnotationSpecSetConfig',
  full_name='google.cloud.datalabeling.v1beta1.VideoClassificationConfig.AnnotationSpecSetConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.VideoClassificationConfig.AnnotationSpecSetConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_multi_label', full_name='google.cloud.datalabeling.v1beta1.VideoClassificationConfig.AnnotationSpecSetConfig.allow_multi_label', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1063,
  serialized_end=1144,
)

_VIDEOCLASSIFICATIONCONFIG = _descriptor.Descriptor(
  name='VideoClassificationConfig',
  full_name='google.cloud.datalabeling.v1beta1.VideoClassificationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set_configs', full_name='google.cloud.datalabeling.v1beta1.VideoClassificationConfig.annotation_spec_set_configs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apply_shot_detection', full_name='google.cloud.datalabeling.v1beta1.VideoClassificationConfig.apply_shot_detection', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=1144,
)


_OBJECTDETECTIONCONFIG = _descriptor.Descriptor(
  name='ObjectDetectionConfig',
  full_name='google.cloud.datalabeling.v1beta1.ObjectDetectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.ObjectDetectionConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraction_frame_rate', full_name='google.cloud.datalabeling.v1beta1.ObjectDetectionConfig.extraction_frame_rate', index=1,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=1146,
  serialized_end=1229,
)


_OBJECTTRACKINGCONFIG = _descriptor.Descriptor(
  name='ObjectTrackingConfig',
  full_name='google.cloud.datalabeling.v1beta1.ObjectTrackingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.ObjectTrackingConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1231,
  serialized_end=1282,
)


_EVENTCONFIG = _descriptor.Descriptor(
  name='EventConfig',
  full_name='google.cloud.datalabeling.v1beta1.EventConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_sets', full_name='google.cloud.datalabeling.v1beta1.EventConfig.annotation_spec_sets', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1284,
  serialized_end=1327,
)


_TEXTCLASSIFICATIONCONFIG = _descriptor.Descriptor(
  name='TextClassificationConfig',
  full_name='google.cloud.datalabeling.v1beta1.TextClassificationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow_multi_label', full_name='google.cloud.datalabeling.v1beta1.TextClassificationConfig.allow_multi_label', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.TextClassificationConfig.annotation_spec_set', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sentiment_config', full_name='google.cloud.datalabeling.v1beta1.TextClassificationConfig.sentiment_config', index=2,
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
  serialized_start=1330,
  serialized_end=1490,
)


_SENTIMENTCONFIG = _descriptor.Descriptor(
  name='SentimentConfig',
  full_name='google.cloud.datalabeling.v1beta1.SentimentConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_label_sentiment_selection', full_name='google.cloud.datalabeling.v1beta1.SentimentConfig.enable_label_sentiment_selection', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1492,
  serialized_end=1551,
)


_TEXTENTITYEXTRACTIONCONFIG = _descriptor.Descriptor(
  name='TextEntityExtractionConfig',
  full_name='google.cloud.datalabeling.v1beta1.TextEntityExtractionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.TextEntityExtractionConfig.annotation_spec_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1553,
  serialized_end=1610,
)

_HUMANANNOTATIONCONFIG.fields_by_name['question_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_IMAGECLASSIFICATIONCONFIG.fields_by_name['answer_aggregation_type'].enum_type = _STRINGAGGREGATIONTYPE
_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG.containing_type = _VIDEOCLASSIFICATIONCONFIG
_VIDEOCLASSIFICATIONCONFIG.fields_by_name['annotation_spec_set_configs'].message_type = _VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG
_TEXTCLASSIFICATIONCONFIG.fields_by_name['sentiment_config'].message_type = _SENTIMENTCONFIG
DESCRIPTOR.message_types_by_name['HumanAnnotationConfig'] = _HUMANANNOTATIONCONFIG
DESCRIPTOR.message_types_by_name['ImageClassificationConfig'] = _IMAGECLASSIFICATIONCONFIG
DESCRIPTOR.message_types_by_name['BoundingPolyConfig'] = _BOUNDINGPOLYCONFIG
DESCRIPTOR.message_types_by_name['PolylineConfig'] = _POLYLINECONFIG
DESCRIPTOR.message_types_by_name['SegmentationConfig'] = _SEGMENTATIONCONFIG
DESCRIPTOR.message_types_by_name['VideoClassificationConfig'] = _VIDEOCLASSIFICATIONCONFIG
DESCRIPTOR.message_types_by_name['ObjectDetectionConfig'] = _OBJECTDETECTIONCONFIG
DESCRIPTOR.message_types_by_name['ObjectTrackingConfig'] = _OBJECTTRACKINGCONFIG
DESCRIPTOR.message_types_by_name['EventConfig'] = _EVENTCONFIG
DESCRIPTOR.message_types_by_name['TextClassificationConfig'] = _TEXTCLASSIFICATIONCONFIG
DESCRIPTOR.message_types_by_name['SentimentConfig'] = _SENTIMENTCONFIG
DESCRIPTOR.message_types_by_name['TextEntityExtractionConfig'] = _TEXTENTITYEXTRACTIONCONFIG
DESCRIPTOR.enum_types_by_name['StringAggregationType'] = _STRINGAGGREGATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HumanAnnotationConfig = _reflection.GeneratedProtocolMessageType('HumanAnnotationConfig', (_message.Message,), {
  'DESCRIPTOR' : _HUMANANNOTATIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.HumanAnnotationConfig)
  })
_sym_db.RegisterMessage(HumanAnnotationConfig)

ImageClassificationConfig = _reflection.GeneratedProtocolMessageType('ImageClassificationConfig', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECLASSIFICATIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.ImageClassificationConfig)
  })
_sym_db.RegisterMessage(ImageClassificationConfig)

BoundingPolyConfig = _reflection.GeneratedProtocolMessageType('BoundingPolyConfig', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGPOLYCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.BoundingPolyConfig)
  })
_sym_db.RegisterMessage(BoundingPolyConfig)

PolylineConfig = _reflection.GeneratedProtocolMessageType('PolylineConfig', (_message.Message,), {
  'DESCRIPTOR' : _POLYLINECONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.PolylineConfig)
  })
_sym_db.RegisterMessage(PolylineConfig)

SegmentationConfig = _reflection.GeneratedProtocolMessageType('SegmentationConfig', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTATIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.SegmentationConfig)
  })
_sym_db.RegisterMessage(SegmentationConfig)

VideoClassificationConfig = _reflection.GeneratedProtocolMessageType('VideoClassificationConfig', (_message.Message,), {

  'AnnotationSpecSetConfig' : _reflection.GeneratedProtocolMessageType('AnnotationSpecSetConfig', (_message.Message,), {
    'DESCRIPTOR' : _VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG,
    '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.VideoClassificationConfig.AnnotationSpecSetConfig)
    })
  ,
  'DESCRIPTOR' : _VIDEOCLASSIFICATIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.VideoClassificationConfig)
  })
_sym_db.RegisterMessage(VideoClassificationConfig)
_sym_db.RegisterMessage(VideoClassificationConfig.AnnotationSpecSetConfig)

ObjectDetectionConfig = _reflection.GeneratedProtocolMessageType('ObjectDetectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDETECTIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.ObjectDetectionConfig)
  })
_sym_db.RegisterMessage(ObjectDetectionConfig)

ObjectTrackingConfig = _reflection.GeneratedProtocolMessageType('ObjectTrackingConfig', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTTRACKINGCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.ObjectTrackingConfig)
  })
_sym_db.RegisterMessage(ObjectTrackingConfig)

EventConfig = _reflection.GeneratedProtocolMessageType('EventConfig', (_message.Message,), {
  'DESCRIPTOR' : _EVENTCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EventConfig)
  })
_sym_db.RegisterMessage(EventConfig)

TextClassificationConfig = _reflection.GeneratedProtocolMessageType('TextClassificationConfig', (_message.Message,), {
  'DESCRIPTOR' : _TEXTCLASSIFICATIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.TextClassificationConfig)
  })
_sym_db.RegisterMessage(TextClassificationConfig)

SentimentConfig = _reflection.GeneratedProtocolMessageType('SentimentConfig', (_message.Message,), {
  'DESCRIPTOR' : _SENTIMENTCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.SentimentConfig)
  })
_sym_db.RegisterMessage(SentimentConfig)

TextEntityExtractionConfig = _reflection.GeneratedProtocolMessageType('TextEntityExtractionConfig', (_message.Message,), {
  'DESCRIPTOR' : _TEXTENTITYEXTRACTIONCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.TextEntityExtractionConfig)
  })
_sym_db.RegisterMessage(TextEntityExtractionConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
