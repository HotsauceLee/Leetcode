# ================== Last encountered index ===================
# Time: O(n)
# Space: O(1)
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_distance = float('inf')
        last_idx = -1
        d = [word1, word2]
        for idx, word in enumerate(words):
            # if not one of the words, keep going
            if word in d:
                # Only do shit when already found one, otherwise update last_idx
                if last_idx != -1 and words[last_idx] != words[idx]:
                    # Update min only when current word if different from the last one
                    if idx - last_idx < min_distance: min_distance = idx - last_idx
                # Update last encountered to the current one
                last_idx = idx
                
        return min_distance
