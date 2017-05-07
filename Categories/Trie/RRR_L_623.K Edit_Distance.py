"""
Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit distance with the target no greater than k.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview? Yes
Example
Given words = ["abc", "abd", "abcd", "adc"] and target = "ac", k = 1
Return ["abc", "adc"]
"""

# =============== Trie + DP ================
# Time:
# Space:
# Idea: Same as edit distance, but instead of comparing all the words
#   with target, build a trie and do dp with every prefix, thus save time.
class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.has_word = False
        self.d = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
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
        
    def dfs(self, word_list, target, k):
        # build the trie
        for word in word_list:
            self.add(word)
        
        # build the first row
        dp = [i for i in xrange(len(target) + 1)]
        result = []
        for c, n in self.root.d.iteritems():
            self.__helper(n, c, target, dp, result, k)
        
        return result
        
    def __helper(self, cur_node, cur_word, target, prev_row, result, k):
        # build the cur dp row
        cur_row = [len(cur_word)]
        # i is the pos in the target string
        # i is 1 behind in the dp list
        for i in xrange(len(target)):
            if target[i] == cur_node.c:
                cur_row.append(prev_row[i])
            else:
                cur_row.append(min(min(prev_row[i + 1], cur_row[i]), prev_row[i]) + 1)
        # if edit distance <= k
        if cur_node.has_word and cur_row[-1] <= k:
            result.append(cur_word)
            
        for next_char, next_node in cur_node.d.iteritems():
            self.__helper(next_node, cur_word + next_char, target, cur_row, result, k)

class Solution:
    # @param {string[]} words a set of strings
    # @param {string} target a target string
    # @param {int} k an integer
    # @return {string[]} output all the stirngs that meet the requirements 
    def kDistance(self, words, target, k):
        # Write your code here
        if not words:
            return []
        if k < 0:
            return []
        if not target:
            return [word for word in words if len(word) <= k]
            
        t = Trie()
        return t.dfs(words, target, k)
        
        
