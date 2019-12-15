# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1beta1/model.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl.v1beta1 import image_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2
from google.cloud.automl.v1beta1 import tables_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2
from google.cloud.automl.v1beta1 import text_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2
from google.cloud.automl.v1beta1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2
from google.cloud.automl.v1beta1 import video_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_video__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl/v1beta1/model.proto',
  package='google.cloud.automl.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1',
  serialized_pb=b'\n\'google/cloud/automl/v1beta1/model.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\'google/cloud/automl/v1beta1/image.proto\x1a(google/cloud/automl/v1beta1/tables.proto\x1a&google/cloud/automl/v1beta1/text.proto\x1a-google/cloud/automl/v1beta1/translation.proto\x1a\'google/cloud/automl/v1beta1/video.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xf2\t\n\x05Model\x12[\n\x1atranslation_model_metadata\x18\x0f \x01(\x0b\x32\x35.google.cloud.automl.v1beta1.TranslationModelMetadataH\x00\x12l\n#image_classification_model_metadata\x18\r \x01(\x0b\x32=.google.cloud.automl.v1beta1.ImageClassificationModelMetadataH\x00\x12j\n\"text_classification_model_metadata\x18\x0e \x01(\x0b\x32<.google.cloud.automl.v1beta1.TextClassificationModelMetadataH\x00\x12o\n%image_object_detection_model_metadata\x18\x14 \x01(\x0b\x32>.google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadataH\x00\x12l\n#video_classification_model_metadata\x18\x17 \x01(\x0b\x32=.google.cloud.automl.v1beta1.VideoClassificationModelMetadataH\x00\x12m\n$video_object_tracking_model_metadata\x18\x15 \x01(\x0b\x32=.google.cloud.automl.v1beta1.VideoObjectTrackingModelMetadataH\x00\x12\x62\n\x1etext_extraction_model_metadata\x18\x13 \x01(\x0b\x32\x38.google.cloud.automl.v1beta1.TextExtractionModelMetadataH\x00\x12Q\n\x15tables_model_metadata\x18\x18 \x01(\x0b\x32\x30.google.cloud.automl.v1beta1.TablesModelMetadataH\x00\x12`\n\x1dtext_sentiment_model_metadata\x18\x16 \x01(\x0b\x32\x37.google.cloud.automl.v1beta1.TextSentimentModelMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12L\n\x10\x64\x65ployment_state\x18\x08 \x01(\x0e\x32\x32.google.cloud.automl.v1beta1.Model.DeploymentState\"Q\n\x0f\x44\x65ploymentState\x12 \n\x1c\x44\x45PLOYMENT_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44\x45PLOYED\x10\x01\x12\x0e\n\nUNDEPLOYED\x10\x02\x42\x10\n\x0emodel_metadataB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_video__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MODEL_DEPLOYMENTSTATE = _descriptor.EnumDescriptor(
  name='DeploymentState',
  full_name='google.cloud.automl.v1beta1.Model.DeploymentState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPLOYMENT_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPLOYED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDEPLOYED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1514,
  serialized_end=1595,
)
_sym_db.RegisterEnumDescriptor(_MODEL_DEPLOYMENTSTATE)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='google.cloud.automl.v1beta1.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation_model_metadata', full_name='google.cloud.automl.v1beta1.Model.translation_model_metadata', index=0,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_classification_model_metadata', full_name='google.cloud.automl.v1beta1.Model.image_classification_model_metadata', index=1,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_classification_model_metadata', full_name='google.cloud.automl.v1beta1.Model.text_classification_model_metadata', index=2,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_object_detection_model_metadata', full_name='google.cloud.automl.v1beta1.Model.image_object_detection_model_metadata', index=3,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_classification_model_metadata', full_name='google.cloud.automl.v1beta1.Model.video_classification_model_metadata', index=4,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_object_tracking_model_metadata', full_name='google.cloud.automl.v1beta1.Model.video_object_tracking_model_metadata', index=5,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_extraction_model_metadata', full_name='google.cloud.automl.v1beta1.Model.text_extraction_model_metadata', index=6,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tables_model_metadata', full_name='google.cloud.automl.v1beta1.Model.tables_model_metadata', index=7,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_sentiment_model_metadata', full_name='google.cloud.automl.v1beta1.Model.text_sentiment_model_metadata', index=8,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.automl.v1beta1.Model.name', index=9,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.automl.v1beta1.Model.display_name', index=10,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.cloud.automl.v1beta1.Model.dataset_id', index=11,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.automl.v1beta1.Model.create_time', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.automl.v1beta1.Model.update_time', index=13,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployment_state', full_name='google.cloud.automl.v1beta1.Model.deployment_state', index=14,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODEL_DEPLOYMENTSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='model_metadata', full_name='google.cloud.automl.v1beta1.Model.model_metadata',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=347,
  serialized_end=1613,
)

_MODEL.fields_by_name['translation_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2._TRANSLATIONMODELMETADATA
_MODEL.fields_by_name['image_classification_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2._IMAGECLASSIFICATIONMODELMETADATA
_MODEL.fields_by_name['text_classification_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2._TEXTCLASSIFICATIONMODELMETADATA
_MODEL.fields_by_name['image_object_detection_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2._IMAGEOBJECTDETECTIONMODELMETADATA
_MODEL.fields_by_name['video_classification_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_video__pb2._VIDEOCLASSIFICATIONMODELMETADATA
_MODEL.fields_by_name['video_object_tracking_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_video__pb2._VIDEOOBJECTTRACKINGMODELMETADATA
_MODEL.fields_by_name['text_extraction_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2._TEXTEXTRACTIONMODELMETADATA
_MODEL.fields_by_name['tables_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2._TABLESMODELMETADATA
_MODEL.fields_by_name['text_sentiment_model_metadata'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2._TEXTSENTIMENTMODELMETADATA
_MODEL.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODEL.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODEL.fields_by_name['deployment_state'].enum_type = _MODEL_DEPLOYMENTSTATE
_MODEL_DEPLOYMENTSTATE.containing_type = _MODEL
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['translation_model_metadata'])
_MODEL.fields_by_name['translation_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['image_classification_model_metadata'])
_MODEL.fields_by_name['image_classification_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['text_classification_model_metadata'])
_MODEL.fields_by_name['text_classification_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['image_object_detection_model_metadata'])
_MODEL.fields_by_name['image_object_detection_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['video_classification_model_metadata'])
_MODEL.fields_by_name['video_classification_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['video_object_tracking_model_metadata'])
_MODEL.fields_by_name['video_object_tracking_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['text_extraction_model_metadata'])
_MODEL.fields_by_name['text_extraction_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['tables_model_metadata'])
_MODEL.fields_by_name['tables_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
_MODEL.oneofs_by_name['model_metadata'].fields.append(
  _MODEL.fields_by_name['text_sentiment_model_metadata'])
_MODEL.fields_by_name['text_sentiment_model_metadata'].containing_oneof = _MODEL.oneofs_by_name['model_metadata']
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'google.cloud.automl.v1beta1.model_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.Model)
  })
_sym_db.RegisterMessage(Model)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
