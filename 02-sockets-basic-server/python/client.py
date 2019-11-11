import socket
import time_pb2
import sys

from shared import SERVER_ADDR, SERVER_PORT, SOCKET_BUFFER_SIZE

# Safe handling of resources that require releasing on exceptions.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    print("Connecting")

    client_socket.connect((SERVER_ADDR, SERVER_PORT))

    request = time_pb2.TimeRequest()

    for argv in sys.argv[1:]:
        if argv == "seconds": request.seconds = True
        if argv == "minutes": request.minutes = True
        if argv == "hours": request.hours = True
        if argv == "mday": request.mday = True
        if argv == "month": request.month = True
        if argv == "year": request.year = True
        if argv == "wday": request.wday = True
        if argv == "yday": request.yday = True
        if argv == "isdst": request.isdst = True

    print("Sending request.")

    data = request.SerializeToString()
    client_socket.send(data)

    print("Receiving answer.")

    answer = time_pb2.TimeMessage()

    while True:
        data = client_socket.recv (SOCKET_BUFFER_SIZE)
        print(data)
        if len (data) == 0 or answer.ParseFromString(data):
            break

    print("Answer received.")

    if request.seconds == True: print(answer.seconds)
    if request.minutes == True: print(answer.minutes)
    if request.hours == True: print(answer.hours)
    if request.mday == True: print(answer.mday)
    if request.month == True: print(answer.month)
    if request.year == True: print(answer.year)
    if request.wday == True: print(answer.wday)
    if request.yday == True: print(answer.yday)
    if request.isdst == True: print(answer.isdst)

    # Shutdown precedes close to make sure protocol level shutdown is executed completely.
    # Close without shutdown may use RST instead of FIN to terminate connection, dropping data that is in flight.
    #
    # It is also possible to use shutdown to close input and output streams independently.
    client_socket.shutdown(socket.SHUT_RDWR)
