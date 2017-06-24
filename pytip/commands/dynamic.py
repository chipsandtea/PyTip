from json import dumps
from .base import Base

class Dynamic(Base):
    """Dynamically split the bill."""

    def __init__(self, options, *args, **kwargs):
        super(Dynamic, self).__init__(options, *args, **kwargs)
        #print 'in dynamic'
        self.gratuity = 15.0
        self.tax = 8.75
        self.subtotal = 0.0
        self.party_size = 1
        self.party = dict()

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

    def collect_names(self):
        print 'Please enter the names of the party members.'
        for i in range(self.party_size):
            name = raw_input("{0}: ".format(str(i + 1)))
            self.party[i] = {'name':name, 'price':0.0}

    def distribute_cost(self):
        tb_distributed = self.subtotal
        while tb_distributed != 0:
            # Check for bel
            print 'Current Distribution'
            print '===================='
            for k,v in self.party.iteritems():
                print k + ': ' + v['name'] + ' ; ' + v['price']
            item_cost = raw_input('Enter an Item Price: ')
            all_purchased_raw = raw_input('Enter number of all who had this item')
            purchased = [person.strip() for person in all_purchased_raw.split(',')]
            # numbers separated by spaces


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

        self.collect_names()

        tax_value = self.calculate_tax()
        print 'Tax (' + str(self.tax) + '%): $' + str(tax_value)
        tot_wo_tip = self.subtotal + tax_value
        print 'Total (w/o Tip): $' + str(tot_wo_tip)

        grat_value = self.calculate_tip()
        print 'Tip (' + str(self.gratuity) + '%): $' + str(grat_value)
        tot_wtip = tot_wo_tip + grat_value
        print 'Total (w/ Tip): $' + str(tot_wtip)



