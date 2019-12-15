# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter/v1/asset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.securitycenter.v1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_security__marks__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/securitycenter/v1/asset.proto',
  package='google.cloud.securitycenter.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.cloud.securitycenter.v1P\001ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\252\002\036Google.Cloud.SecurityCenter.V1\312\002\036Google\\Cloud\\SecurityCenter\\V1\352\002!Google::Cloud::SecurityCenter::V1',
  serialized_pb=b'\n*google/cloud/securitycenter/v1/asset.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a\x33google/cloud/securitycenter/v1/security_marks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa6\x06\n\x05\x41sset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x62\n\x1asecurity_center_properties\x18\x02 \x01(\x0b\x32>.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties\x12Z\n\x13resource_properties\x18\x07 \x03(\x0b\x32=.google.cloud.securitycenter.v1.Asset.ResourcePropertiesEntry\x12\x45\n\x0esecurity_marks\x18\x08 \x01(\x0b\x32-.google.cloud.securitycenter.v1.SecurityMarks\x12/\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\niam_policy\x18\x0b \x01(\x0b\x32/.google.cloud.securitycenter.v1.Asset.IamPolicy\x1a\x94\x01\n\x18SecurityCenterProperties\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x17\n\x0fresource_parent\x18\x03 \x01(\t\x12\x18\n\x10resource_project\x18\x04 \x01(\t\x12\x17\n\x0fresource_owners\x18\x05 \x03(\t\x1a \n\tIamPolicy\x12\x13\n\x0bpolicy_blob\x18\x01 \x01(\t\x1aQ\n\x17ResourcePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01:U\xea\x41R\n#securitycenter.googleapis.com/Asset\x12+organizations/{organization}/assets/{asset}B\xda\x01\n\"com.google.cloud.securitycenter.v1P\x01ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_securitycenter_dot_v1_dot_security__marks__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ASSET_SECURITYCENTERPROPERTIES = _descriptor.Descriptor(
  name='SecurityCenterProperties',
  full_name='google.cloud.securitycenter.v1.Asset.SecurityCenterProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.resource_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_parent', full_name='google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.resource_parent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_project', full_name='google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.resource_project', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_owners', full_name='google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.resource_owners', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=706,
  serialized_end=854,
)

_ASSET_IAMPOLICY = _descriptor.Descriptor(
  name='IamPolicy',
  full_name='google.cloud.securitycenter.v1.Asset.IamPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_blob', full_name='google.cloud.securitycenter.v1.Asset.IamPolicy.policy_blob', index=0,
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
  serialized_start=856,
  serialized_end=888,
)

_ASSET_RESOURCEPROPERTIESENTRY = _descriptor.Descriptor(
  name='ResourcePropertiesEntry',
  full_name='google.cloud.securitycenter.v1.Asset.ResourcePropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.securitycenter.v1.Asset.ResourcePropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.securitycenter.v1.Asset.ResourcePropertiesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=890,
  serialized_end=971,
)

_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='google.cloud.securitycenter.v1.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.securitycenter.v1.Asset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security_center_properties', full_name='google.cloud.securitycenter.v1.Asset.security_center_properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_properties', full_name='google.cloud.securitycenter.v1.Asset.resource_properties', index=2,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security_marks', full_name='google.cloud.securitycenter.v1.Asset.security_marks', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.securitycenter.v1.Asset.create_time', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.securitycenter.v1.Asset.update_time', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iam_policy', full_name='google.cloud.securitycenter.v1.Asset.iam_policy', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ASSET_SECURITYCENTERPROPERTIES, _ASSET_IAMPOLICY, _ASSET_RESOURCEPROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\352AR\n#securitycenter.googleapis.com/Asset\022+organizations/{organization}/assets/{asset}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=1058,
)

_ASSET_SECURITYCENTERPROPERTIES.containing_type = _ASSET
_ASSET_IAMPOLICY.containing_type = _ASSET
_ASSET_RESOURCEPROPERTIESENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_ASSET_RESOURCEPROPERTIESENTRY.containing_type = _ASSET
_ASSET.fields_by_name['security_center_properties'].message_type = _ASSET_SECURITYCENTERPROPERTIES
_ASSET.fields_by_name['resource_properties'].message_type = _ASSET_RESOURCEPROPERTIESENTRY
_ASSET.fields_by_name['security_marks'].message_type = google_dot_cloud_dot_securitycenter_dot_v1_dot_security__marks__pb2._SECURITYMARKS
_ASSET.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSET.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSET.fields_by_name['iam_policy'].message_type = _ASSET_IAMPOLICY
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {

  'SecurityCenterProperties' : _reflection.GeneratedProtocolMessageType('SecurityCenterProperties', (_message.Message,), {
    'DESCRIPTOR' : _ASSET_SECURITYCENTERPROPERTIES,
    '__module__' : 'google.cloud.securitycenter.v1.asset_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Asset.SecurityCenterProperties)
    })
  ,

  'IamPolicy' : _reflection.GeneratedProtocolMessageType('IamPolicy', (_message.Message,), {
    'DESCRIPTOR' : _ASSET_IAMPOLICY,
    '__module__' : 'google.cloud.securitycenter.v1.asset_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Asset.IamPolicy)
    })
  ,

  'ResourcePropertiesEntry' : _reflection.GeneratedProtocolMessageType('ResourcePropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _ASSET_RESOURCEPROPERTIESENTRY,
    '__module__' : 'google.cloud.securitycenter.v1.asset_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Asset.ResourcePropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'google.cloud.securitycenter.v1.asset_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Asset)
  })
_sym_db.RegisterMessage(Asset)
_sym_db.RegisterMessage(Asset.SecurityCenterProperties)
_sym_db.RegisterMessage(Asset.IamPolicy)
_sym_db.RegisterMessage(Asset.ResourcePropertiesEntry)


DESCRIPTOR._options = None
_ASSET_RESOURCEPROPERTIESENTRY._options = None
_ASSET._options = None
# @@protoc_insertion_point(module_scope)