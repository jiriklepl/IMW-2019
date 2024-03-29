# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/remoteworkers/v1test2/tasks.proto

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
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/remoteworkers/v1test2/tasks.proto',
  package='google.devtools.remoteworkers.v1test2',
  syntax='proto3',
  serialized_options=b'\n)com.google.devtools.remoteworkers.v1test2B\022RemoteWorkersTasksP\001ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\242\002\002RW\252\002%Google.DevTools.RemoteWorkers.V1Test2',
  serialized_pb=b'\n1google/devtools/remoteworkers/v1test2/tasks.proto\x12%google.devtools.remoteworkers.v1test2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x19google/protobuf/any.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"\xf9\x01\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x43\n\x04logs\x18\x03 \x03(\x0b\x32\x35.google.devtools.remoteworkers.v1test2.Task.LogsEntry\x1a+\n\tLogsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:F\xea\x41\x43\n!remoteworkers.googleapis.com/Task\x12\x1e{unknown_path=**}/tasks/{task}\"\xef\x01\n\nTaskResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63omplete\x18\x02 \x01(\x08\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12$\n\x06output\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12\"\n\x04meta\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any:S\xea\x41P\n\'remoteworkers.googleapis.com/TaskResult\x12%{unknown_path=**}/tasks/{task}/result\"I\n\x0eGetTaskRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!remoteworkers.googleapis.com/Task\"\xeb\x01\n\x17UpdateTaskResultRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'remoteworkers.googleapis.com/TaskResult\x12\x46\n\x06result\x18\x02 \x01(\x0b\x32\x31.google.devtools.remoteworkers.v1test2.TaskResultB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02\x12\x13\n\x06source\x18\x04 \x01(\tB\x03\xe0\x41\x02\"a\n\x11\x41\x64\x64TaskLogRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!remoteworkers.googleapis.com/Task\x12\x13\n\x06log_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\"$\n\x12\x41\x64\x64TaskLogResponse\x12\x0e\n\x06handle\x18\x01 \x01(\t2\xdf\x04\n\x05Tasks\x12\x98\x01\n\x07GetTask\x12\x35.google.devtools.remoteworkers.v1test2.GetTaskRequest\x1a+.google.devtools.remoteworkers.v1test2.Task\")\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1test2/{name=**/tasks/*}\xda\x41\x04name\x12\xd9\x01\n\x10UpdateTaskResult\x12>.google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest\x1a\x31.google.devtools.remoteworkers.v1test2.TaskResult\"R\x82\xd3\xe4\x93\x02+2!/v1test2/{name=**/tasks/*/result}:\x06result\xda\x41\x1ename,result,update_mask,source\x12\xbd\x01\n\nAddTaskLog\x12\x38.google.devtools.remoteworkers.v1test2.AddTaskLogRequest\x1a\x39.google.devtools.remoteworkers.v1test2.AddTaskLogResponse\":\x82\xd3\xe4\x93\x02&\"!/v1test2/{name=**/tasks/*}:addLog:\x01*\xda\x41\x0bname,log_id\x1a\x1f\xca\x41\x1cremoteworkers.googleapis.comB\xc2\x01\n)com.google.devtools.remoteworkers.v1test2B\x12RemoteWorkersTasksP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_TASK_LOGSENTRY = _descriptor.Descriptor(
  name='LogsEntry',
  full_name='google.devtools.remoteworkers.v1test2.Task.LogsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.remoteworkers.v1test2.Task.LogsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.remoteworkers.v1test2.Task.LogsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=471,
)

_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='google.devtools.remoteworkers.v1test2.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.Task.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.devtools.remoteworkers.v1test2.Task.description', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='google.devtools.remoteworkers.v1test2.Task.logs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_LOGSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\352AC\n!remoteworkers.googleapis.com/Task\022\036{unknown_path=**}/tasks/{task}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=543,
)


_TASKRESULT = _descriptor.Descriptor(
  name='TaskResult',
  full_name='google.devtools.remoteworkers.v1test2.TaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.TaskResult.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='complete', full_name='google.devtools.remoteworkers.v1test2.TaskResult.complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.devtools.remoteworkers.v1test2.TaskResult.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='google.devtools.remoteworkers.v1test2.TaskResult.output', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='google.devtools.remoteworkers.v1test2.TaskResult.meta', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\352AP\n\'remoteworkers.googleapis.com/TaskResult\022%{unknown_path=**}/tasks/{task}/result',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=785,
)


_GETTASKREQUEST = _descriptor.Descriptor(
  name='GetTaskRequest',
  full_name='google.devtools.remoteworkers.v1test2.GetTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.GetTaskRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A#\n!remoteworkers.googleapis.com/Task', file=DESCRIPTOR),
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
  serialized_start=787,
  serialized_end=860,
)


_UPDATETASKRESULTREQUEST = _descriptor.Descriptor(
  name='UpdateTaskResultRequest',
  full_name='google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A)\n\'remoteworkers.googleapis.com/TaskResult', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=863,
  serialized_end=1098,
)


_ADDTASKLOGREQUEST = _descriptor.Descriptor(
  name='AddTaskLogRequest',
  full_name='google.devtools.remoteworkers.v1test2.AddTaskLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.remoteworkers.v1test2.AddTaskLogRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A#\n!remoteworkers.googleapis.com/Task', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_id', full_name='google.devtools.remoteworkers.v1test2.AddTaskLogRequest.log_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1100,
  serialized_end=1197,
)


_ADDTASKLOGRESPONSE = _descriptor.Descriptor(
  name='AddTaskLogResponse',
  full_name='google.devtools.remoteworkers.v1test2.AddTaskLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='google.devtools.remoteworkers.v1test2.AddTaskLogResponse.handle', index=0,
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
  serialized_start=1199,
  serialized_end=1235,
)

_TASK_LOGSENTRY.containing_type = _TASK
_TASK.fields_by_name['description'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TASK.fields_by_name['logs'].message_type = _TASK_LOGSENTRY
_TASKRESULT.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_TASKRESULT.fields_by_name['output'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TASKRESULT.fields_by_name['meta'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_UPDATETASKRESULTREQUEST.fields_by_name['result'].message_type = _TASKRESULT
_UPDATETASKRESULTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TaskResult'] = _TASKRESULT
DESCRIPTOR.message_types_by_name['GetTaskRequest'] = _GETTASKREQUEST
DESCRIPTOR.message_types_by_name['UpdateTaskResultRequest'] = _UPDATETASKRESULTREQUEST
DESCRIPTOR.message_types_by_name['AddTaskLogRequest'] = _ADDTASKLOGREQUEST
DESCRIPTOR.message_types_by_name['AddTaskLogResponse'] = _ADDTASKLOGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {

  'LogsEntry' : _reflection.GeneratedProtocolMessageType('LogsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TASK_LOGSENTRY,
    '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.Task.LogsEntry)
    })
  ,
  'DESCRIPTOR' : _TASK,
  '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.Task)
  })
_sym_db.RegisterMessage(Task)
_sym_db.RegisterMessage(Task.LogsEntry)

TaskResult = _reflection.GeneratedProtocolMessageType('TaskResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESULT,
  '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.TaskResult)
  })
_sym_db.RegisterMessage(TaskResult)

GetTaskRequest = _reflection.GeneratedProtocolMessageType('GetTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKREQUEST,
  '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.GetTaskRequest)
  })
_sym_db.RegisterMessage(GetTaskRequest)

UpdateTaskResultRequest = _reflection.GeneratedProtocolMessageType('UpdateTaskResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETASKRESULTREQUEST,
  '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.UpdateTaskResultRequest)
  })
_sym_db.RegisterMessage(UpdateTaskResultRequest)

AddTaskLogRequest = _reflection.GeneratedProtocolMessageType('AddTaskLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDTASKLOGREQUEST,
  '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.AddTaskLogRequest)
  })
_sym_db.RegisterMessage(AddTaskLogRequest)

AddTaskLogResponse = _reflection.GeneratedProtocolMessageType('AddTaskLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDTASKLOGRESPONSE,
  '__module__' : 'google.devtools.remoteworkers.v1test2.tasks_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.remoteworkers.v1test2.AddTaskLogResponse)
  })
_sym_db.RegisterMessage(AddTaskLogResponse)


DESCRIPTOR._options = None
_TASK_LOGSENTRY._options = None
_TASK._options = None
_TASKRESULT._options = None
_GETTASKREQUEST.fields_by_name['name']._options = None
_UPDATETASKRESULTREQUEST.fields_by_name['name']._options = None
_UPDATETASKRESULTREQUEST.fields_by_name['result']._options = None
_UPDATETASKRESULTREQUEST.fields_by_name['update_mask']._options = None
_UPDATETASKRESULTREQUEST.fields_by_name['source']._options = None
_ADDTASKLOGREQUEST.fields_by_name['name']._options = None
_ADDTASKLOGREQUEST.fields_by_name['log_id']._options = None

_TASKS = _descriptor.ServiceDescriptor(
  name='Tasks',
  full_name='google.devtools.remoteworkers.v1test2.Tasks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\034remoteworkers.googleapis.com',
  serialized_start=1238,
  serialized_end=1845,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTask',
    full_name='google.devtools.remoteworkers.v1test2.Tasks.GetTask',
    index=0,
    containing_service=None,
    input_type=_GETTASKREQUEST,
    output_type=_TASK,
    serialized_options=b'\202\323\344\223\002\034\022\032/v1test2/{name=**/tasks/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTaskResult',
    full_name='google.devtools.remoteworkers.v1test2.Tasks.UpdateTaskResult',
    index=1,
    containing_service=None,
    input_type=_UPDATETASKRESULTREQUEST,
    output_type=_TASKRESULT,
    serialized_options=b'\202\323\344\223\002+2!/v1test2/{name=**/tasks/*/result}:\006result\332A\036name,result,update_mask,source',
  ),
  _descriptor.MethodDescriptor(
    name='AddTaskLog',
    full_name='google.devtools.remoteworkers.v1test2.Tasks.AddTaskLog',
    index=2,
    containing_service=None,
    input_type=_ADDTASKLOGREQUEST,
    output_type=_ADDTASKLOGRESPONSE,
    serialized_options=b'\202\323\344\223\002&\"!/v1test2/{name=**/tasks/*}:addLog:\001*\332A\013name,log_id',
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKS)

DESCRIPTOR.services_by_name['Tasks'] = _TASKS

# @@protoc_insertion_point(module_scope)
