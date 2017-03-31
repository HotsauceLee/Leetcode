"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

# =========== Hash store all 10-letter strings =============
# Time: O(n)
# Space: O(10*(n-10))
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 10:
            return []
            
        d = set()
        result = set()
        for i in xrange(len(s) - 9):
            cur_substring = s[i:i + 10]
            if cur_substring in d:
                result.add(cur_substring)
            else:
                d.add(cur_substring)
                
        return list(result)
        

# ============== Hash store ACGT in 20 bits =============
# Time: O((n-10)*10)
# Space: O(10*(n-10) but less since storing ints)
# idea:
"""
The key point is that it is not doing hash, it is doing the exact coding of a 10-letter sequence into a 4-bytes number, which is simply not possible for any generic string, but is possible for strings in this problem because they can have only 4 differfent characters.

In more detail:

If two objects have same hash it means that they may or may not be equal (though two equal objects are required to have same hash). So hashing is not enough here (like calling just "AACCCCCGGG".hashCode() and storing it in the map), because there can be another (different) string with same hash and the program will output wrong result.

We also cannot store the 10-letter substrings themselves because they consume too much memory and the program will exceed memory limit.

So, instead of hashing or storing strings themselves the solution converts 10 letter string into 4-bytes integer (which is much smaller than string in terms of consumed memory). This would not be possible if the string could contain all 26 letters of English alphabet for example. But it is possible for our case, because there can be only 'A', 'C', 'G' and 'T' letters.

So we have only 4 possible letters, and we can use as little bits as possible to store each character of our 10-letter string. We really need only 2 bits (bits, not bytes) for this. Specifically the solution uses the following coding:

0 = 00 (bits in binary number system) = 'A'

1 = 01 (bits in binary number system) = 'C'

2 = 10 (bits in binary number system) = 'G'

3 = 11 (bits in binary number system) = 'T'

Note that since there 10 letters and each letter requires only 2 bits, we will need only 10 * 2= 20 bits to code the string (which is less then size of integer in java (as well as in all othere popular languages), which is 4 bytes = 32 bits).

For example, this is how "AACCTCCGGT" string will be coded:

A A C C T C C G G T

00 00 01 01 11 01 01 10 10 11 = 00000101110101101011 (binary) = 23915 (decimal)
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        self.m = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3
        }
        d, result = set(), set()
        for i in xrange(len(s) - 9):
            cur_hashcode = self.__hash_code(s[i:i+10])
            if cur_hashcode in d:
                result.add(s[i:i+10])
            else:
                d.add(cur_hashcode)
                
        return list(result)
        
    def __hash_code(self, s):
        result = 0
        for c in s:
            result <<= 2
            result |= self.m[c]
            
        return result
