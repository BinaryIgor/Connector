import sys


def input_or_quit(prompt='', q='q'):
    result = input(prompt)
    if result.lower() == q.lower():
        sys.exit(0)
    return result
