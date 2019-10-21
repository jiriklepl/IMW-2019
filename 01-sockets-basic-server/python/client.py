import socket

from shared import *


# Safe handling of resources that require releasing on exceptions.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_socket.connect((SERVER_ADDR, SERVER_PORT))
    
    data = client_socket.recv(SOCKET_BUFFER_SIZE)
    if data:
        i_size = data[0]
        tm_size = data[1]

        ctm : time.struct_time = parse_tm(data, i_size, tm_size, 2)

        print(time.asctime(ctm_to_tm(ctm)))

    # Shutdown precedes close to make sure protocol level shutdown is executed completely.
    # Close without shutdown may use RST instead of FIN to terminate connection, dropping data that is in flight.
    #
    # It is also possible to use shutdown to close input and output streams independently.
    client_socket.shutdown(socket.SHUT_RDWR)
