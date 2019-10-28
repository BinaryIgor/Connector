from src.presenter.presenter_response import PresenterResponse
from src.validation import validation

DEFAULT_TIMEOUT = 3000


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
        return PresenterResponse(data=int(timeout))
    else:
        return PresenterResponse(error='Timeout must be a positive number')


def get_rate(rate):
    if validation.is_positive_number(rate):
        return PresenterResponse(data=int(rate))
    else:
        return PresenterResponse(error='Rate must be a positive number')


def collect_data(input_collector):
    data = []
    part = input_collector("Data line: ")
    while part:
        data.append(part)
        part = input_collector("Next line(o): ")
    if len(data) > 0:
        return PresenterResponse(data='\n'.join(data))
    else:
        return PresenterResponse(error="Data can't be empty.")
