# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/recommender/v1beta1/recommender_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.recommender.v1beta1 import recommendation_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/recommender/v1beta1/recommender_service.proto',
  package='google.cloud.recommender.v1beta1',
  syntax='proto3',
  serialized_options=b'\n$com.google.cloud.recommender.v1beta1B\020RecommenderProtoP\001ZKgoogle.golang.org/genproto/googleapis/cloud/recommender/v1beta1;recommender\242\002\004CREC\252\002!Google.Cloud.Recommmender.V1Beta1',
  serialized_pb=b'\n:google/cloud/recommender/v1beta1/recommender_service.proto\x12 google.cloud.recommender.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x35google/cloud/recommender/v1beta1/recommendation.proto\x1a\x17google/api/client.proto\"c\n\x1aListRecommendationsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\"\x81\x01\n\x1bListRecommendationsResponse\x12I\n\x0frecommendations\x18\x01 \x03(\x0b\x32\x30.google.cloud.recommender.v1beta1.Recommendation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"(\n\x18GetRecommendationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xe3\x01\n MarkRecommendationClaimedRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12m\n\x0estate_metadata\x18\x02 \x03(\x0b\x32U.google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.StateMetadataEntry\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe7\x01\n\"MarkRecommendationSucceededRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12o\n\x0estate_metadata\x18\x02 \x03(\x0b\x32W.google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.StateMetadataEntry\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe1\x01\n\x1fMarkRecommendationFailedRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12l\n\x0estate_metadata\x18\x02 \x03(\x0b\x32T.google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.StateMetadataEntry\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xf7\t\n\x0bRecommender\x12\xe3\x01\n\x13ListRecommendations\x12<.google.cloud.recommender.v1beta1.ListRecommendationsRequest\x1a=.google.cloud.recommender.v1beta1.ListRecommendationsResponse\"O\x82\xd3\xe4\x93\x02I\x12G/v1beta1/{parent=projects/*/locations/*/recommenders/*}/recommendations\x12\xd2\x01\n\x11GetRecommendation\x12:.google.cloud.recommender.v1beta1.GetRecommendationRequest\x1a\x30.google.cloud.recommender.v1beta1.Recommendation\"O\x82\xd3\xe4\x93\x02I\x12G/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}\x12\xf1\x01\n\x19MarkRecommendationClaimed\x12\x42.google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest\x1a\x30.google.cloud.recommender.v1beta1.Recommendation\"^\x82\xd3\xe4\x93\x02X\"S/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*\x12\xf7\x01\n\x1bMarkRecommendationSucceeded\x12\x44.google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest\x1a\x30.google.cloud.recommender.v1beta1.Recommendation\"`\x82\xd3\xe4\x93\x02Z\"U/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*\x12\xee\x01\n\x18MarkRecommendationFailed\x12\x41.google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest\x1a\x30.google.cloud.recommender.v1beta1.Recommendation\"]\x82\xd3\xe4\x93\x02W\"R/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*\x1aN\xca\x41\x1arecommender.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xb2\x01\n$com.google.cloud.recommender.v1beta1B\x10RecommenderProtoP\x01ZKgoogle.golang.org/genproto/googleapis/cloud/recommender/v1beta1;recommender\xa2\x02\x04\x43REC\xaa\x02!Google.Cloud.Recommmender.V1Beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_LISTRECOMMENDATIONSREQUEST = _descriptor.Descriptor(
  name='ListRecommendationsRequest',
  full_name='google.cloud.recommender.v1beta1.ListRecommendationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.recommender.v1beta1.ListRecommendationsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.recommender.v1beta1.ListRecommendationsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.recommender.v1beta1.ListRecommendationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.recommender.v1beta1.ListRecommendationsRequest.filter', index=3,
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
  ],
  serialized_start=239,
  serialized_end=338,
)


_LISTRECOMMENDATIONSRESPONSE = _descriptor.Descriptor(
  name='ListRecommendationsResponse',
  full_name='google.cloud.recommender.v1beta1.ListRecommendationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recommendations', full_name='google.cloud.recommender.v1beta1.ListRecommendationsResponse.recommendations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.recommender.v1beta1.ListRecommendationsResponse.next_page_token', index=1,
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
  serialized_start=341,
  serialized_end=470,
)


_GETRECOMMENDATIONREQUEST = _descriptor.Descriptor(
  name='GetRecommendationRequest',
  full_name='google.cloud.recommender.v1beta1.GetRecommendationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.recommender.v1beta1.GetRecommendationRequest.name', index=0,
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
  serialized_start=472,
  serialized_end=512,
)


_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY = _descriptor.Descriptor(
  name='StateMetadataEntry',
  full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.StateMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.StateMetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.StateMetadataEntry.value', index=1,
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
  serialized_start=690,
  serialized_end=742,
)

_MARKRECOMMENDATIONCLAIMEDREQUEST = _descriptor.Descriptor(
  name='MarkRecommendationClaimedRequest',
  full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_metadata', full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.state_metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etag', full_name='google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.etag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=742,
)


_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY = _descriptor.Descriptor(
  name='StateMetadataEntry',
  full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.StateMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.StateMetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.StateMetadataEntry.value', index=1,
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
  serialized_start=690,
  serialized_end=742,
)

_MARKRECOMMENDATIONSUCCEEDEDREQUEST = _descriptor.Descriptor(
  name='MarkRecommendationSucceededRequest',
  full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_metadata', full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.state_metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etag', full_name='google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.etag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=745,
  serialized_end=976,
)


_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY = _descriptor.Descriptor(
  name='StateMetadataEntry',
  full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.StateMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.StateMetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.StateMetadataEntry.value', index=1,
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
  serialized_start=690,
  serialized_end=742,
)

_MARKRECOMMENDATIONFAILEDREQUEST = _descriptor.Descriptor(
  name='MarkRecommendationFailedRequest',
  full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_metadata', full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.state_metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etag', full_name='google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.etag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=979,
  serialized_end=1204,
)

_LISTRECOMMENDATIONSRESPONSE.fields_by_name['recommendations'].message_type = google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2._RECOMMENDATION
_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY.containing_type = _MARKRECOMMENDATIONCLAIMEDREQUEST
_MARKRECOMMENDATIONCLAIMEDREQUEST.fields_by_name['state_metadata'].message_type = _MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY
_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY.containing_type = _MARKRECOMMENDATIONSUCCEEDEDREQUEST
_MARKRECOMMENDATIONSUCCEEDEDREQUEST.fields_by_name['state_metadata'].message_type = _MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY
_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY.containing_type = _MARKRECOMMENDATIONFAILEDREQUEST
_MARKRECOMMENDATIONFAILEDREQUEST.fields_by_name['state_metadata'].message_type = _MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY
DESCRIPTOR.message_types_by_name['ListRecommendationsRequest'] = _LISTRECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListRecommendationsResponse'] = _LISTRECOMMENDATIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetRecommendationRequest'] = _GETRECOMMENDATIONREQUEST
DESCRIPTOR.message_types_by_name['MarkRecommendationClaimedRequest'] = _MARKRECOMMENDATIONCLAIMEDREQUEST
DESCRIPTOR.message_types_by_name['MarkRecommendationSucceededRequest'] = _MARKRECOMMENDATIONSUCCEEDEDREQUEST
DESCRIPTOR.message_types_by_name['MarkRecommendationFailedRequest'] = _MARKRECOMMENDATIONFAILEDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListRecommendationsRequest = _reflection.GeneratedProtocolMessageType('ListRecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECOMMENDATIONSREQUEST,
  '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.ListRecommendationsRequest)
  })
_sym_db.RegisterMessage(ListRecommendationsRequest)

ListRecommendationsResponse = _reflection.GeneratedProtocolMessageType('ListRecommendationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECOMMENDATIONSRESPONSE,
  '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.ListRecommendationsResponse)
  })
_sym_db.RegisterMessage(ListRecommendationsResponse)

GetRecommendationRequest = _reflection.GeneratedProtocolMessageType('GetRecommendationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRECOMMENDATIONREQUEST,
  '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.GetRecommendationRequest)
  })
_sym_db.RegisterMessage(GetRecommendationRequest)

MarkRecommendationClaimedRequest = _reflection.GeneratedProtocolMessageType('MarkRecommendationClaimedRequest', (_message.Message,), {

  'StateMetadataEntry' : _reflection.GeneratedProtocolMessageType('StateMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY,
    '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.StateMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _MARKRECOMMENDATIONCLAIMEDREQUEST,
  '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest)
  })
_sym_db.RegisterMessage(MarkRecommendationClaimedRequest)
_sym_db.RegisterMessage(MarkRecommendationClaimedRequest.StateMetadataEntry)

MarkRecommendationSucceededRequest = _reflection.GeneratedProtocolMessageType('MarkRecommendationSucceededRequest', (_message.Message,), {

  'StateMetadataEntry' : _reflection.GeneratedProtocolMessageType('StateMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY,
    '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.StateMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _MARKRECOMMENDATIONSUCCEEDEDREQUEST,
  '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest)
  })
_sym_db.RegisterMessage(MarkRecommendationSucceededRequest)
_sym_db.RegisterMessage(MarkRecommendationSucceededRequest.StateMetadataEntry)

MarkRecommendationFailedRequest = _reflection.GeneratedProtocolMessageType('MarkRecommendationFailedRequest', (_message.Message,), {

  'StateMetadataEntry' : _reflection.GeneratedProtocolMessageType('StateMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY,
    '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.StateMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _MARKRECOMMENDATIONFAILEDREQUEST,
  '__module__' : 'google.cloud.recommender.v1beta1.recommender_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest)
  })
_sym_db.RegisterMessage(MarkRecommendationFailedRequest)
_sym_db.RegisterMessage(MarkRecommendationFailedRequest.StateMetadataEntry)


DESCRIPTOR._options = None
_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY._options = None
_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY._options = None
_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY._options = None

_RECOMMENDER = _descriptor.ServiceDescriptor(
  name='Recommender',
  full_name='google.cloud.recommender.v1beta1.Recommender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\032recommender.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  serialized_start=1207,
  serialized_end=2478,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListRecommendations',
    full_name='google.cloud.recommender.v1beta1.Recommender.ListRecommendations',
    index=0,
    containing_service=None,
    input_type=_LISTRECOMMENDATIONSREQUEST,
    output_type=_LISTRECOMMENDATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002I\022G/v1beta1/{parent=projects/*/locations/*/recommenders/*}/recommendations',
  ),
  _descriptor.MethodDescriptor(
    name='GetRecommendation',
    full_name='google.cloud.recommender.v1beta1.Recommender.GetRecommendation',
    index=1,
    containing_service=None,
    input_type=_GETRECOMMENDATIONREQUEST,
    output_type=google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2._RECOMMENDATION,
    serialized_options=b'\202\323\344\223\002I\022G/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MarkRecommendationClaimed',
    full_name='google.cloud.recommender.v1beta1.Recommender.MarkRecommendationClaimed',
    index=2,
    containing_service=None,
    input_type=_MARKRECOMMENDATIONCLAIMEDREQUEST,
    output_type=google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2._RECOMMENDATION,
    serialized_options=b'\202\323\344\223\002X\"S/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='MarkRecommendationSucceeded',
    full_name='google.cloud.recommender.v1beta1.Recommender.MarkRecommendationSucceeded',
    index=3,
    containing_service=None,
    input_type=_MARKRECOMMENDATIONSUCCEEDEDREQUEST,
    output_type=google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2._RECOMMENDATION,
    serialized_options=b'\202\323\344\223\002Z\"U/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='MarkRecommendationFailed',
    full_name='google.cloud.recommender.v1beta1.Recommender.MarkRecommendationFailed',
    index=4,
    containing_service=None,
    input_type=_MARKRECOMMENDATIONFAILEDREQUEST,
    output_type=google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2._RECOMMENDATION,
    serialized_options=b'\202\323\344\223\002W\"R/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDER)

DESCRIPTOR.services_by_name['Recommender'] = _RECOMMENDER

# @@protoc_insertion_point(module_scope)