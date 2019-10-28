from enum import Enum
import math

BINARY_FORMAT_PREFIX = 'b'


class Protocol(Enum):
    UDP = 1
    TCP = 2
    HTTP = 3


class SocketRequestConfig:

    def __init__(self, ip, port, rate, data,
                 timeout, data_consumer, sending_predicate, src_port=None):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.sending_predicate = sending_predicate
        self.src_port = src_port


class DataWithFormat:

    def __init__(self, str_data):
        self.str_data = str_data
        self.binary = str_data[0:1] == BINARY_FORMAT_PREFIX
        self.text = not self.binary

    def as_text_bytes(self, encoding):
        return bytes(self.str_data, encoding=encoding)

    def as_binary_bytes(self):
        binary = self._prepare_binary()
        bytes_array = []
        bs_len = len(binary)

        if bs_len < 8:
            bytes_array.append(int(binary, 2))
            print(bytes_array)
            return bytes(bytes_array)

        segments = math.floor(bs_len / 8.0)
        first_segment = bs_len - segments * 8

        if first_segment > 0:
            bytes_array.append(int(binary[0:first_segment], 2))

        next_segment = first_segment + 8
        for i in range(segments):
            bytes_array.append(
                int(binary[first_segment:next_segment], 2))
            first_segment = next_segment
            next_segment += 8
        return bytes(bytes_array)

    def _prepare_binary(self):
        segments = self.str_data[1:].split('\n')
        return ''.join(segments)
