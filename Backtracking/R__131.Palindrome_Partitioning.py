#========== Back tracking ============
# Time: ？
# Space: ?
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            begin, end = 0, len(s) - 1
            while begin < end:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True
            
        def helper(s, begin, cur_path, result):
            if begin == len(s):
                result.append(cur_path[:])
                return
        
            for i in xrange(begin, len(s)):
                cur_str = s[begin:i+1]
                if isPalindrome(cur_str):
                    cur_path.append(cur_str)
                    helper(s, i + 1, cur_path, result)
                    cur_path.pop()
                    
        result = []
        helper(s, 0, [], result)
        return result
