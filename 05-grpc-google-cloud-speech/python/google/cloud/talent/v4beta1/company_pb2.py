# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent/v4beta1/company.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.talent.v4beta1 import common_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/talent/v4beta1/company.proto',
  package='google.cloud.talent.v4beta1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.talent.v4beta1B\024CompanyResourceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS',
  serialized_pb=b'\n)google/cloud/talent/v4beta1/company.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/talent/v4beta1/common.proto\"\xf8\x03\n\x07\x43ompany\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x18\n\x0b\x65xternal_id\x18\x03 \x01(\tB\x03\xe0\x41\x02\x12\x36\n\x04size\x18\x04 \x01(\x0e\x32(.google.cloud.talent.v4beta1.CompanySize\x12\x1c\n\x14headquarters_address\x18\x05 \x01(\t\x12\x15\n\rhiring_agency\x18\x06 \x01(\x08\x12\x10\n\x08\x65\x65o_text\x18\x07 \x01(\t\x12\x13\n\x0bwebsite_uri\x18\x08 \x01(\t\x12\x17\n\x0f\x63\x61reer_site_uri\x18\t \x01(\t\x12\x11\n\timage_uri\x18\n \x01(\t\x12\x30\n(keyword_searchable_job_custom_attributes\x18\x0b \x03(\t\x12K\n\x0c\x64\x65rived_info\x18\x0c \x01(\x0b\x32\x30.google.cloud.talent.v4beta1.Company.DerivedInfoB\x03\xe0\x41\x03\x12\x16\n\tsuspended\x18\r \x01(\x08\x42\x03\xe0\x41\x03\x1aS\n\x0b\x44\x65rivedInfo\x12\x44\n\x15headquarters_location\x18\x01 \x01(\x0b\x32%.google.cloud.talent.v4beta1.LocationB\x82\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x14\x43ompanyResourceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2.DESCRIPTOR,])




_COMPANY_DERIVEDINFO = _descriptor.Descriptor(
  name='DerivedInfo',
  full_name='google.cloud.talent.v4beta1.Company.DerivedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='headquarters_location', full_name='google.cloud.talent.v4beta1.Company.DerivedInfo.headquarters_location', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=601,
  serialized_end=684,
)

_COMPANY = _descriptor.Descriptor(
  name='Company',
  full_name='google.cloud.talent.v4beta1.Company',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.talent.v4beta1.Company.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.talent.v4beta1.Company.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_id', full_name='google.cloud.talent.v4beta1.Company.external_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='google.cloud.talent.v4beta1.Company.size', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headquarters_address', full_name='google.cloud.talent.v4beta1.Company.headquarters_address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hiring_agency', full_name='google.cloud.talent.v4beta1.Company.hiring_agency', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eeo_text', full_name='google.cloud.talent.v4beta1.Company.eeo_text', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='website_uri', full_name='google.cloud.talent.v4beta1.Company.website_uri', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='career_site_uri', full_name='google.cloud.talent.v4beta1.Company.career_site_uri', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_uri', full_name='google.cloud.talent.v4beta1.Company.image_uri', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_searchable_job_custom_attributes', full_name='google.cloud.talent.v4beta1.Company.keyword_searchable_job_custom_attributes', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derived_info', full_name='google.cloud.talent.v4beta1.Company.derived_info', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended', full_name='google.cloud.talent.v4beta1.Company.suspended', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMPANY_DERIVEDINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=684,
)

_COMPANY_DERIVEDINFO.fields_by_name['headquarters_location'].message_type = google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2._LOCATION
_COMPANY_DERIVEDINFO.containing_type = _COMPANY
_COMPANY.fields_by_name['size'].enum_type = google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2._COMPANYSIZE
_COMPANY.fields_by_name['derived_info'].message_type = _COMPANY_DERIVEDINFO
DESCRIPTOR.message_types_by_name['Company'] = _COMPANY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Company = _reflection.GeneratedProtocolMessageType('Company', (_message.Message,), {

  'DerivedInfo' : _reflection.GeneratedProtocolMessageType('DerivedInfo', (_message.Message,), {
    'DESCRIPTOR' : _COMPANY_DERIVEDINFO,
    '__module__' : 'google.cloud.talent.v4beta1.company_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.Company.DerivedInfo)
    })
  ,
  'DESCRIPTOR' : _COMPANY,
  '__module__' : 'google.cloud.talent.v4beta1.company_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.Company)
  })
_sym_db.RegisterMessage(Company)
_sym_db.RegisterMessage(Company.DerivedInfo)


DESCRIPTOR._options = None
_COMPANY.fields_by_name['display_name']._options = None
_COMPANY.fields_by_name['external_id']._options = None
_COMPANY.fields_by_name['derived_info']._options = None
_COMPANY.fields_by_name['suspended']._options = None
# @@protoc_insertion_point(module_scope)
