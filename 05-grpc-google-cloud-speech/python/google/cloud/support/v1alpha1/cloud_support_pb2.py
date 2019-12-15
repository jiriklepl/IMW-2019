# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/support/v1alpha1/cloud_support.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.support import common_pb2 as google_dot_cloud_dot_support_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/support/v1alpha1/cloud_support.proto',
  package='google.cloud.support.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n!com.google.cloud.support.v1alpha1B\021CloudSupportProtoZDgoogle.golang.org/genproto/googleapis/cloud/support/v1alpha1;support',
  serialized_pb=b'\n1google/cloud/support/v1alpha1/cloud_support.proto\x12\x1dgoogle.cloud.support.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a!google/cloud/support/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"(\n\x18GetSupportAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"S\n\x1aListSupportAccountsRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"u\n\x1bListSupportAccountsResponse\x12=\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32+.google.cloud.support.common.SupportAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1e\n\x0eGetCaseRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"W\n\x10ListCasesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\t\"^\n\x11ListCasesResponse\x12\x30\n\x05\x63\x61ses\x18\x01 \x03(\x0b\x32!.google.cloud.support.common.Case\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"#\n\x13ListCommentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"N\n\x14ListCommentsResponse\x12\x36\n\x08\x63omments\x18\x01 \x03(\x0b\x32$.google.cloud.support.common.Comment\"T\n\x11\x43reateCaseRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12/\n\x04\x63\x61se\x18\x02 \x01(\x0b\x32!.google.cloud.support.common.Case\"u\n\x11UpdateCaseRequest\x12/\n\x04\x63\x61se\x18\x01 \x01(\x0b\x32!.google.cloud.support.common.Case\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"[\n\x14\x43reateCommentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x07\x63omment\x18\x02 \x01(\x0b\x32$.google.cloud.support.common.Comment\"\x19\n\x17GetIssueTaxonomyRequest2\xe5\x0b\n\x0c\x43loudSupport\x12\xa5\x01\n\x11GetSupportAccount\x12\x37.google.cloud.support.v1alpha1.GetSupportAccountRequest\x1a+.google.cloud.support.common.SupportAccount\"*\x82\xd3\xe4\x93\x02$\x12\"/v1alpha1/{name=supportAccounts/*}\x12\xaf\x01\n\x13ListSupportAccounts\x12\x39.google.cloud.support.v1alpha1.ListSupportAccountsRequest\x1a:.google.cloud.support.v1alpha1.ListSupportAccountsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1alpha1/supportAccounts\x12\x8f\x01\n\x07GetCase\x12-.google.cloud.support.v1alpha1.GetCaseRequest\x1a!.google.cloud.support.common.Case\"2\x82\xd3\xe4\x93\x02,\x12*/v1alpha1/{name=supportAccounts/*/cases/*}\x12\xa0\x01\n\tListCases\x12/.google.cloud.support.v1alpha1.ListCasesRequest\x1a\x30.google.cloud.support.v1alpha1.ListCasesResponse\"0\x82\xd3\xe4\x93\x02*\x12(/v1alpha1/{name=supportAccounts/*}/cases\x12\xb4\x01\n\x0cListComments\x12\x32.google.cloud.support.v1alpha1.ListCommentsRequest\x1a\x33.google.cloud.support.v1alpha1.ListCommentsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/v1alpha1/{name=supportAccounts/*/cases/*}/comments\x12\x9b\x01\n\nCreateCase\x12\x30.google.cloud.support.v1alpha1.CreateCaseRequest\x1a!.google.cloud.support.common.Case\"8\x82\xd3\xe4\x93\x02\x32\"*/v1alpha1/{parent=supportAccounts/*}/cases:\x04\x63\x61se\x12\xa0\x01\n\nUpdateCase\x12\x30.google.cloud.support.v1alpha1.UpdateCaseRequest\x1a!.google.cloud.support.common.Case\"=\x82\xd3\xe4\x93\x02\x37\x32//v1alpha1/{case.name=supportAccounts/*/cases/*}:\x04\x63\x61se\x12\xb0\x01\n\rCreateComment\x12\x33.google.cloud.support.v1alpha1.CreateCommentRequest\x1a$.google.cloud.support.common.Comment\"D\x82\xd3\xe4\x93\x02>\"3/v1alpha1/{name=supportAccounts/*/cases/*}/comments:\x07\x63omment\x12\x9a\x01\n\x10GetIssueTaxonomy\x12\x36.google.cloud.support.v1alpha1.GetIssueTaxonomyRequest\x1a*.google.cloud.support.common.IssueTaxonomy\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1alpha1:getIssueTaxonomyB|\n!com.google.cloud.support.v1alpha1B\x11\x43loudSupportProtoZDgoogle.golang.org/genproto/googleapis/cloud/support/v1alpha1;supportb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_support_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETSUPPORTACCOUNTREQUEST = _descriptor.Descriptor(
  name='GetSupportAccountRequest',
  full_name='google.cloud.support.v1alpha1.GetSupportAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.support.v1alpha1.GetSupportAccountRequest.name', index=0,
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
  serialized_start=212,
  serialized_end=252,
)


_LISTSUPPORTACCOUNTSREQUEST = _descriptor.Descriptor(
  name='ListSupportAccountsRequest',
  full_name='google.cloud.support.v1alpha1.ListSupportAccountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.support.v1alpha1.ListSupportAccountsRequest.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.support.v1alpha1.ListSupportAccountsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.support.v1alpha1.ListSupportAccountsRequest.page_token', index=2,
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
  serialized_start=254,
  serialized_end=337,
)


_LISTSUPPORTACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='ListSupportAccountsResponse',
  full_name='google.cloud.support.v1alpha1.ListSupportAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='google.cloud.support.v1alpha1.ListSupportAccountsResponse.accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.support.v1alpha1.ListSupportAccountsResponse.next_page_token', index=1,
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
  serialized_start=339,
  serialized_end=456,
)


_GETCASEREQUEST = _descriptor.Descriptor(
  name='GetCaseRequest',
  full_name='google.cloud.support.v1alpha1.GetCaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.support.v1alpha1.GetCaseRequest.name', index=0,
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
  serialized_start=458,
  serialized_end=488,
)


_LISTCASESREQUEST = _descriptor.Descriptor(
  name='ListCasesRequest',
  full_name='google.cloud.support.v1alpha1.ListCasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.support.v1alpha1.ListCasesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.support.v1alpha1.ListCasesRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.support.v1alpha1.ListCasesRequest.page_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.support.v1alpha1.ListCasesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=490,
  serialized_end=577,
)


_LISTCASESRESPONSE = _descriptor.Descriptor(
  name='ListCasesResponse',
  full_name='google.cloud.support.v1alpha1.ListCasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cases', full_name='google.cloud.support.v1alpha1.ListCasesResponse.cases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.support.v1alpha1.ListCasesResponse.next_page_token', index=1,
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
  serialized_start=579,
  serialized_end=673,
)


_LISTCOMMENTSREQUEST = _descriptor.Descriptor(
  name='ListCommentsRequest',
  full_name='google.cloud.support.v1alpha1.ListCommentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.support.v1alpha1.ListCommentsRequest.name', index=0,
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
  serialized_start=675,
  serialized_end=710,
)


_LISTCOMMENTSRESPONSE = _descriptor.Descriptor(
  name='ListCommentsResponse',
  full_name='google.cloud.support.v1alpha1.ListCommentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comments', full_name='google.cloud.support.v1alpha1.ListCommentsResponse.comments', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=712,
  serialized_end=790,
)


_CREATECASEREQUEST = _descriptor.Descriptor(
  name='CreateCaseRequest',
  full_name='google.cloud.support.v1alpha1.CreateCaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.support.v1alpha1.CreateCaseRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='case', full_name='google.cloud.support.v1alpha1.CreateCaseRequest.case', index=1,
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
  serialized_start=792,
  serialized_end=876,
)


_UPDATECASEREQUEST = _descriptor.Descriptor(
  name='UpdateCaseRequest',
  full_name='google.cloud.support.v1alpha1.UpdateCaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='case', full_name='google.cloud.support.v1alpha1.UpdateCaseRequest.case', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.support.v1alpha1.UpdateCaseRequest.update_mask', index=1,
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
  serialized_start=878,
  serialized_end=995,
)


_CREATECOMMENTREQUEST = _descriptor.Descriptor(
  name='CreateCommentRequest',
  full_name='google.cloud.support.v1alpha1.CreateCommentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.support.v1alpha1.CreateCommentRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='google.cloud.support.v1alpha1.CreateCommentRequest.comment', index=1,
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
  serialized_start=997,
  serialized_end=1088,
)


_GETISSUETAXONOMYREQUEST = _descriptor.Descriptor(
  name='GetIssueTaxonomyRequest',
  full_name='google.cloud.support.v1alpha1.GetIssueTaxonomyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1090,
  serialized_end=1115,
)

_LISTSUPPORTACCOUNTSRESPONSE.fields_by_name['accounts'].message_type = google_dot_cloud_dot_support_dot_common__pb2._SUPPORTACCOUNT
_LISTCASESRESPONSE.fields_by_name['cases'].message_type = google_dot_cloud_dot_support_dot_common__pb2._CASE
_LISTCOMMENTSRESPONSE.fields_by_name['comments'].message_type = google_dot_cloud_dot_support_dot_common__pb2._COMMENT
_CREATECASEREQUEST.fields_by_name['case'].message_type = google_dot_cloud_dot_support_dot_common__pb2._CASE
_UPDATECASEREQUEST.fields_by_name['case'].message_type = google_dot_cloud_dot_support_dot_common__pb2._CASE
_UPDATECASEREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CREATECOMMENTREQUEST.fields_by_name['comment'].message_type = google_dot_cloud_dot_support_dot_common__pb2._COMMENT
DESCRIPTOR.message_types_by_name['GetSupportAccountRequest'] = _GETSUPPORTACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['ListSupportAccountsRequest'] = _LISTSUPPORTACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['ListSupportAccountsResponse'] = _LISTSUPPORTACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['GetCaseRequest'] = _GETCASEREQUEST
DESCRIPTOR.message_types_by_name['ListCasesRequest'] = _LISTCASESREQUEST
DESCRIPTOR.message_types_by_name['ListCasesResponse'] = _LISTCASESRESPONSE
DESCRIPTOR.message_types_by_name['ListCommentsRequest'] = _LISTCOMMENTSREQUEST
DESCRIPTOR.message_types_by_name['ListCommentsResponse'] = _LISTCOMMENTSRESPONSE
DESCRIPTOR.message_types_by_name['CreateCaseRequest'] = _CREATECASEREQUEST
DESCRIPTOR.message_types_by_name['UpdateCaseRequest'] = _UPDATECASEREQUEST
DESCRIPTOR.message_types_by_name['CreateCommentRequest'] = _CREATECOMMENTREQUEST
DESCRIPTOR.message_types_by_name['GetIssueTaxonomyRequest'] = _GETISSUETAXONOMYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSupportAccountRequest = _reflection.GeneratedProtocolMessageType('GetSupportAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSUPPORTACCOUNTREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.GetSupportAccountRequest)
  })
_sym_db.RegisterMessage(GetSupportAccountRequest)

ListSupportAccountsRequest = _reflection.GeneratedProtocolMessageType('ListSupportAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSUPPORTACCOUNTSREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.ListSupportAccountsRequest)
  })
_sym_db.RegisterMessage(ListSupportAccountsRequest)

ListSupportAccountsResponse = _reflection.GeneratedProtocolMessageType('ListSupportAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSUPPORTACCOUNTSRESPONSE,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.ListSupportAccountsResponse)
  })
_sym_db.RegisterMessage(ListSupportAccountsResponse)

GetCaseRequest = _reflection.GeneratedProtocolMessageType('GetCaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCASEREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.GetCaseRequest)
  })
_sym_db.RegisterMessage(GetCaseRequest)

ListCasesRequest = _reflection.GeneratedProtocolMessageType('ListCasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCASESREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.ListCasesRequest)
  })
_sym_db.RegisterMessage(ListCasesRequest)

ListCasesResponse = _reflection.GeneratedProtocolMessageType('ListCasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCASESRESPONSE,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.ListCasesResponse)
  })
_sym_db.RegisterMessage(ListCasesResponse)

ListCommentsRequest = _reflection.GeneratedProtocolMessageType('ListCommentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOMMENTSREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.ListCommentsRequest)
  })
_sym_db.RegisterMessage(ListCommentsRequest)

ListCommentsResponse = _reflection.GeneratedProtocolMessageType('ListCommentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOMMENTSRESPONSE,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.ListCommentsResponse)
  })
_sym_db.RegisterMessage(ListCommentsResponse)

CreateCaseRequest = _reflection.GeneratedProtocolMessageType('CreateCaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECASEREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.CreateCaseRequest)
  })
_sym_db.RegisterMessage(CreateCaseRequest)

UpdateCaseRequest = _reflection.GeneratedProtocolMessageType('UpdateCaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECASEREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.UpdateCaseRequest)
  })
_sym_db.RegisterMessage(UpdateCaseRequest)

CreateCommentRequest = _reflection.GeneratedProtocolMessageType('CreateCommentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOMMENTREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.CreateCommentRequest)
  })
_sym_db.RegisterMessage(CreateCommentRequest)

GetIssueTaxonomyRequest = _reflection.GeneratedProtocolMessageType('GetIssueTaxonomyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETISSUETAXONOMYREQUEST,
  '__module__' : 'google.cloud.support.v1alpha1.cloud_support_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.support.v1alpha1.GetIssueTaxonomyRequest)
  })
_sym_db.RegisterMessage(GetIssueTaxonomyRequest)


DESCRIPTOR._options = None

_CLOUDSUPPORT = _descriptor.ServiceDescriptor(
  name='CloudSupport',
  full_name='google.cloud.support.v1alpha1.CloudSupport',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1118,
  serialized_end=2627,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSupportAccount',
    full_name='google.cloud.support.v1alpha1.CloudSupport.GetSupportAccount',
    index=0,
    containing_service=None,
    input_type=_GETSUPPORTACCOUNTREQUEST,
    output_type=google_dot_cloud_dot_support_dot_common__pb2._SUPPORTACCOUNT,
    serialized_options=b'\202\323\344\223\002$\022\"/v1alpha1/{name=supportAccounts/*}',
  ),
  _descriptor.MethodDescriptor(
    name='ListSupportAccounts',
    full_name='google.cloud.support.v1alpha1.CloudSupport.ListSupportAccounts',
    index=1,
    containing_service=None,
    input_type=_LISTSUPPORTACCOUNTSREQUEST,
    output_type=_LISTSUPPORTACCOUNTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/v1alpha1/supportAccounts',
  ),
  _descriptor.MethodDescriptor(
    name='GetCase',
    full_name='google.cloud.support.v1alpha1.CloudSupport.GetCase',
    index=2,
    containing_service=None,
    input_type=_GETCASEREQUEST,
    output_type=google_dot_cloud_dot_support_dot_common__pb2._CASE,
    serialized_options=b'\202\323\344\223\002,\022*/v1alpha1/{name=supportAccounts/*/cases/*}',
  ),
  _descriptor.MethodDescriptor(
    name='ListCases',
    full_name='google.cloud.support.v1alpha1.CloudSupport.ListCases',
    index=3,
    containing_service=None,
    input_type=_LISTCASESREQUEST,
    output_type=_LISTCASESRESPONSE,
    serialized_options=b'\202\323\344\223\002*\022(/v1alpha1/{name=supportAccounts/*}/cases',
  ),
  _descriptor.MethodDescriptor(
    name='ListComments',
    full_name='google.cloud.support.v1alpha1.CloudSupport.ListComments',
    index=4,
    containing_service=None,
    input_type=_LISTCOMMENTSREQUEST,
    output_type=_LISTCOMMENTSRESPONSE,
    serialized_options=b'\202\323\344\223\0025\0223/v1alpha1/{name=supportAccounts/*/cases/*}/comments',
  ),
  _descriptor.MethodDescriptor(
    name='CreateCase',
    full_name='google.cloud.support.v1alpha1.CloudSupport.CreateCase',
    index=5,
    containing_service=None,
    input_type=_CREATECASEREQUEST,
    output_type=google_dot_cloud_dot_support_dot_common__pb2._CASE,
    serialized_options=b'\202\323\344\223\0022\"*/v1alpha1/{parent=supportAccounts/*}/cases:\004case',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateCase',
    full_name='google.cloud.support.v1alpha1.CloudSupport.UpdateCase',
    index=6,
    containing_service=None,
    input_type=_UPDATECASEREQUEST,
    output_type=google_dot_cloud_dot_support_dot_common__pb2._CASE,
    serialized_options=b'\202\323\344\223\00272//v1alpha1/{case.name=supportAccounts/*/cases/*}:\004case',
  ),
  _descriptor.MethodDescriptor(
    name='CreateComment',
    full_name='google.cloud.support.v1alpha1.CloudSupport.CreateComment',
    index=7,
    containing_service=None,
    input_type=_CREATECOMMENTREQUEST,
    output_type=google_dot_cloud_dot_support_dot_common__pb2._COMMENT,
    serialized_options=b'\202\323\344\223\002>\"3/v1alpha1/{name=supportAccounts/*/cases/*}/comments:\007comment',
  ),
  _descriptor.MethodDescriptor(
    name='GetIssueTaxonomy',
    full_name='google.cloud.support.v1alpha1.CloudSupport.GetIssueTaxonomy',
    index=8,
    containing_service=None,
    input_type=_GETISSUETAXONOMYREQUEST,
    output_type=google_dot_cloud_dot_support_dot_common__pb2._ISSUETAXONOMY,
    serialized_options=b'\202\323\344\223\002\034\022\032/v1alpha1:getIssueTaxonomy',
  ),
])
_sym_db.RegisterServiceDescriptor(_CLOUDSUPPORT)

DESCRIPTOR.services_by_name['CloudSupport'] = _CLOUDSUPPORT

# @@protoc_insertion_point(module_scope)
