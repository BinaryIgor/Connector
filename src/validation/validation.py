MIN_PORT = 0
MAX_PORT = 65_535
HTTP_PREFIX = 'http://'
HTTPS_PREFIX = 'https://'


def is_valid_http_url(url):
    return (url.find(HTTP_PREFIX) == 0 and len(url) > len(HTTP_PREFIX)) or \
           (url.find(HTTPS_PREFIX) == 0 and len(url) > len(HTTPS_PREFIX))


def is_valid_header(header):
    return len(header.split(':')) == 2


def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        for p in parts:
            int(p)
            return True
    except Exception:
        return False


def is_valid_port(port):
    try:
        return MIN_PORT <= int(port) <= MAX_PORT
    except Exception:
        return False


def is_positive_number(number):
    try:
        return float(number) >= 0
    except Exception:
        return False


def is_valid_binary(data):
    for d in data:
        if d != '1' and d != '0':
            return False
    return True
