#include <string>
#include <string_view>
#include <iostream>
#include <utility>

#include <grpc++/grpc++.h>

#include "shared.h"
#include "time.grpc.pb.h"

using namespace grpc;
using namespace time_message;


int main(int argc, const char* argv[]) {
    // Create the channel used to connect to the server.
    std::shared_ptr<Channel> channel = CreateChannel(
        SERVER_ADDR,
        InsecureChannelCredentials());

    // Create a stub object that provides the service interface.
    std::unique_ptr<TimeService::Stub> stub =
        TimeService::NewStub(channel);

    TimeRequest request;
    for (const char** argp = argv + 1; *argp != nullptr; ++argp) {
        std::string_view arg = *argp;

        if (arg == "seconds") {
            request.set_seconds(true);
        } else if (arg == "minutes") {
            request.set_minutes(true);
        } else if (arg == "hours") {
            request.set_hours(true);
        } else if (arg == "mday") {
            request.set_mday(true);
        } else if (arg == "month") {
            request.set_month(true);
        } else if (arg == "year") {
            request.set_year(true);
        } else if (arg == "wday") {
            request.set_wday(true);
        } else if (arg == "yday") {
            request.set_yday(true);
        } else if (arg == "isdst") {
            request.set_isdst(true);
        }
    }

    std::cout << "Message:" << std::endl;
    std::cout << request.DebugString() << std::endl;

    ClientContext context;
    TimeMessage response;

    // Call the service through the stub object.
    Status status = stub->GetTime(&context, request, &response);

    if (status.ok()) {
        std::cout << "Response:" << std::endl;
        std::cout << response.DebugString() << std::endl;
    }

    return (0);
}
