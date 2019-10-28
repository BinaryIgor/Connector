from src.protocol import tcp_protocol
from src.presenter import socket_presenter
import threading


class TcpRequestConfig:

    def __init__(self, ip, port, rate, data,
                 timeout=socket_presenter.DEFAULT_TIMEOUT,
                 data_consumer=None,
                 interruption=lambda: input()):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.interruption = interruption


def execute_tcp_request(config: TcpRequestConfig):
    keep_sending_flag = True

    def keep_sending():
        nonlocal keep_sending_flag
        return keep_sending_flag

    args = (config.ip, config.port, config.rate, config.data, config.timeout)
    thread = threading.Thread(target=tcp_protocol.execute,
                              args=args,
                              kwargs={'keep_sending': keep_sending,
                                      'data_consumer': config.data_consumer},
                              daemon=True)
    thread.start()
    if config.rate > 0:
        _ = config.interruption()
    else:
        thread.join()
    keep_sending_flag = False
