_input_functions = {}


def configure(input_functions):
    for i in input_functions:
        _input_functions[i] = input_functions[i]


def smart_input(prompt=''):
    result = input(prompt)
    for i in _input_functions:
        if i.lower() == result.lower():
            _input_functions[i]()
    return result
