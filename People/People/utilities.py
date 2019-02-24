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
        print(ord(ch) - ord('a'))
        return ord(ch) - ord('a')
    else:
        return space_index


def index_to_char(ch):
    """
    helper function
    Converts key current character into index
    use only 'a' through 'z'
    :param ch: string of length 1
    :return: integer range: 0 to 26
    """
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    return characters[ch]


def search_persons(keyword):
    """
    :param keyword: A string
    :return: found: True/False results: Array
    """
    from .database import last_name_index, first_name_index, middle_name_index, persons
    from .search import Search, explore, suggest
    from .serializers import PersonSerializer

    # Since there are three columns we need to traverse three trees
    search_objects = [
        Search(first_name_index, keyword),
        Search(middle_name_index, keyword),
        Search(last_name_index, keyword)
    ]

    # Generate results by Levenshtein Automaton based traversal
    found = False
    for search_object in search_objects:
        explore(search_object, search_object.index_tree.root,
                search_object.max_distance, search_object.search_key)
        found = found or search_object.found

    results = []
    for distance in range(search_objects[0].max_distance + 1):
        results.append([])
        count = 0
        for search_object in search_objects:
            count += 1
            for result in search_object.results[distance]:
                results[distance].append(PersonSerializer(persons[result]).data())

    return found, results
