from .indexer import ColumnIndex
from .utilities import clean_string, get_prefixes, get_suffixes
# All data stored in list for now
# Can be stored in memory if time permitted
persons = []

# Three indexes, one for each column of data
name_index = ColumnIndex()


class Person:
    """
    One person object which contain 4 columns
    1. index 2. First Name 3. Middle Name  4. Last Name
    """
    def __init__(self, index, first_name='', middle_name='', last_name=''):
        # clean data

        self.index = index
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = '{} {} {}'.format(first_name, middle_name, last_name)

        first_name = clean_string(first_name)
        middle_name = clean_string(middle_name)
        last_name = clean_string(last_name)

        for name in first_name.split():
            suffixes = get_suffixes(name)
            prefixes = get_prefixes(name)
            name_index.insert(name, index)
            possible_substrings = suffixes + prefixes
            for possible_substring in possible_substrings:
                name_index.insert(possible_substring, index)

        for name in middle_name.split():
            suffixes = get_suffixes(name)
            prefixes = get_prefixes(name)
            name_index.insert(name, index)
            possible_substrings = suffixes + prefixes
            for possible_substring in possible_substrings:
                name_index.insert(possible_substring, index)

        for name in last_name.split():
            suffixes = get_suffixes(name)
            prefixes = get_prefixes(name)
            possible_substrings = suffixes + prefixes
            name_index.insert(name, index)
            for possible_substring in possible_substrings:
                name_index.insert(possible_substring, index)
