"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Seen this question in a real interview before?   Yes  
"""

# =============== check each bit ====================
# Time: O(32)
# Space: O(1)
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int mask = ~0;
        int nSave = n;
        int result = 0;
        while ( (mask & nSave) != 0 ) {
            if ( (n & 1) == 1 ) result++;
            n >>= 1;
            mask <<= 1;
        }
        
        return result;
    }
}

# ============= turn least significant 1 to 0 =============
# Time: O(# of 1 bits)
# Space: O(1)
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int result = 0;
        while ( n != 0 ) {
            result++;
            n &= (n - 1);
        }
        
        return result;
    }
}
