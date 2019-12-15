# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/datasets.proto

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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/genomics/v1/datasets.proto',
  package='google.genomics.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.google.genomics.v1B\rDatasetsProtoP\001Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\370\001\001',
  serialized_pb=b'\n!google/genomics/v1/datasets.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"h\n\x07\x44\x61taset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"P\n\x13ListDatasetsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"^\n\x14ListDatasetsResponse\x12-\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32\x1b.google.genomics.v1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"D\n\x14\x43reateDatasetRequest\x12,\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32\x1b.google.genomics.v1.Dataset\"\x89\x01\n\x14UpdateDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12,\n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32\x1b.google.genomics.v1.Dataset\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"*\n\x14\x44\x65leteDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\",\n\x16UndeleteDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\"\'\n\x11GetDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t2\x9f\t\n\x10\x44\x61tasetServiceV1\x12w\n\x0cListDatasets\x12\'.google.genomics.v1.ListDatasetsRequest\x1a(.google.genomics.v1.ListDatasetsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/datasets\x12u\n\rCreateDataset\x12(.google.genomics.v1.CreateDatasetRequest\x1a\x1b.google.genomics.v1.Dataset\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x0c/v1/datasets:\x07\x64\x61taset\x12s\n\nGetDataset\x12%.google.genomics.v1.GetDatasetRequest\x1a\x1b.google.genomics.v1.Dataset\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/datasets/{dataset_id}\x12\x82\x01\n\rUpdateDataset\x12(.google.genomics.v1.UpdateDatasetRequest\x1a\x1b.google.genomics.v1.Dataset\"*\x82\xd3\xe4\x93\x02$2\x19/v1/datasets/{dataset_id}:\x07\x64\x61taset\x12t\n\rDeleteDataset\x12(.google.genomics.v1.DeleteDatasetRequest\x1a\x16.google.protobuf.Empty\"!\x82\xd3\xe4\x93\x02\x1b*\x19/v1/datasets/{dataset_id}\x12\x89\x01\n\x0fUndeleteDataset\x12*.google.genomics.v1.UndeleteDatasetRequest\x1a\x1b.google.genomics.v1.Dataset\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/datasets/{dataset_id}:undelete:\x01*\x12|\n\x0cSetIamPolicy\x12\".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"1\x82\xd3\xe4\x93\x02+\"&/v1/{resource=datasets/*}:setIamPolicy:\x01*\x12|\n\x0cGetIamPolicy\x12\".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"1\x82\xd3\xe4\x93\x02+\"&/v1/{resource=datasets/*}:getIamPolicy:\x01*\x12\xa2\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse\"7\x82\xd3\xe4\x93\x02\x31\",/v1/{resource=datasets/*}:testIamPermissions:\x01*Bh\n\x16\x63om.google.genomics.v1B\rDatasetsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_iam__policy__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='google.genomics.v1.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.genomics.v1.Dataset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.genomics.v1.Dataset.project_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.genomics.v1.Dataset.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.genomics.v1.Dataset.create_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=243,
  serialized_end=347,
)


_LISTDATASETSREQUEST = _descriptor.Descriptor(
  name='ListDatasetsRequest',
  full_name='google.genomics.v1.ListDatasetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.genomics.v1.ListDatasetsRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.genomics.v1.ListDatasetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.genomics.v1.ListDatasetsRequest.page_token', index=2,
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
  serialized_start=349,
  serialized_end=429,
)


_LISTDATASETSRESPONSE = _descriptor.Descriptor(
  name='ListDatasetsResponse',
  full_name='google.genomics.v1.ListDatasetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datasets', full_name='google.genomics.v1.ListDatasetsResponse.datasets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.genomics.v1.ListDatasetsResponse.next_page_token', index=1,
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
  serialized_start=431,
  serialized_end=525,
)


_CREATEDATASETREQUEST = _descriptor.Descriptor(
  name='CreateDatasetRequest',
  full_name='google.genomics.v1.CreateDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset', full_name='google.genomics.v1.CreateDatasetRequest.dataset', index=0,
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
  serialized_start=527,
  serialized_end=595,
)


_UPDATEDATASETREQUEST = _descriptor.Descriptor(
  name='UpdateDatasetRequest',
  full_name='google.genomics.v1.UpdateDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.genomics.v1.UpdateDatasetRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='google.genomics.v1.UpdateDatasetRequest.dataset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.genomics.v1.UpdateDatasetRequest.update_mask', index=2,
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
  serialized_start=598,
  serialized_end=735,
)


_DELETEDATASETREQUEST = _descriptor.Descriptor(
  name='DeleteDatasetRequest',
  full_name='google.genomics.v1.DeleteDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.genomics.v1.DeleteDatasetRequest.dataset_id', index=0,
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
  serialized_start=737,
  serialized_end=779,
)


_UNDELETEDATASETREQUEST = _descriptor.Descriptor(
  name='UndeleteDatasetRequest',
  full_name='google.genomics.v1.UndeleteDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.genomics.v1.UndeleteDatasetRequest.dataset_id', index=0,
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
  serialized_start=781,
  serialized_end=825,
)


_GETDATASETREQUEST = _descriptor.Descriptor(
  name='GetDatasetRequest',
  full_name='google.genomics.v1.GetDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.genomics.v1.GetDatasetRequest.dataset_id', index=0,
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
  serialized_start=827,
  serialized_end=866,
)

_DATASET.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTDATASETSRESPONSE.fields_by_name['datasets'].message_type = _DATASET
_CREATEDATASETREQUEST.fields_by_name['dataset'].message_type = _DATASET
_UPDATEDATASETREQUEST.fields_by_name['dataset'].message_type = _DATASET
_UPDATEDATASETREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['ListDatasetsRequest'] = _LISTDATASETSREQUEST
DESCRIPTOR.message_types_by_name['ListDatasetsResponse'] = _LISTDATASETSRESPONSE
DESCRIPTOR.message_types_by_name['CreateDatasetRequest'] = _CREATEDATASETREQUEST
DESCRIPTOR.message_types_by_name['UpdateDatasetRequest'] = _UPDATEDATASETREQUEST
DESCRIPTOR.message_types_by_name['DeleteDatasetRequest'] = _DELETEDATASETREQUEST
DESCRIPTOR.message_types_by_name['UndeleteDatasetRequest'] = _UNDELETEDATASETREQUEST
DESCRIPTOR.message_types_by_name['GetDatasetRequest'] = _GETDATASETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

ListDatasetsRequest = _reflection.GeneratedProtocolMessageType('ListDatasetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATASETSREQUEST,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ListDatasetsRequest)
  })
_sym_db.RegisterMessage(ListDatasetsRequest)

ListDatasetsResponse = _reflection.GeneratedProtocolMessageType('ListDatasetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATASETSRESPONSE,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ListDatasetsResponse)
  })
_sym_db.RegisterMessage(ListDatasetsResponse)

CreateDatasetRequest = _reflection.GeneratedProtocolMessageType('CreateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETREQUEST,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.CreateDatasetRequest)
  })
_sym_db.RegisterMessage(CreateDatasetRequest)

UpdateDatasetRequest = _reflection.GeneratedProtocolMessageType('UpdateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETREQUEST,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.UpdateDatasetRequest)
  })
_sym_db.RegisterMessage(UpdateDatasetRequest)

DeleteDatasetRequest = _reflection.GeneratedProtocolMessageType('DeleteDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETREQUEST,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.DeleteDatasetRequest)
  })
_sym_db.RegisterMessage(DeleteDatasetRequest)

UndeleteDatasetRequest = _reflection.GeneratedProtocolMessageType('UndeleteDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNDELETEDATASETREQUEST,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.UndeleteDatasetRequest)
  })
_sym_db.RegisterMessage(UndeleteDatasetRequest)

GetDatasetRequest = _reflection.GeneratedProtocolMessageType('GetDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETREQUEST,
  '__module__' : 'google.genomics.v1.datasets_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.GetDatasetRequest)
  })
_sym_db.RegisterMessage(GetDatasetRequest)


DESCRIPTOR._options = None

_DATASETSERVICEV1 = _descriptor.ServiceDescriptor(
  name='DatasetServiceV1',
  full_name='google.genomics.v1.DatasetServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=869,
  serialized_end=2052,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListDatasets',
    full_name='google.genomics.v1.DatasetServiceV1.ListDatasets',
    index=0,
    containing_service=None,
    input_type=_LISTDATASETSREQUEST,
    output_type=_LISTDATASETSRESPONSE,
    serialized_options=b'\202\323\344\223\002\016\022\014/v1/datasets',
  ),
  _descriptor.MethodDescriptor(
    name='CreateDataset',
    full_name='google.genomics.v1.DatasetServiceV1.CreateDataset',
    index=1,
    containing_service=None,
    input_type=_CREATEDATASETREQUEST,
    output_type=_DATASET,
    serialized_options=b'\202\323\344\223\002\027\"\014/v1/datasets:\007dataset',
  ),
  _descriptor.MethodDescriptor(
    name='GetDataset',
    full_name='google.genomics.v1.DatasetServiceV1.GetDataset',
    index=2,
    containing_service=None,
    input_type=_GETDATASETREQUEST,
    output_type=_DATASET,
    serialized_options=b'\202\323\344\223\002\033\022\031/v1/datasets/{dataset_id}',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateDataset',
    full_name='google.genomics.v1.DatasetServiceV1.UpdateDataset',
    index=3,
    containing_service=None,
    input_type=_UPDATEDATASETREQUEST,
    output_type=_DATASET,
    serialized_options=b'\202\323\344\223\002$2\031/v1/datasets/{dataset_id}:\007dataset',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteDataset',
    full_name='google.genomics.v1.DatasetServiceV1.DeleteDataset',
    index=4,
    containing_service=None,
    input_type=_DELETEDATASETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\033*\031/v1/datasets/{dataset_id}',
  ),
  _descriptor.MethodDescriptor(
    name='UndeleteDataset',
    full_name='google.genomics.v1.DatasetServiceV1.UndeleteDataset',
    index=5,
    containing_service=None,
    input_type=_UNDELETEDATASETREQUEST,
    output_type=_DATASET,
    serialized_options=b'\202\323\344\223\002\'\"\"/v1/datasets/{dataset_id}:undelete:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SetIamPolicy',
    full_name='google.genomics.v1.DatasetServiceV1.SetIamPolicy',
    index=6,
    containing_service=None,
    input_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._SETIAMPOLICYREQUEST,
    output_type=google_dot_iam_dot_v1_dot_policy__pb2._POLICY,
    serialized_options=b'\202\323\344\223\002+\"&/v1/{resource=datasets/*}:setIamPolicy:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GetIamPolicy',
    full_name='google.genomics.v1.DatasetServiceV1.GetIamPolicy',
    index=7,
    containing_service=None,
    input_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._GETIAMPOLICYREQUEST,
    output_type=google_dot_iam_dot_v1_dot_policy__pb2._POLICY,
    serialized_options=b'\202\323\344\223\002+\"&/v1/{resource=datasets/*}:getIamPolicy:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='TestIamPermissions',
    full_name='google.genomics.v1.DatasetServiceV1.TestIamPermissions',
    index=8,
    containing_service=None,
    input_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._TESTIAMPERMISSIONSREQUEST,
    output_type=google_dot_iam_dot_v1_dot_iam__policy__pb2._TESTIAMPERMISSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\0021\",/v1/{resource=datasets/*}:testIamPermissions:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASETSERVICEV1)

DESCRIPTOR.services_by_name['DatasetServiceV1'] = _DATASETSERVICEV1

# @@protoc_insertion_point(module_scope)