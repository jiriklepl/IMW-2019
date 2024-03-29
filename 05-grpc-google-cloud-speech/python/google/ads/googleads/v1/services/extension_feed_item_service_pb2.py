# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/services/extension_feed_item_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v1.resources import extension_feed_item_pb2 as google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_extension__feed__item__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/services/extension_feed_item_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v1.servicesB\035ExtensionFeedItemServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services',
  serialized_pb=b'\nBgoogle/ads/googleads/v1/services/extension_feed_item_service.proto\x12 google.ads.googleads.v1.services\x1a;google/ads/googleads/v1/resources/extension_feed_item.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\"4\n\x1bGetExtensionFeedItemRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x9f\x01\n\x1fMutateExtensionFeedItemsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12P\n\noperations\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v1.services.ExtensionFeedItemOperation\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xfc\x01\n\x1a\x45xtensionFeedItemOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x46\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x34.google.ads.googleads.v1.resources.ExtensionFeedItemH\x00\x12\x46\n\x06update\x18\x02 \x01(\x0b\x32\x34.google.ads.googleads.v1.resources.ExtensionFeedItemH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"t\n MutateExtensionFeedItemsResponse\x12P\n\x07results\x18\x02 \x03(\x0b\x32?.google.ads.googleads.v1.services.MutateExtensionFeedItemResult\"6\n\x1dMutateExtensionFeedItemResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xce\x03\n\x18\x45xtensionFeedItemService\x12\xc9\x01\n\x14GetExtensionFeedItem\x12=.google.ads.googleads.v1.services.GetExtensionFeedItemRequest\x1a\x34.google.ads.googleads.v1.resources.ExtensionFeedItem\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/v1/{resource_name=customers/*/extensionFeedItems/*}\x12\xe5\x01\n\x18MutateExtensionFeedItems\x12\x41.google.ads.googleads.v1.services.MutateExtensionFeedItemsRequest\x1a\x42.google.ads.googleads.v1.services.MutateExtensionFeedItemsResponse\"B\x82\xd3\xe4\x93\x02<\"7/v1/customers/{customer_id=*}/extensionFeedItems:mutate:\x01*B\x84\x02\n$com.google.ads.googleads.v1.servicesB\x1d\x45xtensionFeedItemServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_extension__feed__item__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_GETEXTENSIONFEEDITEMREQUEST = _descriptor.Descriptor(
  name='GetExtensionFeedItemRequest',
  full_name='google.ads.googleads.v1.services.GetExtensionFeedItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetExtensionFeedItemRequest.resource_name', index=0,
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
  serialized_start=261,
  serialized_end=313,
)


_MUTATEEXTENSIONFEEDITEMSREQUEST = _descriptor.Descriptor(
  name='MutateExtensionFeedItemsRequest',
  full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemsRequest.validate_only', index=2,
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
  serialized_start=316,
  serialized_end=475,
)


_EXTENSIONFEEDITEMOPERATION = _descriptor.Descriptor(
  name='ExtensionFeedItemOperation',
  full_name='google.ads.googleads.v1.services.ExtensionFeedItemOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v1.services.ExtensionFeedItemOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.ExtensionFeedItemOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v1.services.ExtensionFeedItemOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.ExtensionFeedItemOperation.remove', index=3,
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
      name='operation', full_name='google.ads.googleads.v1.services.ExtensionFeedItemOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=478,
  serialized_end=730,
)


_MUTATEEXTENSIONFEEDITEMSRESPONSE = _descriptor.Descriptor(
  name='MutateExtensionFeedItemsResponse',
  full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemsResponse.results', index=0,
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
  serialized_start=732,
  serialized_end=848,
)


_MUTATEEXTENSIONFEEDITEMRESULT = _descriptor.Descriptor(
  name='MutateExtensionFeedItemResult',
  full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateExtensionFeedItemResult.resource_name', index=0,
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
  serialized_start=850,
  serialized_end=904,
)

_MUTATEEXTENSIONFEEDITEMSREQUEST.fields_by_name['operations'].message_type = _EXTENSIONFEEDITEMOPERATION
_EXTENSIONFEEDITEMOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_EXTENSIONFEEDITEMOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM
_EXTENSIONFEEDITEMOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM
_EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _EXTENSIONFEEDITEMOPERATION.fields_by_name['create'])
_EXTENSIONFEEDITEMOPERATION.fields_by_name['create'].containing_oneof = _EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation']
_EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _EXTENSIONFEEDITEMOPERATION.fields_by_name['update'])
_EXTENSIONFEEDITEMOPERATION.fields_by_name['update'].containing_oneof = _EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation']
_EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _EXTENSIONFEEDITEMOPERATION.fields_by_name['remove'])
_EXTENSIONFEEDITEMOPERATION.fields_by_name['remove'].containing_oneof = _EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation']
_MUTATEEXTENSIONFEEDITEMSRESPONSE.fields_by_name['results'].message_type = _MUTATEEXTENSIONFEEDITEMRESULT
DESCRIPTOR.message_types_by_name['GetExtensionFeedItemRequest'] = _GETEXTENSIONFEEDITEMREQUEST
DESCRIPTOR.message_types_by_name['MutateExtensionFeedItemsRequest'] = _MUTATEEXTENSIONFEEDITEMSREQUEST
DESCRIPTOR.message_types_by_name['ExtensionFeedItemOperation'] = _EXTENSIONFEEDITEMOPERATION
DESCRIPTOR.message_types_by_name['MutateExtensionFeedItemsResponse'] = _MUTATEEXTENSIONFEEDITEMSRESPONSE
DESCRIPTOR.message_types_by_name['MutateExtensionFeedItemResult'] = _MUTATEEXTENSIONFEEDITEMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetExtensionFeedItemRequest = _reflection.GeneratedProtocolMessageType('GetExtensionFeedItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEXTENSIONFEEDITEMREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetExtensionFeedItemRequest)
  })
_sym_db.RegisterMessage(GetExtensionFeedItemRequest)

MutateExtensionFeedItemsRequest = _reflection.GeneratedProtocolMessageType('MutateExtensionFeedItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEEXTENSIONFEEDITEMSREQUEST,
  '__module__' : 'google.ads.googleads.v1.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateExtensionFeedItemsRequest)
  })
_sym_db.RegisterMessage(MutateExtensionFeedItemsRequest)

ExtensionFeedItemOperation = _reflection.GeneratedProtocolMessageType('ExtensionFeedItemOperation', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONFEEDITEMOPERATION,
  '__module__' : 'google.ads.googleads.v1.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.ExtensionFeedItemOperation)
  })
_sym_db.RegisterMessage(ExtensionFeedItemOperation)

MutateExtensionFeedItemsResponse = _reflection.GeneratedProtocolMessageType('MutateExtensionFeedItemsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEEXTENSIONFEEDITEMSRESPONSE,
  '__module__' : 'google.ads.googleads.v1.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateExtensionFeedItemsResponse)
  })
_sym_db.RegisterMessage(MutateExtensionFeedItemsResponse)

MutateExtensionFeedItemResult = _reflection.GeneratedProtocolMessageType('MutateExtensionFeedItemResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEEXTENSIONFEEDITEMRESULT,
  '__module__' : 'google.ads.googleads.v1.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateExtensionFeedItemResult)
  })
_sym_db.RegisterMessage(MutateExtensionFeedItemResult)


DESCRIPTOR._options = None

_EXTENSIONFEEDITEMSERVICE = _descriptor.ServiceDescriptor(
  name='ExtensionFeedItemService',
  full_name='google.ads.googleads.v1.services.ExtensionFeedItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=907,
  serialized_end=1369,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetExtensionFeedItem',
    full_name='google.ads.googleads.v1.services.ExtensionFeedItemService.GetExtensionFeedItem',
    index=0,
    containing_service=None,
    input_type=_GETEXTENSIONFEEDITEMREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v1_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM,
    serialized_options=b'\202\323\344\223\0026\0224/v1/{resource_name=customers/*/extensionFeedItems/*}',
  ),
  _descriptor.MethodDescriptor(
    name='MutateExtensionFeedItems',
    full_name='google.ads.googleads.v1.services.ExtensionFeedItemService.MutateExtensionFeedItems',
    index=1,
    containing_service=None,
    input_type=_MUTATEEXTENSIONFEEDITEMSREQUEST,
    output_type=_MUTATEEXTENSIONFEEDITEMSRESPONSE,
    serialized_options=b'\202\323\344\223\002<\"7/v1/customers/{customer_id=*}/extensionFeedItems:mutate:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_EXTENSIONFEEDITEMSERVICE)

DESCRIPTOR.services_by_name['ExtensionFeedItemService'] = _EXTENSIONFEEDITEMSERVICE

# @@protoc_insertion_point(module_scope)
