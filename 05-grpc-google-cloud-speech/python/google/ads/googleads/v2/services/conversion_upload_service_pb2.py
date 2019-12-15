# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v2/services/conversion_upload_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v2/services/conversion_upload_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v2.servicesB\034ConversionUploadServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services',
  serialized_pb=b'\n@google/ads/googleads/v2/services/conversion_upload_service.proto\x12 google.ads.googleads.v2.services\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto\"\xac\x01\n\x1dUploadClickConversionsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x46\n\x0b\x63onversions\x18\x02 \x03(\x0b\x32\x31.google.ads.googleads.v2.services.ClickConversion\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x9d\x01\n\x1eUploadClickConversionsResponse\x12\x31\n\x15partial_failure_error\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12H\n\x07results\x18\x02 \x03(\x0b\x32\x37.google.ads.googleads.v2.services.ClickConversionResult\"\xaa\x01\n\x1cUploadCallConversionsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x45\n\x0b\x63onversions\x18\x02 \x03(\x0b\x32\x30.google.ads.googleads.v2.services.CallConversion\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x9b\x01\n\x1dUploadCallConversionsResponse\x12\x31\n\x15partial_failure_error\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12G\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v2.services.CallConversionResult\"\xae\x03\n\x0f\x43lickConversion\x12+\n\x05gclid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x63onversion_action\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x63onversion_date_time\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x63onversion_value\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\rcurrency_code\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08order_id\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\\\n\x19\x65xternal_attribution_data\x18\x07 \x01(\x0b\x32\x39.google.ads.googleads.v2.services.ExternalAttributionData\"\xdf\x02\n\x0e\x43\x61llConversion\x12/\n\tcaller_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x63\x61ll_start_date_time\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x63onversion_action\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x63onversion_date_time\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x63onversion_value\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\rcurrency_code\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x9e\x01\n\x17\x45xternalAttributionData\x12\x41\n\x1b\x65xternal_attribution_credit\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12@\n\x1a\x65xternal_attribution_model\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xb9\x01\n\x15\x43lickConversionResult\x12+\n\x05gclid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x63onversion_action\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x63onversion_date_time\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xf8\x01\n\x14\x43\x61llConversionResult\x12/\n\tcaller_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x63\x61ll_start_date_time\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x63onversion_action\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x63onversion_date_time\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue2\xf0\x03\n\x17\x43onversionUploadService\x12\xdc\x01\n\x16UploadClickConversions\x12?.google.ads.googleads.v2.services.UploadClickConversionsRequest\x1a@.google.ads.googleads.v2.services.UploadClickConversionsResponse\"?\x82\xd3\xe4\x93\x02\x39\"4/v2/customers/{customer_id=*}:uploadClickConversions:\x01*\x12\xd8\x01\n\x15UploadCallConversions\x12>.google.ads.googleads.v2.services.UploadCallConversionsRequest\x1a?.google.ads.googleads.v2.services.UploadCallConversionsResponse\">\x82\xd3\xe4\x93\x02\x38\"3/v2/customers/{customer_id=*}:uploadCallConversions:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x83\x02\n$com.google.ads.googleads.v2.servicesB\x1c\x43onversionUploadServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_UPLOADCLICKCONVERSIONSREQUEST = _descriptor.Descriptor(
  name='UploadClickConversionsRequest',
  full_name='google.ads.googleads.v2.services.UploadClickConversionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.UploadClickConversionsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversions', full_name='google.ads.googleads.v2.services.UploadClickConversionsRequest.conversions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v2.services.UploadClickConversionsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v2.services.UploadClickConversionsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=215,
  serialized_end=387,
)


_UPLOADCLICKCONVERSIONSRESPONSE = _descriptor.Descriptor(
  name='UploadClickConversionsResponse',
  full_name='google.ads.googleads.v2.services.UploadClickConversionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v2.services.UploadClickConversionsResponse.partial_failure_error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.UploadClickConversionsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=390,
  serialized_end=547,
)


_UPLOADCALLCONVERSIONSREQUEST = _descriptor.Descriptor(
  name='UploadCallConversionsRequest',
  full_name='google.ads.googleads.v2.services.UploadCallConversionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.UploadCallConversionsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversions', full_name='google.ads.googleads.v2.services.UploadCallConversionsRequest.conversions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v2.services.UploadCallConversionsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v2.services.UploadCallConversionsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=550,
  serialized_end=720,
)


_UPLOADCALLCONVERSIONSRESPONSE = _descriptor.Descriptor(
  name='UploadCallConversionsResponse',
  full_name='google.ads.googleads.v2.services.UploadCallConversionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v2.services.UploadCallConversionsResponse.partial_failure_error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.UploadCallConversionsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=723,
  serialized_end=878,
)


_CLICKCONVERSION = _descriptor.Descriptor(
  name='ClickConversion',
  full_name='google.ads.googleads.v2.services.ClickConversion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gclid', full_name='google.ads.googleads.v2.services.ClickConversion.gclid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_action', full_name='google.ads.googleads.v2.services.ClickConversion.conversion_action', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_date_time', full_name='google.ads.googleads.v2.services.ClickConversion.conversion_date_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_value', full_name='google.ads.googleads.v2.services.ClickConversion.conversion_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v2.services.ClickConversion.currency_code', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='google.ads.googleads.v2.services.ClickConversion.order_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_attribution_data', full_name='google.ads.googleads.v2.services.ClickConversion.external_attribution_data', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=881,
  serialized_end=1311,
)


_CALLCONVERSION = _descriptor.Descriptor(
  name='CallConversion',
  full_name='google.ads.googleads.v2.services.CallConversion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='caller_id', full_name='google.ads.googleads.v2.services.CallConversion.caller_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_start_date_time', full_name='google.ads.googleads.v2.services.CallConversion.call_start_date_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_action', full_name='google.ads.googleads.v2.services.CallConversion.conversion_action', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_date_time', full_name='google.ads.googleads.v2.services.CallConversion.conversion_date_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_value', full_name='google.ads.googleads.v2.services.CallConversion.conversion_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v2.services.CallConversion.currency_code', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1314,
  serialized_end=1665,
)


_EXTERNALATTRIBUTIONDATA = _descriptor.Descriptor(
  name='ExternalAttributionData',
  full_name='google.ads.googleads.v2.services.ExternalAttributionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='external_attribution_credit', full_name='google.ads.googleads.v2.services.ExternalAttributionData.external_attribution_credit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_attribution_model', full_name='google.ads.googleads.v2.services.ExternalAttributionData.external_attribution_model', index=1,
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
  serialized_start=1668,
  serialized_end=1826,
)


_CLICKCONVERSIONRESULT = _descriptor.Descriptor(
  name='ClickConversionResult',
  full_name='google.ads.googleads.v2.services.ClickConversionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gclid', full_name='google.ads.googleads.v2.services.ClickConversionResult.gclid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_action', full_name='google.ads.googleads.v2.services.ClickConversionResult.conversion_action', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_date_time', full_name='google.ads.googleads.v2.services.ClickConversionResult.conversion_date_time', index=2,
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
  serialized_start=1829,
  serialized_end=2014,
)


_CALLCONVERSIONRESULT = _descriptor.Descriptor(
  name='CallConversionResult',
  full_name='google.ads.googleads.v2.services.CallConversionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='caller_id', full_name='google.ads.googleads.v2.services.CallConversionResult.caller_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_start_date_time', full_name='google.ads.googleads.v2.services.CallConversionResult.call_start_date_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_action', full_name='google.ads.googleads.v2.services.CallConversionResult.conversion_action', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_date_time', full_name='google.ads.googleads.v2.services.CallConversionResult.conversion_date_time', index=3,
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
  serialized_start=2017,
  serialized_end=2265,
)

_UPLOADCLICKCONVERSIONSREQUEST.fields_by_name['conversions'].message_type = _CLICKCONVERSION
_UPLOADCLICKCONVERSIONSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_UPLOADCLICKCONVERSIONSRESPONSE.fields_by_name['results'].message_type = _CLICKCONVERSIONRESULT
_UPLOADCALLCONVERSIONSREQUEST.fields_by_name['conversions'].message_type = _CALLCONVERSION
_UPLOADCALLCONVERSIONSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_UPLOADCALLCONVERSIONSRESPONSE.fields_by_name['results'].message_type = _CALLCONVERSIONRESULT
_CLICKCONVERSION.fields_by_name['gclid'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSION.fields_by_name['conversion_action'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSION.fields_by_name['conversion_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSION.fields_by_name['conversion_value'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_CLICKCONVERSION.fields_by_name['currency_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSION.fields_by_name['order_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSION.fields_by_name['external_attribution_data'].message_type = _EXTERNALATTRIBUTIONDATA
_CALLCONVERSION.fields_by_name['caller_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSION.fields_by_name['call_start_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSION.fields_by_name['conversion_action'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSION.fields_by_name['conversion_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSION.fields_by_name['conversion_value'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_CALLCONVERSION.fields_by_name['currency_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EXTERNALATTRIBUTIONDATA.fields_by_name['external_attribution_credit'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_EXTERNALATTRIBUTIONDATA.fields_by_name['external_attribution_model'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSIONRESULT.fields_by_name['gclid'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSIONRESULT.fields_by_name['conversion_action'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLICKCONVERSIONRESULT.fields_by_name['conversion_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSIONRESULT.fields_by_name['caller_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSIONRESULT.fields_by_name['call_start_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSIONRESULT.fields_by_name['conversion_action'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CALLCONVERSIONRESULT.fields_by_name['conversion_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['UploadClickConversionsRequest'] = _UPLOADCLICKCONVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['UploadClickConversionsResponse'] = _UPLOADCLICKCONVERSIONSRESPONSE
DESCRIPTOR.message_types_by_name['UploadCallConversionsRequest'] = _UPLOADCALLCONVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['UploadCallConversionsResponse'] = _UPLOADCALLCONVERSIONSRESPONSE
DESCRIPTOR.message_types_by_name['ClickConversion'] = _CLICKCONVERSION
DESCRIPTOR.message_types_by_name['CallConversion'] = _CALLCONVERSION
DESCRIPTOR.message_types_by_name['ExternalAttributionData'] = _EXTERNALATTRIBUTIONDATA
DESCRIPTOR.message_types_by_name['ClickConversionResult'] = _CLICKCONVERSIONRESULT
DESCRIPTOR.message_types_by_name['CallConversionResult'] = _CALLCONVERSIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadClickConversionsRequest = _reflection.GeneratedProtocolMessageType('UploadClickConversionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCLICKCONVERSIONSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.UploadClickConversionsRequest)
  })
_sym_db.RegisterMessage(UploadClickConversionsRequest)

UploadClickConversionsResponse = _reflection.GeneratedProtocolMessageType('UploadClickConversionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCLICKCONVERSIONSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.UploadClickConversionsResponse)
  })
_sym_db.RegisterMessage(UploadClickConversionsResponse)

UploadCallConversionsRequest = _reflection.GeneratedProtocolMessageType('UploadCallConversionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCALLCONVERSIONSREQUEST,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.UploadCallConversionsRequest)
  })
_sym_db.RegisterMessage(UploadCallConversionsRequest)

UploadCallConversionsResponse = _reflection.GeneratedProtocolMessageType('UploadCallConversionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCALLCONVERSIONSRESPONSE,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.UploadCallConversionsResponse)
  })
_sym_db.RegisterMessage(UploadCallConversionsResponse)

ClickConversion = _reflection.GeneratedProtocolMessageType('ClickConversion', (_message.Message,), {
  'DESCRIPTOR' : _CLICKCONVERSION,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ClickConversion)
  })
_sym_db.RegisterMessage(ClickConversion)

CallConversion = _reflection.GeneratedProtocolMessageType('CallConversion', (_message.Message,), {
  'DESCRIPTOR' : _CALLCONVERSION,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.CallConversion)
  })
_sym_db.RegisterMessage(CallConversion)

ExternalAttributionData = _reflection.GeneratedProtocolMessageType('ExternalAttributionData', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALATTRIBUTIONDATA,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ExternalAttributionData)
  })
_sym_db.RegisterMessage(ExternalAttributionData)

ClickConversionResult = _reflection.GeneratedProtocolMessageType('ClickConversionResult', (_message.Message,), {
  'DESCRIPTOR' : _CLICKCONVERSIONRESULT,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ClickConversionResult)
  })
_sym_db.RegisterMessage(ClickConversionResult)

CallConversionResult = _reflection.GeneratedProtocolMessageType('CallConversionResult', (_message.Message,), {
  'DESCRIPTOR' : _CALLCONVERSIONRESULT,
  '__module__' : 'google.ads.googleads.v2.services.conversion_upload_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.CallConversionResult)
  })
_sym_db.RegisterMessage(CallConversionResult)


DESCRIPTOR._options = None

_CONVERSIONUPLOADSERVICE = _descriptor.ServiceDescriptor(
  name='ConversionUploadService',
  full_name='google.ads.googleads.v2.services.ConversionUploadService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  serialized_start=2268,
  serialized_end=2764,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadClickConversions',
    full_name='google.ads.googleads.v2.services.ConversionUploadService.UploadClickConversions',
    index=0,
    containing_service=None,
    input_type=_UPLOADCLICKCONVERSIONSREQUEST,
    output_type=_UPLOADCLICKCONVERSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\0029\"4/v2/customers/{customer_id=*}:uploadClickConversions:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='UploadCallConversions',
    full_name='google.ads.googleads.v2.services.ConversionUploadService.UploadCallConversions',
    index=1,
    containing_service=None,
    input_type=_UPLOADCALLCONVERSIONSREQUEST,
    output_type=_UPLOADCALLCONVERSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\0028\"3/v2/customers/{customer_id=*}:uploadCallConversions:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_CONVERSIONUPLOADSERVICE)

DESCRIPTOR.services_by_name['ConversionUploadService'] = _CONVERSIONUPLOADSERVICE

# @@protoc_insertion_point(module_scope)
