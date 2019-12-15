# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/resultstore/v2/test_suite.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/resultstore/v2/test_suite.proto',
  package='google.devtools.resultstore.v2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.devtools.resultstore.v2P\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore',
  serialized_pb=b'\n/google/devtools/resultstore/v2/test_suite.proto\x12\x1egoogle.devtools.resultstore.v2\x1a+google/devtools/resultstore/v2/common.proto\x1a)google/devtools/resultstore/v2/file.proto\"\xf9\x02\n\tTestSuite\x12\x12\n\nsuite_name\x18\x01 \x01(\t\x12\x33\n\x05tests\x18\x02 \x03(\x0b\x32$.google.devtools.resultstore.v2.Test\x12=\n\x08\x66\x61ilures\x18\x03 \x03(\x0b\x32+.google.devtools.resultstore.v2.TestFailure\x12\x39\n\x06\x65rrors\x18\x04 \x03(\x0b\x32).google.devtools.resultstore.v2.TestError\x12\x36\n\x06timing\x18\x06 \x01(\x0b\x32&.google.devtools.resultstore.v2.Timing\x12<\n\nproperties\x18\x07 \x03(\x0b\x32(.google.devtools.resultstore.v2.Property\x12\x33\n\x05\x66iles\x18\x08 \x03(\x0b\x32$.google.devtools.resultstore.v2.File\"\x93\x01\n\x04Test\x12=\n\ttest_case\x18\x01 \x01(\x0b\x32(.google.devtools.resultstore.v2.TestCaseH\x00\x12?\n\ntest_suite\x18\x02 \x01(\x0b\x32).google.devtools.resultstore.v2.TestSuiteH\x00\x42\x0b\n\ttest_type\"\x93\x04\n\x08TestCase\x12\x11\n\tcase_name\x18\x01 \x01(\t\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12?\n\x06result\x18\x03 \x01(\x0e\x32/.google.devtools.resultstore.v2.TestCase.Result\x12=\n\x08\x66\x61ilures\x18\x04 \x03(\x0b\x32+.google.devtools.resultstore.v2.TestFailure\x12\x39\n\x06\x65rrors\x18\x05 \x03(\x0b\x32).google.devtools.resultstore.v2.TestError\x12\x36\n\x06timing\x18\x07 \x01(\x0b\x32&.google.devtools.resultstore.v2.Timing\x12<\n\nproperties\x18\x08 \x03(\x0b\x32(.google.devtools.resultstore.v2.Property\x12\x33\n\x05\x66iles\x18\t \x03(\x0b\x32$.google.devtools.resultstore.v2.File\"z\n\x06Result\x12\x16\n\x12RESULT_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\x0f\n\x0bINTERRUPTED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0c\n\x08\x46ILTERED\x10\x04\x12\x0b\n\x07SKIPPED\x10\x05\x12\x0e\n\nSUPPRESSED\x10\x06\"u\n\x0bTestFailure\x12\x17\n\x0f\x66\x61ilure_message\x18\x01 \x01(\t\x12\x16\n\x0e\x65xception_type\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\t\x12\x10\n\x08\x65xpected\x18\x04 \x03(\t\x12\x0e\n\x06\x61\x63tual\x18\x05 \x03(\t\"O\n\tTestError\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x16\n\x0e\x65xception_type\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\tBq\n\"com.google.devtools.resultstore.v2P\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3'
  ,
  dependencies=[google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2.DESCRIPTOR,google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2.DESCRIPTOR,])



_TESTCASE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='google.devtools.resultstore.v2.TestCase.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERRUPTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILTERED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKIPPED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUPPRESSED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1111,
  serialized_end=1233,
)
_sym_db.RegisterEnumDescriptor(_TESTCASE_RESULT)


_TESTSUITE = _descriptor.Descriptor(
  name='TestSuite',
  full_name='google.devtools.resultstore.v2.TestSuite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='suite_name', full_name='google.devtools.resultstore.v2.TestSuite.suite_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tests', full_name='google.devtools.resultstore.v2.TestSuite.tests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failures', full_name='google.devtools.resultstore.v2.TestSuite.failures', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='google.devtools.resultstore.v2.TestSuite.errors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timing', full_name='google.devtools.resultstore.v2.TestSuite.timing', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.devtools.resultstore.v2.TestSuite.properties', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='google.devtools.resultstore.v2.TestSuite.files', index=6,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=172,
  serialized_end=549,
)


_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='google.devtools.resultstore.v2.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_case', full_name='google.devtools.resultstore.v2.Test.test_case', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_suite', full_name='google.devtools.resultstore.v2.Test.test_suite', index=1,
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
    _descriptor.OneofDescriptor(
      name='test_type', full_name='google.devtools.resultstore.v2.Test.test_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=552,
  serialized_end=699,
)


_TESTCASE = _descriptor.Descriptor(
  name='TestCase',
  full_name='google.devtools.resultstore.v2.TestCase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='case_name', full_name='google.devtools.resultstore.v2.TestCase.case_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='google.devtools.resultstore.v2.TestCase.class_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='google.devtools.resultstore.v2.TestCase.result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failures', full_name='google.devtools.resultstore.v2.TestCase.failures', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='google.devtools.resultstore.v2.TestCase.errors', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timing', full_name='google.devtools.resultstore.v2.TestCase.timing', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.devtools.resultstore.v2.TestCase.properties', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='google.devtools.resultstore.v2.TestCase.files', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TESTCASE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=1233,
)


_TESTFAILURE = _descriptor.Descriptor(
  name='TestFailure',
  full_name='google.devtools.resultstore.v2.TestFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failure_message', full_name='google.devtools.resultstore.v2.TestFailure.failure_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exception_type', full_name='google.devtools.resultstore.v2.TestFailure.exception_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_trace', full_name='google.devtools.resultstore.v2.TestFailure.stack_trace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected', full_name='google.devtools.resultstore.v2.TestFailure.expected', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual', full_name='google.devtools.resultstore.v2.TestFailure.actual', index=4,
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
  serialized_start=1235,
  serialized_end=1352,
)


_TESTERROR = _descriptor.Descriptor(
  name='TestError',
  full_name='google.devtools.resultstore.v2.TestError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_message', full_name='google.devtools.resultstore.v2.TestError.error_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exception_type', full_name='google.devtools.resultstore.v2.TestError.exception_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_trace', full_name='google.devtools.resultstore.v2.TestError.stack_trace', index=2,
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
  serialized_start=1354,
  serialized_end=1433,
)

_TESTSUITE.fields_by_name['tests'].message_type = _TEST
_TESTSUITE.fields_by_name['failures'].message_type = _TESTFAILURE
_TESTSUITE.fields_by_name['errors'].message_type = _TESTERROR
_TESTSUITE.fields_by_name['timing'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._TIMING
_TESTSUITE.fields_by_name['properties'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._PROPERTY
_TESTSUITE.fields_by_name['files'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2._FILE
_TEST.fields_by_name['test_case'].message_type = _TESTCASE
_TEST.fields_by_name['test_suite'].message_type = _TESTSUITE
_TEST.oneofs_by_name['test_type'].fields.append(
  _TEST.fields_by_name['test_case'])
_TEST.fields_by_name['test_case'].containing_oneof = _TEST.oneofs_by_name['test_type']
_TEST.oneofs_by_name['test_type'].fields.append(
  _TEST.fields_by_name['test_suite'])
_TEST.fields_by_name['test_suite'].containing_oneof = _TEST.oneofs_by_name['test_type']
_TESTCASE.fields_by_name['result'].enum_type = _TESTCASE_RESULT
_TESTCASE.fields_by_name['failures'].message_type = _TESTFAILURE
_TESTCASE.fields_by_name['errors'].message_type = _TESTERROR
_TESTCASE.fields_by_name['timing'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._TIMING
_TESTCASE.fields_by_name['properties'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._PROPERTY
_TESTCASE.fields_by_name['files'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2._FILE
_TESTCASE_RESULT.containing_type = _TESTCASE
DESCRIPTOR.message_types_by_name['TestSuite'] = _TESTSUITE
DESCRIPTOR.message_types_by_name['Test'] = _TEST
DESCRIPTOR.message_types_by_name['TestCase'] = _TESTCASE
DESCRIPTOR.message_types_by_name['TestFailure'] = _TESTFAILURE
DESCRIPTOR.message_types_by_name['TestError'] = _TESTERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestSuite = _reflection.GeneratedProtocolMessageType('TestSuite', (_message.Message,), {
  'DESCRIPTOR' : _TESTSUITE,
  '__module__' : 'google.devtools.resultstore.v2.test_suite_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TestSuite)
  })
_sym_db.RegisterMessage(TestSuite)

Test = _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {
  'DESCRIPTOR' : _TEST,
  '__module__' : 'google.devtools.resultstore.v2.test_suite_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.Test)
  })
_sym_db.RegisterMessage(Test)

TestCase = _reflection.GeneratedProtocolMessageType('TestCase', (_message.Message,), {
  'DESCRIPTOR' : _TESTCASE,
  '__module__' : 'google.devtools.resultstore.v2.test_suite_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TestCase)
  })
_sym_db.RegisterMessage(TestCase)

TestFailure = _reflection.GeneratedProtocolMessageType('TestFailure', (_message.Message,), {
  'DESCRIPTOR' : _TESTFAILURE,
  '__module__' : 'google.devtools.resultstore.v2.test_suite_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TestFailure)
  })
_sym_db.RegisterMessage(TestFailure)

TestError = _reflection.GeneratedProtocolMessageType('TestError', (_message.Message,), {
  'DESCRIPTOR' : _TESTERROR,
  '__module__' : 'google.devtools.resultstore.v2.test_suite_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TestError)
  })
_sym_db.RegisterMessage(TestError)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)