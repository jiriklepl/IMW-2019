# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/oslogin/v1beta/oslogin.proto

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
from google.cloud.oslogin.common import common_pb2 as google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/oslogin/v1beta/oslogin.proto',
  package='google.cloud.oslogin.v1beta',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.oslogin.v1betaB\014OsLoginProtoP\001ZBgoogle.golang.org/genproto/googleapis/cloud/oslogin/v1beta;oslogin\252\002\033Google.Cloud.OsLogin.V1Beta\312\002\033Google\\Cloud\\OsLogin\\V1beta',
  serialized_pb=b'\n)google/cloud/oslogin/v1beta/oslogin.proto\x12\x1bgoogle.cloud.oslogin.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/oslogin/common/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\x9c\x02\n\x0cLoginProfile\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x41\n\x0eposix_accounts\x18\x02 \x03(\x0b\x32).google.cloud.oslogin.common.PosixAccount\x12U\n\x0fssh_public_keys\x18\x03 \x03(\x0b\x32<.google.cloud.oslogin.v1beta.LoginProfile.SshPublicKeysEntry\x1a_\n\x12SshPublicKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).google.cloud.oslogin.common.SshPublicKey:\x02\x38\x01\"V\n\x19\x44\x65letePosixAccountRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#oslogin.googleapis.com/PosixAccount\"V\n\x19\x44\x65leteSshPublicKeyRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#oslogin.googleapis.com/SshPublicKey\"r\n\x16GetLoginProfileRequest\x12\x31\n\x04name\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1boslogin.googleapis.com/User\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x11\n\tsystem_id\x18\x03 \x01(\t\"S\n\x16GetSshPublicKeyRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#oslogin.googleapis.com/SshPublicKey\"\xb1\x01\n\x19ImportSshPublicKeyRequest\x12\x38\n\x06parent\x18\x01 \x01(\tB(\xfa\x41%\x12#oslogin.googleapis.com/SshPublicKey\x12\x46\n\x0essh_public_key\x18\x02 \x01(\x0b\x32).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0\x41\x02\x12\x12\n\nproject_id\x18\x03 \x01(\t\"^\n\x1aImportSshPublicKeyResponse\x12@\n\rlogin_profile\x18\x01 \x01(\x0b\x32).google.cloud.oslogin.v1beta.LoginProfile\"\xcf\x01\n\x19UpdateSshPublicKeyRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#oslogin.googleapis.com/SshPublicKey\x12\x46\n\x0essh_public_key\x18\x02 \x01(\x0b\x32).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0\x41\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask2\xf4\n\n\x0eOsLoginService\x12\x96\x01\n\x12\x44\x65letePosixAccount\x12\x36.google.cloud.oslogin.v1beta.DeletePosixAccountRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02#*!/v1beta/{name=users/*/projects/*}\xda\x41\x04name\x12\x9b\x01\n\x12\x44\x65leteSshPublicKey\x12\x36.google.cloud.oslogin.v1beta.DeleteSshPublicKeyRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02(*&/v1beta/{name=users/*/sshPublicKeys/*}\xda\x41\x04name\x12\xa5\x01\n\x0fGetLoginProfile\x12\x33.google.cloud.oslogin.v1beta.GetLoginProfileRequest\x1a).google.cloud.oslogin.v1beta.LoginProfile\"2\x82\xd3\xe4\x93\x02%\x12#/v1beta/{name=users/*}/loginProfile\xda\x41\x04name\x12\xa8\x01\n\x0fGetSshPublicKey\x12\x33.google.cloud.oslogin.v1beta.GetSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey\"5\x82\xd3\xe4\x93\x02(\x12&/v1beta/{name=users/*/sshPublicKeys/*}\xda\x41\x04name\x12\x85\x02\n\x12ImportSshPublicKey\x12\x36.google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest\x1a\x37.google.cloud.oslogin.v1beta.ImportSshPublicKeyResponse\"~\x82\xd3\xe4\x93\x02=\"+/v1beta/{parent=users/*}:importSshPublicKey:\x0essh_public_key\xda\x41\x15parent,ssh_public_key\xda\x41 parent,ssh_public_key,project_id\x12\xef\x01\n\x12UpdateSshPublicKey\x12\x36.google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey\"v\x82\xd3\xe4\x93\x02\x38\x32&/v1beta/{name=users/*/sshPublicKeys/*}:\x0essh_public_key\xda\x41\x13name,ssh_public_key\xda\x41\x1fname,ssh_public_key,update_mask\x1a\xdd\x01\xca\x41\x16oslogin.googleapis.com\xd2\x41\xc0\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonlyB\xb1\x01\n\x1f\x63om.google.cloud.oslogin.v1betaB\x0cOsLoginProtoP\x01ZBgoogle.golang.org/genproto/googleapis/cloud/oslogin/v1beta;oslogin\xaa\x02\x1bGoogle.Cloud.OsLogin.V1Beta\xca\x02\x1bGoogle\\Cloud\\OsLogin\\V1betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_LOGINPROFILE_SSHPUBLICKEYSENTRY = _descriptor.Descriptor(
  name='SshPublicKeysEntry',
  full_name='google.cloud.oslogin.v1beta.LoginProfile.SshPublicKeysEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.oslogin.v1beta.LoginProfile.SshPublicKeysEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.oslogin.v1beta.LoginProfile.SshPublicKeysEntry.value', index=1,
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
  serialized_start=484,
  serialized_end=579,
)

_LOGINPROFILE = _descriptor.Descriptor(
  name='LoginProfile',
  full_name='google.cloud.oslogin.v1beta.LoginProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.oslogin.v1beta.LoginProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='posix_accounts', full_name='google.cloud.oslogin.v1beta.LoginProfile.posix_accounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssh_public_keys', full_name='google.cloud.oslogin.v1beta.LoginProfile.ssh_public_keys', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOGINPROFILE_SSHPUBLICKEYSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=579,
)


_DELETEPOSIXACCOUNTREQUEST = _descriptor.Descriptor(
  name='DeletePosixAccountRequest',
  full_name='google.cloud.oslogin.v1beta.DeletePosixAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.oslogin.v1beta.DeletePosixAccountRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A%\n#oslogin.googleapis.com/PosixAccount', file=DESCRIPTOR),
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
  serialized_start=581,
  serialized_end=667,
)


_DELETESSHPUBLICKEYREQUEST = _descriptor.Descriptor(
  name='DeleteSshPublicKeyRequest',
  full_name='google.cloud.oslogin.v1beta.DeleteSshPublicKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.oslogin.v1beta.DeleteSshPublicKeyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A%\n#oslogin.googleapis.com/SshPublicKey', file=DESCRIPTOR),
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
  serialized_start=669,
  serialized_end=755,
)


_GETLOGINPROFILEREQUEST = _descriptor.Descriptor(
  name='GetLoginProfileRequest',
  full_name='google.cloud.oslogin.v1beta.GetLoginProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.oslogin.v1beta.GetLoginProfileRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\035\n\033oslogin.googleapis.com/User', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.cloud.oslogin.v1beta.GetLoginProfileRequest.project_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_id', full_name='google.cloud.oslogin.v1beta.GetLoginProfileRequest.system_id', index=2,
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
  serialized_start=757,
  serialized_end=871,
)


_GETSSHPUBLICKEYREQUEST = _descriptor.Descriptor(
  name='GetSshPublicKeyRequest',
  full_name='google.cloud.oslogin.v1beta.GetSshPublicKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.oslogin.v1beta.GetSshPublicKeyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A%\n#oslogin.googleapis.com/SshPublicKey', file=DESCRIPTOR),
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
  serialized_start=873,
  serialized_end=956,
)


_IMPORTSSHPUBLICKEYREQUEST = _descriptor.Descriptor(
  name='ImportSshPublicKeyRequest',
  full_name='google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A%\022#oslogin.googleapis.com/SshPublicKey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssh_public_key', full_name='google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest.ssh_public_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest.project_id', index=2,
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
  serialized_start=959,
  serialized_end=1136,
)


_IMPORTSSHPUBLICKEYRESPONSE = _descriptor.Descriptor(
  name='ImportSshPublicKeyResponse',
  full_name='google.cloud.oslogin.v1beta.ImportSshPublicKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login_profile', full_name='google.cloud.oslogin.v1beta.ImportSshPublicKeyResponse.login_profile', index=0,
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
  serialized_start=1138,
  serialized_end=1232,
)


_UPDATESSHPUBLICKEYREQUEST = _descriptor.Descriptor(
  name='UpdateSshPublicKeyRequest',
  full_name='google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A%\n#oslogin.googleapis.com/SshPublicKey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssh_public_key', full_name='google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest.ssh_public_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest.update_mask', index=2,
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
  serialized_start=1235,
  serialized_end=1442,
)

_LOGINPROFILE_SSHPUBLICKEYSENTRY.fields_by_name['value'].message_type = google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2._SSHPUBLICKEY
_LOGINPROFILE_SSHPUBLICKEYSENTRY.containing_type = _LOGINPROFILE
_LOGINPROFILE.fields_by_name['posix_accounts'].message_type = google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2._POSIXACCOUNT
_LOGINPROFILE.fields_by_name['ssh_public_keys'].message_type = _LOGINPROFILE_SSHPUBLICKEYSENTRY
_IMPORTSSHPUBLICKEYREQUEST.fields_by_name['ssh_public_key'].message_type = google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2._SSHPUBLICKEY
_IMPORTSSHPUBLICKEYRESPONSE.fields_by_name['login_profile'].message_type = _LOGINPROFILE
_UPDATESSHPUBLICKEYREQUEST.fields_by_name['ssh_public_key'].message_type = google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2._SSHPUBLICKEY
_UPDATESSHPUBLICKEYREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['LoginProfile'] = _LOGINPROFILE
DESCRIPTOR.message_types_by_name['DeletePosixAccountRequest'] = _DELETEPOSIXACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['DeleteSshPublicKeyRequest'] = _DELETESSHPUBLICKEYREQUEST
DESCRIPTOR.message_types_by_name['GetLoginProfileRequest'] = _GETLOGINPROFILEREQUEST
DESCRIPTOR.message_types_by_name['GetSshPublicKeyRequest'] = _GETSSHPUBLICKEYREQUEST
DESCRIPTOR.message_types_by_name['ImportSshPublicKeyRequest'] = _IMPORTSSHPUBLICKEYREQUEST
DESCRIPTOR.message_types_by_name['ImportSshPublicKeyResponse'] = _IMPORTSSHPUBLICKEYRESPONSE
DESCRIPTOR.message_types_by_name['UpdateSshPublicKeyRequest'] = _UPDATESSHPUBLICKEYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginProfile = _reflection.GeneratedProtocolMessageType('LoginProfile', (_message.Message,), {

  'SshPublicKeysEntry' : _reflection.GeneratedProtocolMessageType('SshPublicKeysEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGINPROFILE_SSHPUBLICKEYSENTRY,
    '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.LoginProfile.SshPublicKeysEntry)
    })
  ,
  'DESCRIPTOR' : _LOGINPROFILE,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.LoginProfile)
  })
_sym_db.RegisterMessage(LoginProfile)
_sym_db.RegisterMessage(LoginProfile.SshPublicKeysEntry)

DeletePosixAccountRequest = _reflection.GeneratedProtocolMessageType('DeletePosixAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOSIXACCOUNTREQUEST,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.DeletePosixAccountRequest)
  })
_sym_db.RegisterMessage(DeletePosixAccountRequest)

DeleteSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('DeleteSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.DeleteSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(DeleteSshPublicKeyRequest)

GetLoginProfileRequest = _reflection.GeneratedProtocolMessageType('GetLoginProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGINPROFILEREQUEST,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.GetLoginProfileRequest)
  })
_sym_db.RegisterMessage(GetLoginProfileRequest)

GetSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('GetSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.GetSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(GetSshPublicKeyRequest)

ImportSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('ImportSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTSSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(ImportSshPublicKeyRequest)

ImportSshPublicKeyResponse = _reflection.GeneratedProtocolMessageType('ImportSshPublicKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTSSHPUBLICKEYRESPONSE,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.ImportSshPublicKeyResponse)
  })
_sym_db.RegisterMessage(ImportSshPublicKeyResponse)

UpdateSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('UpdateSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1beta.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(UpdateSshPublicKeyRequest)


DESCRIPTOR._options = None
_LOGINPROFILE_SSHPUBLICKEYSENTRY._options = None
_LOGINPROFILE.fields_by_name['name']._options = None
_DELETEPOSIXACCOUNTREQUEST.fields_by_name['name']._options = None
_DELETESSHPUBLICKEYREQUEST.fields_by_name['name']._options = None
_GETLOGINPROFILEREQUEST.fields_by_name['name']._options = None
_GETSSHPUBLICKEYREQUEST.fields_by_name['name']._options = None
_IMPORTSSHPUBLICKEYREQUEST.fields_by_name['parent']._options = None
_IMPORTSSHPUBLICKEYREQUEST.fields_by_name['ssh_public_key']._options = None
_UPDATESSHPUBLICKEYREQUEST.fields_by_name['name']._options = None
_UPDATESSHPUBLICKEYREQUEST.fields_by_name['ssh_public_key']._options = None

_OSLOGINSERVICE = _descriptor.ServiceDescriptor(
  name='OsLoginService',
  full_name='google.cloud.oslogin.v1beta.OsLoginService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\026oslogin.googleapis.com\322A\300\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly',
  serialized_start=1445,
  serialized_end=2841,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeletePosixAccount',
    full_name='google.cloud.oslogin.v1beta.OsLoginService.DeletePosixAccount',
    index=0,
    containing_service=None,
    input_type=_DELETEPOSIXACCOUNTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002#*!/v1beta/{name=users/*/projects/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSshPublicKey',
    full_name='google.cloud.oslogin.v1beta.OsLoginService.DeleteSshPublicKey',
    index=1,
    containing_service=None,
    input_type=_DELETESSHPUBLICKEYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002(*&/v1beta/{name=users/*/sshPublicKeys/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='GetLoginProfile',
    full_name='google.cloud.oslogin.v1beta.OsLoginService.GetLoginProfile',
    index=2,
    containing_service=None,
    input_type=_GETLOGINPROFILEREQUEST,
    output_type=_LOGINPROFILE,
    serialized_options=b'\202\323\344\223\002%\022#/v1beta/{name=users/*}/loginProfile\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='GetSshPublicKey',
    full_name='google.cloud.oslogin.v1beta.OsLoginService.GetSshPublicKey',
    index=3,
    containing_service=None,
    input_type=_GETSSHPUBLICKEYREQUEST,
    output_type=google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2._SSHPUBLICKEY,
    serialized_options=b'\202\323\344\223\002(\022&/v1beta/{name=users/*/sshPublicKeys/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='ImportSshPublicKey',
    full_name='google.cloud.oslogin.v1beta.OsLoginService.ImportSshPublicKey',
    index=4,
    containing_service=None,
    input_type=_IMPORTSSHPUBLICKEYREQUEST,
    output_type=_IMPORTSSHPUBLICKEYRESPONSE,
    serialized_options=b'\202\323\344\223\002=\"+/v1beta/{parent=users/*}:importSshPublicKey:\016ssh_public_key\332A\025parent,ssh_public_key\332A parent,ssh_public_key,project_id',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSshPublicKey',
    full_name='google.cloud.oslogin.v1beta.OsLoginService.UpdateSshPublicKey',
    index=5,
    containing_service=None,
    input_type=_UPDATESSHPUBLICKEYREQUEST,
    output_type=google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2._SSHPUBLICKEY,
    serialized_options=b'\202\323\344\223\00282&/v1beta/{name=users/*/sshPublicKeys/*}:\016ssh_public_key\332A\023name,ssh_public_key\332A\037name,ssh_public_key,update_mask',
  ),
])
_sym_db.RegisterServiceDescriptor(_OSLOGINSERVICE)

DESCRIPTOR.services_by_name['OsLoginService'] = _OSLOGINSERVICE

# @@protoc_insertion_point(module_scope)
