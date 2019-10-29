import threading
from src.presenter.presenter_response import PresenterResponse
from src.protocol import protocol, socket_protocol
from src.validation import validation

DEFAULT_TIMEOUT = 3


class SocketRequestConfig:

    def __init__(self, ip, port, rate, data,
                 data_consumer, timeout=DEFAULT_TIMEOUT,
                 interruption=lambda: input(),
                 src_port=None):
        self.ip = ip
        self.port = port
        self.rate = rate
        self.data = data
        self.timeout = timeout
        self.data_consumer = data_consumer
        self.interruption = interruption
        self.src_port = src_port

    def to_protocol_config(self, sending_predicate):
        return protocol.SocketRequestConfig(self.ip, self.port, self.rate,
                                            protocol.DataWithFormat(self.data),
                                            self.timeout,
                                            self.data_consumer,
                                            sending_predicate,
                                            src_port=self.src_port)


def get_ip(ip):
    if validation.is_valid_ip(ip):
        return PresenterResponse(data=ip)
    else:
        return PresenterResponse(error=f'{ip} is not a proper ip address')


def get_port(port):
    if validation.is_valid_port(port):
        return PresenterResponse(data=int(port))
    else:
        return PresenterResponse(
            error=f'Only ports in range {validation.MIN_PORT} - '
                  f'{validation.MAX_PORT} are considered valid')


def get_timeout(timeout):
    if not timeout:
        return PresenterResponse(data=DEFAULT_TIMEOUT)
    if validation.is_positive_number(timeout):
        return PresenterResponse(data=float(timeout))
    else:
        return PresenterResponse(error='Timeout must be a positive number')


def get_rate(rate):
    if validation.is_positive_number(rate):
        return PresenterResponse(data=float(rate))
    else:
        return PresenterResponse(error='Rate must be a positive number')


def collect_data(input_collector):
    data = []
    part = input_collector(
        f'Data line({protocol.BINARY_FORMAT_PREFIX}1010... to send binary): ')
    while part:
        data.append(part)
        part = input_collector("Next line(o): ")
    if len(data) > 0:
        return PresenterResponse(data='\n'.join(data))
    else:
        return PresenterResponse(error="Data can't be empty.")


def execute_tcp_request(config: SocketRequestConfig, on_error):
    _execute_request(config, on_error, udp=False)


def execute_udp_request(config: SocketRequestConfig, on_error):
    _execute_request(config, on_error, udp=True)


def _execute_request(config: SocketRequestConfig, on_error, udp=False):
    keep_sending_flag = True

    def keep_sending():
        nonlocal keep_sending_flag
        return keep_sending_flag

    logging_target = _catching_func(
        socket_protocol.execute_udp if udp else socket_protocol.execute_tcp,
        on_error)
    thread = threading.Thread(
        target=logging_target,
        args=[config.to_protocol_config(keep_sending)],
        daemon=True)
    thread.start()
    if config.rate > 0:
        _ = config.interruption()
    else:
        thread.join()
    keep_sending_flag = False


def _catching_func(func, on_error):
    def logging_func(f, x):
        try:
            f(x)
        except BaseException as e:
            on_error(e)

    return lambda x: logging_func(func, x)
