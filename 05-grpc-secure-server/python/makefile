.PHONY: server client

server: server.py shared.py time_pb2.py time_pb2_grpc.py
	python3 server.py

client: client.py shared.py time_pb2.py time_pb2_grpc.py
	python3 client.py seconds minutes hour hours year

time_pb2.py time_pb2_grpc.py: time.proto
	protoc --plugin=protoc-gen-grpc=$(pkg-config --variable=prefix grpc++)/usr/bin/grpc_python_plugin --python_out="." --grpc_out="." time.proto
