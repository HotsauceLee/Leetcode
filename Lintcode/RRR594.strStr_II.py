# =========== Robin Karp(hash) =============
# Time: O(n)
# Space: O(1)
class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1
            
        len_target = len(target)
        if len_target == 0:
            return 0
        
        base = 1000000
        # get power
        power = 1
        for i in xrange(len_target):
            power = (power*31) % base
        # get target hash code
        target_code = 0
        for i in xrange(len_target):
            target_code = (target_code*31 + ord(target[i])) % base
        # find match
        hash_code = 0
        for i in xrange(len(source)):
            hash_code = (hash_code*31 + ord(source[i])) % base
            if i < len_target:
                continue
            
            prev_char_code = (ord(source[i-len_target])*power) % base
            hash_code = (hash_code - prev_char_code) % base
            
            if hash_code == target_code and source[(i - len_target + 1) : i + 1] == target:
                return i - len_target + 1
                    
        return -1
