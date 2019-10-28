from src.cli import menu_cli
import sys
import traceback
import signal


def signal_handler(sig, frame):
    sys.exit(0)


try:
    signal.signal(signal.SIGINT, signal_handler)
    menu_cli.show()
except KeyboardInterrupt:
    print(traceback.format_exc())
    sys.exit()
