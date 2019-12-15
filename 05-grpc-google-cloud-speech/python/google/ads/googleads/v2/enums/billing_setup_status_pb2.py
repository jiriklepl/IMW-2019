# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/billing_setup_status.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/billing_setup_status.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB\027BillingSetupStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\n8google/ads/googleads/v2/enums/billing_setup_status.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x89\x01\n\x16\x42illingSetupStatusEnum\"o\n\x12\x42illingSetupStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x11\n\rAPPROVED_HELD\x10\x03\x12\x0c\n\x08\x41PPROVED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x42\xec\x01\n!com.google.ads.googleads.v2.enumsB\x17\x42illingSetupStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BILLINGSETUPSTATUSENUM_BILLINGSETUPSTATUS = _descriptor.EnumDescriptor(
  name='BillingSetupStatus',
  full_name='google.ads.googleads.v2.enums.BillingSetupStatusEnum.BillingSetupStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED_HELD', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=148,
  serialized_end=259,
)
_sym_db.RegisterEnumDescriptor(_BILLINGSETUPSTATUSENUM_BILLINGSETUPSTATUS)


_BILLINGSETUPSTATUSENUM = _descriptor.Descriptor(
  name='BillingSetupStatusEnum',
  full_name='google.ads.googleads.v2.enums.BillingSetupStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BILLINGSETUPSTATUSENUM_BILLINGSETUPSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=259,
)

_BILLINGSETUPSTATUSENUM_BILLINGSETUPSTATUS.containing_type = _BILLINGSETUPSTATUSENUM
DESCRIPTOR.message_types_by_name['BillingSetupStatusEnum'] = _BILLINGSETUPSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingSetupStatusEnum = _reflection.GeneratedProtocolMessageType('BillingSetupStatusEnum', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGSETUPSTATUSENUM,
  '__module__' : 'google.ads.googleads.v2.enums.billing_setup_status_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.BillingSetupStatusEnum)
  })
_sym_db.RegisterMessage(BillingSetupStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
