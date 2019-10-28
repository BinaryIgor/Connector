from src.presenter import http_presenter
from src.input.smart_input import input_or_quit


def show():
    url_response = http_presenter.get_url(input_or_quit('Url: '))

    while not url_response.valid:
        url_response = http_presenter.get_url(
            input_or_quit(f'{url_response.error}: '))

    headers = http_presenter.collect_headers(input_or_quit)

    method_response = http_presenter.get_method(input_or_quit('Method: '))
    while not method_response.valid:
        method_response = http_presenter.get_method(
            input_or_quit(f'{method_response.error}: '))
    body = input_or_quit('Body(o): ')
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
