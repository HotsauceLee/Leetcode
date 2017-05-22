"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""

# ============== Round Robbin ==============
# Time: O(n*maxWidth)
# Space: O(n)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words or maxWidth <= 0:
            return [""]
        
        l, cur, result = 0, [], []
        for w in words:
            # + len(cur) means every word appends at
            # least one space
            if l + len(w) + len(cur) > maxWidth:
                for i in xrange(maxWidth - l):
                    # len(cur) - 1: not append space to
                    # the last word.
                    # When len(cur) == 1, if l is maxWidth,
                    # it won't go into the loop. if maxWidth > l,
                    # we only wanna add space to that only word, 
                    # and to make i%(len(cur) - 1) always == 0, 
                    # just do i%1. so i%(len(cur) - 1 or 1)
                    cur[i%(len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                l, cur = 0, []
            cur.append(w)
            l += len(w)
            
        last_line = ' '.join(cur)
        result.append(last_line + (' '*(maxWidth - len(last_line))))
        # or ' '.join(cur).ljust(maxWidth)
        return result
