# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/topic_view_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import topic_view_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_topic__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/topic_view_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\025TopicViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\n9google/ads/googleads/v1/services/topic_view_service.proto\x12 google.ads.googleads.v1.services\x1a\x32google/ads/googleads/v1/resources/topic_view.proto\x1a\x1cgoogle/api/annotations.proto\",\n\x13GetTopicViewRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xbe\x01\n\x10TopicViewService\x12\xa9\x01\n\x0cGetTopicView\x12\x35.google.ads.googleads.v1.services.GetTopicViewRequest\x1a,.google.ads.googleads.v1.resources.TopicView\"4\x82\xd3\xe4\x93\x02.\x12,/v1/{resource_name=customers/*/topicViews/*}B\xfc\x01\n$com.google.ads.googleads.v1.servicesB\x15TopicViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_topic__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETTOPICVIEWREQUEST = _descriptor.Descriptor(
  name='GetTopicViewRequest',
  full_name='google.ads.googleads.v1.services.GetTopicViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetTopicViewRequest.resource_name', index=0,
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
  serialized_start=177,
  serialized_end=221,
)

DESCRIPTOR.message_types_by_name['GetTopicViewRequest'] = _GETTOPICVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTopicViewRequest = _reflection.GeneratedProtocolMessageType('GetTopicViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPICVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.topic_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetTopicViewRequest)
  })
_sym_db.RegisterMessage(GetTopicViewRequest)


DESCRIPTOR._options = None

_TOPICVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='TopicViewService',
  full_name='google.ads.googleads.v1.services.TopicViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=224,
  serialized_end=414,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTopicView',
    full_name='google.ads.googleads.v1.services.TopicViewService.GetTopicView',
    index=0,
    containing_service=None,
    input_type=_GETTOPICVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_topic__view__pb2._TOPICVIEW,
    serialized_options=b'\202\323\344\223\002.\022,/v1/{resource_name=customers/*/topicViews/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_TOPICVIEWSERVICE)

DESCRIPTOR.services_by_name['TopicViewService'] = _TOPICVIEWSERVICE

# @@protoc_insertion_point(module_scope)
