#include "shared.h"

int main(int argc, const char* argv[]) {
    // Create client socket object.
    //
    // The object state resides in the operating system kernel.
    // What we have is merely a file descriptor refering to it.

    int client_socket = socket(AF_INET, SOCK_STREAM, 0);
    ASSERT(client_socket != -1, "Failed to create client socket object.");

    // Construct server address.
    //
    // Note the need to use network order inside address fields.

    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    int aton_status = inet_aton(
        SERVER_ADDR,
        (struct in_addr *) &server_address.sin_addr.s_addr);
    ASSERT(aton_status == 1, "Failed to parse server address.");
    server_address.sin_port = htons(SERVER_PORT);

    // Connect to server.

    int connect_status = connect(
        client_socket,
        (struct sockaddr *) &server_address,
        sizeof(server_address));
    ASSERT(connect_status == 0, "Failed to connect to server.");
    printf("Established outgoing connection.\n");

    // Just send and receive something.
    //
    // We assume that the response is a zero terminated string.

    auto request = parse_options(argc - 1, argv + 1);
    std::string request_string;
    request.SerializeToString(&request_string);
    write(client_socket, request_string.c_str(), request_string.length());

    printf("Sent options.\n");

    time_message::TimeMessage message;
    char buffer[SOCKET_BUFFER_SIZE];

    while (read(client_socket, buffer, SOCKET_BUFFER_SIZE) > 0) {
        if (message.ParseFromString(buffer)) {
            break;
        }
    }

    printf("Sent options connection.\n");

    if (request.seconds()) {
        std::cout << message.seconds();
    }

    if (request.minutes()) {
       std::cout << message.minutes();
    }

    if (request.hours()) {
       std::cout << message.hours();
    }

    if (request.mday()) {
       std::cout << message.mday();
    }

    if (request.month()) {
       std::cout << message.month();
    }

    if (request.year()) {
       std::cout << message.year();
    }

    if (request.wday()) {
       std::cout << message.wday();
    }

    if (request.yday()) {
       std::cout << message.yday();
    }

    if (request.isdst()) {
       std::cout << message.isdst();
    }

    // Clean up by closing the socket.
    //
    // Shutdown precedes close to make sure protocol level,
    // shutdown is executed completely.
    // Close without shutdown may use RST instead of
    // FIN to terminate connection, dropping data that is in flight.
    //
    // It is also possible to use shutdown to close input and
    // output streams independently.

    int shutdown_status = shutdown(client_socket, SHUT_RDWR);
    ASSERT(shutdown_status == 0, "Failed to shutdown incoming connection.");

    int close_status = close(client_socket);
    ASSERT(close_status == 0, "Failed to close incoming connection.");
}
