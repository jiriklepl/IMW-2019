# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/enums/account_budget_proposal_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/enums/account_budget_proposal_type.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v2.enumsB\036AccountBudgetProposalTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums',
  serialized_pb=b'\n@google/ads/googleads/v2/enums/account_budget_proposal_type.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x87\x01\n\x1d\x41\x63\x63ountBudgetProposalTypeEnum\"f\n\x19\x41\x63\x63ountBudgetProposalType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\n\n\x06UPDATE\x10\x03\x12\x07\n\x03\x45ND\x10\x04\x12\n\n\x06REMOVE\x10\x05\x42\xf3\x01\n!com.google.ads.googleads.v2.enumsB\x1e\x41\x63\x63ountBudgetProposalTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ACCOUNTBUDGETPROPOSALTYPEENUM_ACCOUNTBUDGETPROPOSALTYPE = _descriptor.EnumDescriptor(
  name='AccountBudgetProposalType',
  full_name='google.ads.googleads.v2.enums.AccountBudgetProposalTypeEnum.AccountBudgetProposalType',
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
      name='CREATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=163,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTBUDGETPROPOSALTYPEENUM_ACCOUNTBUDGETPROPOSALTYPE)


_ACCOUNTBUDGETPROPOSALTYPEENUM = _descriptor.Descriptor(
  name='AccountBudgetProposalTypeEnum',
  full_name='google.ads.googleads.v2.enums.AccountBudgetProposalTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCOUNTBUDGETPROPOSALTYPEENUM_ACCOUNTBUDGETPROPOSALTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=265,
)

_ACCOUNTBUDGETPROPOSALTYPEENUM_ACCOUNTBUDGETPROPOSALTYPE.containing_type = _ACCOUNTBUDGETPROPOSALTYPEENUM
DESCRIPTOR.message_types_by_name['AccountBudgetProposalTypeEnum'] = _ACCOUNTBUDGETPROPOSALTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountBudgetProposalTypeEnum = _reflection.GeneratedProtocolMessageType('AccountBudgetProposalTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTBUDGETPROPOSALTYPEENUM,
  '__module__' : 'google.ads.googleads.v2.enums.account_budget_proposal_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.AccountBudgetProposalTypeEnum)
  })
_sym_db.RegisterMessage(AccountBudgetProposalTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
