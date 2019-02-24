from math import sqrt
from .utilities import char_to_index, index_to_char


class Search:
    """
    Search object which keeps track of results and suggestions/autocomplete over the recursive strategy
    """
    def __init__(self, index_tree, search_key):
        self.index_tree = index_tree
        self.search_key = search_key
        #Error margin calculation
        max_distance = round(sqrt(len(search_key)-len(search_key)/2))

        # Avoid errors more than 4 since traversal will be huge
        self.max_distance = max_distance if max_distance <= 4 else 4
        self.suggestions = []
        self.found = False
        self.results = []
        for distance in range(self.max_distance+1):
            self.results.append([])


def suggest(search_object):
    pass


def explore(search_object, node, error_left, sub_key, level = 0):
    """
    :param search_object: Search object
    :param node: Index to search
    :param error_left: margin for error left
    :param sub_key: substring to be traversed
    :return:
    """
    # Append results if word like those exist
    if node.isEndOfWord:
        # Avoid larger errors with smaller matches
        if (level+error_left)/len(search_object.search_key) > 0.7:
            search_object.found = True
            search_object.results[search_object.max_distance - error_left].extend(node.indexes)

    # recursion break when room for error becomes negative:
    if error_left < 1:
        return

    index = char_to_index(sub_key[0])
    if len(sub_key) == 1:
        sub_key = '  '
    # Check if key exists or mark as error and traverse
    skip = index
    if node.children[index]:
        parent = node.children[index]
        # Keep adding spaces till margin for error is left
        explore(search_object, parent, error_left, sub_key[1:], level+1)

    error_left -= 1
    parents = [child for i, child in enumerate(node.children) if child and i != index]

    for parent in parents:
        explore(search_object, parent, error_left, sub_key[1:], level+1)
