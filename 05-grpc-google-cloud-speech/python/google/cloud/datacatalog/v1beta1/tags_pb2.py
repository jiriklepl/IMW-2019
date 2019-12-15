# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog/v1beta1/tags.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datacatalog/v1beta1/tags.proto',
  package='google.cloud.datacatalog.v1beta1',
  syntax='proto3',
  serialized_options=b'\n$com.google.cloud.datacatalog.v1beta1P\001ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\370\001\001',
  serialized_pb=b'\n+google/cloud/datacatalog/v1beta1/tags.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x90\x03\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\x08template\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\"\n\x15template_display_name\x18\x05 \x01(\tB\x03\xe0\x41\x03\x12\x10\n\x06\x63olumn\x18\x04 \x01(\tH\x00\x12\x46\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x31.google.cloud.datacatalog.v1beta1.Tag.FieldsEntryB\x03\xe0\x41\x02\x1aY\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.google.cloud.datacatalog.v1beta1.TagField:\x02\x38\x01:\x81\x01\xea\x41~\n\x1e\x64\x61tacatalog.googleapis.com/Tag\x12\\projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}/tags/{tag}B\x07\n\x05scope\"\x99\x02\n\x08TagField\x12\x19\n\x0c\x64isplay_name\x18\x01 \x01(\tB\x03\xe0\x41\x03\x12\x16\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x35\n\x0ftimestamp_value\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12J\n\nenum_value\x18\x06 \x01(\x0b\x32\x34.google.cloud.datacatalog.v1beta1.TagField.EnumValueH\x00\x1a!\n\tEnumValue\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\tB\x06\n\x04kind\"\xd6\x02\n\x0bTagTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12N\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x39.google.cloud.datacatalog.v1beta1.TagTemplate.FieldsEntryB\x03\xe0\x41\x02\x1a\x61\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.google.cloud.datacatalog.v1beta1.TagTemplateField:\x02\x38\x01:p\xea\x41m\n&datacatalog.googleapis.com/TagTemplate\x12\x43projects/{project}/locations/{location}/tagTemplates/{tag_template}\"\x83\x02\n\x10TagTemplateField\x12\x11\n\x04name\x18\x06 \x01(\tB\x03\xe0\x41\x03\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12>\n\x04type\x18\x02 \x01(\x0b\x32+.google.cloud.datacatalog.v1beta1.FieldTypeB\x03\xe0\x41\x02:\x85\x01\xea\x41\x81\x01\n+datacatalog.googleapis.com/TagTemplateField\x12Rprojects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{field}\"\xa7\x03\n\tFieldType\x12S\n\x0eprimitive_type\x18\x01 \x01(\x0e\x32\x39.google.cloud.datacatalog.v1beta1.FieldType.PrimitiveTypeH\x00\x12I\n\tenum_type\x18\x02 \x01(\x0b\x32\x34.google.cloud.datacatalog.v1beta1.FieldType.EnumTypeH\x00\x1a\x8a\x01\n\x08\x45numType\x12V\n\x0e\x61llowed_values\x18\x01 \x03(\x0b\x32>.google.cloud.datacatalog.v1beta1.FieldType.EnumType.EnumValue\x1a&\n\tEnumValue\x12\x19\n\x0c\x64isplay_name\x18\x01 \x01(\tB\x03\xe0\x41\x02\"`\n\rPrimitiveType\x12\x1e\n\x1aPRIMITIVE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06\x44OUBLE\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\r\n\tTIMESTAMP\x10\x04\x42\x0b\n\ttype_declBx\n$com.google.cloud.datacatalog.v1beta1P\x01ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_FIELDTYPE_PRIMITIVETYPE = _descriptor.EnumDescriptor(
  name='PrimitiveType',
  full_name='google.cloud.datacatalog.v1beta1.FieldType.PrimitiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIMITIVE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1783,
  serialized_end=1879,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE_PRIMITIVETYPE)


_TAG_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='google.cloud.datacatalog.v1beta1.Tag.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.datacatalog.v1beta1.Tag.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.datacatalog.v1beta1.Tag.FieldsEntry.value', index=1,
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
  serialized_start=345,
  serialized_end=434,
)

_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='google.cloud.datacatalog.v1beta1.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.datacatalog.v1beta1.Tag.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template', full_name='google.cloud.datacatalog.v1beta1.Tag.template', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_display_name', full_name='google.cloud.datacatalog.v1beta1.Tag.template_display_name', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column', full_name='google.cloud.datacatalog.v1beta1.Tag.column', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.cloud.datacatalog.v1beta1.Tag.fields', index=4,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TAG_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\352A~\n\036datacatalog.googleapis.com/Tag\022\\projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}/tags/{tag}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='scope', full_name='google.cloud.datacatalog.v1beta1.Tag.scope',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=175,
  serialized_end=575,
)


_TAGFIELD_ENUMVALUE = _descriptor.Descriptor(
  name='EnumValue',
  full_name='google.cloud.datacatalog.v1beta1.TagField.EnumValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datacatalog.v1beta1.TagField.EnumValue.display_name', index=0,
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
  serialized_start=818,
  serialized_end=851,
)

_TAGFIELD = _descriptor.Descriptor(
  name='TagField',
  full_name='google.cloud.datacatalog.v1beta1.TagField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datacatalog.v1beta1.TagField.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='google.cloud.datacatalog.v1beta1.TagField.double_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.cloud.datacatalog.v1beta1.TagField.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='google.cloud.datacatalog.v1beta1.TagField.bool_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_value', full_name='google.cloud.datacatalog.v1beta1.TagField.timestamp_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_value', full_name='google.cloud.datacatalog.v1beta1.TagField.enum_value', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TAGFIELD_ENUMVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='google.cloud.datacatalog.v1beta1.TagField.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=578,
  serialized_end=859,
)


_TAGTEMPLATE_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='google.cloud.datacatalog.v1beta1.TagTemplate.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.datacatalog.v1beta1.TagTemplate.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.datacatalog.v1beta1.TagTemplate.FieldsEntry.value', index=1,
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
  serialized_start=993,
  serialized_end=1090,
)

_TAGTEMPLATE = _descriptor.Descriptor(
  name='TagTemplate',
  full_name='google.cloud.datacatalog.v1beta1.TagTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.datacatalog.v1beta1.TagTemplate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datacatalog.v1beta1.TagTemplate.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.cloud.datacatalog.v1beta1.TagTemplate.fields', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TAGTEMPLATE_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\352Am\n&datacatalog.googleapis.com/TagTemplate\022Cprojects/{project}/locations/{location}/tagTemplates/{tag_template}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=1204,
)


_TAGTEMPLATEFIELD = _descriptor.Descriptor(
  name='TagTemplateField',
  full_name='google.cloud.datacatalog.v1beta1.TagTemplateField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.datacatalog.v1beta1.TagTemplateField.name', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datacatalog.v1beta1.TagTemplateField.display_name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.cloud.datacatalog.v1beta1.TagTemplateField.type', index=2,
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
  serialized_options=b'\352A\201\001\n+datacatalog.googleapis.com/TagTemplateField\022Rprojects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{field}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1207,
  serialized_end=1466,
)


_FIELDTYPE_ENUMTYPE_ENUMVALUE = _descriptor.Descriptor(
  name='EnumValue',
  full_name='google.cloud.datacatalog.v1beta1.FieldType.EnumType.EnumValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datacatalog.v1beta1.FieldType.EnumType.EnumValue.display_name', index=0,
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
  serialized_start=1743,
  serialized_end=1781,
)

_FIELDTYPE_ENUMTYPE = _descriptor.Descriptor(
  name='EnumType',
  full_name='google.cloud.datacatalog.v1beta1.FieldType.EnumType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowed_values', full_name='google.cloud.datacatalog.v1beta1.FieldType.EnumType.allowed_values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FIELDTYPE_ENUMTYPE_ENUMVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1643,
  serialized_end=1781,
)

_FIELDTYPE = _descriptor.Descriptor(
  name='FieldType',
  full_name='google.cloud.datacatalog.v1beta1.FieldType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primitive_type', full_name='google.cloud.datacatalog.v1beta1.FieldType.primitive_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_type', full_name='google.cloud.datacatalog.v1beta1.FieldType.enum_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FIELDTYPE_ENUMTYPE, ],
  enum_types=[
    _FIELDTYPE_PRIMITIVETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type_decl', full_name='google.cloud.datacatalog.v1beta1.FieldType.type_decl',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1469,
  serialized_end=1892,
)

_TAG_FIELDSENTRY.fields_by_name['value'].message_type = _TAGFIELD
_TAG_FIELDSENTRY.containing_type = _TAG
_TAG.fields_by_name['fields'].message_type = _TAG_FIELDSENTRY
_TAG.oneofs_by_name['scope'].fields.append(
  _TAG.fields_by_name['column'])
_TAG.fields_by_name['column'].containing_oneof = _TAG.oneofs_by_name['scope']
_TAGFIELD_ENUMVALUE.containing_type = _TAGFIELD
_TAGFIELD.fields_by_name['timestamp_value'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TAGFIELD.fields_by_name['enum_value'].message_type = _TAGFIELD_ENUMVALUE
_TAGFIELD.oneofs_by_name['kind'].fields.append(
  _TAGFIELD.fields_by_name['double_value'])
_TAGFIELD.fields_by_name['double_value'].containing_oneof = _TAGFIELD.oneofs_by_name['kind']
_TAGFIELD.oneofs_by_name['kind'].fields.append(
  _TAGFIELD.fields_by_name['string_value'])
_TAGFIELD.fields_by_name['string_value'].containing_oneof = _TAGFIELD.oneofs_by_name['kind']
_TAGFIELD.oneofs_by_name['kind'].fields.append(
  _TAGFIELD.fields_by_name['bool_value'])
_TAGFIELD.fields_by_name['bool_value'].containing_oneof = _TAGFIELD.oneofs_by_name['kind']
_TAGFIELD.oneofs_by_name['kind'].fields.append(
  _TAGFIELD.fields_by_name['timestamp_value'])
_TAGFIELD.fields_by_name['timestamp_value'].containing_oneof = _TAGFIELD.oneofs_by_name['kind']
_TAGFIELD.oneofs_by_name['kind'].fields.append(
  _TAGFIELD.fields_by_name['enum_value'])
_TAGFIELD.fields_by_name['enum_value'].containing_oneof = _TAGFIELD.oneofs_by_name['kind']
_TAGTEMPLATE_FIELDSENTRY.fields_by_name['value'].message_type = _TAGTEMPLATEFIELD
_TAGTEMPLATE_FIELDSENTRY.containing_type = _TAGTEMPLATE
_TAGTEMPLATE.fields_by_name['fields'].message_type = _TAGTEMPLATE_FIELDSENTRY
_TAGTEMPLATEFIELD.fields_by_name['type'].message_type = _FIELDTYPE
_FIELDTYPE_ENUMTYPE_ENUMVALUE.containing_type = _FIELDTYPE_ENUMTYPE
_FIELDTYPE_ENUMTYPE.fields_by_name['allowed_values'].message_type = _FIELDTYPE_ENUMTYPE_ENUMVALUE
_FIELDTYPE_ENUMTYPE.containing_type = _FIELDTYPE
_FIELDTYPE.fields_by_name['primitive_type'].enum_type = _FIELDTYPE_PRIMITIVETYPE
_FIELDTYPE.fields_by_name['enum_type'].message_type = _FIELDTYPE_ENUMTYPE
_FIELDTYPE_PRIMITIVETYPE.containing_type = _FIELDTYPE
_FIELDTYPE.oneofs_by_name['type_decl'].fields.append(
  _FIELDTYPE.fields_by_name['primitive_type'])
_FIELDTYPE.fields_by_name['primitive_type'].containing_oneof = _FIELDTYPE.oneofs_by_name['type_decl']
_FIELDTYPE.oneofs_by_name['type_decl'].fields.append(
  _FIELDTYPE.fields_by_name['enum_type'])
_FIELDTYPE.fields_by_name['enum_type'].containing_oneof = _FIELDTYPE.oneofs_by_name['type_decl']
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['TagField'] = _TAGFIELD
DESCRIPTOR.message_types_by_name['TagTemplate'] = _TAGTEMPLATE
DESCRIPTOR.message_types_by_name['TagTemplateField'] = _TAGTEMPLATEFIELD
DESCRIPTOR.message_types_by_name['FieldType'] = _FIELDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAG_FIELDSENTRY,
    '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.Tag.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _TAG,
  '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.Tag)
  })
_sym_db.RegisterMessage(Tag)
_sym_db.RegisterMessage(Tag.FieldsEntry)

TagField = _reflection.GeneratedProtocolMessageType('TagField', (_message.Message,), {

  'EnumValue' : _reflection.GeneratedProtocolMessageType('EnumValue', (_message.Message,), {
    'DESCRIPTOR' : _TAGFIELD_ENUMVALUE,
    '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.TagField.EnumValue)
    })
  ,
  'DESCRIPTOR' : _TAGFIELD,
  '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.TagField)
  })
_sym_db.RegisterMessage(TagField)
_sym_db.RegisterMessage(TagField.EnumValue)

TagTemplate = _reflection.GeneratedProtocolMessageType('TagTemplate', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAGTEMPLATE_FIELDSENTRY,
    '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.TagTemplate.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _TAGTEMPLATE,
  '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.TagTemplate)
  })
_sym_db.RegisterMessage(TagTemplate)
_sym_db.RegisterMessage(TagTemplate.FieldsEntry)

TagTemplateField = _reflection.GeneratedProtocolMessageType('TagTemplateField', (_message.Message,), {
  'DESCRIPTOR' : _TAGTEMPLATEFIELD,
  '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.TagTemplateField)
  })
_sym_db.RegisterMessage(TagTemplateField)

FieldType = _reflection.GeneratedProtocolMessageType('FieldType', (_message.Message,), {

  'EnumType' : _reflection.GeneratedProtocolMessageType('EnumType', (_message.Message,), {

    'EnumValue' : _reflection.GeneratedProtocolMessageType('EnumValue', (_message.Message,), {
      'DESCRIPTOR' : _FIELDTYPE_ENUMTYPE_ENUMVALUE,
      '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.FieldType.EnumType.EnumValue)
      })
    ,
    'DESCRIPTOR' : _FIELDTYPE_ENUMTYPE,
    '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.FieldType.EnumType)
    })
  ,
  'DESCRIPTOR' : _FIELDTYPE,
  '__module__' : 'google.cloud.datacatalog.v1beta1.tags_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.FieldType)
  })
_sym_db.RegisterMessage(FieldType)
_sym_db.RegisterMessage(FieldType.EnumType)
_sym_db.RegisterMessage(FieldType.EnumType.EnumValue)


DESCRIPTOR._options = None
_TAG_FIELDSENTRY._options = None
_TAG.fields_by_name['template']._options = None
_TAG.fields_by_name['template_display_name']._options = None
_TAG.fields_by_name['fields']._options = None
_TAG._options = None
_TAGFIELD.fields_by_name['display_name']._options = None
_TAGTEMPLATE_FIELDSENTRY._options = None
_TAGTEMPLATE.fields_by_name['fields']._options = None
_TAGTEMPLATE._options = None
_TAGTEMPLATEFIELD.fields_by_name['name']._options = None
_TAGTEMPLATEFIELD.fields_by_name['type']._options = None
_TAGTEMPLATEFIELD._options = None
_FIELDTYPE_ENUMTYPE_ENUMVALUE.fields_by_name['display_name']._options = None
# @@protoc_insertion_point(module_scope)
