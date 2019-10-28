import socket
import time

BUFFER_SIZE = 1024
ENCODING = "utf8"


def execute(ip, port, rate, data, timeout=3000, keep_sending=lambda: True,
            data_consumer=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        formatted = bytes(data, encoding=ENCODING)
        interval = 1.0 / rate if rate > 0 else 0
        while keep_sending():
            data = send(s, formatted)
            if data_consumer:
                data_consumer(data)
            if interval == 0:
                break
            time.sleep(interval)


def send(s, data):
    s.sendall(data)
    return s.recv(BUFFER_SIZE).decode(ENCODING)
