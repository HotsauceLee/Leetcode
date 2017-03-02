# ============ remaionder ============
# Time: O(len(string))
# Space: O(1)
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        mn = 33
        hash_code = 0
        for i in xrange(len(key)):
            hash_code = (hash_code*mn + ord(key[i])) % HASH_SIZE
            
        return hash_code
