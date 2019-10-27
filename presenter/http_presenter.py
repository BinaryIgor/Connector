from presenter.presenter_response import PresenterResponse
from validation import validation


def get_url(url):
    if url.find('http') == 0 or url.find('https') == 0:
        response = PresenterResponse(data=url)
    else:
        response = PresenterResponse(
            error='Url must start with http or https prefix')
    return response


def collect_headers():
    headers = {}
    header = input('Header: ')
    while header:
        if validation.is_valid_header(header):
            h = header.split(':')
            headers[h[0]] = h[1]
            header = input('Next header: ')
        else:
            header = input('Invalid header. Try again: ')
    return headers
