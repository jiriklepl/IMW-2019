# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.example.library.v1 import library_pb2 as google_dot_example_dot_library_dot_v1_dot_library__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class LibraryServiceStub(object):
  """This API represents a simple digital library.  It lets you manage Shelf
  resources and Book resources in the library. It defines the following
  resource model:

  - The API has a collection of [Shelf][google.example.library.v1.Shelf]
  resources, named `shelves/*`

  - Each Shelf has a collection of [Book][google.example.library.v1.Book]
  resources, named `shelves/*/books/*`
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateShelf = channel.unary_unary(
        '/google.example.library.v1.LibraryService/CreateShelf',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.CreateShelfRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Shelf.FromString,
        )
    self.GetShelf = channel.unary_unary(
        '/google.example.library.v1.LibraryService/GetShelf',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.GetShelfRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Shelf.FromString,
        )
    self.ListShelves = channel.unary_unary(
        '/google.example.library.v1.LibraryService/ListShelves',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListShelvesRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListShelvesResponse.FromString,
        )
    self.DeleteShelf = channel.unary_unary(
        '/google.example.library.v1.LibraryService/DeleteShelf',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.DeleteShelfRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.MergeShelves = channel.unary_unary(
        '/google.example.library.v1.LibraryService/MergeShelves',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.MergeShelvesRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Shelf.FromString,
        )
    self.CreateBook = channel.unary_unary(
        '/google.example.library.v1.LibraryService/CreateBook',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.CreateBookRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.FromString,
        )
    self.GetBook = channel.unary_unary(
        '/google.example.library.v1.LibraryService/GetBook',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.GetBookRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.FromString,
        )
    self.ListBooks = channel.unary_unary(
        '/google.example.library.v1.LibraryService/ListBooks',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListBooksRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListBooksResponse.FromString,
        )
    self.DeleteBook = channel.unary_unary(
        '/google.example.library.v1.LibraryService/DeleteBook',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.DeleteBookRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateBook = channel.unary_unary(
        '/google.example.library.v1.LibraryService/UpdateBook',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.UpdateBookRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.FromString,
        )
    self.MoveBook = channel.unary_unary(
        '/google.example.library.v1.LibraryService/MoveBook',
        request_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.MoveBookRequest.SerializeToString,
        response_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.FromString,
        )


class LibraryServiceServicer(object):
  """This API represents a simple digital library.  It lets you manage Shelf
  resources and Book resources in the library. It defines the following
  resource model:

  - The API has a collection of [Shelf][google.example.library.v1.Shelf]
  resources, named `shelves/*`

  - Each Shelf has a collection of [Book][google.example.library.v1.Book]
  resources, named `shelves/*/books/*`
  """

  def CreateShelf(self, request, context):
    """Creates a shelf, and returns the new Shelf.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetShelf(self, request, context):
    """Gets a shelf. Returns NOT_FOUND if the shelf does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListShelves(self, request, context):
    """Lists shelves. The order is unspecified but deterministic. Newly created
    shelves will not necessarily be added to the end of this list.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteShelf(self, request, context):
    """Deletes a shelf. Returns NOT_FOUND if the shelf does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MergeShelves(self, request, context):
    """Merges two shelves by adding all books from the shelf named
    `other_shelf_name` to shelf `name`, and deletes
    `other_shelf_name`. Returns the updated shelf.
    The book ids of the moved books may not be the same as the original books.

    Returns NOT_FOUND if either shelf does not exist.
    This call is a no-op if the specified shelves are the same.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateBook(self, request, context):
    """Creates a book, and returns the new Book.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBook(self, request, context):
    """Gets a book. Returns NOT_FOUND if the book does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBooks(self, request, context):
    """Lists books in a shelf. The order is unspecified but deterministic. Newly
    created books will not necessarily be added to the end of this list.
    Returns NOT_FOUND if the shelf does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteBook(self, request, context):
    """Deletes a book. Returns NOT_FOUND if the book does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateBook(self, request, context):
    """Updates a book. Returns INVALID_ARGUMENT if the name of the book
    is non-empty and does not equal the existing name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MoveBook(self, request, context):
    """Moves a book to another shelf, and returns the new book. The book
    id of the new book may not be the same as the original book.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LibraryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateShelf': grpc.unary_unary_rpc_method_handler(
          servicer.CreateShelf,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.CreateShelfRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Shelf.SerializeToString,
      ),
      'GetShelf': grpc.unary_unary_rpc_method_handler(
          servicer.GetShelf,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.GetShelfRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Shelf.SerializeToString,
      ),
      'ListShelves': grpc.unary_unary_rpc_method_handler(
          servicer.ListShelves,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListShelvesRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListShelvesResponse.SerializeToString,
      ),
      'DeleteShelf': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteShelf,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.DeleteShelfRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'MergeShelves': grpc.unary_unary_rpc_method_handler(
          servicer.MergeShelves,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.MergeShelvesRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Shelf.SerializeToString,
      ),
      'CreateBook': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBook,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.CreateBookRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.SerializeToString,
      ),
      'GetBook': grpc.unary_unary_rpc_method_handler(
          servicer.GetBook,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.GetBookRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.SerializeToString,
      ),
      'ListBooks': grpc.unary_unary_rpc_method_handler(
          servicer.ListBooks,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListBooksRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.ListBooksResponse.SerializeToString,
      ),
      'DeleteBook': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteBook,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.DeleteBookRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateBook': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateBook,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.UpdateBookRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.SerializeToString,
      ),
      'MoveBook': grpc.unary_unary_rpc_method_handler(
          servicer.MoveBook,
          request_deserializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.MoveBookRequest.FromString,
          response_serializer=google_dot_example_dot_library_dot_v1_dot_library__pb2.Book.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.example.library.v1.LibraryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
