import socket


# TODO handle rate properly
def execute(ip, port, rate, data, timeout=3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        s.sendall(bytes(data, encoding='utf8'))
        data = s.recv(1024)

    print('Received', str(data))
