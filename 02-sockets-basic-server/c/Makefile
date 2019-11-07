CC := g++
C_FLAGS := -std=c++17 -Wall -Wextra -Wpedantic

RELEASE_FLAGS := -O2 -march=native -DNDEBUG
DEBUG_FLAGS   := -g -DDEBUG

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


PROTOBUF_FILES   := $(TMP)/time.pb.cc $(TMP)/time.pb.h
PROTOBUF_SRC     := $(TMP)/time.pb.cc
PROTOBUF_COMMAND := protoc $(PROTO)/time.proto --proto_path=$(PROTO) --cpp_out=$(TMP)


SRC_FILES = $(wildcard $(SRC)/*.c) $(PROTOBUF_SRC)
OBJ_FILES = $(patsubst $(SRC)/%.c,$(TEMP)/%.o,$(patsubst $(TEMP)/%.c,$(TEMP)/%.o,$(SRC_FILES)))

COMPILE = $(CC) -c $(C_FLAGS) -I$(INCLUDE) -o$@ $<

LINK_COMMAND = $(CC) $(C_FLAGS) -o$@ $^


.PHONY: all clean run debug release

all: release

release: C_FLAGS += $(RELEASE_FLAGS)
release: $(BIN) $(TEMP) $(PROTOBUF_FILES) $(BIN)/$(EXECUTABLE)

debug: C_FLAGS += $(DEBUG_FLAGS)
debug: $(BIN) $(TEMP) $(PROTOBUF_FILES) $(BIN)/$(EXECUTABLE)

clean:
	$(RM) $(wildcard $(BIN)/*) $(wildcard $(TEMP)/*)

run: all
	$(BIN)/$(EXECUTABLE)


$(BIN):
	mkdir $(BIN)

$(TEMP):
	mkdir $(TEMP)

$(TEMP)/%.o: $(SRC)/%.c $(wildcard $(INCLUDE)/*)
	$(COMPILE)

$(TEMP)/%.o: $(TEMP)/%.c $(wildcard $(INCLUDE)/*)
	$(COMPILE)

$(PROTOBUF_FILES): $(PROTO)
	$(BISON_COMMAND)

$(BIN)/$(EXECUTABLE): $(OBJ_FILES)
	$(LINK_COMMAND)