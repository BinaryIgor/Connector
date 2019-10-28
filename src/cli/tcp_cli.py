from src.presenter import tcp_presenter
from src.input.smart_input import input_or_quit


def show():
    config = _collect_config()
    print()
    print('Listening to responses, press enter to stop.')
    tcp_presenter.execute_tcp_request(config)


def _collect_config():
    ip_response = tcp_presenter.get_ip(input_or_quit("Ip: "))
    while not ip_response.valid:
        ip_response = tcp_presenter.get_ip(f'{ip_response.error}: ')

    port_response = tcp_presenter.get_port(input_or_quit("Port: "))
    while not port_response.valid:
        port_response = tcp_presenter.get_port(
            input_or_quit(f'{port_response.error}: '))

    timeout_response = tcp_presenter.get_timeout(input_or_quit("Timeout(o): "))
    while not timeout_response.valid:
        timeout_response = tcp_presenter.get_timeout(
            input_or_quit(f'{timeout_response.error}: '))

    rate_response = tcp_presenter.get_rate(
        input_or_quit("Rate(or 0 if data should be send once):"))
    while not rate_response.valid:
        rate_response = tcp_presenter.get_rate(f'{rate_response.error}: ')

    data_response = tcp_presenter.collect_data()
    while not data_response.valid:
        print(data_response.error)
        data_response = tcp_presenter.collect_data()

    return tcp_presenter.TcpRequestConfig(ip_response.data,
                                          port_response.data,
                                          rate_response.data,
                                          data_response.data,
                                          timeout=timeout_response.data,
                                          data_consumer=lambda x: print(str(x)),
                                          interruption=lambda: input())
