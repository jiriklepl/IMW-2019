# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.dataproc.v1beta2 import jobs_pb2 as google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class JobControllerStub(object):
  """The JobController provides methods to manage jobs.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubmitJob = channel.unary_unary(
        '/google.cloud.dataproc.v1beta2.JobController/SubmitJob',
        request_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.SubmitJobRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.FromString,
        )
    self.GetJob = channel.unary_unary(
        '/google.cloud.dataproc.v1beta2.JobController/GetJob',
        request_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.GetJobRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.FromString,
        )
    self.ListJobs = channel.unary_unary(
        '/google.cloud.dataproc.v1beta2.JobController/ListJobs',
        request_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.ListJobsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.ListJobsResponse.FromString,
        )
    self.UpdateJob = channel.unary_unary(
        '/google.cloud.dataproc.v1beta2.JobController/UpdateJob',
        request_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.UpdateJobRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.FromString,
        )
    self.CancelJob = channel.unary_unary(
        '/google.cloud.dataproc.v1beta2.JobController/CancelJob',
        request_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.CancelJobRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.FromString,
        )
    self.DeleteJob = channel.unary_unary(
        '/google.cloud.dataproc.v1beta2.JobController/DeleteJob',
        request_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.DeleteJobRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class JobControllerServicer(object):
  """The JobController provides methods to manage jobs.
  """

  def SubmitJob(self, request, context):
    """Submits a job to a cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetJob(self, request, context):
    """Gets the resource representation for a job in a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListJobs(self, request, context):
    """Lists regions/{region}/jobs in a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateJob(self, request, context):
    """Updates a job in a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelJob(self, request, context):
    """Starts a job cancellation request. To access the job resource
    after cancellation, call
    [regions/{region}/jobs.list](/dataproc/docs/reference/rest/v1beta2/projects.regions.jobs/list)
    or
    [regions/{region}/jobs.get](/dataproc/docs/reference/rest/v1beta2/projects.regions.jobs/get).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteJob(self, request, context):
    """Deletes the job from the project. If the job is active, the delete fails,
    and the response returns `FAILED_PRECONDITION`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubmitJob': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitJob,
          request_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.SubmitJobRequest.FromString,
          response_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.SerializeToString,
      ),
      'GetJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetJob,
          request_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.GetJobRequest.FromString,
          response_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.SerializeToString,
      ),
      'ListJobs': grpc.unary_unary_rpc_method_handler(
          servicer.ListJobs,
          request_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.ListJobsRequest.FromString,
          response_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.ListJobsResponse.SerializeToString,
      ),
      'UpdateJob': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateJob,
          request_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.UpdateJobRequest.FromString,
          response_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.SerializeToString,
      ),
      'CancelJob': grpc.unary_unary_rpc_method_handler(
          servicer.CancelJob,
          request_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.CancelJobRequest.FromString,
          response_serializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.Job.SerializeToString,
      ),
      'DeleteJob': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteJob,
          request_deserializer=google_dot_cloud_dot_dataproc_dot_v1beta2_dot_jobs__pb2.DeleteJobRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.dataproc.v1beta2.JobController', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
