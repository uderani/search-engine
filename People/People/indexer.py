class AlphabetNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class ColumnIndex:
    # Trie data structure class
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        # Returns new trie node (initialized to NULLs)
        return AlphabetNode()

    def _char_to_index(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])

            # if current character is not present
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]

            # mark last node as leaf
        p_crawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]

        return not p_crawl and p_crawl.isEndOfWord
