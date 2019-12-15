# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/connection/v1beta1/connection.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/bigquery/connection/v1beta1/connection.proto',
  package='google.cloud.bigquery.connection.v1beta1',
  syntax='proto3',
  serialized_options=b'\n,com.google.cloud.bigquery.connection.v1beta1B\017ConnectionProtoZRgoogle.golang.org/genproto/googleapis/cloud/bigquery/connection/v1beta1;connection',
  serialized_pb=b'\n9google/cloud/bigquery/connection/v1beta1/connection.proto\x12(google.cloud.bigquery.connection.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/api/client.proto\"\x8a\x01\n\x17\x43reateConnectionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rconnection_id\x18\x02 \x01(\t\x12H\n\nconnection\x18\x03 \x01(\x0b\x32\x34.google.cloud.bigquery.connection.v1beta1.Connection\"$\n\x14GetConnectionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"o\n\x16ListConnectionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x31\n\x0bmax_results\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x12\n\npage_token\x18\x03 \x01(\t\"}\n\x17ListConnectionsResponse\x12\x17\n\x0fnext_page_token\x18\x01 \x01(\t\x12I\n\x0b\x63onnections\x18\x02 \x03(\x0b\x32\x34.google.cloud.bigquery.connection.v1beta1.Connection\"\xa2\x01\n\x17UpdateConnectionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12H\n\nconnection\x18\x02 \x01(\x0b\x32\x34.google.cloud.bigquery.connection.v1beta1.Connection\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x85\x01\n!UpdateConnectionCredentialRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\ncredential\x18\x02 \x01(\x0b\x32>.google.cloud.bigquery.connection.v1beta1.ConnectionCredential\"\'\n\x17\x44\x65leteConnectionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xf2\x01\n\nConnection\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rfriendly_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12Q\n\tcloud_sql\x18\x04 \x01(\x0b\x32<.google.cloud.bigquery.connection.v1beta1.CloudSqlPropertiesH\x00\x12\x15\n\rcreation_time\x18\x05 \x01(\x03\x12\x1a\n\x12last_modified_time\x18\x06 \x01(\x03\x12\x16\n\x0ehas_credential\x18\x07 \x01(\x08\x42\x0c\n\nproperties\"w\n\x14\x43onnectionCredential\x12Q\n\tcloud_sql\x18\x01 \x01(\x0b\x32<.google.cloud.bigquery.connection.v1beta1.CloudSqlCredentialH\x00\x42\x0c\n\ncredential\"\xdc\x01\n\x12\x43loudSqlProperties\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12W\n\x04type\x18\x03 \x01(\x0e\x32I.google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.DatabaseType\"F\n\x0c\x44\x61tabaseType\x12\x1d\n\x19\x44\x41TABASE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\t\n\x05MYSQL\x10\x02\"8\n\x12\x43loudSqlCredential\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t2\xe7\x0e\n\x11\x43onnectionService\x12\xd5\x01\n\x10\x43reateConnection\x12\x41.google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest\x1a\x34.google.cloud.bigquery.connection.v1beta1.Connection\"H\x82\xd3\xe4\x93\x02\x42\"4/v1beta1/{parent=projects/*/locations/*}/connections:\nconnection\x12\xc3\x01\n\rGetConnection\x12>.google.cloud.bigquery.connection.v1beta1.GetConnectionRequest\x1a\x34.google.cloud.bigquery.connection.v1beta1.Connection\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/v1beta1/{name=projects/*/locations/*/connections/*}\x12\xd4\x01\n\x0fListConnections\x12@.google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest\x1a\x41.google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/v1beta1/{parent=projects/*/locations/*}/connections\x12\xd5\x01\n\x10UpdateConnection\x12\x41.google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest\x1a\x34.google.cloud.bigquery.connection.v1beta1.Connection\"H\x82\xd3\xe4\x93\x02\x42\x32\x34/v1beta1/{name=projects/*/locations/*/connections/*}:\nconnection\x12\xd6\x01\n\x1aUpdateConnectionCredential\x12K.google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest\x1a\x16.google.protobuf.Empty\"S\x82\xd3\xe4\x93\x02M2?/v1beta1/{name=projects/*/locations/*/connections/*/credential}:\ncredential\x12\xab\x01\n\x10\x44\x65leteConnection\x12\x41.google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest\x1a\x16.google.protobuf.Empty\"<\x82\xd3\xe4\x93\x02\x36*4/v1beta1/{name=projects/*/locations/*/connections/*}\x12\x9b\x01\n\x0cGetIamPolicy\x12\".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"P\x82\xd3\xe4\x93\x02J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\x01*\x12\x9b\x01\n\x0cSetIamPolicy\x12\".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"P\x82\xd3\xe4\x93\x02J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\x01*\x12\xc1\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse\"V\x82\xd3\xe4\x93\x02P\"K/v1beta1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\x01*\x1a~\xca\x41!bigqueryconnection.googleapis.com\xd2\x41Whttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\x93\x01\n,com.google.cloud.bigquery.connection.v1beta1B\x0f\x43onnectionProtoZRgoogle.golang.org/genproto/googleapis/cloud/bigquery/connection/v1beta1;connectionb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_iam__policy__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])



_CLOUDSQLPROPERTIES_DATABASETYPE = _descriptor.EnumDescriptor(
  name='DatabaseType',
  full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.DatabaseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATABASE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTGRES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYSQL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1591,
  serialized_end=1661,
)
_sym_db.RegisterEnumDescriptor(_CLOUDSQLPROPERTIES_DATABASETYPE)


_CREATECONNECTIONREQUEST = _descriptor.Descriptor(
  name='CreateConnectionRequest',
  full_name='google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest.connection_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection', full_name='google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest.connection', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=314,
  serialized_end=452,
)


_GETCONNECTIONREQUEST = _descriptor.Descriptor(
  name='GetConnectionRequest',
  full_name='google.cloud.bigquery.connection.v1beta1.GetConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.bigquery.connection.v1beta1.GetConnectionRequest.name', index=0,
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
  serialized_start=454,
  serialized_end=490,
)


_LISTCONNECTIONSREQUEST = _descriptor.Descriptor(
  name='ListConnectionsRequest',
  full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest.max_results', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=492,
  serialized_end=603,
)


_LISTCONNECTIONSRESPONSE = _descriptor.Descriptor(
  name='ListConnectionsResponse',
  full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse.next_page_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connections', full_name='google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse.connections', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=605,
  serialized_end=730,
)


_UPDATECONNECTIONREQUEST = _descriptor.Descriptor(
  name='UpdateConnectionRequest',
  full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection', full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest.connection', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=733,
  serialized_end=895,
)


_UPDATECONNECTIONCREDENTIALREQUEST = _descriptor.Descriptor(
  name='UpdateConnectionCredentialRequest',
  full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credential', full_name='google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest.credential', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=898,
  serialized_end=1031,
)


_DELETECONNECTIONREQUEST = _descriptor.Descriptor(
  name='DeleteConnectionRequest',
  full_name='google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest.name', index=0,
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
  serialized_start=1033,
  serialized_end=1072,
)


_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='google.cloud.bigquery.connection.v1beta1.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.bigquery.connection.v1beta1.Connection.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friendly_name', full_name='google.cloud.bigquery.connection.v1beta1.Connection.friendly_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.bigquery.connection.v1beta1.Connection.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_sql', full_name='google.cloud.bigquery.connection.v1beta1.Connection.cloud_sql', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='google.cloud.bigquery.connection.v1beta1.Connection.creation_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_modified_time', full_name='google.cloud.bigquery.connection.v1beta1.Connection.last_modified_time', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_credential', full_name='google.cloud.bigquery.connection.v1beta1.Connection.has_credential', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='properties', full_name='google.cloud.bigquery.connection.v1beta1.Connection.properties',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1075,
  serialized_end=1317,
)


_CONNECTIONCREDENTIAL = _descriptor.Descriptor(
  name='ConnectionCredential',
  full_name='google.cloud.bigquery.connection.v1beta1.ConnectionCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_sql', full_name='google.cloud.bigquery.connection.v1beta1.ConnectionCredential.cloud_sql', index=0,
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
    _descriptor.OneofDescriptor(
      name='credential', full_name='google.cloud.bigquery.connection.v1beta1.ConnectionCredential.credential',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1319,
  serialized_end=1438,
)


_CLOUDSQLPROPERTIES = _descriptor.Descriptor(
  name='CloudSqlProperties',
  full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database', full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.database', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLOUDSQLPROPERTIES_DATABASETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1441,
  serialized_end=1661,
)


_CLOUDSQLCREDENTIAL = _descriptor.Descriptor(
  name='CloudSqlCredential',
  full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlCredential.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='google.cloud.bigquery.connection.v1beta1.CloudSqlCredential.password', index=1,
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
  serialized_start=1663,
  serialized_end=1719,
)

_CREATECONNECTIONREQUEST.fields_by_name['connection'].message_type = _CONNECTION
_LISTCONNECTIONSREQUEST.fields_by_name['max_results'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_LISTCONNECTIONSRESPONSE.fields_by_name['connections'].message_type = _CONNECTION
_UPDATECONNECTIONREQUEST.fields_by_name['connection'].message_type = _CONNECTION
_UPDATECONNECTIONREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATECONNECTIONCREDENTIALREQUEST.fields_by_name['credential'].message_type = _CONNECTIONCREDENTIAL
_CONNECTION.fields_by_name['cloud_sql'].message_type = _CLOUDSQLPROPERTIES
_CONNECTION.oneofs_by_name['properties'].fields.append(
  _CONNECTION.fields_by_name['cloud_sql'])
_CONNECTION.fields_by_name['cloud_sql'].containing_oneof = _CONNECTION.oneofs_by_name['properties']
_CONNECTIONCREDENTIAL.fields_by_name['cloud_sql'].message_type = _CLOUDSQLCREDENTIAL
_CONNECTIONCREDENTIAL.oneofs_by_name['credential'].fields.append(
  _CONNECTIONCREDENTIAL.fields_by_name['cloud_sql'])
_CONNECTIONCREDENTIAL.fields_by_name['cloud_sql'].containing_oneof = _CONNECTIONCREDENTIAL.oneofs_by_name['credential']
_CLOUDSQLPROPERTIES.fields_by_name['type'].enum_type = _CLOUDSQLPROPERTIES_DATABASETYPE
_CLOUDSQLPROPERTIES_DATABASETYPE.containing_type = _CLOUDSQLPROPERTIES
DESCRIPTOR.message_types_by_name['CreateConnectionRequest'] = _CREATECONNECTIONREQUEST
DESCRIPTOR.message_types_by_name['GetConnectionRequest'] = _GETCONNECTIONREQUEST
DESCRIPTOR.message_types_by_name['ListConnectionsRequest'] = _LISTCONNECTIONSREQUEST
DESCRIPTOR.message_types_by_name['ListConnectionsResponse'] = _LISTCONNECTIONSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateConnectionRequest'] = _UPDATECONNECTIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateConnectionCredentialRequest'] = _UPDATECONNECTIONCREDENTIALREQUEST
DESCRIPTOR.message_types_by_name['DeleteConnectionRequest'] = _DELETECONNECTIONREQUEST
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['ConnectionCredential'] = _CONNECTIONCREDENTIAL
DESCRIPTOR.message_types_by_name['CloudSqlProperties'] = _CLOUDSQLPROPERTIES
DESCRIPTOR.message_types_by_name['CloudSqlCredential'] = _CLOUDSQLCREDENTIAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateConnectionRequest = _reflection.GeneratedProtocolMessageType('CreateConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest)
  })
_sym_db.RegisterMessage(CreateConnectionRequest)

GetConnectionRequest = _reflection.GeneratedProtocolMessageType('GetConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.GetConnectionRequest)
  })
_sym_db.RegisterMessage(GetConnectionRequest)

ListConnectionsRequest = _reflection.GeneratedProtocolMessageType('ListConnectionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONNECTIONSREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest)
  })
_sym_db.RegisterMessage(ListConnectionsRequest)

ListConnectionsResponse = _reflection.GeneratedProtocolMessageType('ListConnectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONNECTIONSRESPONSE,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse)
  })
_sym_db.RegisterMessage(ListConnectionsResponse)

UpdateConnectionRequest = _reflection.GeneratedProtocolMessageType('UpdateConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest)
  })
_sym_db.RegisterMessage(UpdateConnectionRequest)

UpdateConnectionCredentialRequest = _reflection.GeneratedProtocolMessageType('UpdateConnectionCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONNECTIONCREDENTIALREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest)
  })
_sym_db.RegisterMessage(UpdateConnectionCredentialRequest)

DeleteConnectionRequest = _reflection.GeneratedProtocolMessageType('DeleteConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest)
  })
_sym_db.RegisterMessage(DeleteConnectionRequest)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.Connection)
  })
_sym_db.RegisterMessage(Connection)

ConnectionCredential = _reflection.GeneratedProtocolMessageType('ConnectionCredential', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONCREDENTIAL,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.ConnectionCredential)
  })
_sym_db.RegisterMessage(ConnectionCredential)

CloudSqlProperties = _reflection.GeneratedProtocolMessageType('CloudSqlProperties', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSQLPROPERTIES,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.CloudSqlProperties)
  })
_sym_db.RegisterMessage(CloudSqlProperties)

CloudSqlCredential = _reflection.GeneratedProtocolMessageType('CloudSqlCredential', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSQLCREDENTIAL,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.CloudSqlCredential)
  })
_sym_db.RegisterMessage(CloudSqlCredential)


DESCRIPTOR._options = None

_CONNECTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ConnectionService',
  full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A!bigqueryconnection.googleapis.com\322AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform',
  serialized_start=1722,
  serialized_end=3617,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateConnection',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.CreateConnection',
    index=0,
    containing_service=None,
    input_type=_CREATECONNECTIONREQUEST,
    output_type=_CONNECTION,
    serialized_options=b'\202\323\344\223\002B\"4/v1beta1/{parent=projects/*/locations/*}/connections:\nconnection',
  ),
  _descriptor.MethodDescriptor(
    name='GetConnection',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.GetConnection',
    index=1,
    containing_service=None,
    input_type=_GETCONNECTIONREQUEST,
    output_type=_CONNECTION,
    serialized_options=b'\202\323\344\223\0026\0224/v1beta1/{name=projects/*/locations/*/connections/*}',
  ),
  _descriptor.MethodDescriptor(
    name='ListConnections',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.ListConnections',
    index=2,
    containing_service=None,
    input_type=_LISTCONNECTIONSREQUEST,
    output_type=_LISTCONNECTIONSRESPONSE,
    serialized_options=b'\202\323\344\223\0026\0224/v1beta1/{parent=projects/*/locations/*}/connections',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateConnection',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.UpdateConnection',
    index=3,
    containing_service=None,
    input_type=_UPDATECONNECTIONREQUEST,
    output_type=_CONNECTION,
    serialized_options=b'\202\323\344\223\002B24/v1beta1/{name=projects/*/locations/*/connections/*}:\nconnection',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateConnectionCredential',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.UpdateConnectionCredential',
    index=4,
    containing_service=None,
    input_type=_UPDATECONNECTIONCREDENTIALREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002M2?/v1beta1/{name=projects/*/locations/*/connections/*/credential}:\ncredential',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteConnection',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.DeleteConnection',
    index=5,
    containing_service=None,
    input_type=_DELETECONNECTIONREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\0026*4/v1beta1/{name=projects/*/locations/*/connections/*}',
  ),
  _descriptor.MethodDescriptor(
    name='GetIamPolicy',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.GetIamPolicy',
    index=6,
    containing_service=None,
    input_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._GETIAMPOLICYREQUEST,
    output_type=google_dot_iam_dot_v1_dot_policy__pb2._POLICY,
    serialized_options=b'\202\323\344\223\002J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SetIamPolicy',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.SetIamPolicy',
    index=7,
    containing_service=None,
    input_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._SETIAMPOLICYREQUEST,
    output_type=google_dot_iam_dot_v1_dot_policy__pb2._POLICY,
    serialized_options=b'\202\323\344\223\002J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='TestIamPermissions',
    full_name='google.cloud.bigquery.connection.v1beta1.ConnectionService.TestIamPermissions',
    index=8,
    containing_service=None,
    input_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._TESTIAMPERMISSIONSREQUEST,
    output_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._TESTIAMPERMISSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002P\"K/v1beta1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTIONSERVICE)

DESCRIPTOR.services_by_name['ConnectionService'] = _CONNECTIONSERVICE

# @@protoc_insertion_point(module_scope)