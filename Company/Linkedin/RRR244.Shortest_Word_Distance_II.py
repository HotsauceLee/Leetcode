# ================= preprocessing ===============
# Time: init: O(n^2) call: O(1)
# Space: O(n^2)
# Idea:
"""
I did the same thing after I got TLE and thought on it for sometime i realized the O(n^2) + O(1) solution is a poor decision any time n (the number of words) > the number of times shortest method is called. Lets take an example say n = 64 and shortest is called 20 times. Now if we look at the approximate total number of operations in our O(n^2) + O(1) solution we would get 64^2 + 20 = 4116. now if you observe others O(n)+O(n) solution their approximate total number of operations would be 64 + (20 * 64) = 1280.

In short O(n^2) + O(1) solution is only better if shortest is called n times.
"""

# ================ compare each position of the two words ===========
# Time: init: O(n) call: O(n)
# Space: O(n)
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for idx, word in enumerate(words):
            if word not in self.d:
                self.d[word] = [idx]
            else:
                self.d[word].append(idx)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1, list2 = self.d[word1], self.d[word2]
        result, c1, c2 = float('inf'), 0, 0
        while c1 < len(list1) and c2 < len(list2):
            if list1[c1] < list2[c2]:
                result = min(result, list2[c2] - list1[c1])
                c1 += 1
            else:
                result = min(result, list1[c1] - list2[c2])
                c2 += 1
                
        return result


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
