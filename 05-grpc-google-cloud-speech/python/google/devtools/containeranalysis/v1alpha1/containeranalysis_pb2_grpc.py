# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.devtools.containeranalysis.v1alpha1 import containeranalysis_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ContainerAnalysisStub(object):
  """Retrieves the results of vulnerability scanning of cloud components such as
  container images. The Container Analysis API is an implementation of the
  [Grafeas](grafeas.io) API.

  The vulnerability results are stored as a series of Occurrences.
  An `Occurrence` contains information about a specific vulnerability in a
  resource. An `Occurrence` references a `Note`. A `Note` contains details
  about the vulnerability and is stored in a stored in a separate project.
  Multiple `Occurrences` can reference the same `Note`. For example, an SSL
  vulnerability could affect multiple packages in an image. In this case,
  there would be one `Note` for the vulnerability and an `Occurrence` for
  each package with the vulnerability referencing that `Note`.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOccurrence = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/GetOccurrence',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetOccurrenceRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Occurrence.FromString,
        )
    self.ListOccurrences = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/ListOccurrences',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListOccurrencesRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListOccurrencesResponse.FromString,
        )
    self.DeleteOccurrence = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/DeleteOccurrence',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.DeleteOccurrenceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateOccurrence = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/CreateOccurrence',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.CreateOccurrenceRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Occurrence.FromString,
        )
    self.UpdateOccurrence = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/UpdateOccurrence',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateOccurrenceRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Occurrence.FromString,
        )
    self.GetOccurrenceNote = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/GetOccurrenceNote',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetOccurrenceNoteRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.FromString,
        )
    self.GetNote = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/GetNote',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetNoteRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.FromString,
        )
    self.ListNotes = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/ListNotes',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNotesRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNotesResponse.FromString,
        )
    self.DeleteNote = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/DeleteNote',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.DeleteNoteRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateNote = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/CreateNote',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.CreateNoteRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.FromString,
        )
    self.UpdateNote = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/UpdateNote',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateNoteRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.FromString,
        )
    self.ListNoteOccurrences = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/ListNoteOccurrences',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNoteOccurrencesRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNoteOccurrencesResponse.FromString,
        )
    self.GetVulnzOccurrencesSummary = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/GetVulnzOccurrencesSummary',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetVulnzOccurrencesSummaryRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetVulnzOccurrencesSummaryResponse.FromString,
        )
    self.SetIamPolicy = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/SetIamPolicy',
        request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString,
        response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString,
        )
    self.GetIamPolicy = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/GetIamPolicy',
        request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString,
        response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString,
        )
    self.TestIamPermissions = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/TestIamPermissions',
        request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString,
        response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString,
        )
    self.CreateOperation = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/CreateOperation',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.CreateOperationRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.UpdateOperation = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/UpdateOperation',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateOperationRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.GetScanConfig = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/GetScanConfig',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetScanConfigRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ScanConfig.FromString,
        )
    self.ListScanConfigs = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/ListScanConfigs',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListScanConfigsRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListScanConfigsResponse.FromString,
        )
    self.UpdateScanConfig = channel.unary_unary(
        '/google.devtools.containeranalysis.v1alpha1.ContainerAnalysis/UpdateScanConfig',
        request_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateScanConfigRequest.SerializeToString,
        response_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ScanConfig.FromString,
        )


class ContainerAnalysisServicer(object):
  """Retrieves the results of vulnerability scanning of cloud components such as
  container images. The Container Analysis API is an implementation of the
  [Grafeas](grafeas.io) API.

  The vulnerability results are stored as a series of Occurrences.
  An `Occurrence` contains information about a specific vulnerability in a
  resource. An `Occurrence` references a `Note`. A `Note` contains details
  about the vulnerability and is stored in a stored in a separate project.
  Multiple `Occurrences` can reference the same `Note`. For example, an SSL
  vulnerability could affect multiple packages in an image. In this case,
  there would be one `Note` for the vulnerability and an `Occurrence` for
  each package with the vulnerability referencing that `Note`.
  """

  def GetOccurrence(self, request, context):
    """Returns the requested `Occurrence`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOccurrences(self, request, context):
    """Lists active `Occurrences` for a given project matching the filters.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteOccurrence(self, request, context):
    """Deletes the given `Occurrence` from the system. Use this when
    an `Occurrence` is no longer applicable for the given resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateOccurrence(self, request, context):
    """Creates a new `Occurrence`. Use this method to create `Occurrences`
    for a resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateOccurrence(self, request, context):
    """Updates an existing occurrence.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOccurrenceNote(self, request, context):
    """Gets the `Note` attached to the given `Occurrence`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNote(self, request, context):
    """Returns the requested `Note`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListNotes(self, request, context):
    """Lists all `Notes` for a given project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteNote(self, request, context):
    """Deletes the given `Note` from the system.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateNote(self, request, context):
    """Creates a new `Note`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateNote(self, request, context):
    """Updates an existing `Note`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListNoteOccurrences(self, request, context):
    """Lists `Occurrences` referencing the specified `Note`. Use this method to
    get all occurrences referencing your `Note` across all your customer
    projects.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVulnzOccurrencesSummary(self, request, context):
    """Gets a summary of the number and severity of occurrences.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetIamPolicy(self, request, context):
    """Sets the access control policy on the specified `Note` or `Occurrence`.
    Requires `containeranalysis.notes.setIamPolicy` or
    `containeranalysis.occurrences.setIamPolicy` permission if the resource is
    a `Note` or an `Occurrence`, respectively.
    Attempting to call this method without these permissions will result in a `
    `PERMISSION_DENIED` error.
    Attempting to call this method on a non-existent resource will result in a
    `NOT_FOUND` error if the user has `containeranalysis.notes.list` permission
    on a `Note` or `containeranalysis.occurrences.list` on an `Occurrence`, or
    a `PERMISSION_DENIED` error otherwise. The resource takes the following
    formats: `projects/{projectid}/occurrences/{occurrenceid}` for occurrences
    and projects/{projectid}/notes/{noteid} for notes
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetIamPolicy(self, request, context):
    """Gets the access control policy for a note or an `Occurrence` resource.
    Requires `containeranalysis.notes.setIamPolicy` or
    `containeranalysis.occurrences.setIamPolicy` permission if the resource is
    a note or occurrence, respectively.
    Attempting to call this method on a resource without the required
    permission will result in a `PERMISSION_DENIED` error. Attempting to call
    this method on a non-existent resource will result in a `NOT_FOUND` error
    if the user has list permission on the project, or a `PERMISSION_DENIED`
    error otherwise. The resource takes the following formats:
    `projects/{PROJECT_ID}/occurrences/{OCCURRENCE_ID}` for occurrences and
    projects/{PROJECT_ID}/notes/{NOTE_ID} for notes
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TestIamPermissions(self, request, context):
    """Returns the permissions that a caller has on the specified note or
    occurrence resource. Requires list permission on the project (for example,
    "storage.objects.list" on the containing bucket for testing permission of
    an object). Attempting to call this method on a non-existent resource will
    result in a `NOT_FOUND` error if the user has list permission on the
    project, or a `PERMISSION_DENIED` error otherwise. The resource takes the
    following formats: `projects/{PROJECT_ID}/occurrences/{OCCURRENCE_ID}` for
    `Occurrences` and `projects/{PROJECT_ID}/notes/{NOTE_ID}` for `Notes`
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateOperation(self, request, context):
    """Creates a new `Operation`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateOperation(self, request, context):
    """Updates an existing operation returns an error if operation
    does not exist. The only valid operations are to update mark the done bit
    change the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetScanConfig(self, request, context):
    """Gets a specific scan configuration for a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListScanConfigs(self, request, context):
    """Lists scan configurations for a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateScanConfig(self, request, context):
    """Updates the scan configuration to a new value.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ContainerAnalysisServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOccurrence': grpc.unary_unary_rpc_method_handler(
          servicer.GetOccurrence,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetOccurrenceRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Occurrence.SerializeToString,
      ),
      'ListOccurrences': grpc.unary_unary_rpc_method_handler(
          servicer.ListOccurrences,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListOccurrencesRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListOccurrencesResponse.SerializeToString,
      ),
      'DeleteOccurrence': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteOccurrence,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.DeleteOccurrenceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateOccurrence': grpc.unary_unary_rpc_method_handler(
          servicer.CreateOccurrence,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.CreateOccurrenceRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Occurrence.SerializeToString,
      ),
      'UpdateOccurrence': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateOccurrence,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateOccurrenceRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Occurrence.SerializeToString,
      ),
      'GetOccurrenceNote': grpc.unary_unary_rpc_method_handler(
          servicer.GetOccurrenceNote,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetOccurrenceNoteRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.SerializeToString,
      ),
      'GetNote': grpc.unary_unary_rpc_method_handler(
          servicer.GetNote,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetNoteRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.SerializeToString,
      ),
      'ListNotes': grpc.unary_unary_rpc_method_handler(
          servicer.ListNotes,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNotesRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNotesResponse.SerializeToString,
      ),
      'DeleteNote': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteNote,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.DeleteNoteRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateNote': grpc.unary_unary_rpc_method_handler(
          servicer.CreateNote,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.CreateNoteRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.SerializeToString,
      ),
      'UpdateNote': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateNote,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateNoteRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.Note.SerializeToString,
      ),
      'ListNoteOccurrences': grpc.unary_unary_rpc_method_handler(
          servicer.ListNoteOccurrences,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNoteOccurrencesRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListNoteOccurrencesResponse.SerializeToString,
      ),
      'GetVulnzOccurrencesSummary': grpc.unary_unary_rpc_method_handler(
          servicer.GetVulnzOccurrencesSummary,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetVulnzOccurrencesSummaryRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetVulnzOccurrencesSummaryResponse.SerializeToString,
      ),
      'SetIamPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.SetIamPolicy,
          request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString,
          response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString,
      ),
      'GetIamPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetIamPolicy,
          request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString,
          response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString,
      ),
      'TestIamPermissions': grpc.unary_unary_rpc_method_handler(
          servicer.TestIamPermissions,
          request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString,
          response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString,
      ),
      'CreateOperation': grpc.unary_unary_rpc_method_handler(
          servicer.CreateOperation,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.CreateOperationRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'UpdateOperation': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateOperation,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateOperationRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'GetScanConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetScanConfig,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.GetScanConfigRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ScanConfig.SerializeToString,
      ),
      'ListScanConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.ListScanConfigs,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListScanConfigsRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ListScanConfigsResponse.SerializeToString,
      ),
      'UpdateScanConfig': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateScanConfig,
          request_deserializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.UpdateScanConfigRequest.FromString,
          response_serializer=google_dot_devtools_dot_containeranalysis_dot_v1alpha1_dot_containeranalysis__pb2.ScanConfig.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.devtools.containeranalysis.v1alpha1.ContainerAnalysis', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))