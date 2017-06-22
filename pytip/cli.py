"""
pytip

Usage:
    pytip split [-gt] <party size> <subtotal>
    pytip dynamic [-gt] <party size> <subtotal>
    pytip -h | --help
    pytip --version

Options:
    -g --gratuity   Custom gratuity rate.
    -t --tax        Custom tax rate.
    -h --help       Show this screen.
    --version       Show version.

Examples:
    pytip split 4 64.00
    pytip dynamic 4 64.00

Help:
    For help using this tool, please open an issue on the Github repository:]
    https://github.com/chipsandtea/pytip
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    """Main CLI Entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)

    # Here we try to dynamically match the command the user is trying to run
    # with a per-defined command class we've already created.

    for k, v in options.iteritems():
        if hasattr(commands, k):
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base']
            command = command(options)
            command.run()