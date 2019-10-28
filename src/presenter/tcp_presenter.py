from src.protocol import tcp_protocol
from src.presenter import socket_presenter
import threading


class TcpRequestConfig:

    def __init__(self, ip, port, rate, data,
                 data_consumer, timeout=socket_presenter.DEFAULT_TIMEOUT,
                 interruption=lambda: input()):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.interruption = interruption

    def to_protocol_config(self, sending_predicate):
        return tcp_protocol.TcpRequestConfig(self.ip, self.port, self.rate,
                                             self.data, self.timeout,
                                             self.data_consumer,
                                             sending_predicate)


def execute_tcp_request(config: TcpRequestConfig):
    keep_sending_flag = True

    def keep_sending():
        nonlocal keep_sending_flag
        return keep_sending_flag

    thread = threading.Thread(target=tcp_protocol.execute,
                              args=[config.to_protocol_config(keep_sending)],
                              daemon=True)
    thread.start()
    if config.rate > 0:
        _ = config.interruption()
    else:
        thread.join()
    keep_sending_flag = False
