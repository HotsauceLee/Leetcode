"""
Design a data structure that supports the following two operations: addWord(word) and search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or ..

A . means it can represent any one letter.

 Notice

You may assume that all words are consist of lowercase letters a-z.

Have you met this question in a real interview? Yes
Example
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true
"""

# ============== Trie ================
# Time: addWord: O(len(word)), search: O(tree size)
# Space: O(n)
class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.has_word=False
        self.d = {}

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.root = TrieNode()


    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        if not word:
            return
        
        cur_node = self.root
        for c in word:
            if c not in cur_node.d:
                cur_node.d[c] = TrieNode(c)
            cur_node = cur_node.d[c]
        cur_node.has_word = True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        return self.__search(word, 0, self.root)
        
    def __search(self, word, cur_word_idx, cur_node):
        for idx in xrange(cur_word_idx, len(word)):
            c = word[idx]
            if c in cur_node.d:
                cur_node = cur_node.d[c]
            elif c == '.':
                for node in cur_node.d.values():
                    if self.__search(word, idx + 1, node):
                        return True
                        
                return False
                
            else:
                return False
                
        return cur_node.has_word
        
        
            
        


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
