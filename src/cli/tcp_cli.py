from src.presenter import tcp_presenter


def show():
    ip_response = tcp_presenter.get_ip(input("Ip: "))
    while not ip_response.valid:
        ip_response = tcp_presenter.get_ip(f'{ip_response.error}: ')
    port_response = tcp_presenter.get_port(input("Port: "))
    while not port_response.valid:
        port_response = tcp_presenter.get_port(
            input(f'{port_response.error}: '))
    timeout_response = tcp_presenter.get_timeout(input("Timeout: "))
    while not timeout_response.valid:
        timeout_response = tcp_presenter.get_timeout(
            input(f'{timeout_response.error}: '))
    data_response = tcp_presenter.collect_data()
    while not data_response.valid:
        print(data_response.error)
        data_response = tcp_presenter.collect_data()
    tcp_presenter.execute_tcp_request(ip_response.data, port_response.data,
                                      timeout_response.data, data_response.data)
