# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/osconfig/v1beta/patch_deployments.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.osconfig.v1beta import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__jobs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/osconfig/v1beta/patch_deployments.proto',
  package='google.cloud.osconfig.v1beta',
  syntax='proto3',
  serialized_options=b'\n com.google.cloud.osconfig.v1betaB\020PatchDeploymentsZDgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1beta;osconfig',
  serialized_pb=b'\n4google/cloud/osconfig/v1beta/patch_deployments.proto\x12\x1cgoogle.cloud.osconfig.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/osconfig/v1beta/patch_jobs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto\"\xdb\x04\n\x0fPatchDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x03\xe0\x41\x01\x12O\n\x0finstance_filter\x18\x03 \x01(\x0b\x32\x31.google.cloud.osconfig.v1beta.PatchInstanceFilterB\x03\xe0\x41\x02\x12\x44\n\x0cpatch_config\x18\x04 \x01(\x0b\x32).google.cloud.osconfig.v1beta.PatchConfigB\x03\xe0\x41\x01\x12\x30\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x03\xe0\x41\x01\x12O\n\x11one_time_schedule\x18\x06 \x01(\x0b\x32-.google.cloud.osconfig.v1beta.OneTimeScheduleB\x03\xe0\x41\x02H\x00\x12R\n\x12recurring_schedule\x18\x07 \x01(\x0b\x32/.google.cloud.osconfig.v1beta.RecurringScheduleB\x03\xe0\x41\x02H\x00\x12\x34\n\x0b\x63reate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x34\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12:\n\x11last_execute_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x42\n\n\x08schedule\"H\n\x0fOneTimeSchedule\x12\x35\n\x0c\x65xecute_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x02\"\x87\x05\n\x11RecurringSchedule\x12-\n\ttime_zone\x18\x01 \x01(\x0b\x32\x15.google.type.TimeZoneB\x03\xe0\x41\x02\x12\x33\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01\x12\x31\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01\x12\x30\n\x0btime_of_day\x18\x04 \x01(\x0b\x32\x16.google.type.TimeOfDayB\x03\xe0\x41\x02\x12Q\n\tfrequency\x18\x05 \x01(\x0e\x32\x39.google.cloud.osconfig.v1beta.RecurringSchedule.FrequencyB\x03\xe0\x41\x02\x12\x43\n\x06weekly\x18\x06 \x01(\x0b\x32,.google.cloud.osconfig.v1beta.WeeklyScheduleB\x03\xe0\x41\x02H\x00\x12\x45\n\x07monthly\x18\x07 \x01(\x0b\x32-.google.cloud.osconfig.v1beta.MonthlyScheduleB\x03\xe0\x41\x02H\x00\x12:\n\x11last_execute_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12:\n\x11next_execute_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\"?\n\tFrequency\x12\x19\n\x15\x46REQUENCY_UNSPECIFIED\x10\x00\x12\n\n\x06WEEKLY\x10\x01\x12\x0b\n\x07MONTHLY\x10\x02\x42\x11\n\x0fschedule_config\"B\n\x0eWeeklySchedule\x12\x30\n\x0b\x64\x61y_of_week\x18\x01 \x01(\x0e\x32\x16.google.type.DayOfWeekB\x03\xe0\x41\x02\"\x8b\x01\n\x0fMonthlySchedule\x12N\n\x11week_day_of_month\x18\x01 \x01(\x0b\x32,.google.cloud.osconfig.v1beta.WeekDayOfMonthB\x03\xe0\x41\x02H\x00\x12\x18\n\tmonth_day\x18\x02 \x01(\x05\x42\x03\xe0\x41\x02H\x00\x42\x0e\n\x0c\x64\x61y_of_month\"]\n\x0eWeekDayOfMonth\x12\x19\n\x0cweek_ordinal\x18\x01 \x01(\x05\x42\x03\xe0\x41\x02\x12\x30\n\x0b\x64\x61y_of_week\x18\x02 \x01(\x0e\x32\x16.google.type.DayOfWeekB\x03\xe0\x41\x02\"\xa3\x01\n\x1c\x43reatePatchDeploymentRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12 \n\x13patch_deployment_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12L\n\x10patch_deployment\x18\x03 \x01(\x0b\x32-.google.cloud.osconfig.v1beta.PatchDeploymentB\x03\xe0\x41\x02\".\n\x19GetPatchDeploymentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\"c\n\x1bListPatchDeploymentsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\"\x81\x01\n\x1cListPatchDeploymentsResponse\x12H\n\x11patch_deployments\x18\x01 \x03(\x0b\x32-.google.cloud.osconfig.v1beta.PatchDeployment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"1\n\x1c\x44\x65letePatchDeploymentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x42z\n com.google.cloud.osconfig.v1betaB\x10PatchDeploymentsZDgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1beta;osconfigb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__jobs__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_type_dot_datetime__pb2.DESCRIPTOR,google_dot_type_dot_dayofweek__pb2.DESCRIPTOR,google_dot_type_dot_timeofday__pb2.DESCRIPTOR,])



_RECURRINGSCHEDULE_FREQUENCY = _descriptor.EnumDescriptor(
  name='Frequency',
  full_name='google.cloud.osconfig.v1beta.RecurringSchedule.Frequency',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FREQUENCY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEEKLY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONTHLY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1590,
  serialized_end=1653,
)
_sym_db.RegisterEnumDescriptor(_RECURRINGSCHEDULE_FREQUENCY)


_PATCHDEPLOYMENT = _descriptor.Descriptor(
  name='PatchDeployment',
  full_name='google.cloud.osconfig.v1beta.PatchDeployment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.osconfig.v1beta.PatchDeployment.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.osconfig.v1beta.PatchDeployment.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_filter', full_name='google.cloud.osconfig.v1beta.PatchDeployment.instance_filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch_config', full_name='google.cloud.osconfig.v1beta.PatchDeployment.patch_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='google.cloud.osconfig.v1beta.PatchDeployment.duration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_time_schedule', full_name='google.cloud.osconfig.v1beta.PatchDeployment.one_time_schedule', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recurring_schedule', full_name='google.cloud.osconfig.v1beta.PatchDeployment.recurring_schedule', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.osconfig.v1beta.PatchDeployment.create_time', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.osconfig.v1beta.PatchDeployment.update_time', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_execute_time', full_name='google.cloud.osconfig.v1beta.PatchDeployment.last_execute_time', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='schedule', full_name='google.cloud.osconfig.v1beta.PatchDeployment.schedule',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=345,
  serialized_end=948,
)


_ONETIMESCHEDULE = _descriptor.Descriptor(
  name='OneTimeSchedule',
  full_name='google.cloud.osconfig.v1beta.OneTimeSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execute_time', full_name='google.cloud.osconfig.v1beta.OneTimeSchedule.execute_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=950,
  serialized_end=1022,
)


_RECURRINGSCHEDULE = _descriptor.Descriptor(
  name='RecurringSchedule',
  full_name='google.cloud.osconfig.v1beta.RecurringSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.time_zone', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.start_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.end_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_of_day', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.time_of_day', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.frequency', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weekly', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.weekly', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monthly', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.monthly', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_execute_time', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.last_execute_time', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_execute_time', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.next_execute_time', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECURRINGSCHEDULE_FREQUENCY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='schedule_config', full_name='google.cloud.osconfig.v1beta.RecurringSchedule.schedule_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1025,
  serialized_end=1672,
)


_WEEKLYSCHEDULE = _descriptor.Descriptor(
  name='WeeklySchedule',
  full_name='google.cloud.osconfig.v1beta.WeeklySchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='google.cloud.osconfig.v1beta.WeeklySchedule.day_of_week', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1674,
  serialized_end=1740,
)


_MONTHLYSCHEDULE = _descriptor.Descriptor(
  name='MonthlySchedule',
  full_name='google.cloud.osconfig.v1beta.MonthlySchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='week_day_of_month', full_name='google.cloud.osconfig.v1beta.MonthlySchedule.week_day_of_month', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month_day', full_name='google.cloud.osconfig.v1beta.MonthlySchedule.month_day', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='day_of_month', full_name='google.cloud.osconfig.v1beta.MonthlySchedule.day_of_month',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1743,
  serialized_end=1882,
)


_WEEKDAYOFMONTH = _descriptor.Descriptor(
  name='WeekDayOfMonth',
  full_name='google.cloud.osconfig.v1beta.WeekDayOfMonth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='week_ordinal', full_name='google.cloud.osconfig.v1beta.WeekDayOfMonth.week_ordinal', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='google.cloud.osconfig.v1beta.WeekDayOfMonth.day_of_week', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1884,
  serialized_end=1977,
)


_CREATEPATCHDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='CreatePatchDeploymentRequest',
  full_name='google.cloud.osconfig.v1beta.CreatePatchDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.osconfig.v1beta.CreatePatchDeploymentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch_deployment_id', full_name='google.cloud.osconfig.v1beta.CreatePatchDeploymentRequest.patch_deployment_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch_deployment', full_name='google.cloud.osconfig.v1beta.CreatePatchDeploymentRequest.patch_deployment', index=2,
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
  serialized_start=1980,
  serialized_end=2143,
)


_GETPATCHDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='GetPatchDeploymentRequest',
  full_name='google.cloud.osconfig.v1beta.GetPatchDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.osconfig.v1beta.GetPatchDeploymentRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=2145,
  serialized_end=2191,
)


_LISTPATCHDEPLOYMENTSREQUEST = _descriptor.Descriptor(
  name='ListPatchDeploymentsRequest',
  full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsRequest.page_token', index=2,
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
  serialized_start=2193,
  serialized_end=2292,
)


_LISTPATCHDEPLOYMENTSRESPONSE = _descriptor.Descriptor(
  name='ListPatchDeploymentsResponse',
  full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='patch_deployments', full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse.patch_deployments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse.next_page_token', index=1,
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
  serialized_start=2295,
  serialized_end=2424,
)


_DELETEPATCHDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='DeletePatchDeploymentRequest',
  full_name='google.cloud.osconfig.v1beta.DeletePatchDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.osconfig.v1beta.DeletePatchDeploymentRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=2426,
  serialized_end=2475,
)

_PATCHDEPLOYMENT.fields_by_name['instance_filter'].message_type = google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__jobs__pb2._PATCHINSTANCEFILTER
_PATCHDEPLOYMENT.fields_by_name['patch_config'].message_type = google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__jobs__pb2._PATCHCONFIG
_PATCHDEPLOYMENT.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PATCHDEPLOYMENT.fields_by_name['one_time_schedule'].message_type = _ONETIMESCHEDULE
_PATCHDEPLOYMENT.fields_by_name['recurring_schedule'].message_type = _RECURRINGSCHEDULE
_PATCHDEPLOYMENT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PATCHDEPLOYMENT.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PATCHDEPLOYMENT.fields_by_name['last_execute_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PATCHDEPLOYMENT.oneofs_by_name['schedule'].fields.append(
  _PATCHDEPLOYMENT.fields_by_name['one_time_schedule'])
_PATCHDEPLOYMENT.fields_by_name['one_time_schedule'].containing_oneof = _PATCHDEPLOYMENT.oneofs_by_name['schedule']
_PATCHDEPLOYMENT.oneofs_by_name['schedule'].fields.append(
  _PATCHDEPLOYMENT.fields_by_name['recurring_schedule'])
_PATCHDEPLOYMENT.fields_by_name['recurring_schedule'].containing_oneof = _PATCHDEPLOYMENT.oneofs_by_name['schedule']
_ONETIMESCHEDULE.fields_by_name['execute_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RECURRINGSCHEDULE.fields_by_name['time_zone'].message_type = google_dot_type_dot_datetime__pb2._TIMEZONE
_RECURRINGSCHEDULE.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RECURRINGSCHEDULE.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RECURRINGSCHEDULE.fields_by_name['time_of_day'].message_type = google_dot_type_dot_timeofday__pb2._TIMEOFDAY
_RECURRINGSCHEDULE.fields_by_name['frequency'].enum_type = _RECURRINGSCHEDULE_FREQUENCY
_RECURRINGSCHEDULE.fields_by_name['weekly'].message_type = _WEEKLYSCHEDULE
_RECURRINGSCHEDULE.fields_by_name['monthly'].message_type = _MONTHLYSCHEDULE
_RECURRINGSCHEDULE.fields_by_name['last_execute_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RECURRINGSCHEDULE.fields_by_name['next_execute_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RECURRINGSCHEDULE_FREQUENCY.containing_type = _RECURRINGSCHEDULE
_RECURRINGSCHEDULE.oneofs_by_name['schedule_config'].fields.append(
  _RECURRINGSCHEDULE.fields_by_name['weekly'])
_RECURRINGSCHEDULE.fields_by_name['weekly'].containing_oneof = _RECURRINGSCHEDULE.oneofs_by_name['schedule_config']
_RECURRINGSCHEDULE.oneofs_by_name['schedule_config'].fields.append(
  _RECURRINGSCHEDULE.fields_by_name['monthly'])
_RECURRINGSCHEDULE.fields_by_name['monthly'].containing_oneof = _RECURRINGSCHEDULE.oneofs_by_name['schedule_config']
_WEEKLYSCHEDULE.fields_by_name['day_of_week'].enum_type = google_dot_type_dot_dayofweek__pb2._DAYOFWEEK
_MONTHLYSCHEDULE.fields_by_name['week_day_of_month'].message_type = _WEEKDAYOFMONTH
_MONTHLYSCHEDULE.oneofs_by_name['day_of_month'].fields.append(
  _MONTHLYSCHEDULE.fields_by_name['week_day_of_month'])
_MONTHLYSCHEDULE.fields_by_name['week_day_of_month'].containing_oneof = _MONTHLYSCHEDULE.oneofs_by_name['day_of_month']
_MONTHLYSCHEDULE.oneofs_by_name['day_of_month'].fields.append(
  _MONTHLYSCHEDULE.fields_by_name['month_day'])
_MONTHLYSCHEDULE.fields_by_name['month_day'].containing_oneof = _MONTHLYSCHEDULE.oneofs_by_name['day_of_month']
_WEEKDAYOFMONTH.fields_by_name['day_of_week'].enum_type = google_dot_type_dot_dayofweek__pb2._DAYOFWEEK
_CREATEPATCHDEPLOYMENTREQUEST.fields_by_name['patch_deployment'].message_type = _PATCHDEPLOYMENT
_LISTPATCHDEPLOYMENTSRESPONSE.fields_by_name['patch_deployments'].message_type = _PATCHDEPLOYMENT
DESCRIPTOR.message_types_by_name['PatchDeployment'] = _PATCHDEPLOYMENT
DESCRIPTOR.message_types_by_name['OneTimeSchedule'] = _ONETIMESCHEDULE
DESCRIPTOR.message_types_by_name['RecurringSchedule'] = _RECURRINGSCHEDULE
DESCRIPTOR.message_types_by_name['WeeklySchedule'] = _WEEKLYSCHEDULE
DESCRIPTOR.message_types_by_name['MonthlySchedule'] = _MONTHLYSCHEDULE
DESCRIPTOR.message_types_by_name['WeekDayOfMonth'] = _WEEKDAYOFMONTH
DESCRIPTOR.message_types_by_name['CreatePatchDeploymentRequest'] = _CREATEPATCHDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['GetPatchDeploymentRequest'] = _GETPATCHDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['ListPatchDeploymentsRequest'] = _LISTPATCHDEPLOYMENTSREQUEST
DESCRIPTOR.message_types_by_name['ListPatchDeploymentsResponse'] = _LISTPATCHDEPLOYMENTSRESPONSE
DESCRIPTOR.message_types_by_name['DeletePatchDeploymentRequest'] = _DELETEPATCHDEPLOYMENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PatchDeployment = _reflection.GeneratedProtocolMessageType('PatchDeployment', (_message.Message,), {
  'DESCRIPTOR' : _PATCHDEPLOYMENT,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.PatchDeployment)
  })
_sym_db.RegisterMessage(PatchDeployment)

OneTimeSchedule = _reflection.GeneratedProtocolMessageType('OneTimeSchedule', (_message.Message,), {
  'DESCRIPTOR' : _ONETIMESCHEDULE,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.OneTimeSchedule)
  })
_sym_db.RegisterMessage(OneTimeSchedule)

RecurringSchedule = _reflection.GeneratedProtocolMessageType('RecurringSchedule', (_message.Message,), {
  'DESCRIPTOR' : _RECURRINGSCHEDULE,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.RecurringSchedule)
  })
_sym_db.RegisterMessage(RecurringSchedule)

WeeklySchedule = _reflection.GeneratedProtocolMessageType('WeeklySchedule', (_message.Message,), {
  'DESCRIPTOR' : _WEEKLYSCHEDULE,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.WeeklySchedule)
  })
_sym_db.RegisterMessage(WeeklySchedule)

MonthlySchedule = _reflection.GeneratedProtocolMessageType('MonthlySchedule', (_message.Message,), {
  'DESCRIPTOR' : _MONTHLYSCHEDULE,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.MonthlySchedule)
  })
_sym_db.RegisterMessage(MonthlySchedule)

WeekDayOfMonth = _reflection.GeneratedProtocolMessageType('WeekDayOfMonth', (_message.Message,), {
  'DESCRIPTOR' : _WEEKDAYOFMONTH,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.WeekDayOfMonth)
  })
_sym_db.RegisterMessage(WeekDayOfMonth)

CreatePatchDeploymentRequest = _reflection.GeneratedProtocolMessageType('CreatePatchDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPATCHDEPLOYMENTREQUEST,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.CreatePatchDeploymentRequest)
  })
_sym_db.RegisterMessage(CreatePatchDeploymentRequest)

GetPatchDeploymentRequest = _reflection.GeneratedProtocolMessageType('GetPatchDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPATCHDEPLOYMENTREQUEST,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.GetPatchDeploymentRequest)
  })
_sym_db.RegisterMessage(GetPatchDeploymentRequest)

ListPatchDeploymentsRequest = _reflection.GeneratedProtocolMessageType('ListPatchDeploymentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPATCHDEPLOYMENTSREQUEST,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.ListPatchDeploymentsRequest)
  })
_sym_db.RegisterMessage(ListPatchDeploymentsRequest)

ListPatchDeploymentsResponse = _reflection.GeneratedProtocolMessageType('ListPatchDeploymentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPATCHDEPLOYMENTSRESPONSE,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse)
  })
_sym_db.RegisterMessage(ListPatchDeploymentsResponse)

DeletePatchDeploymentRequest = _reflection.GeneratedProtocolMessageType('DeletePatchDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPATCHDEPLOYMENTREQUEST,
  '__module__' : 'google.cloud.osconfig.v1beta.patch_deployments_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1beta.DeletePatchDeploymentRequest)
  })
_sym_db.RegisterMessage(DeletePatchDeploymentRequest)


DESCRIPTOR._options = None
_PATCHDEPLOYMENT.fields_by_name['description']._options = None
_PATCHDEPLOYMENT.fields_by_name['instance_filter']._options = None
_PATCHDEPLOYMENT.fields_by_name['patch_config']._options = None
_PATCHDEPLOYMENT.fields_by_name['duration']._options = None
_PATCHDEPLOYMENT.fields_by_name['one_time_schedule']._options = None
_PATCHDEPLOYMENT.fields_by_name['recurring_schedule']._options = None
_PATCHDEPLOYMENT.fields_by_name['create_time']._options = None
_PATCHDEPLOYMENT.fields_by_name['update_time']._options = None
_PATCHDEPLOYMENT.fields_by_name['last_execute_time']._options = None
_ONETIMESCHEDULE.fields_by_name['execute_time']._options = None
_RECURRINGSCHEDULE.fields_by_name['time_zone']._options = None
_RECURRINGSCHEDULE.fields_by_name['start_time']._options = None
_RECURRINGSCHEDULE.fields_by_name['end_time']._options = None
_RECURRINGSCHEDULE.fields_by_name['time_of_day']._options = None
_RECURRINGSCHEDULE.fields_by_name['frequency']._options = None
_RECURRINGSCHEDULE.fields_by_name['weekly']._options = None
_RECURRINGSCHEDULE.fields_by_name['monthly']._options = None
_RECURRINGSCHEDULE.fields_by_name['last_execute_time']._options = None
_RECURRINGSCHEDULE.fields_by_name['next_execute_time']._options = None
_WEEKLYSCHEDULE.fields_by_name['day_of_week']._options = None
_MONTHLYSCHEDULE.fields_by_name['week_day_of_month']._options = None
_MONTHLYSCHEDULE.fields_by_name['month_day']._options = None
_WEEKDAYOFMONTH.fields_by_name['week_ordinal']._options = None
_WEEKDAYOFMONTH.fields_by_name['day_of_week']._options = None
_CREATEPATCHDEPLOYMENTREQUEST.fields_by_name['parent']._options = None
_CREATEPATCHDEPLOYMENTREQUEST.fields_by_name['patch_deployment_id']._options = None
_CREATEPATCHDEPLOYMENTREQUEST.fields_by_name['patch_deployment']._options = None
_GETPATCHDEPLOYMENTREQUEST.fields_by_name['name']._options = None
_LISTPATCHDEPLOYMENTSREQUEST.fields_by_name['parent']._options = None
_LISTPATCHDEPLOYMENTSREQUEST.fields_by_name['page_size']._options = None
_LISTPATCHDEPLOYMENTSREQUEST.fields_by_name['page_token']._options = None
_DELETEPATCHDEPLOYMENTREQUEST.fields_by_name['name']._options = None
# @@protoc_insertion_point(module_scope)
