# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/admin/table/v1/bigtable_table_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.bigtable.admin.table.v1 import bigtable_table_data_pb2 as google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2
from google.bigtable.admin.table.v1 import bigtable_table_service_messages_pb2 as google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bigtable/admin/table/v1/bigtable_table_service.proto',
  package='google.bigtable.admin.table.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.bigtable.admin.table.v1B\032BigtableTableServicesProtoP\001ZCgoogle.golang.org/genproto/googleapis/bigtable/admin/table/v1;table',
  serialized_pb=b'\n;google/bigtable/admin/table/v1/bigtable_table_service.proto\x12\x1egoogle.bigtable.admin.table.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x38google/bigtable/admin/table/v1/bigtable_table_data.proto\x1a\x44google/bigtable/admin/table/v1/bigtable_table_service_messages.proto\x1a\x1bgoogle/protobuf/empty.proto2\xbe\x0c\n\x14\x42igtableTableService\x12\xa4\x01\n\x0b\x43reateTable\x12\x32.google.bigtable.admin.table.v1.CreateTableRequest\x1a%.google.bigtable.admin.table.v1.Table\":\x82\xd3\xe4\x93\x02\x34\"//v1/{name=projects/*/zones/*/clusters/*}/tables:\x01*\x12\xac\x01\n\nListTables\x12\x31.google.bigtable.admin.table.v1.ListTablesRequest\x1a\x32.google.bigtable.admin.table.v1.ListTablesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//v1/{name=projects/*/zones/*/clusters/*}/tables\x12\x9d\x01\n\x08GetTable\x12/.google.bigtable.admin.table.v1.GetTableRequest\x1a%.google.bigtable.admin.table.v1.Table\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/{name=projects/*/zones/*/clusters/*/tables/*}\x12\x94\x01\n\x0b\x44\x65leteTable\x12\x32.google.bigtable.admin.table.v1.DeleteTableRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v1/{name=projects/*/zones/*/clusters/*/tables/*}\x12\x9e\x01\n\x0bRenameTable\x12\x32.google.bigtable.admin.table.v1.RenameTableRequest\x1a\x16.google.protobuf.Empty\"C\x82\xd3\xe4\x93\x02=\"8/v1/{name=projects/*/zones/*/clusters/*/tables/*}:rename:\x01*\x12\xca\x01\n\x12\x43reateColumnFamily\x12\x39.google.bigtable.admin.table.v1.CreateColumnFamilyRequest\x1a,.google.bigtable.admin.table.v1.ColumnFamily\"K\x82\xd3\xe4\x93\x02\x45\"@/v1/{name=projects/*/zones/*/clusters/*/tables/*}/columnFamilies:\x01*\x12\xbf\x01\n\x12UpdateColumnFamily\x12,.google.bigtable.admin.table.v1.ColumnFamily\x1a,.google.bigtable.admin.table.v1.ColumnFamily\"M\x82\xd3\xe4\x93\x02G\x1a\x42/v1/{name=projects/*/zones/*/clusters/*/tables/*/columnFamilies/*}:\x01*\x12\xb3\x01\n\x12\x44\x65leteColumnFamily\x12\x39.google.bigtable.admin.table.v1.DeleteColumnFamilyRequest\x1a\x16.google.protobuf.Empty\"J\x82\xd3\xe4\x93\x02\x44*B/v1/{name=projects/*/zones/*/clusters/*/tables/*/columnFamilies/*}\x12\xb2\x01\n\x0e\x42ulkDeleteRows\x12\x35.google.bigtable.admin.table.v1.BulkDeleteRowsRequest\x1a\x16.google.protobuf.Empty\"Q\x82\xd3\xe4\x93\x02K\"F/v1/{table_name=projects/*/zones/*/clusters/*/tables/*}:bulkDeleteRows:\x01*B\x87\x01\n\"com.google.bigtable.admin.table.v1B\x1a\x42igtableTableServicesProtoP\x01ZCgoogle.golang.org/genproto/googleapis/bigtable/admin/table/v1;tableb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2.DESCRIPTOR,google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_BIGTABLETABLESERVICE = _descriptor.ServiceDescriptor(
  name='BigtableTableService',
  full_name='google.bigtable.admin.table.v1.BigtableTableService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=283,
  serialized_end=1881,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTable',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.CreateTable',
    index=0,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._CREATETABLEREQUEST,
    output_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._TABLE,
    serialized_options=b'\202\323\344\223\0024\"//v1/{name=projects/*/zones/*/clusters/*}/tables:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='ListTables',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.ListTables',
    index=1,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._LISTTABLESREQUEST,
    output_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._LISTTABLESRESPONSE,
    serialized_options=b'\202\323\344\223\0021\022//v1/{name=projects/*/zones/*/clusters/*}/tables',
  ),
  _descriptor.MethodDescriptor(
    name='GetTable',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.GetTable',
    index=2,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._GETTABLEREQUEST,
    output_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._TABLE,
    serialized_options=b'\202\323\344\223\0023\0221/v1/{name=projects/*/zones/*/clusters/*/tables/*}',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTable',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.DeleteTable',
    index=3,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._DELETETABLEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\0023*1/v1/{name=projects/*/zones/*/clusters/*/tables/*}',
  ),
  _descriptor.MethodDescriptor(
    name='RenameTable',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.RenameTable',
    index=4,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._RENAMETABLEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002=\"8/v1/{name=projects/*/zones/*/clusters/*/tables/*}:rename:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='CreateColumnFamily',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.CreateColumnFamily',
    index=5,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._CREATECOLUMNFAMILYREQUEST,
    output_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._COLUMNFAMILY,
    serialized_options=b'\202\323\344\223\002E\"@/v1/{name=projects/*/zones/*/clusters/*/tables/*}/columnFamilies:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateColumnFamily',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.UpdateColumnFamily',
    index=6,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._COLUMNFAMILY,
    output_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._COLUMNFAMILY,
    serialized_options=b'\202\323\344\223\002G\032B/v1/{name=projects/*/zones/*/clusters/*/tables/*/columnFamilies/*}:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteColumnFamily',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.DeleteColumnFamily',
    index=7,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._DELETECOLUMNFAMILYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002D*B/v1/{name=projects/*/zones/*/clusters/*/tables/*/columnFamilies/*}',
  ),
  _descriptor.MethodDescriptor(
    name='BulkDeleteRows',
    full_name='google.bigtable.admin.table.v1.BigtableTableService.BulkDeleteRows',
    index=8,
    containing_service=None,
    input_type=google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__service__messages__pb2._BULKDELETEROWSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002K\"F/v1/{table_name=projects/*/zones/*/clusters/*/tables/*}:bulkDeleteRows:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_BIGTABLETABLESERVICE)

DESCRIPTOR.services_by_name['BigtableTableService'] = _BIGTABLETABLESERVICE

# @@protoc_insertion_point(module_scope)
