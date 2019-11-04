# Sockets: The Hard Way


## Part One

Implement a socket server that will:
- Listen for incoming connections.
- Provide information on current time to connected clients.

Implement a socket client that will:
- Connect to the server described above.
- Query information on current time.
- Wrap all this in a local function.
- Print the time.

### C Local Function

```
/**
 * Return server time in standard structure.
 * @param result Caller allocated structure to fill.
 * @return Zero for success, non zero error code otherwise.
 */
int server_time (struct tm *result);

struct tm {
    int tm_sec;    // Seconds (0-60)
    int tm_min;    // Minutes (0-59)
    int tm_hour;   // Hours (0-23)
    int tm_mday;   // Day of the month (1-31)
    int tm_mon;    // Month (0-11)
    int tm_year;   // Year - 1900
    int tm_wday;   // Day of the week (0-6, Sunday = 0)
    int tm_yday;   // Day in the year (0-365, 1 Jan = 0)
    int tm_isdst;  // Daylight saving time
};
```

Check `man localtime` ...

### Java Local Function

```
/**
 * Access server time in standard structure.
 */
public interface ServerTime {
    int getSecond ();           // Gets the second-of-minute field.
    int getMinute ();           // Gets the minute-of-hour field.
    int getHour ();             // Gets the hour-of-day field.
    int getDayOfMonth ();       // Gets the day-of-month field.
    Month getMonth ();          // Gets the month-of-year field.
    int getYear ();             // Gets the year field.
    DayOfWeek getDayOfWeek ();  // Gets the day-of-week field.
    int getDayOfYear ();        // Gets the day-of-year field.
}
```

Check `LocalDateTime` ...

### Python Local Function

```
def server_time ():
    """Returns server time in datetime.datetime class."""
    ...

# Instance attributes (read-only):
#
#     datetime.year
#         Between MINYEAR and MAXYEAR inclusive.
#     datetime.month
#         Between 1 and 12 inclusive.
#     datetime.day
#         Between 1 and the number of days in the given month of the given year.
#     datetime.hour
#         In range(24).
#     datetime.minute
#         In range(60).
#     datetime.second
#         In range(60).
```

Check `help (datetime.datetime)` ...


## Part Two

Implement Part One in at least two programming languages.

Make sure your clients and servers in both languages are interchangeable:
- Run any client with any server.
- Basic fields are enough (YYYY-MM-DD HH:MM:SS).
- Use sensible defaults for other fields (TZ, DOW, DOY).
