from src.presenter.presenter_response import PresenterResponse
from src.protocol import tcp_protocol
import threading


# TODO: validations

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


def execute_tcp_request(ip, port, rate, data, timeout):
    keep_sending_flag = True

    def keep_sending():
        nonlocal keep_sending_flag
        return keep_sending_flag

    def print_next(r_data):
        print(f'Received: {r_data}')

    thread = threading.Thread(target=tcp_protocol.execute,
                              args=(ip, port, rate, data),
                              kwargs={'timeout': timeout,
                                      'keep_sending': keep_sending,
                                      'data_consumer': print_next},
                              daemon=True)
    print('Press enter to stop.')
    thread.start()
    _ = input()
    keep_sending_flag = False
