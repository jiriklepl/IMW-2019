# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='time.proto',
  package='time_message',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntime.proto\x12\x0ctime_message\"\x94\x01\n\x0bTimeMessage\x12\x0f\n\x07seconds\x18\x01 \x01(\r\x12\x0f\n\x07minutes\x18\x02 \x01(\r\x12\r\n\x05hours\x18\x03 \x01(\r\x12\x0c\n\x04mday\x18\x04 \x01(\r\x12\r\n\x05month\x18\x05 \x01(\r\x12\x0c\n\x04year\x18\x06 \x01(\r\x12\x0c\n\x04wday\x18\x07 \x01(\r\x12\x0c\n\x04yday\x18\x08 \x01(\r\x12\r\n\x05isdst\x18\t \x01(\r\"\x94\x01\n\x0bTimeRequest\x12\x0f\n\x07seconds\x18\x01 \x01(\x08\x12\x0f\n\x07minutes\x18\x02 \x01(\x08\x12\r\n\x05hours\x18\x03 \x01(\x08\x12\x0c\n\x04mday\x18\x04 \x01(\x08\x12\r\n\x05month\x18\x05 \x01(\x08\x12\x0c\n\x04year\x18\x06 \x01(\x08\x12\x0c\n\x04wday\x18\x07 \x01(\x08\x12\x0c\n\x04yday\x18\x08 \x01(\x08\x12\r\n\x05isdst\x18\t \x01(\x08\x32P\n\x0bTimeService\x12\x41\n\x07GetTime\x12\x19.time_message.TimeRequest\x1a\x19.time_message.TimeMessage\"\x00\x62\x06proto3')
)




_TIMEMESSAGE = _descriptor.Descriptor(
  name='TimeMessage',
  full_name='time_message.TimeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='time_message.TimeMessage.seconds', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='time_message.TimeMessage.minutes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hours', full_name='time_message.TimeMessage.hours', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mday', full_name='time_message.TimeMessage.mday', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='time_message.TimeMessage.month', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='time_message.TimeMessage.year', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wday', full_name='time_message.TimeMessage.wday', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yday', full_name='time_message.TimeMessage.yday', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isdst', full_name='time_message.TimeMessage.isdst', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=29,
  serialized_end=177,
)


_TIMEREQUEST = _descriptor.Descriptor(
  name='TimeRequest',
  full_name='time_message.TimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='time_message.TimeRequest.seconds', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='time_message.TimeRequest.minutes', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hours', full_name='time_message.TimeRequest.hours', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mday', full_name='time_message.TimeRequest.mday', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='time_message.TimeRequest.month', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='time_message.TimeRequest.year', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wday', full_name='time_message.TimeRequest.wday', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yday', full_name='time_message.TimeRequest.yday', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isdst', full_name='time_message.TimeRequest.isdst', index=8,
      number=9, type=8, cpp_type=7, label=1,
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
  ],
  serialized_start=180,
  serialized_end=328,
)

DESCRIPTOR.message_types_by_name['TimeMessage'] = _TIMEMESSAGE
DESCRIPTOR.message_types_by_name['TimeRequest'] = _TIMEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeMessage = _reflection.GeneratedProtocolMessageType('TimeMessage', (_message.Message,), {
  'DESCRIPTOR' : _TIMEMESSAGE,
  '__module__' : 'time_pb2'
  # @@protoc_insertion_point(class_scope:time_message.TimeMessage)
  })
_sym_db.RegisterMessage(TimeMessage)

TimeRequest = _reflection.GeneratedProtocolMessageType('TimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _TIMEREQUEST,
  '__module__' : 'time_pb2'
  # @@protoc_insertion_point(class_scope:time_message.TimeRequest)
  })
_sym_db.RegisterMessage(TimeRequest)



_TIMESERVICE = _descriptor.ServiceDescriptor(
  name='TimeService',
  full_name='time_message.TimeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=330,
  serialized_end=410,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTime',
    full_name='time_message.TimeService.GetTime',
    index=0,
    containing_service=None,
    input_type=_TIMEREQUEST,
    output_type=_TIMEMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIMESERVICE)

DESCRIPTOR.services_by_name['TimeService'] = _TIMESERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TimeServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetTime = channel.unary_unary(
          '/time_message.TimeService/GetTime',
          request_serializer=TimeRequest.SerializeToString,
          response_deserializer=TimeMessage.FromString,
          )


  class TimeServiceServicer(object):

    def GetTime(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TimeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetTime': grpc.unary_unary_rpc_method_handler(
            servicer.GetTime,
            request_deserializer=TimeRequest.FromString,
            response_serializer=TimeMessage.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'time_message.TimeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTimeServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetTime(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTimeServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetTime(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetTime.future = None


  def beta_create_TimeService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('time_message.TimeService', 'GetTime'): TimeRequest.FromString,
    }
    response_serializers = {
      ('time_message.TimeService', 'GetTime'): TimeMessage.SerializeToString,
    }
    method_implementations = {
      ('time_message.TimeService', 'GetTime'): face_utilities.unary_unary_inline(servicer.GetTime),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_TimeService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('time_message.TimeService', 'GetTime'): TimeRequest.SerializeToString,
    }
    response_deserializers = {
      ('time_message.TimeService', 'GetTime'): TimeMessage.FromString,
    }
    cardinalities = {
      'GetTime': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'time_message.TimeService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
