CC := g++
C_FLAGS := -std=c++17 -O2 -DNDEBUG -march=native

RELEASE_FLAGS := 
DEBUG_FLAGS   := 

BIN     := bin
SRC     := src
INCLUDE := include
LIB     := lib
TEMP    := tmp
PROTO   := ../proto


ifeq ($(OS),Windows_NT)
EXECUTABLE  := main.exe
else
EXECUTABLE  := main
endif


PROTOBUF_FILES   := $(TEMP)/time.pb.cc $(TEMP)/time.pb.h
PROTOBUF_SRC     := $(TEMP)/time.pb.cc
PROTOBUF_COMMAND := protoc $(PROTO)/time.proto --proto_path=$(PROTO) --cpp_out=$(TEMP)


SERVER_FILES := $(SRC)/server.cc $(PROTOBUF_SRC)
CLIENT_FILES := $(SRC)/client.cc $(PROTOBUF_SRC)

SERVER_OBJ_FILES = $(patsubst $(SRC)/%.cc,$(TEMP)/%.o,$(patsubst $(TEMP)/%.cc,$(TEMP)/%.o,$(SERVER_FILES)))
CLIENT_OBJ_FILES = $(patsubst $(SRC)/%.cc,$(TEMP)/%.o,$(patsubst $(TEMP)/%.cc,$(TEMP)/%.o,$(CLIENT_FILES)))

COMPILE = $(CC) -c $(C_FLAGS) -I$(INCLUDE) -I$(TEMP) $(shell pkg-config --cflags protobuf) -o$@ $<

LINK_COMMAND = $(CC) $(C_FLAGS) -o$@ $^ $(shell pkg-config --libs protobuf) 


.PHONY: all clean server client

all: $(BIN)/server $(BIN)/client

server: $(BIN)/server

client: $(BIN)/client

all: $(BIN)/server $(BIN)/client

clean:
	$(RM) $(wildcard $(BIN)/*) $(wildcard $(TEMP)/*)

$(TEMP)/%.o: $(SRC)/%.cc $(wildcard $(INCLUDE)/*) $(PROTOBUF_FILES)
	$(COMPILE)

$(TEMP)/%.o: $(TEMP)/%.cc $(wildcard $(INCLUDE)/*) $(PROTOBUF_FILES)
	$(COMPILE)

$(PROTOBUF_FILES): $(PROTO)/time.proto
	$(PROTOBUF_COMMAND)

$(BIN)/server: $(SERVER_OBJ_FILES)
	$(LINK_COMMAND)

$(BIN)/client: $(CLIENT_OBJ_FILES)
	$(LINK_COMMAND)
