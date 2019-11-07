.PHONY: all clean

# Settings

MAKEFLAGS += --no-builtin-rules --no-builtin-variables

CPP = g++ -std=c++17
CPP_OPTS = -O0 -g -Wall -Wextra -Werror

# Files

ALL_EX = client server
ALL_DD = $(addsuffix .dep, $(ALL_EX))

# Rules

all: $(ALL_EX)

clean:
	rm -f *.o
	rm -f *.dep
	rm -f $(ALL_EX)

$(ALL_EX): %: %.cc
	$(CC) $(CC_OPTS) -o $@ $<

# Deps

-include $(ALL_DD)

%.dep: %.cc
	$(CC) -MM -MT "$@ $(basename $@).o" -o $@ $<
