# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/enums/policy_topic_evidence_destination_mismatch_url_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/enums/policy_topic_evidence_destination_mismatch_url_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v1.enumsB2PolicyTopicEvidenceDestinationMismatchUrlTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums',
  serialized_pb=b'\nWgoogle/ads/googleads/v1/enums/policy_topic_evidence_destination_mismatch_url_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xe4\x01\n1PolicyTopicEvidenceDestinationMismatchUrlTypeEnum\"\xae\x01\n-PolicyTopicEvidenceDestinationMismatchUrlType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0b\x44ISPLAY_URL\x10\x02\x12\r\n\tFINAL_URL\x10\x03\x12\x14\n\x10\x46INAL_MOBILE_URL\x10\x04\x12\x10\n\x0cTRACKING_URL\x10\x05\x12\x17\n\x13MOBILE_TRACKING_URL\x10\x06\x42\x87\x02\n!com.google.ads.googleads.v1.enumsB2PolicyTopicEvidenceDestinationMismatchUrlTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPE = _descriptor.EnumDescriptor(
  name='PolicyTopicEvidenceDestinationMismatchUrlType',
  full_name='google.ads.googleads.v1.enums.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType',
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
      name='DISPLAY_URL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILE_TRACKING_URL', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=207,
  serialized_end=381,
)
_sym_db.RegisterEnumDescriptor(_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPE)


_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM = _descriptor.Descriptor(
  name='PolicyTopicEvidenceDestinationMismatchUrlTypeEnum',
  full_name='google.ads.googleads.v1.enums.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=381,
)

_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPE.containing_type = _POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM
DESCRIPTOR.message_types_by_name['PolicyTopicEvidenceDestinationMismatchUrlTypeEnum'] = _POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyTopicEvidenceDestinationMismatchUrlTypeEnum = _reflection.GeneratedProtocolMessageType('PolicyTopicEvidenceDestinationMismatchUrlTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM,
  '__module__' : 'google.ads.googleads.v1.enums.policy_topic_evidence_destination_mismatch_url_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum)
  })
_sym_db.RegisterMessage(PolicyTopicEvidenceDestinationMismatchUrlTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
