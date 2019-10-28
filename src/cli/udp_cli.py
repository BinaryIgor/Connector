from src.presenter import udp_presenter, socket_presenter
from src.input.smart_input import smart_input


def show():
    _collect_config()


def _collect_config():
    ip_response = socket_presenter.get_ip(smart_input("Ip: "))
    while not ip_response.valid:
        ip_response = socket_presenter.get_ip(
            smart_input(f'{ip_response.error}: '))

    port_response = socket_presenter.get_port(smart_input("Port: "))
    while not port_response.valid:
        port_response = socket_presenter.get_port(
            smart_input(f'{port_response.error}: '))

    src_port_response = socket_presenter.get_port(
        smart_input("Listener port: "))
    while not src_port_response.valid:
        src_port_response = socket_presenter.get_port(
            smart_input(f'{port_response.error}: '))

    timeout_response = socket_presenter.get_timeout(smart_input(
        f'Timeout(o, default: {socket_presenter.DEFAULT_TIMEOUT}): '))
    while not timeout_response.valid:
        timeout_response = socket_presenter.get_timeout(
            smart_input(f'{timeout_response.error}: '))

    rate_response = socket_presenter.get_rate(
        smart_input("Rate(or 0 if data should be send once):"))
    while not rate_response.valid:
        rate_response = socket_presenter.get_rate(
            smart_input(f'{rate_response.error}: '))

    data_response = socket_presenter.collect_data(smart_input)
    while not data_response.valid:
        print(data_response.error)
        data_response = socket_presenter.collect_data(smart_input)
