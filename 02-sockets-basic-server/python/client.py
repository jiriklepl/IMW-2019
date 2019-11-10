import socket
import time_pb2
import sys

from shared import SERVER_ADDR, SERVER_PORT, SOCKET_BUFFER_SIZE

# Safe handling of resources that require releasing on exceptions.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    print("Connecting")

    client_socket.connect((SERVER_ADDR, SERVER_PORT))

    request = time_pb2.TimeRequest()

    def set_true(x):
        x = True

    switcher = {
        "seconds": lambda : set_true(request.seconds),
        "minutes": lambda : set_true(request.minutes),
        "hours": lambda : set_true(request.hours),
        "mday": lambda : set_true(request.mday),
        "month": lambda : set_true(request.month),
        "year": lambda : set_true(request.year),
        "wday": lambda : set_true(request.wday),
        "yday": lambda : set_true(request.yday),
        "isdst": lambda : set_true(request.isdst),
    }

    for argv in sys.argv[1:]:
        switcher[argv]()

    print("Sending request.")

    client_socket.send(request.SerializeToString())

    print("Receiving answer.")

    answer = time_pb2.TimeMessage()
    answer.ParseFromString(client_socket.recv(SOCKET_BUFFER_SIZE))

    # Shutdown precedes close to make sure protocol level shutdown is executed completely.
    # Close without shutdown may use RST instead of FIN to terminate connection, dropping data that is in flight.
    #
    # It is also possible to use shutdown to close input and output streams independently.
    client_socket.shutdown(socket.SHUT_RDWR)
