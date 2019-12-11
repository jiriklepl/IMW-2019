# gRPC Based Server

Melo by byt vsechno OK, bylo zapotrebi dat knihovny v linkeru na spravna mista. Ale po spusteni nejaka core funkce v ramci NewStub vyhazuje chybu v aritmetice, takze nejde overit spravnost. Nefunguje g++ ani clang++

## Running the example

```bash
> make
> ./server &
> ./client
```

## Tracing execution

Launch with `GRPC_VERBOSITY=info` and `GRPC_TRACE=all` to enable logging.

## Inspecting server API

Add `-lgrpc++_reflection` to `LD_OPTS` in `Makefile` and build again.
This enables server reflection, which permits inspecting the API,
using for example command line tools.

```bash
> grpc_cli ls localhost:8888
> grpc_cli ls localhost:8888 --l
> grpc_cli type localhost:8888 example.AnExampleMessage
> grpc_cli call localhost:8888 example.AnExampleService.CloneMessage "some_integer: 8"
```
