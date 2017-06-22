# pytip/commands/split.py
"""The split command. Equally splits the bill amongst all party members."""

from json import dumps
from .base import Base

class Split(Base):
    """Split the bill!"""

    def run(self):
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        print(self.args)
        print('Mama we made it')
