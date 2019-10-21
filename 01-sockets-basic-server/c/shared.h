#ifndef SHARED_H_
#define SHARED_H_

#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <unistd.h>

#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <time.h>

#define FALSE 0
#define TRUE !0

#define SERVER_ADDR "127.0.0.1"
#define SERVER_PORT 8888

#define SERVER_SOCKET_BACKLOG 8

#define SOCKET_BUFFER_SIZE 16384

// Custom assert macro for custom message in error report.
// Reuses assert helper definitions from standard library.

#define ASSERT(cond, text) \
    ((cond) \
        ? __ASSERT_VOID_CAST(0) \
        : __assert_fail(text, __FILE__, __LINE__, __ASSERT_FUNCTION))

void hton_tm(struct tm* converted) {
    converted->tm_sec = htonl(converted->tm_sec);
    converted->tm_min = htonl(converted->tm_min);
    converted->tm_hour = htonl(converted->tm_hour);
    converted->tm_mday = htonl(converted->tm_mday);
    converted->tm_mon = htonl(converted->tm_mon);
    converted->tm_year = htonl(converted->tm_year);
    converted->tm_wday = htonl(converted->tm_wday);
    converted->tm_yday = htonl(converted->tm_yday);
    converted->tm_isdst = htonl(converted->tm_isdst);
}

void ntoh_tm(struct tm* converted) {
    converted->tm_sec = ntohl(converted->tm_sec);
    converted->tm_min = ntohl(converted->tm_min);
    converted->tm_hour = ntohl(converted->tm_hour);
    converted->tm_mday = ntohl(converted->tm_mday);
    converted->tm_mon = ntohl(converted->tm_mon);
    converted->tm_year = ntohl(converted->tm_year);
    converted->tm_wday = ntohl(converted->tm_wday);
    converted->tm_yday = ntohl(converted->tm_yday);
    converted->tm_isdst = ntohl(converted->tm_isdst);
}

#endif  // SHARED_H_
