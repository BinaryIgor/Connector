import threading
import socket
import time

LOCAL_IP = '127.0.0.1'
BUFFER_SIZE = 1024


def execute(dest_ip, dest_port, src_port, data, timeout,
            keep_sending=lambda: True,
            data_consumer=None):
    pass


def _start_listening(port, timeout, keep_listening, data_consumer):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setttimeout(timeout)
        s.bind((LOCAL_IP, port))
        while keep_listening():
            msg, _ = s.recvfrom(BUFFER_SIZE)
            data_consumer(msg)
