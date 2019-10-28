import requests

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'
OPTIONS = 'OPTIONS'
HEAD = 'HEAD'


def execute(url, method, headers, body=None):
    method = method.upper()
    if method == GET:
        response = requests.get(url, headers=headers)
    elif method == POST:
        response = requests.post(url, headers=headers, data=body)
    elif method == PUT:
        response = requests.post(url, headers=headers, data=body)
    elif method == PATCH:
        response = requests.patch(url, headers=headers, data=body)
    elif method == DELETE:
        response = requests.delete(url, headers=headers)
    elif method == OPTIONS:
        response = requests.options(url, headers=headers, data=body)
    elif method == HEAD:
        response = requests.head(url, headers=headers)
    else:
        raise Exception(f'{method} is not supported')
    return response


def is_method_supported(method):
    method = method.upper()
    return GET == method or POST == method or PUT == method or \
           PATCH == method or DELETE == method or OPTIONS == method or \
           HEAD == method
