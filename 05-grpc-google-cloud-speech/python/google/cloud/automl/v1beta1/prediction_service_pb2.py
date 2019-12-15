# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1beta1/prediction_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.cloud.automl.v1beta1 import annotation_payload_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__payload__pb2
from google.cloud.automl.v1beta1 import data_items_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2
from google.cloud.automl.v1beta1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2
from google.cloud.automl.v1beta1 import operations_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_operations__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl/v1beta1/prediction_service.proto',
  package='google.cloud.automl.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.automl.v1beta1B\026PredictionServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1',
  serialized_pb=b'\n4google/cloud/automl/v1beta1/prediction_service.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x34google/cloud/automl/v1beta1/annotation_payload.proto\x1a,google/cloud/automl/v1beta1/data_items.proto\x1a$google/cloud/automl/v1beta1/io.proto\x1a,google/cloud/automl/v1beta1/operations.proto\x1a#google/longrunning/operations.proto\"\xd4\x01\n\x0ePredictRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x07payload\x18\x02 \x01(\x0b\x32+.google.cloud.automl.v1beta1.ExamplePayload\x12G\n\x06params\x18\x03 \x03(\x0b\x32\x37.google.cloud.automl.v1beta1.PredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9a\x02\n\x0fPredictResponse\x12?\n\x07payload\x18\x01 \x03(\x0b\x32..google.cloud.automl.v1beta1.AnnotationPayload\x12G\n\x12preprocessed_input\x18\x03 \x01(\x0b\x32+.google.cloud.automl.v1beta1.ExamplePayload\x12L\n\x08metadata\x18\x02 \x03(\x0b\x32:.google.cloud.automl.v1beta1.PredictResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x02\n\x13\x42\x61tchPredictRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12J\n\x0cinput_config\x18\x03 \x01(\x0b\x32\x34.google.cloud.automl.v1beta1.BatchPredictInputConfig\x12L\n\routput_config\x18\x04 \x01(\x0b\x32\x35.google.cloud.automl.v1beta1.BatchPredictOutputConfig\x12L\n\x06params\x18\x05 \x03(\x0b\x32<.google.cloud.automl.v1beta1.BatchPredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x96\x01\n\x12\x42\x61tchPredictResult\x12O\n\x08metadata\x18\x01 \x03(\x0b\x32=.google.cloud.automl.v1beta1.BatchPredictResult.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xb4\x03\n\x11PredictionService\x12\xa8\x01\n\x07Predict\x12+.google.cloud.automl.v1beta1.PredictRequest\x1a,.google.cloud.automl.v1beta1.PredictResponse\"B\x82\xd3\xe4\x93\x02<\"7/v1beta1/{name=projects/*/locations/*/models/*}:predict:\x01*\x12\xa8\x01\n\x0c\x42\x61tchPredict\x12\x30.google.cloud.automl.v1beta1.BatchPredictRequest\x1a\x1d.google.longrunning.Operation\"G\x82\xd3\xe4\x93\x02\x41\"</v1beta1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*\x1aI\xca\x41\x15\x61utoml.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xbd\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\x16PredictionServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__payload__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1beta1_dot_operations__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,])




_PREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='google.cloud.automl.v1beta1.PredictRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.PredictRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.PredictRequest.ParamsEntry.value', index=1,
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
  serialized_start=529,
  serialized_end=574,
)

_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='google.cloud.automl.v1beta1.PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.automl.v1beta1.PredictRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.cloud.automl.v1beta1.PredictRequest.payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='google.cloud.automl.v1beta1.PredictRequest.params', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTREQUEST_PARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=574,
)


_PREDICTRESPONSE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='google.cloud.automl.v1beta1.PredictResponse.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.PredictResponse.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.PredictResponse.MetadataEntry.value', index=1,
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
  serialized_start=812,
  serialized_end=859,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='google.cloud.automl.v1beta1.PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.cloud.automl.v1beta1.PredictResponse.payload', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preprocessed_input', full_name='google.cloud.automl.v1beta1.PredictResponse.preprocessed_input', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.cloud.automl.v1beta1.PredictResponse.metadata', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=859,
)


_BATCHPREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='google.cloud.automl.v1beta1.BatchPredictRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.BatchPredictRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.BatchPredictRequest.ParamsEntry.value', index=1,
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
  serialized_start=529,
  serialized_end=574,
)

_BATCHPREDICTREQUEST = _descriptor.Descriptor(
  name='BatchPredictRequest',
  full_name='google.cloud.automl.v1beta1.BatchPredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.automl.v1beta1.BatchPredictRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_config', full_name='google.cloud.automl.v1beta1.BatchPredictRequest.input_config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_config', full_name='google.cloud.automl.v1beta1.BatchPredictRequest.output_config', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='google.cloud.automl.v1beta1.BatchPredictRequest.params', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BATCHPREDICTREQUEST_PARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=1176,
)


_BATCHPREDICTRESULT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='google.cloud.automl.v1beta1.BatchPredictResult.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.automl.v1beta1.BatchPredictResult.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.automl.v1beta1.BatchPredictResult.MetadataEntry.value', index=1,
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
  serialized_start=812,
  serialized_end=859,
)

_BATCHPREDICTRESULT = _descriptor.Descriptor(
  name='BatchPredictResult',
  full_name='google.cloud.automl.v1beta1.BatchPredictResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.cloud.automl.v1beta1.BatchPredictResult.metadata', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BATCHPREDICTRESULT_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1329,
)

_PREDICTREQUEST_PARAMSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name['payload'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2._EXAMPLEPAYLOAD
_PREDICTREQUEST.fields_by_name['params'].message_type = _PREDICTREQUEST_PARAMSENTRY
_PREDICTRESPONSE_METADATAENTRY.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name['payload'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__payload__pb2._ANNOTATIONPAYLOAD
_PREDICTRESPONSE.fields_by_name['preprocessed_input'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2._EXAMPLEPAYLOAD
_PREDICTRESPONSE.fields_by_name['metadata'].message_type = _PREDICTRESPONSE_METADATAENTRY
_BATCHPREDICTREQUEST_PARAMSENTRY.containing_type = _BATCHPREDICTREQUEST
_BATCHPREDICTREQUEST.fields_by_name['input_config'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2._BATCHPREDICTINPUTCONFIG
_BATCHPREDICTREQUEST.fields_by_name['output_config'].message_type = google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2._BATCHPREDICTOUTPUTCONFIG
_BATCHPREDICTREQUEST.fields_by_name['params'].message_type = _BATCHPREDICTREQUEST_PARAMSENTRY
_BATCHPREDICTRESULT_METADATAENTRY.containing_type = _BATCHPREDICTRESULT
_BATCHPREDICTRESULT.fields_by_name['metadata'].message_type = _BATCHPREDICTRESULT_METADATAENTRY
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
DESCRIPTOR.message_types_by_name['BatchPredictRequest'] = _BATCHPREDICTREQUEST
DESCRIPTOR.message_types_by_name['BatchPredictResult'] = _BATCHPREDICTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_PARAMSENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.PredictRequest.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.ParamsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTRESPONSE_METADATAENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.PredictResponse.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.MetadataEntry)

BatchPredictRequest = _reflection.GeneratedProtocolMessageType('BatchPredictRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTREQUEST_PARAMSENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.BatchPredictRequest.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _BATCHPREDICTREQUEST,
  '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.BatchPredictRequest)
  })
_sym_db.RegisterMessage(BatchPredictRequest)
_sym_db.RegisterMessage(BatchPredictRequest.ParamsEntry)

BatchPredictResult = _reflection.GeneratedProtocolMessageType('BatchPredictResult', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTRESULT_METADATAENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.BatchPredictResult.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _BATCHPREDICTRESULT,
  '__module__' : 'google.cloud.automl.v1beta1.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.BatchPredictResult)
  })
_sym_db.RegisterMessage(BatchPredictResult)
_sym_db.RegisterMessage(BatchPredictResult.MetadataEntry)


DESCRIPTOR._options = None
_PREDICTREQUEST_PARAMSENTRY._options = None
_PREDICTRESPONSE_METADATAENTRY._options = None
_BATCHPREDICTREQUEST_PARAMSENTRY._options = None
_BATCHPREDICTRESULT_METADATAENTRY._options = None

_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
  name='PredictionService',
  full_name='google.cloud.automl.v1beta1.PredictionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\025automl.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  serialized_start=1332,
  serialized_end=1768,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='google.cloud.automl.v1beta1.PredictionService.Predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_PREDICTRESPONSE,
    serialized_options=b'\202\323\344\223\002<\"7/v1beta1/{name=projects/*/locations/*/models/*}:predict:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='BatchPredict',
    full_name='google.cloud.automl.v1beta1.PredictionService.BatchPredict',
    index=1,
    containing_service=None,
    input_type=_BATCHPREDICTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002A\"</v1beta1/{name=projects/*/locations/*/models/*}:batchPredict:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name['PredictionService'] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)