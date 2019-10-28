from enum import Enum


class Protocol(Enum):
    UDP = 1
    TCP = 2
    HTTP = 3


class SocketRequestConfig:

    def __init__(self, ip, port, rate, data,
                 timeout, data_consumer, sending_predicate):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.sending_predicate = sending_predicate
