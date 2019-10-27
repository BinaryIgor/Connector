import socket
import time


# TODO handle rate properly
def execute(ip, port, rate, data, timeout=3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        formatted = bytes(data, encoding='utf8')
        interval = 1.0 / rate
        while True:
            data = send(s, formatted)
            print(f'Received: {data}')
            if rate == 0:
                break
            time.sleep(interval)


def send(s, data):
    s.sendall(data)
    return s.recv(1024).decode('utf8')
