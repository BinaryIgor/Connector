from src.protocol.protocol import SocketRequestConfig, format_bytes
import socket
import time

LOCAL_IP = '127.0.0.1'
BUFFER_SIZE = 1024
ENCODING = "utf8"


def execute_udp(config: SocketRequestConfig):
    _execute(config, True)


def execute_tcp(config: SocketRequestConfig):
    _execute(config, False)


def _execute(config: SocketRequestConfig, udp: bool):
    with socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM if udp else socket.SOCK_STREAM) as s:
        _prepare_socket(config, udp, s)
        formatted = _prepare_data(config)

        interval = 1.0 / config.rate if config.rate > 0 else 0
        dst_address = (config.ip, config.port) if udp else None
        while config.send_predicate():
            data = _send_receive(s, formatted, config.data_with_format.text,
                                 address=dst_address)
            config.data_consumer(data)
            if interval == 0:
                break
            time.sleep(interval)


def _prepare_socket(config: SocketRequestConfig, udp, s):
    s.settimeout(config.timeout)
    if config.src_port and udp:
        s.bind((LOCAL_IP, config.src_port))
    elif not udp:
        s.connect((config.ip, config.port))


def _prepare_data(config: SocketRequestConfig):
    if config.data_with_format.binary:
        formatted = config.data_with_format.as_binary_bytes()
    else:
        formatted = config.data_with_format.as_text_bytes(encoding=ENCODING)
    return formatted


def _send_receive(s, data, decode, address=None):
    if address:
        s.sendto(data, address)
        r_data = s.recvfrom(BUFFER_SIZE)[0]
    else:
        s.sendall(data)
        r_data = s.recv(BUFFER_SIZE)
    return r_data.decode(ENCODING) if decode else format_bytes(r_data)
