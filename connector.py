from src.cli import menu_cli, error_cli
import sys
import signal


def signal_handler(sig, frame):
    menu_cli.close()


try:
    signal.signal(signal.SIGINT, signal_handler)
    menu_cli.setup()
    menu_cli.show()
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    error_cli.handle_error(e)
