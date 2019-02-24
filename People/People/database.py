
class Person:

    def __init__(self, first_name='', middle_name='', last_name=''):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = '{} {} {}'.format(first_name, middle_name, last_name)


""" Tuples are faster for creation so used them for now
 List in-case if the table will dynamically increase"""
persons = []
