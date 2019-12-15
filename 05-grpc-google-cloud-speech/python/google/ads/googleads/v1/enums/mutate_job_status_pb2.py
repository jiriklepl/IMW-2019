# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v1/enums/mutate_job_status.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v1/enums/mutate_job_status.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v1.enumsB\024MutateJobStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums',
  serialized_pb=b'\n5google/ads/googleads/v1/enums/mutate_job_status.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"j\n\x13MutateJobStatusEnum\"S\n\x0fMutateJobStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x08\n\x04\x44ONE\x10\x04\x42\xe9\x01\n!com.google.ads.googleads.v1.enumsB\x14MutateJobStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MUTATEJOBSTATUSENUM_MUTATEJOBSTATUS = _descriptor.EnumDescriptor(
  name='MutateJobStatus',
  full_name='google.ads.googleads.v1.enums.MutateJobStatusEnum.MutateJobStatus',
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
      name='RUNNING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=141,
  serialized_end=224,
)
_sym_db.RegisterEnumDescriptor(_MUTATEJOBSTATUSENUM_MUTATEJOBSTATUS)


_MUTATEJOBSTATUSENUM = _descriptor.Descriptor(
  name='MutateJobStatusEnum',
  full_name='google.ads.googleads.v1.enums.MutateJobStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MUTATEJOBSTATUSENUM_MUTATEJOBSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=224,
)

_MUTATEJOBSTATUSENUM_MUTATEJOBSTATUS.containing_type = _MUTATEJOBSTATUSENUM
DESCRIPTOR.message_types_by_name['MutateJobStatusEnum'] = _MUTATEJOBSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MutateJobStatusEnum = _reflection.GeneratedProtocolMessageType('MutateJobStatusEnum', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEJOBSTATUSENUM,
  '__module__' : 'google.ads.googleads.v1.enums.mutate_job_status_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.MutateJobStatusEnum)
  })
_sym_db.RegisterMessage(MutateJobStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
