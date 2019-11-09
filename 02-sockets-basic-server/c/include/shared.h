#ifndef SHARED_H_
#define SHARED_H_

#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <unistd.h>

#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <ctime>
#include <string>
#include <map>

#include "time.pb.h"

#define FALSE 0
#define TRUE !0

#define SERVER_ADDR "127.0.0.1"
#define SERVER_PORT 8888

#define SERVER_SOCKET_BACKLOG 8

#define SOCKET_BUFFER_SIZE 16384

// Custom assert macro for custom message in error report.
// Reuses assert helper definitions from standard library.

#ifdef DEBUG
#define ASSERT(cond, text) \
    ((cond) \
        ? __ASSERT_VOID_CAST(0) \
        : __assert_fail(text, __FILE__, __LINE__, __ASSERT_FUNCTION))
#else
#define ASSERT(cond, text) __ASSERT_VOID_CAST (0)
#endif


class request_parser {
 public:
    const std::map<
        std::string,
        void (time_message::TimeRequest::*)(bool)> options{
        {"seconds", &time_message::TimeRequest::set_seconds},
        {"minutes", &time_message::TimeRequest::set_minutes},
        {"hours", &time_message::TimeRequest::set_hours},
        {"mday", &time_message::TimeRequest::set_mday},
        {"month", &time_message::TimeRequest::set_month},
        {"year", &time_message::TimeRequest::set_year},
        {"wday", &time_message::TimeRequest::set_wday},
        {"yday", &time_message::TimeRequest::set_yday},
        {"isdst", &time_message::TimeRequest::set_isdst},
    };
};

/**
 * @brief  parses null terminated char** array of unix-style options
 *
 * @param  options[]: null terminated char** array of unix-style options
 *
 * @retval returns a time_message::TimeRequest object of requested time values
 */
time_message::TimeRequest parse_options(int count, const char* options[]) {
    time_message::TimeRequest request;
    request_parser parser;
    const char** option = options;

    while (count-- > 0) {
        std::string option_string;
        bool set_value;

        if (**option == '-') {
            option_string = *option + 1;
            set_value = false;
        } else {
            option_string = *option;
            set_value = true;
        }

        if (
            auto iterator = parser.options.find(option_string);
            iterator != parser.options.end()
        ) {
            (request.*(iterator->second))(set_value);
        }

        ++option;
    }

    return request;
}

time_message::TimeMessage create_message(
    const time_message::TimeRequest& request
) {
    time_message::TimeMessage message;
    time_t now = time(NULL);
    tm *gmtm = gmtime(&now);

    if (request.seconds()) {
        message.set_seconds(gmtm->tm_sec);
    }

    if (request.minutes()) {
        message.set_minutes(gmtm->tm_min);
    }

    if (request.hours()) {
        message.set_hours(gmtm->tm_hour);
    }

    if (request.mday()) {
        message.set_mday(gmtm->tm_mday);
    }

    if (request.month()) {
        message.set_month(gmtm->tm_mon);
    }

    if (request.year()) {
        message.set_year(gmtm->tm_year + 1900);
    }

    if (request.wday()) {
        message.set_wday(gmtm->tm_wday);
    }

    if (request.yday()) {
        message.set_yday(gmtm->tm_yday);
    }

    if (request.isdst()) {
        message.set_isdst(gmtm->tm_isdst);
    }

    return message;
}

#endif  // SHARED_H_
