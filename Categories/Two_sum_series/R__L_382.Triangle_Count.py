"""
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

Have you met this question in a real interview? Yes
Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
"""

# ========= hi&lo pointers ==============
# Time: O(n^2)
# Space: O(1)
class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        if not S:
            return 0
          
        S.sort() 
        biggest, result = len(S) - 1, 0
        while biggest >= 2:
            begin, end = 0, biggest - 1
            while begin < end:
                if S[begin] + S[end] > S[biggest]:
                    result += end - begin
                    end -= 1
                else:
                    begin += 1
            biggest -= 1
                    
        return result
