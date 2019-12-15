# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/feed_item_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import feed_item_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__item__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/feed_item_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\024FeedItemServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\n8google/ads/googleads/v1/services/feed_item_service.proto\x12 google.ads.googleads.v1.services\x1a\x31google/ads/googleads/v1/resources/feed_item.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"+\n\x12GetFeedItemRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xa6\x01\n\x16MutateFeedItemsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12G\n\noperations\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v1.services.FeedItemOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xe1\x01\n\x11\x46\x65\x65\x64ItemOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12=\n\x06\x63reate\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v1.resources.FeedItemH\x00\x12=\n\x06update\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v1.resources.FeedItemH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x95\x01\n\x17MutateFeedItemsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12G\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v1.services.MutateFeedItemResult\"-\n\x14MutateFeedItemResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xfd\x02\n\x0f\x46\x65\x65\x64ItemService\x12\xa5\x01\n\x0bGetFeedItem\x12\x34.google.ads.googleads.v1.services.GetFeedItemRequest\x1a+.google.ads.googleads.v1.resources.FeedItem\"3\x82\xd3\xe4\x93\x02-\x12+/v1/{resource_name=customers/*/feedItems/*}\x12\xc1\x01\n\x0fMutateFeedItems\x12\x38.google.ads.googleads.v1.services.MutateFeedItemsRequest\x1a\x39.google.ads.googleads.v1.services.MutateFeedItemsResponse\"9\x82\xd3\xe4\x93\x02\x33\"./v1/customers/{customer_id=*}/feedItems:mutate:\x01*B\xfb\x01\n$com.google.ads.googleads.v1.servicesB\x14\x46\x65\x65\x64ItemServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__item__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETFEEDITEMREQUEST = _descriptor.Descriptor(
  name='GetFeedItemRequest',
  full_name='google.ads.googleads.v1.services.GetFeedItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetFeedItemRequest.resource_name', index=0,
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
  serialized_start=266,
  serialized_end=309,
)


_MUTATEFEEDITEMSREQUEST = _descriptor.Descriptor(
  name='MutateFeedItemsRequest',
  full_name='google.ads.googleads.v1.services.MutateFeedItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateFeedItemsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateFeedItemsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v1.services.MutateFeedItemsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v1.services.MutateFeedItemsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=312,
  serialized_end=478,
)


_FEEDITEMOPERATION = _descriptor.Descriptor(
  name='FeedItemOperation',
  full_name='google.ads.googleads.v1.services.FeedItemOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v1.services.FeedItemOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.FeedItemOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v1.services.FeedItemOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.FeedItemOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
      name='operation', full_name='google.ads.googleads.v1.services.FeedItemOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=481,
  serialized_end=706,
)


_MUTATEFEEDITEMSRESPONSE = _descriptor.Descriptor(
  name='MutateFeedItemsResponse',
  full_name='google.ads.googleads.v1.services.MutateFeedItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v1.services.MutateFeedItemsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateFeedItemsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=709,
  serialized_end=858,
)


_MUTATEFEEDITEMRESULT = _descriptor.Descriptor(
  name='MutateFeedItemResult',
  full_name='google.ads.googleads.v1.services.MutateFeedItemResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateFeedItemResult.resource_name', index=0,
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
  serialized_start=860,
  serialized_end=905,
)

_MUTATEFEEDITEMSREQUEST.fields_by_name['operations'].message_type = _FEEDITEMOPERATION
_FEEDITEMOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_FEEDITEMOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__item__pb2._FEEDITEM
_FEEDITEMOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__item__pb2._FEEDITEM
_FEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDITEMOPERATION.fields_by_name['create'])
_FEEDITEMOPERATION.fields_by_name['create'].containing_oneof = _FEEDITEMOPERATION.oneofs_by_name['operation']
_FEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDITEMOPERATION.fields_by_name['update'])
_FEEDITEMOPERATION.fields_by_name['update'].containing_oneof = _FEEDITEMOPERATION.oneofs_by_name['operation']
_FEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDITEMOPERATION.fields_by_name['remove'])
_FEEDITEMOPERATION.fields_by_name['remove'].containing_oneof = _FEEDITEMOPERATION.oneofs_by_name['operation']
_MUTATEFEEDITEMSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEFEEDITEMSRESPONSE.fields_by_name['results'].message_type = _MUTATEFEEDITEMRESULT
DESCRIPTOR.message_types_by_name['GetFeedItemRequest'] = _GETFEEDITEMREQUEST
DESCRIPTOR.message_types_by_name['MutateFeedItemsRequest'] = _MUTATEFEEDITEMSREQUEST
DESCRIPTOR.message_types_by_name['FeedItemOperation'] = _FEEDITEMOPERATION
DESCRIPTOR.message_types_by_name['MutateFeedItemsResponse'] = _MUTATEFEEDITEMSRESPONSE
DESCRIPTOR.message_types_by_name['MutateFeedItemResult'] = _MUTATEFEEDITEMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeedItemRequest = _reflection.GeneratedProtocolMessageType('GetFeedItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEEDITEMREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetFeedItemRequest)
  })
_sym_db.RegisterMessage(GetFeedItemRequest)

MutateFeedItemsRequest = _reflection.GeneratedProtocolMessageType('MutateFeedItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEFEEDITEMSREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateFeedItemsRequest)
  })
_sym_db.RegisterMessage(MutateFeedItemsRequest)

FeedItemOperation = _reflection.GeneratedProtocolMessageType('FeedItemOperation', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMOPERATION,
  '__module__' : 'google.ads.googleads.v1.services.feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.FeedItemOperation)
  })
_sym_db.RegisterMessage(FeedItemOperation)

MutateFeedItemsResponse = _reflection.GeneratedProtocolMessageType('MutateFeedItemsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEFEEDITEMSRESPONSE,
  '__module__' : 'google.ads.googleads.v1.services.feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateFeedItemsResponse)
  })
_sym_db.RegisterMessage(MutateFeedItemsResponse)

MutateFeedItemResult = _reflection.GeneratedProtocolMessageType('MutateFeedItemResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEFEEDITEMRESULT,
  '__module__' : 'google.ads.googleads.v1.services.feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateFeedItemResult)
  })
_sym_db.RegisterMessage(MutateFeedItemResult)


DESCRIPTOR._options = None

_FEEDITEMSERVICE = _descriptor.ServiceDescriptor(
  name='FeedItemService',
  full_name='google.ads.googleads.v1.services.FeedItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=908,
  serialized_end=1289,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeedItem',
    full_name='google.ads.googleads.v1.services.FeedItemService.GetFeedItem',
    index=0,
    containing_service=None,
    input_type=_GETFEEDITEMREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_feed__item__pb2._FEEDITEM,
    serialized_options=b'\202\323\344\223\002-\022+/v1/{resource_name=customers/*/feedItems/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateFeedItems',
    full_name='google.ads.googleads.v1.services.FeedItemService.MutateFeedItems',
    index=1,
    containing_service=None,
    input_type=_MUTATEFEEDITEMSREQUEST,
    output_type=_MUTATEFEEDITEMSRESPONSE,
    serialized_options=b'\202\323\344\223\0023\"./v1/customers/{customer_id=*}/feedItems:mutate:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_FEEDITEMSERVICE)

DESCRIPTOR.services_by_name['FeedItemService'] = _FEEDITEMSERVICE

# @@protoc_insertion_point(module_scope)