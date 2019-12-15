# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataproc/v1beta2/autoscaling_policies.proto

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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dataproc/v1beta2/autoscaling_policies.proto',
  package='google.cloud.dataproc.v1beta2',
  syntax='proto3',
  serialized_options=b'\n!com.google.cloud.dataproc.v1beta2B\030AutoscalingPoliciesProtoP\001ZEgoogle.golang.org/genproto/googleapis/cloud/dataproc/v1beta2;dataproc',
  serialized_pb=b'\n8google/cloud/dataproc/v1beta2/autoscaling_policies.proto\x12\x1dgoogle.cloud.dataproc.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xb9\x04\n\x11\x41utoscalingPolicy\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0\x41\x03\x12S\n\x0f\x62\x61sic_algorithm\x18\x03 \x01(\x0b\x32\x38.google.cloud.dataproc.v1beta2.BasicAutoscalingAlgorithmH\x00\x12_\n\rworker_config\x18\x04 \x01(\x0b\x32\x43.google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfigB\x03\xe0\x41\x02\x12i\n\x17secondary_worker_config\x18\x05 \x01(\x0b\x32\x43.google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfigB\x03\xe0\x41\x01:\xd1\x01\xea\x41\xcd\x01\n)dataproc.googleapis.com/AutoscalingPolicy\x12Lprojects/{project}/regions/{region}/autoscalingPolicies/{autoscaling_policy}\x12Pprojects/{project}/locations/{location}/autoscalingPolicies/{autoscaling_policy} \x01\x42\x0b\n\talgorithm\"\xa9\x01\n\x19\x42\x61sicAutoscalingAlgorithm\x12S\n\x0byarn_config\x18\x01 \x01(\x0b\x32\x39.google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfigB\x03\xe0\x41\x02\x12\x37\n\x0f\x63ooldown_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x03\xe0\x41\x01\"\xf9\x01\n\x1a\x42\x61sicYarnAutoscalingConfig\x12\x45\n\x1dgraceful_decommission_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x03\xe0\x41\x02\x12\x1c\n\x0fscale_up_factor\x18\x01 \x01(\x01\x42\x03\xe0\x41\x02\x12\x1e\n\x11scale_down_factor\x18\x02 \x01(\x01\x42\x03\xe0\x41\x02\x12)\n\x1cscale_up_min_worker_fraction\x18\x03 \x01(\x01\x42\x03\xe0\x41\x01\x12+\n\x1escale_down_min_worker_fraction\x18\x04 \x01(\x01\x42\x03\xe0\x41\x01\"s\n$InstanceGroupAutoscalingPolicyConfig\x12\x1a\n\rmin_instances\x18\x01 \x01(\x05\x42\x03\xe0\x41\x01\x12\x1a\n\rmax_instances\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x13\n\x06weight\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01\"\xaa\x01\n\x1e\x43reateAutoscalingPolicyRequest\x12\x41\n\x06parent\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\x12)dataproc.googleapis.com/AutoscalingPolicy\x12\x45\n\x06policy\x18\x02 \x01(\x0b\x32\x30.google.cloud.dataproc.v1beta2.AutoscalingPolicyB\x03\xe0\x41\x02\"^\n\x1bGetAutoscalingPolicyRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)dataproc.googleapis.com/AutoscalingPolicy\"\x95\x01\n\x1eUpdateAutoscalingPolicyRequest\x12s\n\x06policy\x18\x01 \x01(\x0b\x32\x30.google.cloud.dataproc.v1beta2.AutoscalingPolicyB1\xe0\x41\x02\xfa\x41+\n)dataproc.googleapis.com/AutoscalingPolicy\"a\n\x1e\x44\x65leteAutoscalingPolicyRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)dataproc.googleapis.com/AutoscalingPolicy\"\x94\x01\n\x1eListAutoscalingPoliciesRequest\x12\x41\n\x06parent\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\x12)dataproc.googleapis.com/AutoscalingPolicy\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\"\x88\x01\n\x1fListAutoscalingPoliciesResponse\x12G\n\x08policies\x18\x01 \x03(\x0b\x32\x30.google.cloud.dataproc.v1beta2.AutoscalingPolicyB\x03\xe0\x41\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03\x32\x8f\x0c\n\x18\x41utoscalingPolicyService\x12\xb0\x02\n\x17\x43reateAutoscalingPolicy\x12=.google.cloud.dataproc.v1beta2.CreateAutoscalingPolicyRequest\x1a\x30.google.cloud.dataproc.v1beta2.AutoscalingPolicy\"\xa3\x01\x82\xd3\xe4\x93\x02\x8c\x01\"</v1beta2/{parent=projects/*/locations/*}/autoscalingPolicies:\x06policyZD\":/v1beta2/{parent=projects/*/regions/*}/autoscalingPolicies:\x06policy\xda\x41\rparent,policy\x12\xb7\x02\n\x17UpdateAutoscalingPolicy\x12=.google.cloud.dataproc.v1beta2.UpdateAutoscalingPolicyRequest\x1a\x30.google.cloud.dataproc.v1beta2.AutoscalingPolicy\"\xaa\x01\x82\xd3\xe4\x93\x02\x9a\x01\x1a\x43/v1beta2/{policy.name=projects/*/locations/*/autoscalingPolicies/*}:\x06policyZK\x1a\x41/v1beta2/{policy.name=projects/*/regions/*/autoscalingPolicies/*}:\x06policy\xda\x41\x06policy\x12\x90\x02\n\x14GetAutoscalingPolicy\x12:.google.cloud.dataproc.v1beta2.GetAutoscalingPolicyRequest\x1a\x30.google.cloud.dataproc.v1beta2.AutoscalingPolicy\"\x89\x01\x82\xd3\xe4\x93\x02|\x12</v1beta2/{name=projects/*/locations/*/autoscalingPolicies/*}Z<\x12:/v1beta2/{name=projects/*/regions/*/autoscalingPolicies/*}\xda\x41\x04name\x12\xa6\x02\n\x17ListAutoscalingPolicies\x12=.google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesRequest\x1a>.google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesResponse\"\x8b\x01\x82\xd3\xe4\x93\x02|\x12</v1beta2/{parent=projects/*/locations/*}/autoscalingPoliciesZ<\x12:/v1beta2/{parent=projects/*/regions/*}/autoscalingPolicies\xda\x41\x06parent\x12\xfc\x01\n\x17\x44\x65leteAutoscalingPolicy\x12=.google.cloud.dataproc.v1beta2.DeleteAutoscalingPolicyRequest\x1a\x16.google.protobuf.Empty\"\x89\x01\x82\xd3\xe4\x93\x02|*</v1beta2/{name=projects/*/locations/*/autoscalingPolicies/*}Z<*:/v1beta2/{name=projects/*/regions/*/autoscalingPolicies/*}\xda\x41\x04name\x1aK\xca\x41\x17\x64\x61taproc.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x86\x01\n!com.google.cloud.dataproc.v1beta2B\x18\x41utoscalingPoliciesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/cloud/dataproc/v1beta2;dataprocb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_AUTOSCALINGPOLICY = _descriptor.Descriptor(
  name='AutoscalingPolicy',
  full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='basic_algorithm', full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy.basic_algorithm', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker_config', full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy.worker_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_worker_config', full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy.secondary_worker_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\352A\315\001\n)dataproc.googleapis.com/AutoscalingPolicy\022Lprojects/{project}/regions/{region}/autoscalingPolicies/{autoscaling_policy}\022Pprojects/{project}/locations/{location}/autoscalingPolicies/{autoscaling_policy} \001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='algorithm', full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicy.algorithm',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=268,
  serialized_end=837,
)


_BASICAUTOSCALINGALGORITHM = _descriptor.Descriptor(
  name='BasicAutoscalingAlgorithm',
  full_name='google.cloud.dataproc.v1beta2.BasicAutoscalingAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='yarn_config', full_name='google.cloud.dataproc.v1beta2.BasicAutoscalingAlgorithm.yarn_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cooldown_period', full_name='google.cloud.dataproc.v1beta2.BasicAutoscalingAlgorithm.cooldown_period', index=1,
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
  serialized_start=840,
  serialized_end=1009,
)


_BASICYARNAUTOSCALINGCONFIG = _descriptor.Descriptor(
  name='BasicYarnAutoscalingConfig',
  full_name='google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graceful_decommission_timeout', full_name='google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig.graceful_decommission_timeout', index=0,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_up_factor', full_name='google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig.scale_up_factor', index=1,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_down_factor', full_name='google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig.scale_down_factor', index=2,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_up_min_worker_fraction', full_name='google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig.scale_up_min_worker_fraction', index=3,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_down_min_worker_fraction', full_name='google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig.scale_down_min_worker_fraction', index=4,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1012,
  serialized_end=1261,
)


_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG = _descriptor.Descriptor(
  name='InstanceGroupAutoscalingPolicyConfig',
  full_name='google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_instances', full_name='google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfig.min_instances', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_instances', full_name='google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfig.max_instances', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfig.weight', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1263,
  serialized_end=1378,
)


_CREATEAUTOSCALINGPOLICYREQUEST = _descriptor.Descriptor(
  name='CreateAutoscalingPolicyRequest',
  full_name='google.cloud.dataproc.v1beta2.CreateAutoscalingPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dataproc.v1beta2.CreateAutoscalingPolicyRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A+\022)dataproc.googleapis.com/AutoscalingPolicy', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policy', full_name='google.cloud.dataproc.v1beta2.CreateAutoscalingPolicyRequest.policy', index=1,
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
  serialized_start=1381,
  serialized_end=1551,
)


_GETAUTOSCALINGPOLICYREQUEST = _descriptor.Descriptor(
  name='GetAutoscalingPolicyRequest',
  full_name='google.cloud.dataproc.v1beta2.GetAutoscalingPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dataproc.v1beta2.GetAutoscalingPolicyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A+\n)dataproc.googleapis.com/AutoscalingPolicy', file=DESCRIPTOR),
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
  serialized_start=1553,
  serialized_end=1647,
)


_UPDATEAUTOSCALINGPOLICYREQUEST = _descriptor.Descriptor(
  name='UpdateAutoscalingPolicyRequest',
  full_name='google.cloud.dataproc.v1beta2.UpdateAutoscalingPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='google.cloud.dataproc.v1beta2.UpdateAutoscalingPolicyRequest.policy', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A+\n)dataproc.googleapis.com/AutoscalingPolicy', file=DESCRIPTOR),
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
  serialized_start=1650,
  serialized_end=1799,
)


_DELETEAUTOSCALINGPOLICYREQUEST = _descriptor.Descriptor(
  name='DeleteAutoscalingPolicyRequest',
  full_name='google.cloud.dataproc.v1beta2.DeleteAutoscalingPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dataproc.v1beta2.DeleteAutoscalingPolicyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A+\n)dataproc.googleapis.com/AutoscalingPolicy', file=DESCRIPTOR),
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
  serialized_start=1801,
  serialized_end=1898,
)


_LISTAUTOSCALINGPOLICIESREQUEST = _descriptor.Descriptor(
  name='ListAutoscalingPoliciesRequest',
  full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A+\022)dataproc.googleapis.com/AutoscalingPolicy', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesRequest.page_token', index=2,
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
  serialized_start=1901,
  serialized_end=2049,
)


_LISTAUTOSCALINGPOLICIESRESPONSE = _descriptor.Descriptor(
  name='ListAutoscalingPoliciesResponse',
  full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policies', full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesResponse.policies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
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
  serialized_start=2052,
  serialized_end=2188,
)

_AUTOSCALINGPOLICY.fields_by_name['basic_algorithm'].message_type = _BASICAUTOSCALINGALGORITHM
_AUTOSCALINGPOLICY.fields_by_name['worker_config'].message_type = _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG
_AUTOSCALINGPOLICY.fields_by_name['secondary_worker_config'].message_type = _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG
_AUTOSCALINGPOLICY.oneofs_by_name['algorithm'].fields.append(
  _AUTOSCALINGPOLICY.fields_by_name['basic_algorithm'])
_AUTOSCALINGPOLICY.fields_by_name['basic_algorithm'].containing_oneof = _AUTOSCALINGPOLICY.oneofs_by_name['algorithm']
_BASICAUTOSCALINGALGORITHM.fields_by_name['yarn_config'].message_type = _BASICYARNAUTOSCALINGCONFIG
_BASICAUTOSCALINGALGORITHM.fields_by_name['cooldown_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_BASICYARNAUTOSCALINGCONFIG.fields_by_name['graceful_decommission_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy'].message_type = _AUTOSCALINGPOLICY
_UPDATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy'].message_type = _AUTOSCALINGPOLICY
_LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['policies'].message_type = _AUTOSCALINGPOLICY
DESCRIPTOR.message_types_by_name['AutoscalingPolicy'] = _AUTOSCALINGPOLICY
DESCRIPTOR.message_types_by_name['BasicAutoscalingAlgorithm'] = _BASICAUTOSCALINGALGORITHM
DESCRIPTOR.message_types_by_name['BasicYarnAutoscalingConfig'] = _BASICYARNAUTOSCALINGCONFIG
DESCRIPTOR.message_types_by_name['InstanceGroupAutoscalingPolicyConfig'] = _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG
DESCRIPTOR.message_types_by_name['CreateAutoscalingPolicyRequest'] = _CREATEAUTOSCALINGPOLICYREQUEST
DESCRIPTOR.message_types_by_name['GetAutoscalingPolicyRequest'] = _GETAUTOSCALINGPOLICYREQUEST
DESCRIPTOR.message_types_by_name['UpdateAutoscalingPolicyRequest'] = _UPDATEAUTOSCALINGPOLICYREQUEST
DESCRIPTOR.message_types_by_name['DeleteAutoscalingPolicyRequest'] = _DELETEAUTOSCALINGPOLICYREQUEST
DESCRIPTOR.message_types_by_name['ListAutoscalingPoliciesRequest'] = _LISTAUTOSCALINGPOLICIESREQUEST
DESCRIPTOR.message_types_by_name['ListAutoscalingPoliciesResponse'] = _LISTAUTOSCALINGPOLICIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AutoscalingPolicy = _reflection.GeneratedProtocolMessageType('AutoscalingPolicy', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSCALINGPOLICY,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.AutoscalingPolicy)
  })
_sym_db.RegisterMessage(AutoscalingPolicy)

BasicAutoscalingAlgorithm = _reflection.GeneratedProtocolMessageType('BasicAutoscalingAlgorithm', (_message.Message,), {
  'DESCRIPTOR' : _BASICAUTOSCALINGALGORITHM,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.BasicAutoscalingAlgorithm)
  })
_sym_db.RegisterMessage(BasicAutoscalingAlgorithm)

BasicYarnAutoscalingConfig = _reflection.GeneratedProtocolMessageType('BasicYarnAutoscalingConfig', (_message.Message,), {
  'DESCRIPTOR' : _BASICYARNAUTOSCALINGCONFIG,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.BasicYarnAutoscalingConfig)
  })
_sym_db.RegisterMessage(BasicYarnAutoscalingConfig)

InstanceGroupAutoscalingPolicyConfig = _reflection.GeneratedProtocolMessageType('InstanceGroupAutoscalingPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.InstanceGroupAutoscalingPolicyConfig)
  })
_sym_db.RegisterMessage(InstanceGroupAutoscalingPolicyConfig)

CreateAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('CreateAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.CreateAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(CreateAutoscalingPolicyRequest)

GetAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('GetAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.GetAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(GetAutoscalingPolicyRequest)

UpdateAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('UpdateAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.UpdateAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(UpdateAutoscalingPolicyRequest)

DeleteAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('DeleteAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.DeleteAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(DeleteAutoscalingPolicyRequest)

ListAutoscalingPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListAutoscalingPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTOSCALINGPOLICIESREQUEST,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesRequest)
  })
_sym_db.RegisterMessage(ListAutoscalingPoliciesRequest)

ListAutoscalingPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListAutoscalingPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTOSCALINGPOLICIESRESPONSE,
  '__module__' : 'google.cloud.dataproc.v1beta2.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1beta2.ListAutoscalingPoliciesResponse)
  })
_sym_db.RegisterMessage(ListAutoscalingPoliciesResponse)


DESCRIPTOR._options = None
_AUTOSCALINGPOLICY.fields_by_name['id']._options = None
_AUTOSCALINGPOLICY.fields_by_name['name']._options = None
_AUTOSCALINGPOLICY.fields_by_name['worker_config']._options = None
_AUTOSCALINGPOLICY.fields_by_name['secondary_worker_config']._options = None
_AUTOSCALINGPOLICY._options = None
_BASICAUTOSCALINGALGORITHM.fields_by_name['yarn_config']._options = None
_BASICAUTOSCALINGALGORITHM.fields_by_name['cooldown_period']._options = None
_BASICYARNAUTOSCALINGCONFIG.fields_by_name['graceful_decommission_timeout']._options = None
_BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_up_factor']._options = None
_BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_down_factor']._options = None
_BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_up_min_worker_fraction']._options = None
_BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_down_min_worker_fraction']._options = None
_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['min_instances']._options = None
_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['max_instances']._options = None
_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['weight']._options = None
_CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['parent']._options = None
_CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy']._options = None
_GETAUTOSCALINGPOLICYREQUEST.fields_by_name['name']._options = None
_UPDATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy']._options = None
_DELETEAUTOSCALINGPOLICYREQUEST.fields_by_name['name']._options = None
_LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['parent']._options = None
_LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['page_size']._options = None
_LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['page_token']._options = None
_LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['policies']._options = None
_LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['next_page_token']._options = None

_AUTOSCALINGPOLICYSERVICE = _descriptor.ServiceDescriptor(
  name='AutoscalingPolicyService',
  full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\027dataproc.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  serialized_start=2191,
  serialized_end=3742,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateAutoscalingPolicy',
    full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicyService.CreateAutoscalingPolicy',
    index=0,
    containing_service=None,
    input_type=_CREATEAUTOSCALINGPOLICYREQUEST,
    output_type=_AUTOSCALINGPOLICY,
    serialized_options=b'\202\323\344\223\002\214\001\"</v1beta2/{parent=projects/*/locations/*}/autoscalingPolicies:\006policyZD\":/v1beta2/{parent=projects/*/regions/*}/autoscalingPolicies:\006policy\332A\rparent,policy',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAutoscalingPolicy',
    full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicyService.UpdateAutoscalingPolicy',
    index=1,
    containing_service=None,
    input_type=_UPDATEAUTOSCALINGPOLICYREQUEST,
    output_type=_AUTOSCALINGPOLICY,
    serialized_options=b'\202\323\344\223\002\232\001\032C/v1beta2/{policy.name=projects/*/locations/*/autoscalingPolicies/*}:\006policyZK\032A/v1beta2/{policy.name=projects/*/regions/*/autoscalingPolicies/*}:\006policy\332A\006policy',
  ),
  _descriptor.MethodDescriptor(
    name='GetAutoscalingPolicy',
    full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicyService.GetAutoscalingPolicy',
    index=2,
    containing_service=None,
    input_type=_GETAUTOSCALINGPOLICYREQUEST,
    output_type=_AUTOSCALINGPOLICY,
    serialized_options=b'\202\323\344\223\002|\022</v1beta2/{name=projects/*/locations/*/autoscalingPolicies/*}Z<\022:/v1beta2/{name=projects/*/regions/*/autoscalingPolicies/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='ListAutoscalingPolicies',
    full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicyService.ListAutoscalingPolicies',
    index=3,
    containing_service=None,
    input_type=_LISTAUTOSCALINGPOLICIESREQUEST,
    output_type=_LISTAUTOSCALINGPOLICIESRESPONSE,
    serialized_options=b'\202\323\344\223\002|\022</v1beta2/{parent=projects/*/locations/*}/autoscalingPoliciesZ<\022:/v1beta2/{parent=projects/*/regions/*}/autoscalingPolicies\332A\006parent',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAutoscalingPolicy',
    full_name='google.cloud.dataproc.v1beta2.AutoscalingPolicyService.DeleteAutoscalingPolicy',
    index=4,
    containing_service=None,
    input_type=_DELETEAUTOSCALINGPOLICYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002|*</v1beta2/{name=projects/*/locations/*/autoscalingPolicies/*}Z<*:/v1beta2/{name=projects/*/regions/*/autoscalingPolicies/*}\332A\004name',
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTOSCALINGPOLICYSERVICE)

DESCRIPTOR.services_by_name['AutoscalingPolicyService'] = _AUTOSCALINGPOLICYSERVICE

# @@protoc_insertion_point(module_scope)