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
            print'Remaining Subtotal: ' + str(tb_distributed)
            print 'Current Distribution'
            print '===================='
            for k,v in self.party.iteritems():
                print str(k) + ': ' + v['name'] + ' ; ' + str(v['price'])
            item_cost = float(raw_input('Enter an Item Price: '))
            shared_flag = raw_input('Was this item shared? (y/n): ').lower()
            if shared_flag == 'y' or shared_flag == 'yes':
                shared_flag = True
            elif shared_flag == 'n' or shared_flag == 'no':
                shared_flag = False
            else:
                raise TypeError
            if shared_flag:
                print 'Enter the number of each person who shared this item.'
                print 'Enter \'d\' or \'done\' when all have been entered.'
                keep_going = True
                shared = set()
                while keep_going and len(shared) < self.party_size:
                    num = raw_input('#: ')
                    if num == 'd' or num == 'done':
                        keep_going = False
                    elif int(num) in self.party.keys():
                        shared.add(int(num))
                shared_cost = item_cost / len(shared)
                for person_id in shared:
                    self.party[person_id]['price'] += shared_cost
                tb_distributed -= item_cost
            else:
                print 'Enter the number of each person who ordered this item.'
                print 'Enter \'d\' or \'done\' when all have been entered.'
                keep_going = True
                ordered = set()
                while keep_going and len(ordered) < self.party_size:
                    num = raw_input('#: ')
                    if num == 'd' or num == 'done':
                        keep_going = False
                    elif int(num) in self.party.keys():
                        ordered.add(int(num))
                ordered_cost = item_cost * len(ordered)
                for person_id in ordered:
                    self.party[person_id]['price'] += item_cost
                tb_distributed -= ordered_cost

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
        self.distribute_cost()

        tax_value = self.calculate_tax()
        print 'Tax (' + str(self.tax) + '%): $' + str(tax_value)
        tot_wo_tip = self.subtotal + tax_value
        print 'Total (w/o Tip): $' + str(tot_wo_tip)

        grat_value = self.calculate_tip()
        print 'Tip (' + str(self.gratuity) + '%): $' + str(grat_value)
        tot_wtip = tot_wo_tip + grat_value
        print 'Total (w/ Tip): $' + str(tot_wtip)

        tip_per = grat_value/self.party_size
        tax_per = tax_value/self.party_size
        print 'Final Distribution'
        print '=================='
        for person in self.party:
            final_per = person['price'] + tip_per + tax_per
            print person['name'] + ' : $' + str(final_per)



