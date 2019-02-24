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