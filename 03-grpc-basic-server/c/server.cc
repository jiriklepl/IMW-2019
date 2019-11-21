#include <grpc++/grpc++.h>
#include <ctime>

#include "shared.h"

#include "time.grpc.pb.h"
using namespace grpc;
using namespace time_message;


// Service implementation.
//
// The implementation inherits from a generated base class.

class MyService : public TimeService::Service {
    Status GetTime(
        ServerContext *context,
        const TimeRequest *request,
        TimeMessage *response
    ) override {
        time_t rawtime;
        time(&rawtime);
        tm* now = localtime(&rawtime);

        if (request->seconds()) {
            response->set_seconds(now->tm_sec);
        }

        if (request->minutes()) {
            response->set_minutes(now->tm_min);
        }

        if (request->hours()) {
            response->set_hours(now->tm_hour);
        }

        if (request->mday()) {
            response->set_mday(now->tm_mday);
        }

        if (request->month()) {
            response->set_month(now->tm_mon);
        }

        if (request->year()) {
            response->set_year(now->tm_year);
        }

        if (request->wday()) {
            response->set_wday(now->tm_wday);
        }

        if (request->yday()) {
            response->set_yday(now->tm_yday);
        }

        if (request->isdst()) {
            response->set_isdst(now->tm_isdst);
        }

        return Status::OK;
    }
};


int main() {
    // Create the server object.
    //
    // The server object represents the server runtime.
    // It needs to be told what service to provide
    // and what port to listen on.

    MyService service;
    ServerBuilder builder;
    builder.AddListeningPort(SERVER_ADDR, InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<Server> server(builder.BuildAndStart());

    // The server is never asked to terminate in this example,
    // it therefore waits here until interrupted from outside.

    server->Wait();

    return 0; 
}
