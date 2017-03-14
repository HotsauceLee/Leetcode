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
