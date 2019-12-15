# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/remoteworkers/v1test2/bots.proto

from google.protobuf.internal import enum_type_wrapper
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
from google.devtools.remoteworkers.v1test2 import worker_pb2 as google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_worker__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/remoteworkers/v1test2/bots.proto',
  package='google.devtools.remoteworkers.v1test2',
  syntax='proto3',
  serialized_options=b'\n)com.google.devtools.remoteworkers.v1test2B\021RemoteWorkersBotsP\001ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\242\002\002RW\252\002%Google.DevTools.RemoteWorkers.V1Test2',
  serialized_pb=b'\n0google/devtools/remoteworkers/v1test2/bots.proto\x12%google.devtools.remoteworkers.v1test2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x32google/devtools/remoteworkers/v1test2/worker.proto\x1a\x19google/protobuf/any.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\x86\x03\n\nBotSession\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x62ot_id\x18\x02 \x01(\t\x12@\n\x06status\x18\x03 \x01(\x0e\x32\x30.google.devtools.remoteworkers.v1test2.BotStatus\x12=\n\x06worker\x18\x04 \x01(\x0b\x32-.google.devtools.remoteworkers.v1test2.Worker\x12<\n\x06leases\x18\x05 \x03(\x0b\x32,.google.devtools.remoteworkers.v1test2.Lease\x12/\n\x0b\x65xpire_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x07 \x01(\t:Y\xea\x41V\n\'remoteworkers.googleapis.com/BotSession\x12+{unknown_path=**}/botSessions/{bot_session}\"\x89\x03\n\x05Lease\x12\n\n\x02id\x18\x07 \x01(\t\x12%\n\x07payload\x18\x08 \x01(\x0b\x32\x14.google.protobuf.Any\x12$\n\x06result\x18\t \x01(\x0b\x32\x14.google.protobuf.Any\x12@\n\x05state\x18\x02 \x01(\x0e\x32\x31.google.devtools.remoteworkers.v1test2.LeaseState\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12\x43\n\x0crequirements\x18\x04 \x01(\x0b\x32-.google.devtools.remoteworkers.v1test2.Worker\x12/\n\x0b\x65xpire_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\nassignment\x18\x01 \x01(\tB\x02\x18\x01\x12\x33\n\x11inline_assignment\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyB\x02\x18\x01\"\xc5\x01\n\tAdminTemp\x12I\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\x38.google.devtools.remoteworkers.v1test2.AdminTemp.Command\x12\x0b\n\x03\x61rg\x18\x02 \x01(\t\"`\n\x07\x43ommand\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nBOT_UPDATE\x10\x01\x12\x0f\n\x0b\x42OT_RESTART\x10\x02\x12\x11\n\rBOT_TERMINATE\x10\x03\x12\x10\n\x0cHOST_RESTART\x10\x04\"{\n\x17\x43reateBotSessionRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12K\n\x0b\x62ot_session\x18\x02 \x01(\x0b\x32\x31.google.devtools.remoteworkers.v1test2.BotSessionB\x03\xe0\x41\x02\"\xdb\x01\n\x17UpdateBotSessionRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'remoteworkers.googleapis.com/BotSession\x12K\n\x0b\x62ot_session\x18\x02 \x01(\x0b\x32\x31.google.devtools.remoteworkers.v1test2.BotSessionB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02*y\n\tBotStatus\x12\x1a\n\x16\x42OT_STATUS_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\r\n\tUNHEALTHY\x10\x02\x12\x12\n\x0eHOST_REBOOTING\x10\x03\x12\x13\n\x0f\x42OT_TERMINATING\x10\x04\x12\x10\n\x0cINITIALIZING\x10\x05*`\n\nLeaseState\x12\x1b\n\x17LEASE_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\r\n\tCOMPLETED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x32\xd9\x03\n\x04\x42ots\x12\xd1\x01\n\x10\x43reateBotSession\x12>.google.devtools.remoteworkers.v1test2.CreateBotSessionRequest\x1a\x31.google.devtools.remoteworkers.v1test2.BotSession\"J\x82\xd3\xe4\x93\x02/\" /v1test2/{parent=**}/botSessions:\x0b\x62ot_session\xda\x41\x12parent,bot_session\x12\xdb\x01\n\x10UpdateBotSession\x12>.google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest\x1a\x31.google.devtools.remoteworkers.v1test2.BotSession\"T\x82\xd3\xe4\x93\x02/2 /v1test2/{name=**/botSessions/*}:\x0b\x62ot_session\xda\x41\x1cname,bot_session,update_mask\x1a\x1f\xca\x41\x1cremoteworkers.googleapis.comB\xc1\x01\n)com.google.devtools.remoteworkers.v1test2B\x11RemoteWorkersBotsP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_worker__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])

_BOTSTATUS = _descriptor.EnumDescriptor(
  name='BotStatus',
  full_name='google.devtools.remoteworkers.v1test2.BotStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOT_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNHEALTHY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_REBOOTING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_TERMINATING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1713,
  serialized_end=1834,
)
_sym_db.RegisterEnumDescriptor(_BOTSTATUS)

BotStatus = enum_type_wrapper.EnumTypeWrapper(_BOTSTATUS)
_LEASESTATE = _descriptor.EnumDescriptor(
  name='LeaseState',
  full_name='google.devtools.remoteworkers.v1test2.LeaseState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEASE_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1836,
  serialized_end=1932,
)
_sym_db.RegisterEnumDescriptor(_LEASESTATE)

LeaseState = enum_type_wrapper.EnumTypeWrapper(_LEASESTATE)
BOT_STATUS_UNSPECIFIED = 0
OK = 1
UNHEALTHY = 2
HOST_REBOOTING = 3
BOT_TERMINATING = 4
INITIALIZING = 5
LEASE_STATE_UNSPECIFIED = 0
PENDING = 1
ACTIVE = 2
COMPLETED = 4
CANCELLED = 5


_ADMINTEMP_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='google.devtools.remoteworkers.v1test2.AdminTemp.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_UPDATE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_RESTART', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_TERMINATE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_RESTART', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1268,
  serialized_end=1364,
)
_sym_db.RegisterEnumDescriptor(_ADMINTEMP_COMMAND)


_BOTSESSION = _descriptor.Descriptor(
  name='BotSession',
  full_name='google.devtools.remoteworkers.v1test2.BotSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.BotSession.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='google.devtools.remoteworkers.v1test2.BotSession.bot_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.devtools.remoteworkers.v1test2.BotSession.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker', full_name='google.devtools.remoteworkers.v1test2.BotSession.worker', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leases', full_name='google.devtools.remoteworkers.v1test2.BotSession.leases', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='google.devtools.remoteworkers.v1test2.BotSession.expire_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.devtools.remoteworkers.v1test2.BotSession.version', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\352AV\n\'remoteworkers.googleapis.com/BotSession\022+{unknown_path=**}/botSessions/{bot_session}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=768,
)


_LEASE = _descriptor.Descriptor(
  name='Lease',
  full_name='google.devtools.remoteworkers.v1test2.Lease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.remoteworkers.v1test2.Lease.id', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.devtools.remoteworkers.v1test2.Lease.payload', index=1,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='google.devtools.remoteworkers.v1test2.Lease.result', index=2,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.devtools.remoteworkers.v1test2.Lease.state', index=3,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.devtools.remoteworkers.v1test2.Lease.status', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirements', full_name='google.devtools.remoteworkers.v1test2.Lease.requirements', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='google.devtools.remoteworkers.v1test2.Lease.expire_time', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignment', full_name='google.devtools.remoteworkers.v1test2.Lease.assignment', index=7,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inline_assignment', full_name='google.devtools.remoteworkers.v1test2.Lease.inline_assignment', index=8,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
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
  serialized_start=771,
  serialized_end=1164,
)


_ADMINTEMP = _descriptor.Descriptor(
  name='AdminTemp',
  full_name='google.devtools.remoteworkers.v1test2.AdminTemp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='google.devtools.remoteworkers.v1test2.AdminTemp.command', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg', full_name='google.devtools.remoteworkers.v1test2.AdminTemp.arg', index=1,
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
    _ADMINTEMP_COMMAND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1167,
  serialized_end=1364,
)


_CREATEBOTSESSIONREQUEST = _descriptor.Descriptor(
  name='CreateBotSessionRequest',
  full_name='google.devtools.remoteworkers.v1test2.CreateBotSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.devtools.remoteworkers.v1test2.CreateBotSessionRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_session', full_name='google.devtools.remoteworkers.v1test2.CreateBotSessionRequest.bot_session', index=1,
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
  serialized_start=1366,
  serialized_end=1489,
)


_UPDATEBOTSESSIONREQUEST = _descriptor.Descriptor(
  name='UpdateBotSessionRequest',
  full_name='google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A)\n\'remoteworkers.googleapis.com/BotSession', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_session', full_name='google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest.bot_session', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1492,
  serialized_end=1711,
)

_BOTSESSION.fields_by_name['status'].enum_type = _BOTSTATUS
_BOTSESSION.fields_by_name['worker'].message_type = google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_worker__pb2._WORKER
_BOTSESSION.fields_by_name['leases'].message_type = _LEASE
_BOTSESSION.fields_by_name['expire_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LEASE.fields_by_name['payload'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_LEASE.fields_by_name['result'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_LEASE.fields_by_name['state'].enum_type = _LEASESTATE
_LEASE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LEASE.fields_by_name['requirements'].message_type = google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_worker__pb2._WORKER
_LEASE.fields_by_name['expire_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LEASE.fields_by_name['inline_assignment'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ADMINTEMP.fields_by_name['command'].enum_type = _ADMINTEMP_COMMAND
_ADMINTEMP_COMMAND.containing_type = _ADMINTEMP
_CREATEBOTSESSIONREQUEST.fields_by_name['bot_session'].message_type = _BOTSESSION
_UPDATEBOTSESSIONREQUEST.fields_by_name['bot_session'].message_type = _BOTSESSION
_UPDATEBOTSESSIONREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['BotSession'] = _BOTSESSION
DESCRIPTOR.message_types_by_name['Lease'] = _LEASE
DESCRIPTOR.message_types_by_name['AdminTemp'] = _ADMINTEMP
DESCRIPTOR.message_types_by_name['CreateBotSessionRequest'] = _CREATEBOTSESSIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateBotSessionRequest'] = _UPDATEBOTSESSIONREQUEST
DESCRIPTOR.enum_types_by_name['BotStatus'] = _BOTSTATUS
DESCRIPTOR.enum_types_by_name['LeaseState'] = _LEASESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BotSession = _reflection.GeneratedProtocolMessageType('BotSession', (_message.Message,), {
  'DESCRIPTOR' : _BOTSESSION,
  '__module__' : 'google.devtools.remoteworkers.v1test2.bots_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.BotSession)
  })
_sym_db.RegisterMessage(BotSession)

Lease = _reflection.GeneratedProtocolMessageType('Lease', (_message.Message,), {
  'DESCRIPTOR' : _LEASE,
  '__module__' : 'google.devtools.remoteworkers.v1test2.bots_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.Lease)
  })
_sym_db.RegisterMessage(Lease)

AdminTemp = _reflection.GeneratedProtocolMessageType('AdminTemp', (_message.Message,), {
  'DESCRIPTOR' : _ADMINTEMP,
  '__module__' : 'google.devtools.remoteworkers.v1test2.bots_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.AdminTemp)
  })
_sym_db.RegisterMessage(AdminTemp)

CreateBotSessionRequest = _reflection.GeneratedProtocolMessageType('CreateBotSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOTSESSIONREQUEST,
  '__module__' : 'google.devtools.remoteworkers.v1test2.bots_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.CreateBotSessionRequest)
  })
_sym_db.RegisterMessage(CreateBotSessionRequest)

UpdateBotSessionRequest = _reflection.GeneratedProtocolMessageType('UpdateBotSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBOTSESSIONREQUEST,
  '__module__' : 'google.devtools.remoteworkers.v1test2.bots_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest)
  })
_sym_db.RegisterMessage(UpdateBotSessionRequest)


DESCRIPTOR._options = None
_BOTSESSION._options = None
_LEASE.fields_by_name['assignment']._options = None
_LEASE.fields_by_name['inline_assignment']._options = None
_CREATEBOTSESSIONREQUEST.fields_by_name['parent']._options = None
_CREATEBOTSESSIONREQUEST.fields_by_name['bot_session']._options = None
_UPDATEBOTSESSIONREQUEST.fields_by_name['name']._options = None
_UPDATEBOTSESSIONREQUEST.fields_by_name['bot_session']._options = None
_UPDATEBOTSESSIONREQUEST.fields_by_name['update_mask']._options = None

_BOTS = _descriptor.ServiceDescriptor(
  name='Bots',
  full_name='google.devtools.remoteworkers.v1test2.Bots',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\034remoteworkers.googleapis.com',
  serialized_start=1935,
  serialized_end=2408,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBotSession',
    full_name='google.devtools.remoteworkers.v1test2.Bots.CreateBotSession',
    index=0,
    containing_service=None,
    input_type=_CREATEBOTSESSIONREQUEST,
    output_type=_BOTSESSION,
    serialized_options=b'\202\323\344\223\002/\" /v1test2/{parent=**}/botSessions:\013bot_session\332A\022parent,bot_session',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBotSession',
    full_name='google.devtools.remoteworkers.v1test2.Bots.UpdateBotSession',
    index=1,
    containing_service=None,
    input_type=_UPDATEBOTSESSIONREQUEST,
    output_type=_BOTSESSION,
    serialized_options=b'\202\323\344\223\002/2 /v1test2/{name=**/botSessions/*}:\013bot_session\332A\034name,bot_session,update_mask',
  ),
])
_sym_db.RegisterServiceDescriptor(_BOTS)

DESCRIPTOR.services_by_name['Bots'] = _BOTS

# @@protoc_insertion_point(module_scope)