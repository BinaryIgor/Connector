from src.cli import http_cli, socket_cli
from src.protocol.protocol import Protocol
from src.input import smart_input
import sys


class Option:

    def __init__(self, key, value, action=None):
        self.key = key
        self.value = value
        self._action = action

    def execute(self):
        if self._action is not None:
            self._action()


def setup():
    smart_input.configure({
        ':q': close,
        ':m': show
    })


def show():
    options = []
    for p in Protocol:
        options.append(Option(p.name, p.value,
                              action=_protocol_action(p)))

    print('Welcome to connector.')
    _print_shortcuts()
    print()

    last_option = None
    while True:
        if last_option:
            _print_shortcuts()
            print()
            print(f'{last_option.key}')
            last_option.execute()
        else:
            _show_options(options)
            last_option = _choose(options,
                                  smart_input.smart_input('Choose protocol: '))


def _print_shortcuts():
    print('Press :q to quit, :m to go back to menu,',
          'enter to skip any optional(o) input.')


def _repeat_last_option(last_option):
    return last_option and smart_input.smart_input(
        'Change protocol?(y/n): ').lower() != 'y'


def close():
    print()
    print('Stay connected.')
    sys.exit(0)


def _protocol_action(protocol):
    if protocol == Protocol.UDP:
        return lambda: socket_cli.show(udp=True)
    elif protocol == Protocol.TCP:
        return lambda: socket_cli.show(udp=False)
    elif protocol == Protocol.HTTP:
        return http_cli.show
    else:
        return lambda: print("{} isn't a proper protocol".format(protocol))


def _show_options(options):
    print('\n'.join(
        [str(o.value) + ' - ' + str(o.key) for o in options]))


def _choose(options, option):
    for o in options:
        if str(o.value) == option:
            print()
            o.execute()
            return o
    print()
    print(f'Choose proper option. {option} is unknown')
    return None
