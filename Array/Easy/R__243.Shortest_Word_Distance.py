class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last_word = None
        distance = 0
        min_distance = float('inf')
        d = [word1, word2]
        for word in words:
            if word in d:
                if last_word:
                    if word != last_word:
                        if distance + 1 < min_distance: min_distance = distance + 1
                    distance = 0
                last_word = word
            else:
                if last_word: distance += 1
            
            if min_distance == 1: return 1
        return min_distance
