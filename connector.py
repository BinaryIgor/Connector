from cli import menu
from protocol import protocol

options = []
for p in protocol.Protocol:
    options.append(
        menu.Option(p.name, p.value, action=protocol.action(p)))

print("Welcome to connector. Choose protocol:")
menu.show_options(options)
menu.choose(options, input())
