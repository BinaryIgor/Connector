from src.presenter import http_presenter


def show():
    url_response = http_presenter.get_url(input('Url: '))
    while not url_response.valid:
        url_response = http_presenter.get_url(input(f'{url_response.error}: '))
    headers = http_presenter.collect_headers()
    method_response = http_presenter.get_method(input('Method: '))
    while not method_response.valid:
        method_response = http_presenter.get_method(
            input(f'{method_response.error}: '))
    body = input('Body: ')
    response = http_presenter.execute_request(url_response.data,
                                              method_response.data,
                                              headers, body)
    print("Response:")
    print(f'{response.status_code}')
    print('Headers:')
    for h in response.headers:
        print(h)
    print('Body:')
    print(response.body)
