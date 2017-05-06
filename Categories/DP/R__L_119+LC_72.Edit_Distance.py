"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview? Yes
Example
Given word1 = "mart" and word2 = "karma", return 3.
"""

# ================ DP =================
# Time: O(len(word1) + len(word1)*len(word2))
# Space: O(len(word1))
# Idea:
"""
 replace | insert
  ----------------
  delete | now
  
if word1[i] == word2[j]:
    # no need to care about the current char
    # equals word1[i - 1] => word2[j - 1]
    dp[i][j] = dp[i-1][j-1]
else:
    # min among:
    #   delete: word1[i] => word2[j - 1],  plus the delete(1)
    #   insert: word1[i - 1] => word2[j], plus the insert(1)
    #   replace: word1[i - 1] => word2[j - 1], plus the replace(1)
    dp[i][j] = min((dp[i][j-1], dp[i-1][j]), dp[i-1][j-1]) + 1
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        if not word1 or not word2:
            return len(word1) or len(word2)
            
        prev_row = [i for i in xrange(len(word1) + 1)]
            
        for row in xrange(1, len(word2) + 1):
            cur_row = [row]
            for col in xrange(1, len(word1) + 1):
                if word1[col - 1] == word2[row - 1]:
                    cur_row.append(prev_row[col - 1])
                else:
                    cur_row.append(min(min(cur_row[col - 1], prev_row[col]), prev_row[col - 1]) + 1)
            prev_row = cur_row
                    
        return cur_row[-1]
        
