import grpc
import time
import sys

sys.path.append('.')

from concurrent import futures

from shared import *

from proto.time_pb2 import *
from proto.time_pb2_grpc import *


# Service implementation.
#
# The implementation inherits from a generated base class.

class MyServicer (TimeServiceServicer):
    def GetTime (self, request, context):
        now = time.localtime(time.time())
        response = TimeMessage ()
        if request.seconds:
            response.seconds = now.tm_sec
        if request.minutes:
            response.minutes = now.tm_min
        if request.hours:
            response.hours = now.tm_hour
        if request.mday:
            response.mday = now.tm_mday
        if request.month:
            response.month = now.tm_mon
        if request.year:
            response.year = now.tm_year
        if request.wday:
            response.wday = now.tm_wday
        if request.yday:
            response.yday = now.tm_yday
        if request.isdst:
            response.isdst = now.tm_isdst
        return response


# Create the server object.
#
# The server object represents the server runtime.
# It needs to be told what service to provide
# and what port to listen on.

server = grpc.server (futures.ThreadPoolExecutor (max_workers = SERVER_THREAD_COUNT))
add_TimeServiceServicer_to_server (MyServicer (), server)
server.add_insecure_port (SERVER_ADDR)
server.start ()

# Sleep to prevent server termination.

while True:
    time.sleep (1)
