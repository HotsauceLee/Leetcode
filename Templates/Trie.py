"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
    def __init__(self, c=None):
        # Initialize your data structure here.
        self.c = c
        self.d = {}
        self.has_word = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if not word:
            return
      
        cur_node = self.root
        for c in word:
            if c in cur_node.d:
                cur_node = cur_node.d[c]
            else:
                new_node = TrieNode(c)
                cur_node.d[c] = new_node
                cur_node = new_node

        cur_node.has_word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        if not word:
            return False
            
        cur_node = self.root
        for c in word:
            if c not in cur_node.d:
                return False
            cur_node = cur_node.d[c]
            
        return cur_node.has_word
            
    
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        if not prefix:
            return False
            
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.d:
                return False
            cur_node = cur_node.d[c]
            
        return cur_node.has_word or len(cur_node.d) != 0
