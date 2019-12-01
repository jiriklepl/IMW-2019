[ -d "c/tmp" ] || mkdir "c/tmp"
[ -d "c/bin" ] || mkdir "c/bin"
make -C c

echo "c client && c server"

c/bin/server > /dev/null &
server=$!

echo "running 10000 clients sequentially"

i=0
time {
    while [ $i -lt 10000 ]; do
        c/bin/client seconds minutes hour year
        i=$(($i+1))
    done;
} > /dev/null

kill -9 $server
sleep 10

echo "c client && python server"

python python/server.py > /dev/null &
server=$!

echo "running 10000 clients sequentially"

i=0
time {
    while [ $i -lt 10000 ]; do
        c/bin/client seconds minutes hour year
        i=$(($i+1))
    done;
} > /dev/null

# c should be more efficient:
# on my machyne: c real: 1m12.477s && python real: 1m24.058s
# (both using c clients)

kill -9 $server
sleep 3

make -C c clean
[ -d "python/__pycache__" ] && rm -rf "python/__pycache__"