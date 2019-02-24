from .indexer import ColumnIndex

# All data stored in list for now
# Can be stored in memory if time permitted
persons = []

# Three indexes, one for each column of data
first_name_index = ColumnIndex()
middle_name_index = ColumnIndex()
last_name_index = ColumnIndex()


class Person:
    """
    One person object which contain 4 columns
    1. index 2. First Name 3. Middle Name  4. Last Name
    """
    def __init__(self, index, first_name='', middle_name='', last_name=''):
        self.index = index
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        first_name_index.insert(first_name, index)
        middle_name_index.insert(middle_name, index)
        last_name_index.insert(last_name, index)
        self.full_name = '{} {} {}'.format(first_name, middle_name, last_name)




