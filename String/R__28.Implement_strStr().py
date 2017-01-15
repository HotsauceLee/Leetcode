# =========== Traditional way TLE =================
# Time: O(n*k) - k is the length of the target
# Space: O(1)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None: return -1
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        
        i = 0
        while i < len(haystack):
            t_index = 0
            s_index = i
            while s_index < len(haystack) and t_index < len(needle) and haystack[s_index] == needle[t_index]:
                s_index += 1
                t_index += 1
            if t_index == len(needle):
                return i
            # This saves a lot of time
            if s_index == len(haystack): return -1
            i += 1

        return -1

# ================= Better ================
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """
        if haystack is None or needle is None: return -1
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        """
        
        i = 0
        while 1:
            j = 0
            while 1:
                if j == len(needle): return i
                if i + j == len(haystack): return -1
                if needle[j] != haystack[i + j]: break
                j += 1
                
            i += 1
        
# ============= Python string.find() ==============
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        
# ============== TODO: KMP and RK =====================
