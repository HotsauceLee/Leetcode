"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""

# ============= BFS ================
# Time: O(w*wl + w*c)
"""
w = len(word)
wl = len(wordList)
c = # of distinct chars
"""
# Space: O(wl + wl + c)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # O(len(word)*len(wordList))
        d = set()
        all_chars = set()
        for w in wordList:
            d.add(w)
            for c in w:
                all_chars.add(c)

        if endWord not in d:
            return 0

        visited = set([beginWord])
        level = 0
        q = collections.deque([beginWord])
        # O(len(wordList))
        while len(q) > 0:
            level += 1
            print q
            cur_len = len(q)
            for i in xrange(cur_len):
                cur_word = q.pop()
                # O(len(word))
                for c in xrange(len(cur_word)):
                    # O(distinct chars)
                    for next_c in all_chars:
                        if cur_word[c] == next_c:
                            continue
                        
                        next_word = cur_word[:c] + next_c + cur_word[c+1:]
                        if next_word == endWord:
                            return level + 1
                        if next_word in d and next_word not in visited:
                            q.appendleft(next_word)
                            visited.add(next_word)
                        
        return 0
        
