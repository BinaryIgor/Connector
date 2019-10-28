from src.protocol.protocol import SocketRequestConfig
import socket
import time

BUFFER = 1024
ENCODING = "utf8"


def execute(config: SocketRequestConfig):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(config.timeout)
        s.connect((config.ip, config.port))
        formatted = bytes(config.data, encoding=ENCODING)
        interval = 1.0 / config.rate if config.rate > 0 else 0
        while config.sending_predicate():
            data = _send_receive(s, formatted)
            config.data_consumer(data)
            if interval == 0:
                break
            time.sleep(interval)


def _send_receive(s, data):
    s.sendall(data)
    return s.recv(BUFFER).decode(ENCODING)
