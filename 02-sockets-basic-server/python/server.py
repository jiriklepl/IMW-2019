import socket
import time_pb2
import datetime

from shared import SERVER_PORT, SERVER_SOCKET_BACKLOG, SOCKET_BUFFER_SIZE

# Safe handling of resources that require releasing on exceptions.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_socket.bind(('', SERVER_PORT))
    server_socket.listen(SERVER_SOCKET_BACKLOG)

    print('Waiting for incoming connection.')

    while True:

        # Safe handling of resources that require releasing on exceptions.
        with server_socket.accept()[0] as client_socket:
            print('Accepted an incoming connection.')
            
            print('Receiving request now.')
    
            request = time_pb2.TimeRequest()
            request.ParseFromString(client_socket.recv(SOCKET_BUFFER_SIZE))

            answer = time_pb2.TimeMessage()
            now = datetime.datetime.now()

            if request.seconds: answer.seconds = now.seconds
            if request.minutes: answer.minutes = now.minutes
            if request.hours: answer.hours = now.hours
            if request.mday: answer.mday = now.mday
            if request.month: answer.month = now.month
            if request.year: answer.year = now.year
            if request.wday: answer.wday = now.wday
            if request.yday: answer.yday = now.yday
            if request.isdst: answer.isdst = now.isdst
            
            print('Sending answer now.')

            client_socket.send(answer.SerializeToString())

            print('Client disconnected.')

            # Shutdown precedes close to make sure protocol level shutdown is executed completely.
            # Close without shutdown may use RST instead of FIN to terminate connection, dropping data that is in flight.
            #
            # It is also possible to use shutdown to close input and output streams independently.
            client_socket.shutdown(socket.SHUT_RDWR)
