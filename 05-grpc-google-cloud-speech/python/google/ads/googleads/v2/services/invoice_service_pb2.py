# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/invoice_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v2.enums import month_of_year_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_month__of__year__pb2
from google.ads.googleads.v2.resources import invoice_pb2 as google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_invoice__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/invoice_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB\023InvoiceServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\n6google/ads/googleads/v2/services/invoice_service.proto\x12 google.ads.googleads.v2.services\x1a\x31google/ads/googleads/v2/enums/month_of_year.proto\x1a/google/ads/googleads/v2/resources/invoice.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\"\xa6\x01\n\x13ListInvoicesRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x15\n\rbilling_setup\x18\x02 \x01(\t\x12\x12\n\nissue_year\x18\x03 \x01(\t\x12O\n\x0bissue_month\x18\x04 \x01(\x0e\x32:.google.ads.googleads.v2.enums.MonthOfYearEnum.MonthOfYear\"T\n\x14ListInvoicesResponse\x12<\n\x08invoices\x18\x01 \x03(\x0b\x32*.google.ads.googleads.v2.resources.Invoice2\xdd\x01\n\x0eInvoiceService\x12\xad\x01\n\x0cListInvoices\x12\x35.google.ads.googleads.v2.services.ListInvoicesRequest\x1a\x36.google.ads.googleads.v2.services.ListInvoicesResponse\".\x82\xd3\xe4\x93\x02(\x12&/v2/customers/{customer_id=*}/invoices\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xfa\x01\n$com.google.ads.googleads.v2.servicesB\x13InvoiceServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_month__of__year__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_invoice__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_LISTINVOICESREQUEST = _descriptor.Descriptor(
  name='ListInvoicesRequest',
  full_name='google.ads.googleads.v2.services.ListInvoicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.ListInvoicesRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='billing_setup', full_name='google.ads.googleads.v2.services.ListInvoicesRequest.billing_setup', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue_year', full_name='google.ads.googleads.v2.services.ListInvoicesRequest.issue_year', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue_month', full_name='google.ads.googleads.v2.services.ListInvoicesRequest.issue_month', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=248,
  serialized_end=414,
)


_LISTINVOICESRESPONSE = _descriptor.Descriptor(
  name='ListInvoicesResponse',
  full_name='google.ads.googleads.v2.services.ListInvoicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invoices', full_name='google.ads.googleads.v2.services.ListInvoicesResponse.invoices', index=0,
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
  serialized_start=416,
  serialized_end=500,
)

_LISTINVOICESREQUEST.fields_by_name['issue_month'].enum_type = google_dot_ads_dot_googleads_dot_v2_dot_enums_dot_month__of__year__pb2._MONTHOFYEARENUM_MONTHOFYEAR
_LISTINVOICESRESPONSE.fields_by_name['invoices'].message_type = google_dot_ads_dot_googleads_dot_v2_dot_resources_dot_invoice__pb2._INVOICE
DESCRIPTOR.message_types_by_name['ListInvoicesRequest'] = _LISTINVOICESREQUEST
DESCRIPTOR.message_types_by_name['ListInvoicesResponse'] = _LISTINVOICESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListInvoicesRequest = _reflection.GeneratedProtocolMessageType('ListInvoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.invoice_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ListInvoicesRequest)
  })
_sym_db.RegisterMessage(ListInvoicesRequest)

ListInvoicesResponse = _reflection.GeneratedProtocolMessageType('ListInvoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.invoice_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ListInvoicesResponse)
  })
_sym_db.RegisterMessage(ListInvoicesResponse)


DESCRIPTOR._options = None

_INVOICESERVICE = _descriptor.ServiceDescriptor(
  name='InvoiceService',
  full_name='google.ads.googleads.v2.services.InvoiceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=503,
  serialized_end=724,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListInvoices',
    full_name='google.ads.googleads.v2.services.InvoiceService.ListInvoices',
    index=0,
    containing_service=None,
    input_type=_LISTINVOICESREQUEST,
    output_type=_LISTINVOICESRESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/v2/customers/{customer_id=*}/invoices',
  ),
])
_sym_db.RegisterServiceDescriptor(_INVOICESERVICE)

DESCRIPTOR.services_by_name['InvoiceService'] = _INVOICESERVICE

# @@protoc_insertion_point(module_scope)
