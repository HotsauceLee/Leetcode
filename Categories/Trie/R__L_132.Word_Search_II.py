"""
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. 


Have you met this question in a real interview? Yes
Example
Given matrix:
doaf
agai
dcan
and dictionary:
{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}


dog:
doaf
agai
dcan
dad:
doaf
agai
dcan
can:
doaf
agai
dcan
again:
doaf
agai
dcan
"""

# ============= Trie ==============
# Time: fucktard
# Space: fucktard
class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.d = {}
        self.has_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.delta_x = [0, 0, 1, -1]
        self.delta_y = [1, -1, 0, 0]
        
    def add(self, word):
        if not word:
            return
        
        cur_node = self.root
        for c in word:
            if c not in cur_node.d:
                cur_node.d[c] = TrieNode(c)
            cur_node = cur_node.d[c]
        cur_node.has_word = True
        
    def find(self, word):
        if not word:
            return False
            
        cur_node = self.root
        for c in word:
            if c not in cur_node.d:
                return False
            cur_node = cur_node[c]
            
        return cur_node.has_word
        
    def __inbound(self, x, y, max_x, max_y):
        return 0 <= x < max_x and 0 <= y < max_y

    def dfs(self, cur_x, cur_y, chars_so_far, cur_node, board, result):
        cur_node = cur_node or self.root
        cur_char = board[cur_x][cur_y]
        if cur_node.has_word:
            result.add(''.join(chars_so_far))
        if cur_char not in cur_node.d:
            return

        for i in xrange(len(self.delta_x)):
            next_x = cur_x + self.delta_x[i]
            next_y = cur_y + self.delta_y[i]
            if self.__inbound(next_x, next_y, len(board), len(board[0])):
                board[cur_x][cur_y] = '#'
                chars_so_far.append(cur_char)
                self.dfs(next_x, next_y, chars_so_far, cur_node.d[cur_char], board, result)
                chars_so_far.pop()
                board[cur_x][cur_y] = cur_char
                    
                
            

class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []

        t = Trie()
        # Build the trie using dict
        for w in words:
            t.add(w)

        # find each possible word in board
        len_row, len_col = len(board), len(board[0])
        result = set()
        for row in xrange(len_row):
            for col in xrange(len_col):
                t.dfs(row, col, [], None, board, result)

        return list(result)
