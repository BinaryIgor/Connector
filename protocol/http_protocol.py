import requests

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'


def execute(url, method, headers, body=None):
    method = method.upper()
    if method == GET:
        response = requests.get(url, headers=headers)
    elif method is POST:
        response = requests.post(url, headers=headers, data=body)
    elif method is PUT:
        response = requests.post(url, headers=headers, data=body)
    elif method is DELETE:
        response = requests.delete(url, headers=headers)
    else:
        raise Exception(f'{method} is not supported')
    return response


def is_method_valid(method):
    method = method.upper()
    return GET == method or POST == method or PUT == method or DELETE == method
