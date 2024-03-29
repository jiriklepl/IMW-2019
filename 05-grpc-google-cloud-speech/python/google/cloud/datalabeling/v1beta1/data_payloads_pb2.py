# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling/v1beta1/data_payloads.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datalabeling/v1beta1/data_payloads.proto',
  package='google.cloud.datalabeling.v1beta1',
  syntax='proto3',
  serialized_options=b'\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling',
  serialized_pb=b'\n5google/cloud/datalabeling/v1beta1/data_payloads.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"a\n\x0cImagePayload\x12\x11\n\tmime_type\x18\x01 \x01(\t\x12\x17\n\x0fimage_thumbnail\x18\x02 \x01(\x0c\x12\x11\n\timage_uri\x18\x03 \x01(\t\x12\x12\n\nsigned_uri\x18\x04 \x01(\t\"#\n\x0bTextPayload\x12\x14\n\x0ctext_content\x18\x01 \x01(\t\"S\n\x0eVideoThumbnail\x12\x11\n\tthumbnail\x18\x01 \x01(\x0c\x12.\n\x0btime_offset\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xa9\x01\n\x0cVideoPayload\x12\x11\n\tmime_type\x18\x01 \x01(\t\x12\x11\n\tvideo_uri\x18\x02 \x01(\t\x12K\n\x10video_thumbnails\x18\x03 \x03(\x0b\x32\x31.google.cloud.datalabeling.v1beta1.VideoThumbnail\x12\x12\n\nframe_rate\x18\x04 \x01(\x02\x12\x12\n\nsigned_uri\x18\x05 \x01(\tBx\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabelingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_IMAGEPAYLOAD = _descriptor.Descriptor(
  name='ImagePayload',
  full_name='google.cloud.datalabeling.v1beta1.ImagePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.cloud.datalabeling.v1beta1.ImagePayload.mime_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_thumbnail', full_name='google.cloud.datalabeling.v1beta1.ImagePayload.image_thumbnail', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_uri', full_name='google.cloud.datalabeling.v1beta1.ImagePayload.image_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signed_uri', full_name='google.cloud.datalabeling.v1beta1.ImagePayload.signed_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=187,
  serialized_end=284,
)


_TEXTPAYLOAD = _descriptor.Descriptor(
  name='TextPayload',
  full_name='google.cloud.datalabeling.v1beta1.TextPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_content', full_name='google.cloud.datalabeling.v1beta1.TextPayload.text_content', index=0,
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
  serialized_start=286,
  serialized_end=321,
)


_VIDEOTHUMBNAIL = _descriptor.Descriptor(
  name='VideoThumbnail',
  full_name='google.cloud.datalabeling.v1beta1.VideoThumbnail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='thumbnail', full_name='google.cloud.datalabeling.v1beta1.VideoThumbnail.thumbnail', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_offset', full_name='google.cloud.datalabeling.v1beta1.VideoThumbnail.time_offset', index=1,
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
  ],
  serialized_start=323,
  serialized_end=406,
)


_VIDEOPAYLOAD = _descriptor.Descriptor(
  name='VideoPayload',
  full_name='google.cloud.datalabeling.v1beta1.VideoPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.cloud.datalabeling.v1beta1.VideoPayload.mime_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_uri', full_name='google.cloud.datalabeling.v1beta1.VideoPayload.video_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_thumbnails', full_name='google.cloud.datalabeling.v1beta1.VideoPayload.video_thumbnails', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_rate', full_name='google.cloud.datalabeling.v1beta1.VideoPayload.frame_rate', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signed_uri', full_name='google.cloud.datalabeling.v1beta1.VideoPayload.signed_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=409,
  serialized_end=578,
)

_VIDEOTHUMBNAIL.fields_by_name['time_offset'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_VIDEOPAYLOAD.fields_by_name['video_thumbnails'].message_type = _VIDEOTHUMBNAIL
DESCRIPTOR.message_types_by_name['ImagePayload'] = _IMAGEPAYLOAD
DESCRIPTOR.message_types_by_name['TextPayload'] = _TEXTPAYLOAD
DESCRIPTOR.message_types_by_name['VideoThumbnail'] = _VIDEOTHUMBNAIL
DESCRIPTOR.message_types_by_name['VideoPayload'] = _VIDEOPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImagePayload = _reflection.GeneratedProtocolMessageType('ImagePayload', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPAYLOAD,
  '__module__' : 'google.cloud.datalabeling.v1beta1.data_payloads_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.ImagePayload)
  })
_sym_db.RegisterMessage(ImagePayload)

TextPayload = _reflection.GeneratedProtocolMessageType('TextPayload', (_message.Message,), {
  'DESCRIPTOR' : _TEXTPAYLOAD,
  '__module__' : 'google.cloud.datalabeling.v1beta1.data_payloads_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.TextPayload)
  })
_sym_db.RegisterMessage(TextPayload)

VideoThumbnail = _reflection.GeneratedProtocolMessageType('VideoThumbnail', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOTHUMBNAIL,
  '__module__' : 'google.cloud.datalabeling.v1beta1.data_payloads_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.VideoThumbnail)
  })
_sym_db.RegisterMessage(VideoThumbnail)

VideoPayload = _reflection.GeneratedProtocolMessageType('VideoPayload', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOPAYLOAD,
  '__module__' : 'google.cloud.datalabeling.v1beta1.data_payloads_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.VideoPayload)
  })
_sym_db.RegisterMessage(VideoPayload)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
