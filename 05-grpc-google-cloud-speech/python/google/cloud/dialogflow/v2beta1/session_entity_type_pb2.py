# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/session_entity_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.dialogflow.v2beta1 import entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_entity__type__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow/v2beta1/session_entity_type.proto',
  package='google.cloud.dialogflow.v2beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.dialogflow.v2beta1B\026SessionEntityTypeProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1',
  serialized_pb=b'\n9google/cloud/dialogflow/v2beta1/session_entity_type.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x31google/cloud/dialogflow/v2beta1/entity_type.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto\"\xd1\x02\n\x11SessionEntityType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x63\n\x14\x65ntity_override_mode\x18\x02 \x01(\x0e\x32\x45.google.cloud.dialogflow.v2beta1.SessionEntityType.EntityOverrideMode\x12\x44\n\x08\x65ntities\x18\x03 \x03(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.EntityType.Entity\"\x82\x01\n\x12\x45ntityOverrideMode\x12$\n ENTITY_OVERRIDE_MODE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45NTITY_OVERRIDE_MODE_OVERRIDE\x10\x01\x12#\n\x1f\x45NTITY_OVERRIDE_MODE_SUPPLEMENT\x10\x02\"V\n\x1dListSessionEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x8b\x01\n\x1eListSessionEntityTypesResponse\x12P\n\x14session_entity_types\x18\x01 \x03(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.SessionEntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"+\n\x1bGetSessionEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x81\x01\n\x1e\x43reateSessionEntityTypeRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12O\n\x13session_entity_type\x18\x02 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.SessionEntityType\"\xa2\x01\n\x1eUpdateSessionEntityTypeRequest\x12O\n\x13session_entity_type\x18\x01 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.SessionEntityType\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\".\n\x1e\x44\x65leteSessionEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\x8f\x15\n\x12SessionEntityTypes\x12\xdb\x03\n\x16ListSessionEntityTypes\x12>.google.cloud.dialogflow.v2beta1.ListSessionEntityTypesRequest\x1a?.google.cloud.dialogflow.v2beta1.ListSessionEntityTypesResponse\"\xbf\x02\x82\xd3\xe4\x93\x02\xb8\x02\x12\x39/v2beta1/{parent=projects/*/agent/sessions/*}/entityTypesZR\x12P/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypesZG\x12\x45/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/entityTypesZ^\x12\\/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes\x12\xca\x03\n\x14GetSessionEntityType\x12<.google.cloud.dialogflow.v2beta1.GetSessionEntityTypeRequest\x1a\x32.google.cloud.dialogflow.v2beta1.SessionEntityType\"\xbf\x02\x82\xd3\xe4\x93\x02\xb8\x02\x12\x39/v2beta1/{name=projects/*/agent/sessions/*/entityTypes/*}ZR\x12P/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZG\x12\x45/v2beta1/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}Z^\x12\\/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\x12\xa4\x04\n\x17\x43reateSessionEntityType\x12?.google.cloud.dialogflow.v2beta1.CreateSessionEntityTypeRequest\x1a\x32.google.cloud.dialogflow.v2beta1.SessionEntityType\"\x93\x03\x82\xd3\xe4\x93\x02\x8c\x03\"9/v2beta1/{parent=projects/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZg\"P/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_typeZ\\\"E/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZs\"\\/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_type\x12\xf5\x04\n\x17UpdateSessionEntityType\x12?.google.cloud.dialogflow.v2beta1.UpdateSessionEntityTypeRequest\x1a\x32.google.cloud.dialogflow.v2beta1.SessionEntityType\"\xe4\x03\x82\xd3\xe4\x93\x02\xdd\x03\x32M/v2beta1/{session_entity_type.name=projects/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZ{2d/v2beta1/{session_entity_type.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_typeZp2Y/v2beta1/{session_entity_type.name=projects/*/locations/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZ\x87\x01\x32p/v2beta1/{session_entity_type.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_type\x12\xb4\x03\n\x17\x44\x65leteSessionEntityType\x12?.google.cloud.dialogflow.v2beta1.DeleteSessionEntityTypeRequest\x1a\x16.google.protobuf.Empty\"\xbf\x02\x82\xd3\xe4\x93\x02\xb8\x02*9/v2beta1/{name=projects/*/agent/sessions/*/entityTypes/*}ZR*P/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZG*E/v2beta1/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}Z^*\\/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xb4\x01\n#com.google.cloud.dialogflow.v2beta1B\x16SessionEntityTypeProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_entity__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])



_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE = _descriptor.EnumDescriptor(
  name='EntityOverrideMode',
  full_name='google.cloud.dialogflow.v2beta1.SessionEntityType.EntityOverrideMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTITY_OVERRIDE_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY_OVERRIDE_MODE_OVERRIDE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY_OVERRIDE_MODE_SUPPLEMENT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=471,
  serialized_end=601,
)
_sym_db.RegisterEnumDescriptor(_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE)


_SESSIONENTITYTYPE = _descriptor.Descriptor(
  name='SessionEntityType',
  full_name='google.cloud.dialogflow.v2beta1.SessionEntityType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.SessionEntityType.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_override_mode', full_name='google.cloud.dialogflow.v2beta1.SessionEntityType.entity_override_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entities', full_name='google.cloud.dialogflow.v2beta1.SessionEntityType.entities', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONENTITYTYPE_ENTITYOVERRIDEMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=601,
)


_LISTSESSIONENTITYTYPESREQUEST = _descriptor.Descriptor(
  name='ListSessionEntityTypesRequest',
  full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesRequest.page_token', index=2,
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
  ],
  serialized_start=603,
  serialized_end=689,
)


_LISTSESSIONENTITYTYPESRESPONSE = _descriptor.Descriptor(
  name='ListSessionEntityTypesResponse',
  full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_entity_types', full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesResponse.session_entity_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.v2beta1.ListSessionEntityTypesResponse.next_page_token', index=1,
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
  serialized_start=692,
  serialized_end=831,
)


_GETSESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='GetSessionEntityTypeRequest',
  full_name='google.cloud.dialogflow.v2beta1.GetSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.GetSessionEntityTypeRequest.name', index=0,
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
  serialized_start=833,
  serialized_end=876,
)


_CREATESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='CreateSessionEntityTypeRequest',
  full_name='google.cloud.dialogflow.v2beta1.CreateSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.CreateSessionEntityTypeRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_entity_type', full_name='google.cloud.dialogflow.v2beta1.CreateSessionEntityTypeRequest.session_entity_type', index=1,
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
  serialized_start=879,
  serialized_end=1008,
)


_UPDATESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateSessionEntityTypeRequest',
  full_name='google.cloud.dialogflow.v2beta1.UpdateSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_entity_type', full_name='google.cloud.dialogflow.v2beta1.UpdateSessionEntityTypeRequest.session_entity_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.dialogflow.v2beta1.UpdateSessionEntityTypeRequest.update_mask', index=1,
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
  serialized_start=1011,
  serialized_end=1173,
)


_DELETESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='DeleteSessionEntityTypeRequest',
  full_name='google.cloud.dialogflow.v2beta1.DeleteSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.DeleteSessionEntityTypeRequest.name', index=0,
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
  serialized_start=1175,
  serialized_end=1221,
)

_SESSIONENTITYTYPE.fields_by_name['entity_override_mode'].enum_type = _SESSIONENTITYTYPE_ENTITYOVERRIDEMODE
_SESSIONENTITYTYPE.fields_by_name['entities'].message_type = google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_entity__type__pb2._ENTITYTYPE_ENTITY
_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE.containing_type = _SESSIONENTITYTYPE
_LISTSESSIONENTITYTYPESRESPONSE.fields_by_name['session_entity_types'].message_type = _SESSIONENTITYTYPE
_CREATESESSIONENTITYTYPEREQUEST.fields_by_name['session_entity_type'].message_type = _SESSIONENTITYTYPE
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name['session_entity_type'].message_type = _SESSIONENTITYTYPE
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['SessionEntityType'] = _SESSIONENTITYTYPE
DESCRIPTOR.message_types_by_name['ListSessionEntityTypesRequest'] = _LISTSESSIONENTITYTYPESREQUEST
DESCRIPTOR.message_types_by_name['ListSessionEntityTypesResponse'] = _LISTSESSIONENTITYTYPESRESPONSE
DESCRIPTOR.message_types_by_name['GetSessionEntityTypeRequest'] = _GETSESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['CreateSessionEntityTypeRequest'] = _CREATESESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateSessionEntityTypeRequest'] = _UPDATESESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['DeleteSessionEntityTypeRequest'] = _DELETESESSIONENTITYTYPEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionEntityType = _reflection.GeneratedProtocolMessageType('SessionEntityType', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONENTITYTYPE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.SessionEntityType)
  })
_sym_db.RegisterMessage(SessionEntityType)

ListSessionEntityTypesRequest = _reflection.GeneratedProtocolMessageType('ListSessionEntityTypesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSESSIONENTITYTYPESREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListSessionEntityTypesRequest)
  })
_sym_db.RegisterMessage(ListSessionEntityTypesRequest)

ListSessionEntityTypesResponse = _reflection.GeneratedProtocolMessageType('ListSessionEntityTypesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSESSIONENTITYTYPESRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListSessionEntityTypesResponse)
  })
_sym_db.RegisterMessage(ListSessionEntityTypesResponse)

GetSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('GetSessionEntityTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSESSIONENTITYTYPEREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetSessionEntityTypeRequest)
  })
_sym_db.RegisterMessage(GetSessionEntityTypeRequest)

CreateSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('CreateSessionEntityTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESESSIONENTITYTYPEREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateSessionEntityTypeRequest)
  })
_sym_db.RegisterMessage(CreateSessionEntityTypeRequest)

UpdateSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateSessionEntityTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESESSIONENTITYTYPEREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.UpdateSessionEntityTypeRequest)
  })
_sym_db.RegisterMessage(UpdateSessionEntityTypeRequest)

DeleteSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('DeleteSessionEntityTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESESSIONENTITYTYPEREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DeleteSessionEntityTypeRequest)
  })
_sym_db.RegisterMessage(DeleteSessionEntityTypeRequest)


DESCRIPTOR._options = None

_SESSIONENTITYTYPES = _descriptor.ServiceDescriptor(
  name='SessionEntityTypes',
  full_name='google.cloud.dialogflow.v2beta1.SessionEntityTypes',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow',
  serialized_start=1224,
  serialized_end=3927,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListSessionEntityTypes',
    full_name='google.cloud.dialogflow.v2beta1.SessionEntityTypes.ListSessionEntityTypes',
    index=0,
    containing_service=None,
    input_type=_LISTSESSIONENTITYTYPESREQUEST,
    output_type=_LISTSESSIONENTITYTYPESRESPONSE,
    serialized_options=b'\202\323\344\223\002\270\002\0229/v2beta1/{parent=projects/*/agent/sessions/*}/entityTypesZR\022P/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypesZG\022E/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/entityTypesZ^\022\\/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes',
  ),
  _descriptor.MethodDescriptor(
    name='GetSessionEntityType',
    full_name='google.cloud.dialogflow.v2beta1.SessionEntityTypes.GetSessionEntityType',
    index=1,
    containing_service=None,
    input_type=_GETSESSIONENTITYTYPEREQUEST,
    output_type=_SESSIONENTITYTYPE,
    serialized_options=b'\202\323\344\223\002\270\002\0229/v2beta1/{name=projects/*/agent/sessions/*/entityTypes/*}ZR\022P/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZG\022E/v2beta1/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}Z^\022\\/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}',
  ),
  _descriptor.MethodDescriptor(
    name='CreateSessionEntityType',
    full_name='google.cloud.dialogflow.v2beta1.SessionEntityTypes.CreateSessionEntityType',
    index=2,
    containing_service=None,
    input_type=_CREATESESSIONENTITYTYPEREQUEST,
    output_type=_SESSIONENTITYTYPE,
    serialized_options=b'\202\323\344\223\002\214\003\"9/v2beta1/{parent=projects/*/agent/sessions/*}/entityTypes:\023session_entity_typeZg\"P/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes:\023session_entity_typeZ\\\"E/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/entityTypes:\023session_entity_typeZs\"\\/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes:\023session_entity_type',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSessionEntityType',
    full_name='google.cloud.dialogflow.v2beta1.SessionEntityTypes.UpdateSessionEntityType',
    index=3,
    containing_service=None,
    input_type=_UPDATESESSIONENTITYTYPEREQUEST,
    output_type=_SESSIONENTITYTYPE,
    serialized_options=b'\202\323\344\223\002\335\0032M/v2beta1/{session_entity_type.name=projects/*/agent/sessions/*/entityTypes/*}:\023session_entity_typeZ{2d/v2beta1/{session_entity_type.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\023session_entity_typeZp2Y/v2beta1/{session_entity_type.name=projects/*/locations/*/agent/sessions/*/entityTypes/*}:\023session_entity_typeZ\207\0012p/v2beta1/{session_entity_type.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\023session_entity_type',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSessionEntityType',
    full_name='google.cloud.dialogflow.v2beta1.SessionEntityTypes.DeleteSessionEntityType',
    index=4,
    containing_service=None,
    input_type=_DELETESESSIONENTITYTYPEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\270\002*9/v2beta1/{name=projects/*/agent/sessions/*/entityTypes/*}ZR*P/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZG*E/v2beta1/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}Z^*\\/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONENTITYTYPES)

DESCRIPTOR.services_by_name['SessionEntityTypes'] = _SESSIONENTITYTYPES

# @@protoc_insertion_point(module_scope)
