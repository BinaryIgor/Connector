MIN_PORT = 0
MAX_PORT = 65_535


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
