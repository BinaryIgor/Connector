from protocol import http_protocol
from presenter import http_presenter


def show():
    url_response = http_presenter.get_url(input('Url: '))
    while not url_response.valid:
        url_response = http_presenter.get_url(input(f'{url_response.error}: '))
    headers = http_presenter.collect_headers()
    method = input('Method: ')
    body = input('Body: ')
    response = http_protocol.execute(url_response.data, method, headers,
                                     body=body)
    print(f'{response}')
