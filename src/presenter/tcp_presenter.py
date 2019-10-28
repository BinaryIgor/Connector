from src.presenter.presenter_response import PresenterResponse
from src.protocol import tcp_protocol
import threading


# TODO: validations

class TcpRequestConfig:

    def __init__(self, ip, port, rate, data, timeout=3000, data_consumer=None,
                 interruption=lambda: input()):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.interruption = interruption


def get_ip(ip):
    return PresenterResponse(data=ip)


def get_port(port):
    return PresenterResponse(data=int(port))


def get_timeout(timeout):
    return PresenterResponse(data=int(timeout))


def get_rate(rate):
    return PresenterResponse(data=int(rate))


def collect_data():
    data = []
    part = input("Data: ")
    while part:
        data.append(part)
        part = input("More data: ")
    if len(data) > 0:
        return PresenterResponse(data=''.join(data))
    else:
        return PresenterResponse(error="Data can't be empty.")


def execute_tcp_request(config: TcpRequestConfig):
    keep_sending_flag = True

    def keep_sending():
        nonlocal keep_sending_flag
        return keep_sending_flag

    args = (config.ip, config.port, config.rate, config.data)
    thread = threading.Thread(target=tcp_protocol.execute,
                              args=args,
                              kwargs={'timeout': config.timeout,
                                      'keep_sending': keep_sending,
                                      'data_consumer': config.data_consumer},
                              daemon=True)
    thread.start()
    _ = config.interruption()
    keep_sending_flag = False
