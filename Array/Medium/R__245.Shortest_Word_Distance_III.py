#========== Keep track of last encountered ==========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev = None
        d = [word1, word2]
        result = float('inf')
        for idx in xrange(len(words)):
            word = words[idx]
            # Got a match
            if word in d:
                # Update distance if prev exists and word1 and word2 are the
                # same or current word and previous word are different.
                if prev is not None and (word1 == word2 or word != words[prev]):
                    if idx - prev < result: result = idx - prev
                # Update prev
                prev = idx
            
        return result
