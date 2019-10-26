from enum import Enum

NOT_IMPLEMENTED = 'Not implemented yet'


class Protocol(Enum):
    UDP = 1
    TCP = 2
    HTTP = 3


def action(protocol: Protocol):
    if protocol == Protocol.UDP:
        return _udp
    elif protocol == Protocol.TCP:
        return _tcp
    elif protocol == Protocol.HTTP:
        return _http
    else:
        return lambda: print("{} isn't proper protocol".format(protocol))


def _http():
    print(NOT_IMPLEMENTED)


def _udp():
    print(NOT_IMPLEMENTED)


def _tcp():
    print(NOT_IMPLEMENTED)
