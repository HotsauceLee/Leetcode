"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
Seen this question in a real interview before?   Yes  
"""

# =============== set ==============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        
        result = []
        for w in words:
            w_set = set(w.lower())
            if w_set.issubset(row1) or w_set.issubset(row2) or w_set.issubset(row3):
                result.append(w)
                
        return result
            
# ============== regular traversal =============
# Time: O(n*len(word))
# Space: O(1)
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        rows = [row1, row2, row3]
        result = []
        # O(n)
        for w in words:
            if not w:
                continue
            row = -1
            first_letter = w[0].lower()
            # O(3)
            for idx, r in enumerate(rows):
                if first_letter in r:
                    row = idx
                    break
            # O(len(w))
            for i in xrange(1, len(w) + 1):
                if i == len(w):
                    result.append(w)
                    break
                if w[i].lower() not in rows[row]:
                    break
                    
        return result
