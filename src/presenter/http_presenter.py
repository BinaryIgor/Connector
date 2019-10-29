from src.presenter.presenter_response import PresenterResponse
from src.validation import validation
from src.protocol import http_protocol


class ResponseViewModel:
    def __init__(self, status_code, headers, body):
        self.status_code = status_code
        self.headers = headers
        self.body = body


def get_url(url):
    if url.find('http') == 0 or url.find('https') == 0:
        response = PresenterResponse(data=url)
    else:
        response = PresenterResponse(
            error='Url must start with http or https prefix')
    return response


def collect_headers(input_collector):
    headers = {}
    header = input_collector('Header(o): ')
    while header:
        if validation.is_valid_header(header):
            h = header.split(':')
            headers[h[0].strip()] = h[1].strip()
            header = input_collector('Next header(o): ')
        else:
            header = input_collector(
                'Invalid header(valid format k:v). Try again(o): ')
    return headers


def get_method(method):
    if http_protocol.is_method_supported(method):
        return PresenterResponse(data=method)
    else:
        return PresenterResponse(error=f'{method} is not supported')


def execute_request(url, method, headers, body):
    with http_protocol.execute(url, method, headers, body) as response:
        formatted_code = f'Status: {response.status_code}'
        formatted_headers = []
        for h in response.headers:
            formatted_headers.append(f'{h}:{response.headers[h]}')
        return ResponseViewModel(formatted_code, formatted_headers,
                                 response.text)
