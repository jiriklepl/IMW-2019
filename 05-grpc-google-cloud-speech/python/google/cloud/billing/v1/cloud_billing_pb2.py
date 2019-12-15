# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/billing/v1/cloud_billing.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/billing/v1/cloud_billing.proto',
  package='google.cloud.billing.v1',
  syntax='proto3',
  serialized_options=b'\n\033com.google.cloud.billing.v1B\021CloudBillingProtoP\001Z>google.golang.org/genproto/googleapis/cloud/billing/v1;billing',
  serialized_pb=b'\n+google/cloud/billing/v1/cloud_billing.proto\x12\x17google.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\"B\n\x0e\x42illingAccount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x08\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\"m\n\x12ProjectBillingInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x1c\n\x14\x62illing_account_name\x18\x03 \x01(\t\x12\x17\n\x0f\x62illing_enabled\x18\x04 \x01(\x08\"(\n\x18GetBillingAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"C\n\x1aListBillingAccountsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"y\n\x1bListBillingAccountsResponse\x12\x41\n\x10\x62illing_accounts\x18\x01 \x03(\x0b\x32\'.google.cloud.billing.v1.BillingAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"T\n\x1dListProjectBillingInfoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x84\x01\n\x1eListProjectBillingInfoResponse\x12I\n\x14project_billing_info\x18\x01 \x03(\x0b\x32+.google.cloud.billing.v1.ProjectBillingInfo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\",\n\x1cGetProjectBillingInfoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"z\n\x1fUpdateProjectBillingInfoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x14project_billing_info\x18\x02 \x01(\x0b\x32+.google.cloud.billing.v1.ProjectBillingInfo2\xef\x06\n\x0c\x43loudBilling\x12\x95\x01\n\x11GetBillingAccount\x12\x31.google.cloud.billing.v1.GetBillingAccountRequest\x1a\'.google.cloud.billing.v1.BillingAccount\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=billingAccounts/*}\x12\x9d\x01\n\x13ListBillingAccounts\x12\x33.google.cloud.billing.v1.ListBillingAccountsRequest\x1a\x34.google.cloud.billing.v1.ListBillingAccountsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/billingAccounts\x12\xb8\x01\n\x16ListProjectBillingInfo\x12\x36.google.cloud.billing.v1.ListProjectBillingInfoRequest\x1a\x37.google.cloud.billing.v1.ListProjectBillingInfoResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1/{name=billingAccounts/*}/projects\x12\xa6\x01\n\x15GetProjectBillingInfo\x12\x35.google.cloud.billing.v1.GetProjectBillingInfoRequest\x1a+.google.cloud.billing.v1.ProjectBillingInfo\")\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*}/billingInfo\x12\xc2\x01\n\x18UpdateProjectBillingInfo\x12\x38.google.cloud.billing.v1.UpdateProjectBillingInfoRequest\x1a+.google.cloud.billing.v1.ProjectBillingInfo\"?\x82\xd3\xe4\x93\x02\x39\x1a!/v1/{name=projects/*}/billingInfo:\x14project_billing_infoBr\n\x1b\x63om.google.cloud.billing.v1B\x11\x43loudBillingProtoP\x01Z>google.golang.org/genproto/googleapis/cloud/billing/v1;billingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_BILLINGACCOUNT = _descriptor.Descriptor(
  name='BillingAccount',
  full_name='google.cloud.billing.v1.BillingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.v1.BillingAccount.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='google.cloud.billing.v1.BillingAccount.open', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.billing.v1.BillingAccount.display_name', index=2,
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
  serialized_start=102,
  serialized_end=168,
)


_PROJECTBILLINGINFO = _descriptor.Descriptor(
  name='ProjectBillingInfo',
  full_name='google.cloud.billing.v1.ProjectBillingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.v1.ProjectBillingInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.cloud.billing.v1.ProjectBillingInfo.project_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='billing_account_name', full_name='google.cloud.billing.v1.ProjectBillingInfo.billing_account_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='billing_enabled', full_name='google.cloud.billing.v1.ProjectBillingInfo.billing_enabled', index=3,
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
  serialized_start=170,
  serialized_end=279,
)


_GETBILLINGACCOUNTREQUEST = _descriptor.Descriptor(
  name='GetBillingAccountRequest',
  full_name='google.cloud.billing.v1.GetBillingAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.v1.GetBillingAccountRequest.name', index=0,
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
  serialized_start=281,
  serialized_end=321,
)


_LISTBILLINGACCOUNTSREQUEST = _descriptor.Descriptor(
  name='ListBillingAccountsRequest',
  full_name='google.cloud.billing.v1.ListBillingAccountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.billing.v1.ListBillingAccountsRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.billing.v1.ListBillingAccountsRequest.page_token', index=1,
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
  serialized_start=323,
  serialized_end=390,
)


_LISTBILLINGACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='ListBillingAccountsResponse',
  full_name='google.cloud.billing.v1.ListBillingAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='billing_accounts', full_name='google.cloud.billing.v1.ListBillingAccountsResponse.billing_accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.billing.v1.ListBillingAccountsResponse.next_page_token', index=1,
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
  serialized_start=392,
  serialized_end=513,
)


_LISTPROJECTBILLINGINFOREQUEST = _descriptor.Descriptor(
  name='ListProjectBillingInfoRequest',
  full_name='google.cloud.billing.v1.ListProjectBillingInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.v1.ListProjectBillingInfoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.billing.v1.ListProjectBillingInfoRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.billing.v1.ListProjectBillingInfoRequest.page_token', index=2,
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
  serialized_start=515,
  serialized_end=599,
)


_LISTPROJECTBILLINGINFORESPONSE = _descriptor.Descriptor(
  name='ListProjectBillingInfoResponse',
  full_name='google.cloud.billing.v1.ListProjectBillingInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_billing_info', full_name='google.cloud.billing.v1.ListProjectBillingInfoResponse.project_billing_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.billing.v1.ListProjectBillingInfoResponse.next_page_token', index=1,
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
  serialized_start=602,
  serialized_end=734,
)


_GETPROJECTBILLINGINFOREQUEST = _descriptor.Descriptor(
  name='GetProjectBillingInfoRequest',
  full_name='google.cloud.billing.v1.GetProjectBillingInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.v1.GetProjectBillingInfoRequest.name', index=0,
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
  serialized_start=736,
  serialized_end=780,
)


_UPDATEPROJECTBILLINGINFOREQUEST = _descriptor.Descriptor(
  name='UpdateProjectBillingInfoRequest',
  full_name='google.cloud.billing.v1.UpdateProjectBillingInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.v1.UpdateProjectBillingInfoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_billing_info', full_name='google.cloud.billing.v1.UpdateProjectBillingInfoRequest.project_billing_info', index=1,
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
  serialized_start=782,
  serialized_end=904,
)

_LISTBILLINGACCOUNTSRESPONSE.fields_by_name['billing_accounts'].message_type = _BILLINGACCOUNT
_LISTPROJECTBILLINGINFORESPONSE.fields_by_name['project_billing_info'].message_type = _PROJECTBILLINGINFO
_UPDATEPROJECTBILLINGINFOREQUEST.fields_by_name['project_billing_info'].message_type = _PROJECTBILLINGINFO
DESCRIPTOR.message_types_by_name['BillingAccount'] = _BILLINGACCOUNT
DESCRIPTOR.message_types_by_name['ProjectBillingInfo'] = _PROJECTBILLINGINFO
DESCRIPTOR.message_types_by_name['GetBillingAccountRequest'] = _GETBILLINGACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['ListBillingAccountsRequest'] = _LISTBILLINGACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['ListBillingAccountsResponse'] = _LISTBILLINGACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['ListProjectBillingInfoRequest'] = _LISTPROJECTBILLINGINFOREQUEST
DESCRIPTOR.message_types_by_name['ListProjectBillingInfoResponse'] = _LISTPROJECTBILLINGINFORESPONSE
DESCRIPTOR.message_types_by_name['GetProjectBillingInfoRequest'] = _GETPROJECTBILLINGINFOREQUEST
DESCRIPTOR.message_types_by_name['UpdateProjectBillingInfoRequest'] = _UPDATEPROJECTBILLINGINFOREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingAccount = _reflection.GeneratedProtocolMessageType('BillingAccount', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGACCOUNT,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.BillingAccount)
  })
_sym_db.RegisterMessage(BillingAccount)

ProjectBillingInfo = _reflection.GeneratedProtocolMessageType('ProjectBillingInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTBILLINGINFO,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.ProjectBillingInfo)
  })
_sym_db.RegisterMessage(ProjectBillingInfo)

GetBillingAccountRequest = _reflection.GeneratedProtocolMessageType('GetBillingAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGACCOUNTREQUEST,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.GetBillingAccountRequest)
  })
_sym_db.RegisterMessage(GetBillingAccountRequest)

ListBillingAccountsRequest = _reflection.GeneratedProtocolMessageType('ListBillingAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLINGACCOUNTSREQUEST,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.ListBillingAccountsRequest)
  })
_sym_db.RegisterMessage(ListBillingAccountsRequest)

ListBillingAccountsResponse = _reflection.GeneratedProtocolMessageType('ListBillingAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLINGACCOUNTSRESPONSE,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.ListBillingAccountsResponse)
  })
_sym_db.RegisterMessage(ListBillingAccountsResponse)

ListProjectBillingInfoRequest = _reflection.GeneratedProtocolMessageType('ListProjectBillingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTBILLINGINFOREQUEST,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.ListProjectBillingInfoRequest)
  })
_sym_db.RegisterMessage(ListProjectBillingInfoRequest)

ListProjectBillingInfoResponse = _reflection.GeneratedProtocolMessageType('ListProjectBillingInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTBILLINGINFORESPONSE,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.ListProjectBillingInfoResponse)
  })
_sym_db.RegisterMessage(ListProjectBillingInfoResponse)

GetProjectBillingInfoRequest = _reflection.GeneratedProtocolMessageType('GetProjectBillingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTBILLINGINFOREQUEST,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.GetProjectBillingInfoRequest)
  })
_sym_db.RegisterMessage(GetProjectBillingInfoRequest)

UpdateProjectBillingInfoRequest = _reflection.GeneratedProtocolMessageType('UpdateProjectBillingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTBILLINGINFOREQUEST,
  '__module__' : 'google.cloud.billing.v1.cloud_billing_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.v1.UpdateProjectBillingInfoRequest)
  })
_sym_db.RegisterMessage(UpdateProjectBillingInfoRequest)


DESCRIPTOR._options = None

_CLOUDBILLING = _descriptor.ServiceDescriptor(
  name='CloudBilling',
  full_name='google.cloud.billing.v1.CloudBilling',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=907,
  serialized_end=1786,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBillingAccount',
    full_name='google.cloud.billing.v1.CloudBilling.GetBillingAccount',
    index=0,
    containing_service=None,
    input_type=_GETBILLINGACCOUNTREQUEST,
    output_type=_BILLINGACCOUNT,
    serialized_options=b'\202\323\344\223\002\036\022\034/v1/{name=billingAccounts/*}',
  ),
  _descriptor.MethodDescriptor(
    name='ListBillingAccounts',
    full_name='google.cloud.billing.v1.CloudBilling.ListBillingAccounts',
    index=1,
    containing_service=None,
    input_type=_LISTBILLINGACCOUNTSREQUEST,
    output_type=_LISTBILLINGACCOUNTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\025\022\023/v1/billingAccounts',
  ),
  _descriptor.MethodDescriptor(
    name='ListProjectBillingInfo',
    full_name='google.cloud.billing.v1.CloudBilling.ListProjectBillingInfo',
    index=2,
    containing_service=None,
    input_type=_LISTPROJECTBILLINGINFOREQUEST,
    output_type=_LISTPROJECTBILLINGINFORESPONSE,
    serialized_options=b'\202\323\344\223\002\'\022%/v1/{name=billingAccounts/*}/projects',
  ),
  _descriptor.MethodDescriptor(
    name='GetProjectBillingInfo',
    full_name='google.cloud.billing.v1.CloudBilling.GetProjectBillingInfo',
    index=3,
    containing_service=None,
    input_type=_GETPROJECTBILLINGINFOREQUEST,
    output_type=_PROJECTBILLINGINFO,
    serialized_options=b'\202\323\344\223\002#\022!/v1/{name=projects/*}/billingInfo',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProjectBillingInfo',
    full_name='google.cloud.billing.v1.CloudBilling.UpdateProjectBillingInfo',
    index=4,
    containing_service=None,
    input_type=_UPDATEPROJECTBILLINGINFOREQUEST,
    output_type=_PROJECTBILLINGINFO,
    serialized_options=b'\202\323\344\223\0029\032!/v1/{name=projects/*}/billingInfo:\024project_billing_info',
  ),
])
_sym_db.RegisterServiceDescriptor(_CLOUDBILLING)

DESCRIPTOR.services_by_name['CloudBilling'] = _CLOUDBILLING

# @@protoc_insertion_point(module_scope)
