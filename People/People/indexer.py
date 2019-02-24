from .utilities import char_to_index


class AlphabetNode:
    """
    A tree node
    """

    def __init__(self):
        """
        Create possible children 26 alphabets + space to support one of the edge case names
        """
        self.children = [None] * 27  # 26 to support space
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
        self.possible = 0
        self.indexes = []


class ColumnIndex:
    """
    The index tree which is based on Trie Data Structure
                    (Root)
                     /  \
                   (a)  (b)<-AlphabetNode
                   /     \
                  /       \
               (n)         (a)
              /   \         \
            (t)  (y)        (r)
    """
    def __init__(self):
        """
        # Create default empty root node
        """
        self.root = self.get_node()

    def get_node(self):
        """
        Creates alphabet node
        """
        return AlphabetNode()

    def insert(self, key, position):
        """
        1. Inserts key into the tree
        2. If prefix is present in just marks nodes on the way
        3. Marks leaf node
        4. Adds position of the key in database
        """

        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = char_to_index(key[level])

            # if current character is not present
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]
            p_crawl.possible += 1
            # mention start and end index in table

            # mark last node as leaf
        p_crawl.indexes.append(position)
        p_crawl.isEndOfWord = True
