# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/document.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.dialogflow.v2beta1 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_gcs__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow/v2beta1/document.proto',
  package='google.cloud.dialogflow.v2beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.dialogflow.v2beta1B\rDocumentProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1',
  serialized_pb=b'\n.google/cloud/dialogflow/v2beta1/document.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a)google/cloud/dialogflow/v2beta1/gcs.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto\"\xaf\x02\n\x08\x44ocument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x11\n\tmime_type\x18\x03 \x01(\t\x12P\n\x0fknowledge_types\x18\x04 \x03(\x0e\x32\x37.google.cloud.dialogflow.v2beta1.Document.KnowledgeType\x12\x15\n\x0b\x63ontent_uri\x18\x05 \x01(\tH\x00\x12\x15\n\x07\x63ontent\x18\x06 \x01(\tB\x02\x18\x01H\x00\x12\x15\n\x0braw_content\x18\t \x01(\x0cH\x00\"K\n\rKnowledgeType\x12\x1e\n\x1aKNOWLEDGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03\x46\x41Q\x10\x01\x12\x11\n\rEXTRACTIVE_QA\x10\x02\x42\x08\n\x06source\"M\n\x14ListDocumentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"n\n\x15ListDocumentsResponse\x12<\n\tdocuments\x18\x01 \x03(\x0b\x32).google.cloud.dialogflow.v2beta1.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\"\n\x12GetDocumentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"d\n\x15\x43reateDocumentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12;\n\x08\x64ocument\x18\x02 \x01(\x0b\x32).google.cloud.dialogflow.v2beta1.Document\"%\n\x15\x44\x65leteDocumentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x85\x01\n\x15UpdateDocumentRequest\x12;\n\x08\x64ocument\x18\x01 \x01(\x0b\x32).google.cloud.dialogflow.v2beta1.Document\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xb2\x01\n\x1aKnowledgeOperationMetadata\x12P\n\x05state\x18\x01 \x01(\x0e\x32\x41.google.cloud.dialogflow.v2beta1.KnowledgeOperationMetadata.State\"B\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\"q\n\x15ReloadDocumentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\ngcs_source\x18\x03 \x01(\x0b\x32*.google.cloud.dialogflow.v2beta1.GcsSourceH\x00\x42\x08\n\x06source2\x81\r\n\tDocuments\x12\x81\x02\n\rListDocuments\x12\x35.google.cloud.dialogflow.v2beta1.ListDocumentsRequest\x1a\x36.google.cloud.dialogflow.v2beta1.ListDocumentsResponse\"\x80\x01\x82\xd3\xe4\x93\x02z\x12\x37/v2beta1/{parent=projects/*/knowledgeBases/*}/documentsZ?\x12=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents\x12\xf0\x01\n\x0bGetDocument\x12\x33.google.cloud.dialogflow.v2beta1.GetDocumentRequest\x1a).google.cloud.dialogflow.v2beta1.Document\"\x80\x01\x82\xd3\xe4\x93\x02z\x12\x37/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}Z?\x12=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}\x12\xff\x01\n\x0e\x43reateDocument\x12\x36.google.cloud.dialogflow.v2beta1.CreateDocumentRequest\x1a\x1d.google.longrunning.Operation\"\x95\x01\x82\xd3\xe4\x93\x02\x8e\x01\"7/v2beta1/{parent=projects/*/knowledgeBases/*}/documents:\x08\x64ocumentZI\"=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents:\x08\x64ocument\x12\xea\x01\n\x0e\x44\x65leteDocument\x12\x36.google.cloud.dialogflow.v2beta1.DeleteDocumentRequest\x1a\x1d.google.longrunning.Operation\"\x80\x01\x82\xd3\xe4\x93\x02z*7/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}Z?*=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}\x12\x91\x02\n\x0eUpdateDocument\x12\x36.google.cloud.dialogflow.v2beta1.UpdateDocumentRequest\x1a\x1d.google.longrunning.Operation\"\xa7\x01\x82\xd3\xe4\x93\x02\xa0\x01\x32@/v2beta1/{document.name=projects/*/knowledgeBases/*/documents/*}:\x08\x64ocumentZR2F/v2beta1/{document.name=projects/*/agent/knowledgeBases/*/documents/*}:\x08\x64ocument\x12\xff\x01\n\x0eReloadDocument\x12\x36.google.cloud.dialogflow.v2beta1.ReloadDocumentRequest\x1a\x1d.google.longrunning.Operation\"\x95\x01\x82\xd3\xe4\x93\x02\x8e\x01\">/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}:reload:\x01*ZI\"D/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload:\x01*\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xab\x01\n#com.google.cloud.dialogflow.v2beta1B\rDocumentProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_gcs__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])



_DOCUMENT_KNOWLEDGETYPE = _descriptor.EnumDescriptor(
  name='KnowledgeType',
  full_name='google.cloud.dialogflow.v2beta1.Document.KnowledgeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KNOWLEDGE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAQ', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTRACTIVE_QA', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=558,
  serialized_end=633,
)
_sym_db.RegisterEnumDescriptor(_DOCUMENT_KNOWLEDGETYPE)

_KNOWLEDGEOPERATIONMETADATA_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.dialogflow.v2beta1.KnowledgeOperationMetadata.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1262,
  serialized_end=1328,
)
_sym_db.RegisterEnumDescriptor(_KNOWLEDGEOPERATIONMETADATA_STATE)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='google.cloud.dialogflow.v2beta1.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.Document.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.dialogflow.v2beta1.Document.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.cloud.dialogflow.v2beta1.Document.mime_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='knowledge_types', full_name='google.cloud.dialogflow.v2beta1.Document.knowledge_types', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_uri', full_name='google.cloud.dialogflow.v2beta1.Document.content_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='google.cloud.dialogflow.v2beta1.Document.content', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_content', full_name='google.cloud.dialogflow.v2beta1.Document.raw_content', index=6,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOCUMENT_KNOWLEDGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='google.cloud.dialogflow.v2beta1.Document.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=340,
  serialized_end=643,
)


_LISTDOCUMENTSREQUEST = _descriptor.Descriptor(
  name='ListDocumentsRequest',
  full_name='google.cloud.dialogflow.v2beta1.ListDocumentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.ListDocumentsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.v2beta1.ListDocumentsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.v2beta1.ListDocumentsRequest.page_token', index=2,
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
  serialized_start=645,
  serialized_end=722,
)


_LISTDOCUMENTSRESPONSE = _descriptor.Descriptor(
  name='ListDocumentsResponse',
  full_name='google.cloud.dialogflow.v2beta1.ListDocumentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='documents', full_name='google.cloud.dialogflow.v2beta1.ListDocumentsResponse.documents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.v2beta1.ListDocumentsResponse.next_page_token', index=1,
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
  serialized_end=834,
)


_GETDOCUMENTREQUEST = _descriptor.Descriptor(
  name='GetDocumentRequest',
  full_name='google.cloud.dialogflow.v2beta1.GetDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.GetDocumentRequest.name', index=0,
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
  serialized_start=836,
  serialized_end=870,
)


_CREATEDOCUMENTREQUEST = _descriptor.Descriptor(
  name='CreateDocumentRequest',
  full_name='google.cloud.dialogflow.v2beta1.CreateDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.CreateDocumentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document', full_name='google.cloud.dialogflow.v2beta1.CreateDocumentRequest.document', index=1,
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
  serialized_start=872,
  serialized_end=972,
)


_DELETEDOCUMENTREQUEST = _descriptor.Descriptor(
  name='DeleteDocumentRequest',
  full_name='google.cloud.dialogflow.v2beta1.DeleteDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.DeleteDocumentRequest.name', index=0,
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
  serialized_start=974,
  serialized_end=1011,
)


_UPDATEDOCUMENTREQUEST = _descriptor.Descriptor(
  name='UpdateDocumentRequest',
  full_name='google.cloud.dialogflow.v2beta1.UpdateDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='google.cloud.dialogflow.v2beta1.UpdateDocumentRequest.document', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.dialogflow.v2beta1.UpdateDocumentRequest.update_mask', index=1,
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
  serialized_start=1014,
  serialized_end=1147,
)


_KNOWLEDGEOPERATIONMETADATA = _descriptor.Descriptor(
  name='KnowledgeOperationMetadata',
  full_name='google.cloud.dialogflow.v2beta1.KnowledgeOperationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.dialogflow.v2beta1.KnowledgeOperationMetadata.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KNOWLEDGEOPERATIONMETADATA_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1150,
  serialized_end=1328,
)


_RELOADDOCUMENTREQUEST = _descriptor.Descriptor(
  name='ReloadDocumentRequest',
  full_name='google.cloud.dialogflow.v2beta1.ReloadDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.ReloadDocumentRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcs_source', full_name='google.cloud.dialogflow.v2beta1.ReloadDocumentRequest.gcs_source', index=1,
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
    _descriptor.OneofDescriptor(
      name='source', full_name='google.cloud.dialogflow.v2beta1.ReloadDocumentRequest.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1330,
  serialized_end=1443,
)

_DOCUMENT.fields_by_name['knowledge_types'].enum_type = _DOCUMENT_KNOWLEDGETYPE
_DOCUMENT_KNOWLEDGETYPE.containing_type = _DOCUMENT
_DOCUMENT.oneofs_by_name['source'].fields.append(
  _DOCUMENT.fields_by_name['content_uri'])
_DOCUMENT.fields_by_name['content_uri'].containing_oneof = _DOCUMENT.oneofs_by_name['source']
_DOCUMENT.oneofs_by_name['source'].fields.append(
  _DOCUMENT.fields_by_name['content'])
_DOCUMENT.fields_by_name['content'].containing_oneof = _DOCUMENT.oneofs_by_name['source']
_DOCUMENT.oneofs_by_name['source'].fields.append(
  _DOCUMENT.fields_by_name['raw_content'])
_DOCUMENT.fields_by_name['raw_content'].containing_oneof = _DOCUMENT.oneofs_by_name['source']
_LISTDOCUMENTSRESPONSE.fields_by_name['documents'].message_type = _DOCUMENT
_CREATEDOCUMENTREQUEST.fields_by_name['document'].message_type = _DOCUMENT
_UPDATEDOCUMENTREQUEST.fields_by_name['document'].message_type = _DOCUMENT
_UPDATEDOCUMENTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_KNOWLEDGEOPERATIONMETADATA.fields_by_name['state'].enum_type = _KNOWLEDGEOPERATIONMETADATA_STATE
_KNOWLEDGEOPERATIONMETADATA_STATE.containing_type = _KNOWLEDGEOPERATIONMETADATA
_RELOADDOCUMENTREQUEST.fields_by_name['gcs_source'].message_type = google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_gcs__pb2._GCSSOURCE
_RELOADDOCUMENTREQUEST.oneofs_by_name['source'].fields.append(
  _RELOADDOCUMENTREQUEST.fields_by_name['gcs_source'])
_RELOADDOCUMENTREQUEST.fields_by_name['gcs_source'].containing_oneof = _RELOADDOCUMENTREQUEST.oneofs_by_name['source']
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['ListDocumentsRequest'] = _LISTDOCUMENTSREQUEST
DESCRIPTOR.message_types_by_name['ListDocumentsResponse'] = _LISTDOCUMENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetDocumentRequest'] = _GETDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['CreateDocumentRequest'] = _CREATEDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['DeleteDocumentRequest'] = _DELETEDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['UpdateDocumentRequest'] = _UPDATEDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['KnowledgeOperationMetadata'] = _KNOWLEDGEOPERATIONMETADATA
DESCRIPTOR.message_types_by_name['ReloadDocumentRequest'] = _RELOADDOCUMENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.Document)
  })
_sym_db.RegisterMessage(Document)

ListDocumentsRequest = _reflection.GeneratedProtocolMessageType('ListDocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOCUMENTSREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListDocumentsRequest)
  })
_sym_db.RegisterMessage(ListDocumentsRequest)

ListDocumentsResponse = _reflection.GeneratedProtocolMessageType('ListDocumentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOCUMENTSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListDocumentsResponse)
  })
_sym_db.RegisterMessage(ListDocumentsResponse)

GetDocumentRequest = _reflection.GeneratedProtocolMessageType('GetDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDOCUMENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetDocumentRequest)
  })
_sym_db.RegisterMessage(GetDocumentRequest)

CreateDocumentRequest = _reflection.GeneratedProtocolMessageType('CreateDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOCUMENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateDocumentRequest)
  })
_sym_db.RegisterMessage(CreateDocumentRequest)

DeleteDocumentRequest = _reflection.GeneratedProtocolMessageType('DeleteDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOCUMENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DeleteDocumentRequest)
  })
_sym_db.RegisterMessage(DeleteDocumentRequest)

UpdateDocumentRequest = _reflection.GeneratedProtocolMessageType('UpdateDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDOCUMENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.UpdateDocumentRequest)
  })
_sym_db.RegisterMessage(UpdateDocumentRequest)

KnowledgeOperationMetadata = _reflection.GeneratedProtocolMessageType('KnowledgeOperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _KNOWLEDGEOPERATIONMETADATA,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.KnowledgeOperationMetadata)
  })
_sym_db.RegisterMessage(KnowledgeOperationMetadata)

ReloadDocumentRequest = _reflection.GeneratedProtocolMessageType('ReloadDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELOADDOCUMENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ReloadDocumentRequest)
  })
_sym_db.RegisterMessage(ReloadDocumentRequest)


DESCRIPTOR._options = None
_DOCUMENT.fields_by_name['content']._options = None

_DOCUMENTS = _descriptor.ServiceDescriptor(
  name='Documents',
  full_name='google.cloud.dialogflow.v2beta1.Documents',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow',
  serialized_start=1446,
  serialized_end=3111,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListDocuments',
    full_name='google.cloud.dialogflow.v2beta1.Documents.ListDocuments',
    index=0,
    containing_service=None,
    input_type=_LISTDOCUMENTSREQUEST,
    output_type=_LISTDOCUMENTSRESPONSE,
    serialized_options=b'\202\323\344\223\002z\0227/v2beta1/{parent=projects/*/knowledgeBases/*}/documentsZ?\022=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents',
  ),
  _descriptor.MethodDescriptor(
    name='GetDocument',
    full_name='google.cloud.dialogflow.v2beta1.Documents.GetDocument',
    index=1,
    containing_service=None,
    input_type=_GETDOCUMENTREQUEST,
    output_type=_DOCUMENT,
    serialized_options=b'\202\323\344\223\002z\0227/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}Z?\022=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}',
  ),
  _descriptor.MethodDescriptor(
    name='CreateDocument',
    full_name='google.cloud.dialogflow.v2beta1.Documents.CreateDocument',
    index=2,
    containing_service=None,
    input_type=_CREATEDOCUMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\216\001\"7/v2beta1/{parent=projects/*/knowledgeBases/*}/documents:\010documentZI\"=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents:\010document',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteDocument',
    full_name='google.cloud.dialogflow.v2beta1.Documents.DeleteDocument',
    index=3,
    containing_service=None,
    input_type=_DELETEDOCUMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002z*7/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}Z?*=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateDocument',
    full_name='google.cloud.dialogflow.v2beta1.Documents.UpdateDocument',
    index=4,
    containing_service=None,
    input_type=_UPDATEDOCUMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\240\0012@/v2beta1/{document.name=projects/*/knowledgeBases/*/documents/*}:\010documentZR2F/v2beta1/{document.name=projects/*/agent/knowledgeBases/*/documents/*}:\010document',
  ),
  _descriptor.MethodDescriptor(
    name='ReloadDocument',
    full_name='google.cloud.dialogflow.v2beta1.Documents.ReloadDocument',
    index=5,
    containing_service=None,
    input_type=_RELOADDOCUMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\216\001\">/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}:reload:\001*ZI\"D/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_DOCUMENTS)

DESCRIPTOR.services_by_name['Documents'] = _DOCUMENTS

# @@protoc_insertion_point(module_scope)