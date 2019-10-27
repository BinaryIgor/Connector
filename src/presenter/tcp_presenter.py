from src.presenter.presenter_response import PresenterResponse
from src.protocol import tcp_protocol


# TODO: validations

def get_ip(ip):
    return PresenterResponse(data=ip)


def get_port(port):
    return PresenterResponse(data=int(port))


def get_timeout(timeout):
    return PresenterResponse(data=int(timeout))


def get_rate(rate):
    return PresenterResponse(data=rate)


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


def execute_tcp_request(ip, port, rate, data, timeout):
    tcp_protocol.execute(ip, port, rate, data, timeout=timeout)
