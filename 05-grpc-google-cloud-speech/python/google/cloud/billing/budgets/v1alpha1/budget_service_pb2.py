# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/billing/budgets/v1alpha1/budget_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.billing.budgets.v1alpha1 import budget_model_pb2 as google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/billing/budgets/v1alpha1/budget_service.proto',
  package='google.cloud.billing.budgets.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n)com.google.cloud.billing.budgets.v1alpha1P\001ZLgoogle.golang.org/genproto/googleapis/cloud/billing/budgets/v1alpha1;budgets',
  serialized_pb=b'\n:google/cloud/billing/budgets/v1alpha1/budget_service.proto\x12%google.cloud.billing.budgets.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x38google/cloud/billing/budgets/v1alpha1/budget_model.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\x97\x01\n\x13\x43reateBudgetRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\x12$billingbudgets.googleapis.com/Budget\x12\x42\n\x06\x62udget\x18\x02 \x01(\x0b\x32-.google.cloud.billing.budgets.v1alpha1.BudgetB\x03\xe0\x41\x02\"\x8f\x01\n\x13UpdateBudgetRequest\x12\x42\n\x06\x62udget\x18\x01 \x01(\x0b\x32-.google.cloud.billing.budgets.v1alpha1.BudgetB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01\"N\n\x10GetBudgetRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\n$billingbudgets.googleapis.com/Budget\"\x83\x01\n\x12ListBudgetsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\x12$billingbudgets.googleapis.com/Budget\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\"n\n\x13ListBudgetsResponse\x12>\n\x07\x62udgets\x18\x01 \x03(\x0b\x32-.google.cloud.billing.budgets.v1alpha1.Budget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"Q\n\x13\x44\x65leteBudgetRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\n$billingbudgets.googleapis.com/Budget2\xd7\x07\n\rBudgetService\x12\xb2\x01\n\x0c\x43reateBudget\x12:.google.cloud.billing.budgets.v1alpha1.CreateBudgetRequest\x1a-.google.cloud.billing.budgets.v1alpha1.Budget\"7\x82\xd3\xe4\x93\x02\x31\",/v1alpha1/{parent=billingAccounts/*}/budgets:\x01*\x12\xb9\x01\n\x0cUpdateBudget\x12:.google.cloud.billing.budgets.v1alpha1.UpdateBudgetRequest\x1a-.google.cloud.billing.budgets.v1alpha1.Budget\">\x82\xd3\xe4\x93\x02\x38\x32\x33/v1alpha1/{budget.name=billingAccounts/*/budgets/*}:\x01*\x12\xa9\x01\n\tGetBudget\x12\x37.google.cloud.billing.budgets.v1alpha1.GetBudgetRequest\x1a-.google.cloud.billing.budgets.v1alpha1.Budget\"4\x82\xd3\xe4\x93\x02.\x12,/v1alpha1/{name=billingAccounts/*/budgets/*}\x12\xba\x01\n\x0bListBudgets\x12\x39.google.cloud.billing.budgets.v1alpha1.ListBudgetsRequest\x1a:.google.cloud.billing.budgets.v1alpha1.ListBudgetsResponse\"4\x82\xd3\xe4\x93\x02.\x12,/v1alpha1/{parent=billingAccounts/*}/budgets\x12\x98\x01\n\x0c\x44\x65leteBudget\x12:.google.cloud.billing.budgets.v1alpha1.DeleteBudgetRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.*,/v1alpha1/{name=billingAccounts/*/budgets/*}\x1aQ\xca\x41\x1d\x62illingbudgets.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB{\n)com.google.cloud.billing.budgets.v1alpha1P\x01ZLgoogle.golang.org/genproto/googleapis/cloud/billing/budgets/v1alpha1;budgetsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_CREATEBUDGETREQUEST = _descriptor.Descriptor(
  name='CreateBudgetRequest',
  full_name='google.cloud.billing.budgets.v1alpha1.CreateBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.billing.budgets.v1alpha1.CreateBudgetRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A&\022$billingbudgets.googleapis.com/Budget', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='budget', full_name='google.cloud.billing.budgets.v1alpha1.CreateBudgetRequest.budget', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
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
  serialized_start=338,
  serialized_end=489,
)


_UPDATEBUDGETREQUEST = _descriptor.Descriptor(
  name='UpdateBudgetRequest',
  full_name='google.cloud.billing.budgets.v1alpha1.UpdateBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='budget', full_name='google.cloud.billing.budgets.v1alpha1.UpdateBudgetRequest.budget', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.billing.budgets.v1alpha1.UpdateBudgetRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
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
  serialized_start=492,
  serialized_end=635,
)


_GETBUDGETREQUEST = _descriptor.Descriptor(
  name='GetBudgetRequest',
  full_name='google.cloud.billing.budgets.v1alpha1.GetBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.budgets.v1alpha1.GetBudgetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A&\n$billingbudgets.googleapis.com/Budget', file=DESCRIPTOR),
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
  serialized_start=637,
  serialized_end=715,
)


_LISTBUDGETSREQUEST = _descriptor.Descriptor(
  name='ListBudgetsRequest',
  full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A&\022$billingbudgets.googleapis.com/Budget', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
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
  serialized_start=718,
  serialized_end=849,
)


_LISTBUDGETSRESPONSE = _descriptor.Descriptor(
  name='ListBudgetsResponse',
  full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='budgets', full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsResponse.budgets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.billing.budgets.v1alpha1.ListBudgetsResponse.next_page_token', index=1,
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
  serialized_start=851,
  serialized_end=961,
)


_DELETEBUDGETREQUEST = _descriptor.Descriptor(
  name='DeleteBudgetRequest',
  full_name='google.cloud.billing.budgets.v1alpha1.DeleteBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.billing.budgets.v1alpha1.DeleteBudgetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A&\n$billingbudgets.googleapis.com/Budget', file=DESCRIPTOR),
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
  serialized_start=963,
  serialized_end=1044,
)

_CREATEBUDGETREQUEST.fields_by_name['budget'].message_type = google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2._BUDGET
_UPDATEBUDGETREQUEST.fields_by_name['budget'].message_type = google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2._BUDGET
_UPDATEBUDGETREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTBUDGETSRESPONSE.fields_by_name['budgets'].message_type = google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2._BUDGET
DESCRIPTOR.message_types_by_name['CreateBudgetRequest'] = _CREATEBUDGETREQUEST
DESCRIPTOR.message_types_by_name['UpdateBudgetRequest'] = _UPDATEBUDGETREQUEST
DESCRIPTOR.message_types_by_name['GetBudgetRequest'] = _GETBUDGETREQUEST
DESCRIPTOR.message_types_by_name['ListBudgetsRequest'] = _LISTBUDGETSREQUEST
DESCRIPTOR.message_types_by_name['ListBudgetsResponse'] = _LISTBUDGETSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteBudgetRequest'] = _DELETEBUDGETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBudgetRequest = _reflection.GeneratedProtocolMessageType('CreateBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1alpha1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1alpha1.CreateBudgetRequest)
  })
_sym_db.RegisterMessage(CreateBudgetRequest)

UpdateBudgetRequest = _reflection.GeneratedProtocolMessageType('UpdateBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1alpha1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1alpha1.UpdateBudgetRequest)
  })
_sym_db.RegisterMessage(UpdateBudgetRequest)

GetBudgetRequest = _reflection.GeneratedProtocolMessageType('GetBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1alpha1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1alpha1.GetBudgetRequest)
  })
_sym_db.RegisterMessage(GetBudgetRequest)

ListBudgetsRequest = _reflection.GeneratedProtocolMessageType('ListBudgetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUDGETSREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1alpha1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1alpha1.ListBudgetsRequest)
  })
_sym_db.RegisterMessage(ListBudgetsRequest)

ListBudgetsResponse = _reflection.GeneratedProtocolMessageType('ListBudgetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUDGETSRESPONSE,
  '__module__' : 'google.cloud.billing.budgets.v1alpha1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1alpha1.ListBudgetsResponse)
  })
_sym_db.RegisterMessage(ListBudgetsResponse)

DeleteBudgetRequest = _reflection.GeneratedProtocolMessageType('DeleteBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1alpha1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1alpha1.DeleteBudgetRequest)
  })
_sym_db.RegisterMessage(DeleteBudgetRequest)


DESCRIPTOR._options = None
_CREATEBUDGETREQUEST.fields_by_name['parent']._options = None
_CREATEBUDGETREQUEST.fields_by_name['budget']._options = None
_UPDATEBUDGETREQUEST.fields_by_name['budget']._options = None
_UPDATEBUDGETREQUEST.fields_by_name['update_mask']._options = None
_GETBUDGETREQUEST.fields_by_name['name']._options = None
_LISTBUDGETSREQUEST.fields_by_name['parent']._options = None
_LISTBUDGETSREQUEST.fields_by_name['page_size']._options = None
_LISTBUDGETSREQUEST.fields_by_name['page_token']._options = None
_DELETEBUDGETREQUEST.fields_by_name['name']._options = None

_BUDGETSERVICE = _descriptor.ServiceDescriptor(
  name='BudgetService',
  full_name='google.cloud.billing.budgets.v1alpha1.BudgetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\035billingbudgets.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  serialized_start=1047,
  serialized_end=2030,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBudget',
    full_name='google.cloud.billing.budgets.v1alpha1.BudgetService.CreateBudget',
    index=0,
    containing_service=None,
    input_type=_CREATEBUDGETREQUEST,
    output_type=google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2._BUDGET,
    serialized_options=b'\202\323\344\223\0021\",/v1alpha1/{parent=billingAccounts/*}/budgets:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBudget',
    full_name='google.cloud.billing.budgets.v1alpha1.BudgetService.UpdateBudget',
    index=1,
    containing_service=None,
    input_type=_UPDATEBUDGETREQUEST,
    output_type=google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2._BUDGET,
    serialized_options=b'\202\323\344\223\002823/v1alpha1/{budget.name=billingAccounts/*/budgets/*}:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GetBudget',
    full_name='google.cloud.billing.budgets.v1alpha1.BudgetService.GetBudget',
    index=2,
    containing_service=None,
    input_type=_GETBUDGETREQUEST,
    output_type=google_dot_cloud_dot_billing_dot_budgets_dot_v1alpha1_dot_budget__model__pb2._BUDGET,
    serialized_options=b'\202\323\344\223\002.\022,/v1alpha1/{name=billingAccounts/*/budgets/*}',
  ),
  _descriptor.MethodDescriptor(
    name='ListBudgets',
    full_name='google.cloud.billing.budgets.v1alpha1.BudgetService.ListBudgets',
    index=3,
    containing_service=None,
    input_type=_LISTBUDGETSREQUEST,
    output_type=_LISTBUDGETSRESPONSE,
    serialized_options=b'\202\323\344\223\002.\022,/v1alpha1/{parent=billingAccounts/*}/budgets',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBudget',
    full_name='google.cloud.billing.budgets.v1alpha1.BudgetService.DeleteBudget',
    index=4,
    containing_service=None,
    input_type=_DELETEBUDGETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002.*,/v1alpha1/{name=billingAccounts/*/budgets/*}',
  ),
])
_sym_db.RegisterServiceDescriptor(_BUDGETSERVICE)

DESCRIPTOR.services_by_name['BudgetService'] = _BUDGETSERVICE

# @@protoc_insertion_point(module_scope)
