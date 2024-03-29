# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/credentials/v1/iamcredentials.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.iam.credentials.v1 import common_pb2 as google_dot_iam_dot_credentials_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/iam/credentials/v1/iamcredentials.proto',
  package='google.iam.credentials.v1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.iam.credentials.v1B\023IAMCredentialsProtoP\001ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\370\001\001',
  serialized_pb=b'\n.google/iam/credentials/v1/iamcredentials.proto\x12\x19google.iam.credentials.v1\x1a\x1cgoogle/api/annotations.proto\x1a&google/iam/credentials/v1/common.proto2\xe0\x05\n\x0eIAMCredentials\x12\xcc\x01\n\x13GenerateAccessToken\x12\x35.google.iam.credentials.v1.GenerateAccessTokenRequest\x1a\x36.google.iam.credentials.v1.GenerateAccessTokenResponse\"F\x82\xd3\xe4\x93\x02@\";/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken:\x01*\x12\xbc\x01\n\x0fGenerateIdToken\x12\x31.google.iam.credentials.v1.GenerateIdTokenRequest\x1a\x32.google.iam.credentials.v1.GenerateIdTokenResponse\"B\x82\xd3\xe4\x93\x02<\"7/v1/{name=projects/*/serviceAccounts/*}:generateIdToken:\x01*\x12\xa0\x01\n\x08SignBlob\x12*.google.iam.credentials.v1.SignBlobRequest\x1a+.google.iam.credentials.v1.SignBlobResponse\";\x82\xd3\xe4\x93\x02\x35\"0/v1/{name=projects/*/serviceAccounts/*}:signBlob:\x01*\x12\x9c\x01\n\x07SignJwt\x12).google.iam.credentials.v1.SignJwtRequest\x1a*.google.iam.credentials.v1.SignJwtResponse\":\x82\xd3\xe4\x93\x02\x34\"//v1/{name=projects/*/serviceAccounts/*}:signJwt:\x01*B\x85\x01\n#com.google.cloud.iam.credentials.v1B\x13IAMCredentialsProtoP\x01ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_iam_dot_credentials_dot_v1_dot_common__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_IAMCREDENTIALS = _descriptor.ServiceDescriptor(
  name='IAMCredentials',
  full_name='google.iam.credentials.v1.IAMCredentials',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=148,
  serialized_end=884,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateAccessToken',
    full_name='google.iam.credentials.v1.IAMCredentials.GenerateAccessToken',
    index=0,
    containing_service=None,
    input_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._GENERATEACCESSTOKENREQUEST,
    output_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._GENERATEACCESSTOKENRESPONSE,
    serialized_options=b'\202\323\344\223\002@\";/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GenerateIdToken',
    full_name='google.iam.credentials.v1.IAMCredentials.GenerateIdToken',
    index=1,
    containing_service=None,
    input_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._GENERATEIDTOKENREQUEST,
    output_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._GENERATEIDTOKENRESPONSE,
    serialized_options=b'\202\323\344\223\002<\"7/v1/{name=projects/*/serviceAccounts/*}:generateIdToken:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SignBlob',
    full_name='google.iam.credentials.v1.IAMCredentials.SignBlob',
    index=2,
    containing_service=None,
    input_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._SIGNBLOBREQUEST,
    output_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._SIGNBLOBRESPONSE,
    serialized_options=b'\202\323\344\223\0025\"0/v1/{name=projects/*/serviceAccounts/*}:signBlob:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SignJwt',
    full_name='google.iam.credentials.v1.IAMCredentials.SignJwt',
    index=3,
    containing_service=None,
    input_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._SIGNJWTREQUEST,
    output_type=google_dot_iam_dot_credentials_dot_v1_dot_common__pb2._SIGNJWTRESPONSE,
    serialized_options=b'\202\323\344\223\0024\"//v1/{name=projects/*/serviceAccounts/*}:signJwt:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_IAMCREDENTIALS)

DESCRIPTOR.services_by_name['IAMCredentials'] = _IAMCREDENTIALS

# @@protoc_insertion_point(module_scope)
