from src.presenter import http_presenter
from src.input.smart_input import smart_input


def show():
    url_response = http_presenter.get_url(smart_input('Url: '))

    while not url_response.valid:
        url_response = http_presenter.get_url(
            smart_input(f'{url_response.error}: '))

    headers = http_presenter.collect_headers(smart_input)

    method_response = http_presenter.get_method(smart_input('Method: '))
    while not method_response.valid:
        method_response = http_presenter.get_method(
            smart_input(f'{method_response.error}: '))
    body = smart_input('Body(o): ')
    response = http_presenter.execute_request(url_response.data,
                                              method_response.data,
                                              headers, body)
    print()
    print("Received response:")
    print(f'{response.status_code}')
    print('Headers:')
    for h in response.headers:
        print(h)
    print('Body:')
    print(response.body)
    print()
