# Protocol Buffers: Marshalling

## Part One

Implement a server that will provide information on current time:

- The server should accept a spec of what fields to return.
- Fields should be standard YYYY-MM-DD HH:MM:SS.

Implement a client that will query server time:

- Pick a random combination of fields.
- Query information on current time.
- Print the time.

Implement compatible clients and servers in two languages.

## Part Two

Measure the performance of your implementation.

Stick to the following, or provide arguments for why not:

- Random field mix, each field with probability 1/2.
- Measure at least two minutes long traffic.
- Report average invocation throughput.
- No printing during measurement.
- Compare with past assignments.
