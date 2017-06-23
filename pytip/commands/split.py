# pytip/commands/split.py
"""The split command. Equally splits the bill amongst all party members."""

from json import dumps
from .base import Base

class Split(Base):
    """Split the bill!"""
    def __init__(self, options, *args, **kwargs):
        super(Split, self).__init__(options, *args, **kwargs)
        self.gratuity = 15.0
        self.tax = 8.75
        self.subtotal = 0.0
        self.party_size = 1

    def set_gratuity(self, custom_gratuity):
        try:
            self.gratuity = float(custom_gratuity)
        except TypeError as e:
            print e
            quit()

    def set_tax(self, custom_tax):
        try:
            self.tax = float(custom_tax)
        except TypeError as e:
            print e
            quit()

    def set_subtotal(self, subtotal):
        try:
            self.subtotal = float(subtotal)
        except TypeError as e:
            print e
            quit()

    def set_party_size(self, size):
        try:
            self.party_size = int(size)
        except TypeError as e:
            print e
            quit()

    def calculate_tax(self):
        return (self.tax / 100) * self.subtotal

    def calculate_tip(self):
        return (self.gratuity / 100) * self.subtotal

    def run(self):
        # print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
        self.set_subtotal(self.options['<subtotal>'])
        self.set_party_size(self.options['<party_size>'])
        print 'Subtotal: $' + str(self.subtotal)
        print 'Party Size: ' + str(self.party_size)
        if self.options['--gratuity']:
            custom_gratuity = raw_input('Please enter custom tip value: ')
            self.set_gratuity(custom_gratuity)
        if self.options['--tax']:
            custom_tax = raw_input('Please enter custom tax value: ')
            self.set_tax(custom_tax)

        tax_value = self.calculate_tax()
        print 'Tax (' + str(self.tax) + '%): $' + str(tax_value)
        tot_wo_tip = self.subtotal + tax_value
        print 'Total (w/o Tip): $' + str(tot_wo_tip)

        grat_value = self.calculate_tip()
        print 'Tip (' + str(self.gratuity) + '%): $' + str(grat_value)
        tot_wtip = tot_wo_tip + grat_value
        print 'Total (w/ Tip): $' + str(tot_wtip)

        #per_person = "0.2f"
        print 'Per Person (Party of: ' + str(self.party_size) + '): $' + ("%0.2f" % (tot_wtip / self.party_size))
