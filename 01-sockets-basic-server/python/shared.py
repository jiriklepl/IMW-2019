import time
import struct

SERVER_ADDR = '127.0.0.1'
SERVER_PORT = 8888

SERVER_SOCKET_BACKLOG = 8

SOCKET_BUFFER_SIZE = 16384

def raiser(ex):
    raise ex

def parse_tm(data : bytes, i_size : int, tm_size : int, offset : int): # converts binary to tm
    return \
        struct.unpack_from('!iiiiiiiii', data, offset) \
        if i_size == 4 \
        \
        else struct.unpack_from('!qqqqqqqqq', data, offset) \
        if i_size == 8 \
        \
        else struct.unpack_from('!hhhhhhhhh', data, offset) \
        if i_size == 2 \
        \
        else raiser(RuntimeError('format not recognized'))

def make_tm():
    tm : time.struct_time = time.localtime(time.time())
    return tm

def pack_tm(tm : time.struct_time): # packs time to be sent (alongside a head saying its word size and length)
    data : bytearray = bytearray(SOCKET_BUFFER_SIZE)
    data[0] = 4
    data[1] = 36
    struct.pack_into(
        '!iiiiiiiii',
        data,
        2,
        tm[0], tm[1], tm[2], tm[3], tm[4], tm[5], tm[6], tm[7], tm[8])
    return data

def ctm_to_tm(tm : time.struct_time): # reorders the tm struct to be readable by time library
    return (
        tm[5] + 1900, # cause python counts from 0 and C from 1900
        tm[4] + 1, # now C counts from 0 and python from 1
        tm[3],
        tm[2],
        tm[1],
        tm[0],
        tm[6] - 1 if tm[6] > 0 else 6, # in C day 0 is Sunday and in python it's Monday...
        tm[7],
        tm[8])

def tm_to_ctm(tm : time.struct_time): # reorders the tm struct to fit ISO 9899
    return (
        tm[5],
        tm[4],
        tm[3],
        tm[2],
        tm[1] - 1, # now C counts from 0 and python from 1
        tm[0] - 1900, # cause python counts from 0 and C from 1900
        (tm[6] + 1) % 7, # in C day 0 is Sunday and in python it's Monday...
        tm[7],
        tm[8])