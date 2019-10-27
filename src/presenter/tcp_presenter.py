from src.presenter.presenter_response import PresenterResponse


# TODO: validations

def get_ip(ip):
    return PresenterResponse(data=ip)


def get_port(port):
    return PresenterResponse(data=port)


def get_timeout(timeout):
    return PresenterResponse(data=timeout)


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


def execute_tcp_request(ip, port, timeout, data):
    print(f'{ip}, {port}, {timeout}, {data}')
