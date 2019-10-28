import socket
import time

BUFFER = 1024
ENCODING = "utf8"


class TcpRequestConfig:

    def __init__(self, ip, port, rate, data,
                 timeout, data_consumer, sending_predicate):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.sending_predicate = sending_predicate


def execute(config: TcpRequestConfig):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(config.timeout)
        s.connect((config.ip, config.port))
        formatted = bytes(config.data, encoding=ENCODING)
        interval = 1.0 / config.rate if config.rate > 0 else 0
        while config.sending_predicate():
            data = send(s, formatted)
            config.data_consumer(data)
            if interval == 0:
                break
            time.sleep(interval)


def send(s, data):
    s.sendall(data)
    return s.recv(BUFFER).decode(ENCODING)
