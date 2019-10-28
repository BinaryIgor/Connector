import socket
import time


def execute(ip, port, rate, data, timeout=3000, keep_sending=lambda: True,
            data_consumer=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        formatted = bytes(data, encoding='utf8')
        interval = 1.0 / rate
        while keep_sending():
            data = send(s, formatted)
            if data_consumer:
                data_consumer(data)
            if rate == 0:
                break
            time.sleep(interval)


def send(s, data):
    s.sendall(data)
    return s.recv(1024).decode('utf8')
