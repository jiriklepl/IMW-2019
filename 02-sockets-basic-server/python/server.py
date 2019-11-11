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

            while True:
                data = client_socket.recv (SOCKET_BUFFER_SIZE)
                print(data)
                if len (data) == 0 or request.ParseFromString(data):
                    break
                

            answer = time_pb2.TimeMessage()
            now = datetime.datetime.now()

            if request.seconds == True: answer.seconds = now.seconds
            if request.minutes == True: answer.minutes = now.minutes
            if request.hours == True: answer.hours = now.hours
            if request.mday == True: answer.mday = now.mday
            if request.month == True: answer.month = now.month
            if request.year == True: answer.year = now.year
            if request.wday == True: answer.wday = now.wday
            if request.yday == True: answer.yday = now.yday
            if request.isdst == True: answer.isdst = now.isdst
            
            print('Sending answer now.')

            data = answer.SerializeToString()
            client_socket.send(data)

            print('Client disconnected.')

            # Shutdown precedes close to make sure protocol level shutdown is executed completely.
            # Close without shutdown may use RST instead of FIN to terminate connection, dropping data that is in flight.
            #
            # It is also possible to use shutdown to close input and output streams independently.
            client_socket.shutdown(socket.SHUT_RDWR)
