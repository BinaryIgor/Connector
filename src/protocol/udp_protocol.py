from src.protocol.protocol import SocketRequestConfig
import socket
import time

LOCAL_IP = '127.0.0.1'
BUFFER_SIZE = 1024
ENCODING = 'utf8'


def execute(config: SocketRequestConfig):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        if config.src_port:
            s.bind((LOCAL_IP, config.src_port))
        s.settimeout(config.timeout)
        formatted = bytes(config.data, encoding=ENCODING)
        interval = 1.0 / config.rate if config.rate > 0 else 0
        while config.sending_predicate():
            data = _send_receive(s, (config.ip, config.port), formatted)
            config.data_consumer(data)
            if interval == 0:
                break
            time.sleep(interval)


def _send_receive(s, address, data):
    s.sendto(data, address)
    return s.recvfrom(BUFFER_SIZE)[0].decode(ENCODING)
