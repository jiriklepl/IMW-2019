import grpc

from shared import *

from time_pb2 import *
from time_pb2_grpc import *

# Create the channel used to connect to the server.
crt_data = open ('server.crt', 'rb').read ()
credentials = grpc.ssl_channel_credentials (root_certificates = crt_data)
with grpc.secure_channel (SERVER_ADDR, credentials) as channel:

    # Create a stub object that provides the service interface.
    stub = TimeServiceStub (channel)

    request = TimeRequest()
    for arg in sys.argv[1:]:
        if arg == 'seconds':
            request.seconds = True
        elif arg == 'minutes':
            request.minutes = True
        elif arg == 'hours':
            request.hours = True
        elif arg == 'mday':
            request.mday = True
        elif arg == 'month':
            request.month = True
        elif arg == 'year':
            request.year = True
        elif arg == 'wday':
            request.wday = True
        elif arg == 'yday':
            request.yday = True
        elif arg == 'isdst':
            request.isdst = True
    print('Message:')
    print(request)

    # Call the service through the stub object.
    response = stub.GetTime (request)

    print('Response:')
    print(response)
