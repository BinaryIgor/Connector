import sys
from src.cli import menu_cli
from src.input.smart_input import SmartException


def handle_error(error, restart=True):
    try:
        print()
        if isinstance(error, SmartException):
            error.to_execute()
        else:
            print('Something went wrong...', file=sys.stderr)
            print(error, file=sys.stderr)
            print()
            if restart:
                menu_cli.show()
    except Exception as e:
        handle_error(e)
