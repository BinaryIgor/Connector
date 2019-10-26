QUIT = 'q'


class Option:

    def __init__(self, key, value, action=None):
        self.key = key
        self.value = value
        self._action = action

    def execute(self):
        if self._action is not None:
            self._action()


def show_options(options):
    print('\n'.join(
        [str(o.key) + ' - ' + str(o.value) for o in options]))


def choose(options, option):
    if option == QUIT:
        return
    executed = False
    for o in options:
        print(o.value)
        if str(o.value) == option:
            o.execute()
            executed = True
            break
    if not executed:
        print('Choose proper option. {} is unknown'.format(option))
