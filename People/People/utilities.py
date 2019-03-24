from .constants import space_index


def char_to_index(ch):
    """
    helper function
    Converts key current character into index
    use only 'a' through 'z'
    :param ch: string of length 1
    :return: integer range: 0 to 26
    """
    if ch.isalpha():
        ch = ch.lower()
        return ord(ch) - ord('a')
    return space_index


def clean_string(str_data):
    """
    helper function
    Removes special characters from strings and converts it to lower case
    :param str_data: string
    :return: clean_string
    """
    import re
    str_data = str(str_data.lower())
    clean = re.sub('[^a-z ]+', '', str_data)
    return clean


def search_persons(keyword):
    """
    :param keyword: A string
    :return: found: True/False results: Array
    """
    from .database import name_index, persons
    from .search import Search, explore, suggest
    from .serializers import PersonSerializer

    found = False
    results = [[]]
    result_data = [[]]

    for key in keyword.split():
        search_object = Search(name_index, key)
        # Generate results by Levenshtein Automaton based traversal
        explore(search_object, search_object.index_tree.root,
                search_object.max_distance, search_object.search_key)
        found = found or search_object.found
        for distance in range(search_object.max_distance+1):
            if distance >= len(results):
                results.append([])
                result_data.append([])
            results[distance].extend(search_object.results[distance])

    # Remove duplicates
    already_present = set()
    for result in results:
        result = set(result) - set(already_present)
        already_present.union(set(result))

    rank = 0
    for result in results:
        for person_id in result:
            result_data[rank].append(PersonSerializer(persons[person_id]).data())

    return found, result_data


def get_suffixes(string_name):
    """
    :return: an array of possible suffixes
    """
    name_suffixes = []

    while len(string_name) > 3:
        string_name = string_name[1:]
        name_suffixes.append(string_name)

    return name_suffixes


def get_prefixes(string_name):
    """
    :return:an array of possible preixes
    """

    name_prefixes = []

    while len(string_name) > 3:
        string_name = string_name[:-1]
        name_prefixes.append(string_name)

    return name_prefixes

