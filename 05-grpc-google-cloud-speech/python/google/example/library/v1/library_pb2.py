# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/example/library/v1/library.proto

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
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/example/library/v1/library.proto',
  package='google.example.library.v1',
  syntax='proto3',
  serialized_options=b'\n\035com.google.example.library.v1B\014LibraryProtoP\001Z@google.golang.org/genproto/googleapis/example/library/v1;library',
  serialized_pb=b'\n\'google/example/library/v1/library.proto\x12\x19google.example.library.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xbc\x01\n\x04\x42ook\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#library-example.googleapis.com/Book\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04read\x18\x04 \x01(\x08:L\xea\x41I\n#library-example.googleapis.com/Book\x12\"shelves/{shelf_id}/books/{book_id}\"\x91\x01\n\x05Shelf\x12:\n\x04name\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\n$library-example.googleapis.com/Shelf\x12\r\n\x05theme\x18\x02 \x01(\t:=\xea\x41:\n$library-example.googleapis.com/Shelf\x12\x12shelves/{shelf_id}\"J\n\x12\x43reateShelfRequest\x12\x34\n\x05shelf\x18\x01 \x01(\x0b\x32 .google.example.library.v1.ShelfB\x03\xe0\x41\x02\".\n\x0fGetShelfRequest\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf\";\n\x12ListShelvesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"a\n\x13ListShelvesResponse\x12\x31\n\x07shelves\x18\x01 \x03(\x0b\x32 .google.example.library.v1.Shelf\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"1\n\x12\x44\x65leteShelfRequest\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf\"[\n\x13MergeShelvesRequest\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf\x12\'\n\x10other_shelf_name\x18\x02 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf\"d\n\x11\x43reateBookRequest\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf\x12\x32\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x1f.google.example.library.v1.BookB\x03\xe0\x41\x02\",\n\x0eGetBookRequest\x12\x1a\n\x04name\x18\x01 \x01(\tB\x0c\xe0\x41\x02\xfa\x41\x06\n\x04\x42ook\"V\n\x10ListBooksRequest\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\\\n\x11ListBooksResponse\x12.\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x1f.google.example.library.v1.Book\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"Z\n\x11UpdateBookRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x32\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x1f.google.example.library.v1.BookB\x03\xe0\x41\x02\"/\n\x11\x44\x65leteBookRequest\x12\x1a\n\x04name\x18\x01 \x01(\tB\x0c\xe0\x41\x02\xfa\x41\x06\n\x04\x42ook\"V\n\x0fMoveBookRequest\x12\x1a\n\x04name\x18\x01 \x01(\tB\x0c\xe0\x41\x02\xfa\x41\x06\n\x04\x42ook\x12\'\n\x10other_shelf_name\x18\x02 \x01(\tB\r\xe0\x41\x02\xfa\x41\x07\n\x05Shelf2\x92\x0c\n\x0eLibraryService\x12\x82\x01\n\x0b\x43reateShelf\x12-.google.example.library.v1.CreateShelfRequest\x1a .google.example.library.v1.Shelf\"\"\x82\xd3\xe4\x93\x02\x14\"\x0b/v1/shelves:\x05shelf\xda\x41\x05shelf\x12}\n\x08GetShelf\x12*.google.example.library.v1.GetShelfRequest\x1a .google.example.library.v1.Shelf\"#\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/{name=shelves/*}\xda\x41\x04name\x12\x81\x01\n\x0bListShelves\x12-.google.example.library.v1.ListShelvesRequest\x1a..google.example.library.v1.ListShelvesResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/shelves\x12y\n\x0b\x44\x65leteShelf\x12-.google.example.library.v1.DeleteShelfRequest\x1a\x16.google.protobuf.Empty\"#\x82\xd3\xe4\x93\x02\x16*\x14/v1/{name=shelves/*}\xda\x41\x04name\x12\x9f\x01\n\x0cMergeShelves\x12..google.example.library.v1.MergeShelvesRequest\x1a .google.example.library.v1.Shelf\"=\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/{name=shelves/*}:merge:\x01*\xda\x41\x15name,other_shelf_name\x12\x91\x01\n\nCreateBook\x12,.google.example.library.v1.CreateBookRequest\x1a\x1f.google.example.library.v1.Book\"4\x82\xd3\xe4\x93\x02\"\"\x1a/v1/{name=shelves/*}/books:\x04\x62ook\xda\x41\tname,book\x12\x82\x01\n\x07GetBook\x12).google.example.library.v1.GetBookRequest\x1a\x1f.google.example.library.v1.Book\"+\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=shelves/*/books/*}\xda\x41\x04name\x12\x91\x01\n\tListBooks\x12+.google.example.library.v1.ListBooksRequest\x1a,.google.example.library.v1.ListBooksResponse\")\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/{name=shelves/*}/books\xda\x41\x04name\x12x\n\nDeleteBook\x12,.google.example.library.v1.DeleteBookRequest\x1a\x16.google.protobuf.Empty\"$\x82\xd3\xe4\x93\x02\x1e*\x1c/v1/{name=shelves/*/books/*}\x12\x93\x01\n\nUpdateBook\x12,.google.example.library.v1.UpdateBookRequest\x1a\x1f.google.example.library.v1.Book\"6\x82\xd3\xe4\x93\x02)\x1a!/v1/{book.name=shelves/*/books/*}:\x04\x62ook\xda\x41\x04\x62ook\x12\x9d\x01\n\x08MoveBook\x12*.google.example.library.v1.MoveBookRequest\x1a\x1f.google.example.library.v1.Book\"D\x82\xd3\xe4\x93\x02&\"!/v1/{name=shelves/*/books/*}:move:\x01*\xda\x41\x15name,other_shelf_nameBq\n\x1d\x63om.google.example.library.v1B\x0cLibraryProtoP\x01Z@google.golang.org/genproto/googleapis/example/library/v1;libraryb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='google.example.library.v1.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.Book.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A%\n#library-example.googleapis.com/Book', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='google.example.library.v1.Book.author', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='google.example.library.v1.Book.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read', full_name='google.example.library.v1.Book.read', index=3,
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
  serialized_options=b'\352AI\n#library-example.googleapis.com/Book\022\"shelves/{shelf_id}/books/{book_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=403,
)


_SHELF = _descriptor.Descriptor(
  name='Shelf',
  full_name='google.example.library.v1.Shelf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.Shelf.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A&\n$library-example.googleapis.com/Shelf', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme', full_name='google.example.library.v1.Shelf.theme', index=1,
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
  serialized_options=b'\352A:\n$library-example.googleapis.com/Shelf\022\022shelves/{shelf_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=551,
)


_CREATESHELFREQUEST = _descriptor.Descriptor(
  name='CreateShelfRequest',
  full_name='google.example.library.v1.CreateShelfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='google.example.library.v1.CreateShelfRequest.shelf', index=0,
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
  serialized_start=553,
  serialized_end=627,
)


_GETSHELFREQUEST = _descriptor.Descriptor(
  name='GetShelfRequest',
  full_name='google.example.library.v1.GetShelfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.GetShelfRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
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
  serialized_start=629,
  serialized_end=675,
)


_LISTSHELVESREQUEST = _descriptor.Descriptor(
  name='ListShelvesRequest',
  full_name='google.example.library.v1.ListShelvesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.example.library.v1.ListShelvesRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.example.library.v1.ListShelvesRequest.page_token', index=1,
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
  serialized_start=677,
  serialized_end=736,
)


_LISTSHELVESRESPONSE = _descriptor.Descriptor(
  name='ListShelvesResponse',
  full_name='google.example.library.v1.ListShelvesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelves', full_name='google.example.library.v1.ListShelvesResponse.shelves', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.example.library.v1.ListShelvesResponse.next_page_token', index=1,
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
  serialized_start=738,
  serialized_end=835,
)


_DELETESHELFREQUEST = _descriptor.Descriptor(
  name='DeleteShelfRequest',
  full_name='google.example.library.v1.DeleteShelfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.DeleteShelfRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
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
  serialized_start=837,
  serialized_end=886,
)


_MERGESHELVESREQUEST = _descriptor.Descriptor(
  name='MergeShelvesRequest',
  full_name='google.example.library.v1.MergeShelvesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.MergeShelvesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_shelf_name', full_name='google.example.library.v1.MergeShelvesRequest.other_shelf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
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
  serialized_start=888,
  serialized_end=979,
)


_CREATEBOOKREQUEST = _descriptor.Descriptor(
  name='CreateBookRequest',
  full_name='google.example.library.v1.CreateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.CreateBookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book', full_name='google.example.library.v1.CreateBookRequest.book', index=1,
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
  serialized_start=981,
  serialized_end=1081,
)


_GETBOOKREQUEST = _descriptor.Descriptor(
  name='GetBookRequest',
  full_name='google.example.library.v1.GetBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.GetBookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\006\n\004Book', file=DESCRIPTOR),
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
  serialized_start=1083,
  serialized_end=1127,
)


_LISTBOOKSREQUEST = _descriptor.Descriptor(
  name='ListBooksRequest',
  full_name='google.example.library.v1.ListBooksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.ListBooksRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.example.library.v1.ListBooksRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.example.library.v1.ListBooksRequest.page_token', index=2,
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
  serialized_start=1129,
  serialized_end=1215,
)


_LISTBOOKSRESPONSE = _descriptor.Descriptor(
  name='ListBooksResponse',
  full_name='google.example.library.v1.ListBooksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='google.example.library.v1.ListBooksResponse.books', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.example.library.v1.ListBooksResponse.next_page_token', index=1,
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
  serialized_start=1217,
  serialized_end=1309,
)


_UPDATEBOOKREQUEST = _descriptor.Descriptor(
  name='UpdateBookRequest',
  full_name='google.example.library.v1.UpdateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.UpdateBookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book', full_name='google.example.library.v1.UpdateBookRequest.book', index=1,
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
  serialized_start=1311,
  serialized_end=1401,
)


_DELETEBOOKREQUEST = _descriptor.Descriptor(
  name='DeleteBookRequest',
  full_name='google.example.library.v1.DeleteBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.DeleteBookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\006\n\004Book', file=DESCRIPTOR),
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
  serialized_start=1403,
  serialized_end=1450,
)


_MOVEBOOKREQUEST = _descriptor.Descriptor(
  name='MoveBookRequest',
  full_name='google.example.library.v1.MoveBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.library.v1.MoveBookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\006\n\004Book', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_shelf_name', full_name='google.example.library.v1.MoveBookRequest.other_shelf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\007\n\005Shelf', file=DESCRIPTOR),
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
  serialized_start=1452,
  serialized_end=1538,
)

_CREATESHELFREQUEST.fields_by_name['shelf'].message_type = _SHELF
_LISTSHELVESRESPONSE.fields_by_name['shelves'].message_type = _SHELF
_CREATEBOOKREQUEST.fields_by_name['book'].message_type = _BOOK
_LISTBOOKSRESPONSE.fields_by_name['books'].message_type = _BOOK
_UPDATEBOOKREQUEST.fields_by_name['book'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['Shelf'] = _SHELF
DESCRIPTOR.message_types_by_name['CreateShelfRequest'] = _CREATESHELFREQUEST
DESCRIPTOR.message_types_by_name['GetShelfRequest'] = _GETSHELFREQUEST
DESCRIPTOR.message_types_by_name['ListShelvesRequest'] = _LISTSHELVESREQUEST
DESCRIPTOR.message_types_by_name['ListShelvesResponse'] = _LISTSHELVESRESPONSE
DESCRIPTOR.message_types_by_name['DeleteShelfRequest'] = _DELETESHELFREQUEST
DESCRIPTOR.message_types_by_name['MergeShelvesRequest'] = _MERGESHELVESREQUEST
DESCRIPTOR.message_types_by_name['CreateBookRequest'] = _CREATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookRequest'] = _GETBOOKREQUEST
DESCRIPTOR.message_types_by_name['ListBooksRequest'] = _LISTBOOKSREQUEST
DESCRIPTOR.message_types_by_name['ListBooksResponse'] = _LISTBOOKSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateBookRequest'] = _UPDATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['DeleteBookRequest'] = _DELETEBOOKREQUEST
DESCRIPTOR.message_types_by_name['MoveBookRequest'] = _MOVEBOOKREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.Book)
  })
_sym_db.RegisterMessage(Book)

Shelf = _reflection.GeneratedProtocolMessageType('Shelf', (_message.Message,), {
  'DESCRIPTOR' : _SHELF,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.Shelf)
  })
_sym_db.RegisterMessage(Shelf)

CreateShelfRequest = _reflection.GeneratedProtocolMessageType('CreateShelfRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESHELFREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.CreateShelfRequest)
  })
_sym_db.RegisterMessage(CreateShelfRequest)

GetShelfRequest = _reflection.GeneratedProtocolMessageType('GetShelfRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSHELFREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.GetShelfRequest)
  })
_sym_db.RegisterMessage(GetShelfRequest)

ListShelvesRequest = _reflection.GeneratedProtocolMessageType('ListShelvesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSHELVESREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.ListShelvesRequest)
  })
_sym_db.RegisterMessage(ListShelvesRequest)

ListShelvesResponse = _reflection.GeneratedProtocolMessageType('ListShelvesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSHELVESRESPONSE,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.ListShelvesResponse)
  })
_sym_db.RegisterMessage(ListShelvesResponse)

DeleteShelfRequest = _reflection.GeneratedProtocolMessageType('DeleteShelfRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESHELFREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.DeleteShelfRequest)
  })
_sym_db.RegisterMessage(DeleteShelfRequest)

MergeShelvesRequest = _reflection.GeneratedProtocolMessageType('MergeShelvesRequest', (_message.Message,), {
  'DESCRIPTOR' : _MERGESHELVESREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.MergeShelvesRequest)
  })
_sym_db.RegisterMessage(MergeShelvesRequest)

CreateBookRequest = _reflection.GeneratedProtocolMessageType('CreateBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOOKREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.CreateBookRequest)
  })
_sym_db.RegisterMessage(CreateBookRequest)

GetBookRequest = _reflection.GeneratedProtocolMessageType('GetBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.GetBookRequest)
  })
_sym_db.RegisterMessage(GetBookRequest)

ListBooksRequest = _reflection.GeneratedProtocolMessageType('ListBooksRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBOOKSREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.ListBooksRequest)
  })
_sym_db.RegisterMessage(ListBooksRequest)

ListBooksResponse = _reflection.GeneratedProtocolMessageType('ListBooksResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBOOKSRESPONSE,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.ListBooksResponse)
  })
_sym_db.RegisterMessage(ListBooksResponse)

UpdateBookRequest = _reflection.GeneratedProtocolMessageType('UpdateBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBOOKREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.UpdateBookRequest)
  })
_sym_db.RegisterMessage(UpdateBookRequest)

DeleteBookRequest = _reflection.GeneratedProtocolMessageType('DeleteBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBOOKREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.DeleteBookRequest)
  })
_sym_db.RegisterMessage(DeleteBookRequest)

MoveBookRequest = _reflection.GeneratedProtocolMessageType('MoveBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVEBOOKREQUEST,
  '__module__' : 'google.example.library.v1.library_pb2'
  # @@protoc_insertion_point(class_scope:google.example.library.v1.MoveBookRequest)
  })
_sym_db.RegisterMessage(MoveBookRequest)


DESCRIPTOR._options = None
_BOOK.fields_by_name['name']._options = None
_BOOK._options = None
_SHELF.fields_by_name['name']._options = None
_SHELF._options = None
_CREATESHELFREQUEST.fields_by_name['shelf']._options = None
_GETSHELFREQUEST.fields_by_name['name']._options = None
_DELETESHELFREQUEST.fields_by_name['name']._options = None
_MERGESHELVESREQUEST.fields_by_name['name']._options = None
_MERGESHELVESREQUEST.fields_by_name['other_shelf_name']._options = None
_CREATEBOOKREQUEST.fields_by_name['name']._options = None
_CREATEBOOKREQUEST.fields_by_name['book']._options = None
_GETBOOKREQUEST.fields_by_name['name']._options = None
_LISTBOOKSREQUEST.fields_by_name['name']._options = None
_UPDATEBOOKREQUEST.fields_by_name['name']._options = None
_UPDATEBOOKREQUEST.fields_by_name['book']._options = None
_DELETEBOOKREQUEST.fields_by_name['name']._options = None
_MOVEBOOKREQUEST.fields_by_name['name']._options = None
_MOVEBOOKREQUEST.fields_by_name['other_shelf_name']._options = None

_LIBRARYSERVICE = _descriptor.ServiceDescriptor(
  name='LibraryService',
  full_name='google.example.library.v1.LibraryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1541,
  serialized_end=3095,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateShelf',
    full_name='google.example.library.v1.LibraryService.CreateShelf',
    index=0,
    containing_service=None,
    input_type=_CREATESHELFREQUEST,
    output_type=_SHELF,
    serialized_options=b'\202\323\344\223\002\024\"\013/v1/shelves:\005shelf\332A\005shelf',
  ),
  _descriptor.MethodDescriptor(
    name='GetShelf',
    full_name='google.example.library.v1.LibraryService.GetShelf',
    index=1,
    containing_service=None,
    input_type=_GETSHELFREQUEST,
    output_type=_SHELF,
    serialized_options=b'\202\323\344\223\002\026\022\024/v1/{name=shelves/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='ListShelves',
    full_name='google.example.library.v1.LibraryService.ListShelves',
    index=2,
    containing_service=None,
    input_type=_LISTSHELVESREQUEST,
    output_type=_LISTSHELVESRESPONSE,
    serialized_options=b'\202\323\344\223\002\r\022\013/v1/shelves',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteShelf',
    full_name='google.example.library.v1.LibraryService.DeleteShelf',
    index=3,
    containing_service=None,
    input_type=_DELETESHELFREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\026*\024/v1/{name=shelves/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='MergeShelves',
    full_name='google.example.library.v1.LibraryService.MergeShelves',
    index=4,
    containing_service=None,
    input_type=_MERGESHELVESREQUEST,
    output_type=_SHELF,
    serialized_options=b'\202\323\344\223\002\037\"\032/v1/{name=shelves/*}:merge:\001*\332A\025name,other_shelf_name',
  ),
  _descriptor.MethodDescriptor(
    name='CreateBook',
    full_name='google.example.library.v1.LibraryService.CreateBook',
    index=5,
    containing_service=None,
    input_type=_CREATEBOOKREQUEST,
    output_type=_BOOK,
    serialized_options=b'\202\323\344\223\002\"\"\032/v1/{name=shelves/*}/books:\004book\332A\tname,book',
  ),
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='google.example.library.v1.LibraryService.GetBook',
    index=6,
    containing_service=None,
    input_type=_GETBOOKREQUEST,
    output_type=_BOOK,
    serialized_options=b'\202\323\344\223\002\036\022\034/v1/{name=shelves/*/books/*}\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='ListBooks',
    full_name='google.example.library.v1.LibraryService.ListBooks',
    index=7,
    containing_service=None,
    input_type=_LISTBOOKSREQUEST,
    output_type=_LISTBOOKSRESPONSE,
    serialized_options=b'\202\323\344\223\002\034\022\032/v1/{name=shelves/*}/books\332A\004name',
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBook',
    full_name='google.example.library.v1.LibraryService.DeleteBook',
    index=8,
    containing_service=None,
    input_type=_DELETEBOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\036*\034/v1/{name=shelves/*/books/*}',
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBook',
    full_name='google.example.library.v1.LibraryService.UpdateBook',
    index=9,
    containing_service=None,
    input_type=_UPDATEBOOKREQUEST,
    output_type=_BOOK,
    serialized_options=b'\202\323\344\223\002)\032!/v1/{book.name=shelves/*/books/*}:\004book\332A\004book',
  ),
  _descriptor.MethodDescriptor(
    name='MoveBook',
    full_name='google.example.library.v1.LibraryService.MoveBook',
    index=10,
    containing_service=None,
    input_type=_MOVEBOOKREQUEST,
    output_type=_BOOK,
    serialized_options=b'\202\323\344\223\002&\"!/v1/{name=shelves/*/books/*}:move:\001*\332A\025name,other_shelf_name',
  ),
])
_sym_db.RegisterServiceDescriptor(_LIBRARYSERVICE)

DESCRIPTOR.services_by_name['LibraryService'] = _LIBRARYSERVICE

# @@protoc_insertion_point(module_scope)
