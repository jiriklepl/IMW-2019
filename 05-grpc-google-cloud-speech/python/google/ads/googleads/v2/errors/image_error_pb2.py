# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/errors/image_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/errors/image_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v2.errorsB\017ImageErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors',
  serialized_pb=b'\n0google/ads/googleads/v2/errors/image_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"\x8a\x08\n\x0eImageErrorEnum\"\xf7\x07\n\nImageError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rINVALID_IMAGE\x10\x02\x12\x11\n\rSTORAGE_ERROR\x10\x03\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x04\x12\x13\n\x0fUNEXPECTED_SIZE\x10\x05\x12\x18\n\x14\x41NIMATED_NOT_ALLOWED\x10\x06\x12\x16\n\x12\x41NIMATION_TOO_LONG\x10\x07\x12\x10\n\x0cSERVER_ERROR\x10\x08\x12\x19\n\x15\x43MYK_JPEG_NOT_ALLOWED\x10\t\x12\x15\n\x11\x46LASH_NOT_ALLOWED\x10\n\x12\x1a\n\x16\x46LASH_WITHOUT_CLICKTAG\x10\x0b\x12&\n\"FLASH_ERROR_AFTER_FIXING_CLICK_TAG\x10\x0c\x12\x1a\n\x16\x41NIMATED_VISUAL_EFFECT\x10\r\x12\x0f\n\x0b\x46LASH_ERROR\x10\x0e\x12\x12\n\x0eLAYOUT_PROBLEM\x10\x0f\x12\x1e\n\x1aPROBLEM_READING_IMAGE_FILE\x10\x10\x12\x17\n\x13\x45RROR_STORING_IMAGE\x10\x11\x12\x1c\n\x18\x41SPECT_RATIO_NOT_ALLOWED\x10\x12\x12\x1d\n\x19\x46LASH_HAS_NETWORK_OBJECTS\x10\x13\x12\x1d\n\x19\x46LASH_HAS_NETWORK_METHODS\x10\x14\x12\x11\n\rFLASH_HAS_URL\x10\x15\x12\x1c\n\x18\x46LASH_HAS_MOUSE_TRACKING\x10\x16\x12\x18\n\x14\x46LASH_HAS_RANDOM_NUM\x10\x17\x12\x16\n\x12\x46LASH_SELF_TARGETS\x10\x18\x12\x1b\n\x17\x46LASH_BAD_GETURL_TARGET\x10\x19\x12\x1f\n\x1b\x46LASH_VERSION_NOT_SUPPORTED\x10\x1a\x12&\n\"FLASH_WITHOUT_HARD_CODED_CLICK_URL\x10\x1b\x12\x16\n\x12INVALID_FLASH_FILE\x10\x1c\x12$\n FAILED_TO_FIX_CLICK_TAG_IN_FLASH\x10\x1d\x12$\n FLASH_ACCESSES_NETWORK_RESOURCES\x10\x1e\x12\x1a\n\x16\x46LASH_EXTERNAL_JS_CALL\x10\x1f\x12\x1a\n\x16\x46LASH_EXTERNAL_FS_CALL\x10 \x12\x12\n\x0e\x46ILE_TOO_LARGE\x10!\x12\x18\n\x14IMAGE_DATA_TOO_LARGE\x10\"\x12\x1a\n\x16IMAGE_PROCESSING_ERROR\x10#\x12\x13\n\x0fIMAGE_TOO_SMALL\x10$\x12\x11\n\rINVALID_INPUT\x10%\x12\x18\n\x14PROBLEM_READING_FILE\x10&B\xea\x01\n\"com.google.ads.googleads.v2.errorsB\x0fImageErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_IMAGEERRORENUM_IMAGEERROR = _descriptor.EnumDescriptor(
  name='ImageError',
  full_name='google.ads.googleads.v2.errors.ImageErrorEnum.ImageError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_IMAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORAGE_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_SIZE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANIMATED_NOT_ALLOWED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANIMATION_TOO_LONG', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CMYK_JPEG_NOT_ALLOWED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_NOT_ALLOWED', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_WITHOUT_CLICKTAG', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_ERROR_AFTER_FIXING_CLICK_TAG', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANIMATED_VISUAL_EFFECT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_ERROR', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAYOUT_PROBLEM', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROBLEM_READING_IMAGE_FILE', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_STORING_IMAGE', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASPECT_RATIO_NOT_ALLOWED', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_HAS_NETWORK_OBJECTS', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_HAS_NETWORK_METHODS', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_HAS_URL', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_HAS_MOUSE_TRACKING', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_HAS_RANDOM_NUM', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_SELF_TARGETS', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_BAD_GETURL_TARGET', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_VERSION_NOT_SUPPORTED', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_WITHOUT_HARD_CODED_CLICK_URL', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FLASH_FILE', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_TO_FIX_CLICK_TAG_IN_FLASH', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_ACCESSES_NETWORK_RESOURCES', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_EXTERNAL_JS_CALL', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_EXTERNAL_FS_CALL', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE_TOO_LARGE', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_DATA_TOO_LARGE', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_PROCESSING_ERROR', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_TOO_SMALL', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROBLEM_READING_FILE', index=38, number=38,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=134,
  serialized_end=1149,
)
_sym_db.RegisterEnumDescriptor(_IMAGEERRORENUM_IMAGEERROR)


_IMAGEERRORENUM = _descriptor.Descriptor(
  name='ImageErrorEnum',
  full_name='google.ads.googleads.v2.errors.ImageErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMAGEERRORENUM_IMAGEERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=1149,
)

_IMAGEERRORENUM_IMAGEERROR.containing_type = _IMAGEERRORENUM
DESCRIPTOR.message_types_by_name['ImageErrorEnum'] = _IMAGEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageErrorEnum = _reflection.GeneratedProtocolMessageType('ImageErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEERRORENUM,
  '__module__' : 'google.ads.googleads.v2.errors.image_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.ImageErrorEnum)
  })
_sym_db.RegisterMessage(ImageErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
