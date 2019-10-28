from src.cli import http_cli, tcp_cli
from src.protocol.protocol import Protocol

NOT_IMPLEMENTED = 'Not implemented yet'
QUIT = 'q'


class Option:

    def __init__(self, key, value, action=None):
        self.key = key
        self.value = value
        self._action = action

    def execute(self):
        if self._action is not None:
            self._action()


def show():
    options = []
    for p in Protocol:
        options.append(Option(p.name, p.value,
                              action=_protocol_action(p)))

    print('Welcome to connector.',
          'Press q to quit, press enter to skip any optional input.')
    print('Choose protocol:')
    next_option = True
    while next_option:
        _show_options(options)
        option = input()
        if option.lower() == 'q':
            break
        if _choose(options, option):
            next_option = input("Continue?(y/n)").lower() == 'y'
        else:
            next_option = True


def _protocol_action(protocol):
    if protocol == Protocol.UDP:
        return lambda: print(NOT_IMPLEMENTED)
    elif protocol == Protocol.TCP:
        return tcp_cli.show
    elif protocol == Protocol.HTTP:
        return http_cli.show
    else:
        return lambda: print("{} isn't proper protocol".format(protocol))


def _show_options(options):
    print('\n'.join(
        [str(o.key) + ' - ' + str(o.value) for o in options]))


def _choose(options, option):
    if option == QUIT:
        return True
    executed = False
    for o in options:
        print(o.value)
        if str(o.value) == option:
            o.execute()
            executed = True
            break
    if not executed:
        print(f'Choose proper option. {option} is unknown')
    return executed
