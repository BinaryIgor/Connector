from enum import Enum
from src.validation.validation import is_valid_binary
import math

BINARY_FORMAT_PREFIX = ':b'


class Protocol(Enum):
    UDP = 1
    TCP = 2
    HTTP = 3


class SocketRequestConfig:

    def __init__(self, ip, port, rate, data_with_format,
                 timeout, data_consumer, send_predicate, src_port=None):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data_with_format = data_with_format
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.send_predicate = send_predicate
        self.src_port = src_port


class DataWithFormat:

    def __init__(self, str_data):
        self.str_data = str_data
        self.binary = str_data.find(BINARY_FORMAT_PREFIX) == 0
        self.text = not self.binary

    def as_text_bytes(self, encoding):
        return bytes(self.str_data, encoding=encoding)

    def as_binary_bytes(self):
        binary = self._prepare_binary()

        if not binary:
            raise Exception('Empty binary data')
        elif not is_valid_binary(binary):
            raise Exception(f'{binary} is not a valid binary number')

        bytes_array = []
        bs_len = len(binary)

        if bs_len < 8:
            bytes_array.append(int(binary, 2))
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
        segments = self.str_data[len(BINARY_FORMAT_PREFIX):].split('\n')
        return ''.join(segments)


def format_bytes(raw_bytes):
    return ''.join(
        ['{:08b}'.format(raw_bytes[i]) if i > 0 else '{:b}'.format(raw_bytes[i])
         for i in range(len(raw_bytes))])
