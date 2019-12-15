# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/servicecontrol/v1/distribution.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/servicecontrol/v1/distribution.proto',
  package='google.api.servicecontrol.v1',
  syntax='proto3',
  serialized_options=b'\n com.google.api.servicecontrol.v1B\021DistributionProtoP\001ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\370\001\001',
  serialized_pb=b'\n/google/api/servicecontrol/v1/distribution.proto\x12\x1cgoogle.api.servicecontrol.v1\"\xe8\x04\n\x0c\x44istribution\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x0c\n\x04mean\x18\x02 \x01(\x01\x12\x0f\n\x07minimum\x18\x03 \x01(\x01\x12\x0f\n\x07maximum\x18\x04 \x01(\x01\x12 \n\x18sum_of_squared_deviation\x18\x05 \x01(\x01\x12\x15\n\rbucket_counts\x18\x06 \x03(\x03\x12R\n\x0elinear_buckets\x18\x07 \x01(\x0b\x32\x38.google.api.servicecontrol.v1.Distribution.LinearBucketsH\x00\x12\\\n\x13\x65xponential_buckets\x18\x08 \x01(\x0b\x32=.google.api.servicecontrol.v1.Distribution.ExponentialBucketsH\x00\x12V\n\x10\x65xplicit_buckets\x18\t \x01(\x0b\x32:.google.api.servicecontrol.v1.Distribution.ExplicitBucketsH\x00\x1aJ\n\rLinearBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06offset\x18\x03 \x01(\x01\x1aV\n\x12\x45xponentialBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\x15\n\rgrowth_factor\x18\x02 \x01(\x01\x12\r\n\x05scale\x18\x03 \x01(\x01\x1a!\n\x0f\x45xplicitBuckets\x12\x0e\n\x06\x62ounds\x18\x01 \x03(\x01\x42\x0f\n\rbucket_optionB\x86\x01\n com.google.api.servicecontrol.v1B\x11\x44istributionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\xf8\x01\x01\x62\x06proto3'
)




_DISTRIBUTION_LINEARBUCKETS = _descriptor.Descriptor(
  name='LinearBuckets',
  full_name='google.api.servicecontrol.v1.Distribution.LinearBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_finite_buckets', full_name='google.api.servicecontrol.v1.Distribution.LinearBuckets.num_finite_buckets', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='google.api.servicecontrol.v1.Distribution.LinearBuckets.width', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='google.api.servicecontrol.v1.Distribution.LinearBuckets.offset', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=484,
  serialized_end=558,
)

_DISTRIBUTION_EXPONENTIALBUCKETS = _descriptor.Descriptor(
  name='ExponentialBuckets',
  full_name='google.api.servicecontrol.v1.Distribution.ExponentialBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_finite_buckets', full_name='google.api.servicecontrol.v1.Distribution.ExponentialBuckets.num_finite_buckets', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='growth_factor', full_name='google.api.servicecontrol.v1.Distribution.ExponentialBuckets.growth_factor', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='google.api.servicecontrol.v1.Distribution.ExponentialBuckets.scale', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=560,
  serialized_end=646,
)

_DISTRIBUTION_EXPLICITBUCKETS = _descriptor.Descriptor(
  name='ExplicitBuckets',
  full_name='google.api.servicecontrol.v1.Distribution.ExplicitBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounds', full_name='google.api.servicecontrol.v1.Distribution.ExplicitBuckets.bounds', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=648,
  serialized_end=681,
)

_DISTRIBUTION = _descriptor.Descriptor(
  name='Distribution',
  full_name='google.api.servicecontrol.v1.Distribution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='google.api.servicecontrol.v1.Distribution.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean', full_name='google.api.servicecontrol.v1.Distribution.mean', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum', full_name='google.api.servicecontrol.v1.Distribution.minimum', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='google.api.servicecontrol.v1.Distribution.maximum', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum_of_squared_deviation', full_name='google.api.servicecontrol.v1.Distribution.sum_of_squared_deviation', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket_counts', full_name='google.api.servicecontrol.v1.Distribution.bucket_counts', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_buckets', full_name='google.api.servicecontrol.v1.Distribution.linear_buckets', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exponential_buckets', full_name='google.api.servicecontrol.v1.Distribution.exponential_buckets', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='explicit_buckets', full_name='google.api.servicecontrol.v1.Distribution.explicit_buckets', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DISTRIBUTION_LINEARBUCKETS, _DISTRIBUTION_EXPONENTIALBUCKETS, _DISTRIBUTION_EXPLICITBUCKETS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='bucket_option', full_name='google.api.servicecontrol.v1.Distribution.bucket_option',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=82,
  serialized_end=698,
)

_DISTRIBUTION_LINEARBUCKETS.containing_type = _DISTRIBUTION
_DISTRIBUTION_EXPONENTIALBUCKETS.containing_type = _DISTRIBUTION
_DISTRIBUTION_EXPLICITBUCKETS.containing_type = _DISTRIBUTION
_DISTRIBUTION.fields_by_name['linear_buckets'].message_type = _DISTRIBUTION_LINEARBUCKETS
_DISTRIBUTION.fields_by_name['exponential_buckets'].message_type = _DISTRIBUTION_EXPONENTIALBUCKETS
_DISTRIBUTION.fields_by_name['explicit_buckets'].message_type = _DISTRIBUTION_EXPLICITBUCKETS
_DISTRIBUTION.oneofs_by_name['bucket_option'].fields.append(
  _DISTRIBUTION.fields_by_name['linear_buckets'])
_DISTRIBUTION.fields_by_name['linear_buckets'].containing_oneof = _DISTRIBUTION.oneofs_by_name['bucket_option']
_DISTRIBUTION.oneofs_by_name['bucket_option'].fields.append(
  _DISTRIBUTION.fields_by_name['exponential_buckets'])
_DISTRIBUTION.fields_by_name['exponential_buckets'].containing_oneof = _DISTRIBUTION.oneofs_by_name['bucket_option']
_DISTRIBUTION.oneofs_by_name['bucket_option'].fields.append(
  _DISTRIBUTION.fields_by_name['explicit_buckets'])
_DISTRIBUTION.fields_by_name['explicit_buckets'].containing_oneof = _DISTRIBUTION.oneofs_by_name['bucket_option']
DESCRIPTOR.message_types_by_name['Distribution'] = _DISTRIBUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Distribution = _reflection.GeneratedProtocolMessageType('Distribution', (_message.Message,), {

  'LinearBuckets' : _reflection.GeneratedProtocolMessageType('LinearBuckets', (_message.Message,), {
    'DESCRIPTOR' : _DISTRIBUTION_LINEARBUCKETS,
    '__module__' : 'google.api.servicecontrol.v1.distribution_pb2'
    # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.Distribution.LinearBuckets)
    })
  ,

  'ExponentialBuckets' : _reflection.GeneratedProtocolMessageType('ExponentialBuckets', (_message.Message,), {
    'DESCRIPTOR' : _DISTRIBUTION_EXPONENTIALBUCKETS,
    '__module__' : 'google.api.servicecontrol.v1.distribution_pb2'
    # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.Distribution.ExponentialBuckets)
    })
  ,

  'ExplicitBuckets' : _reflection.GeneratedProtocolMessageType('ExplicitBuckets', (_message.Message,), {
    'DESCRIPTOR' : _DISTRIBUTION_EXPLICITBUCKETS,
    '__module__' : 'google.api.servicecontrol.v1.distribution_pb2'
    # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.Distribution.ExplicitBuckets)
    })
  ,
  'DESCRIPTOR' : _DISTRIBUTION,
  '__module__' : 'google.api.servicecontrol.v1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.Distribution)
  })
_sym_db.RegisterMessage(Distribution)
_sym_db.RegisterMessage(Distribution.LinearBuckets)
_sym_db.RegisterMessage(Distribution.ExponentialBuckets)
_sym_db.RegisterMessage(Distribution.ExplicitBuckets)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)