"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?

The above arrows point to positions where the corresponding bits are different.
"""

# ================ mask to stop when out of 1s =============
# Time: O(32)
# Sapce: O(1)
public class Solution {
    public int hammingDistance(int x, int y) {
        int mask = ~0;
        int diff, diffSave;
        diff = diffSave = x^y;
        int result = 0;
        while ( (mask & diffSave) != 0 ) {
            if ( (diff & 1) == 1 ) {
                result++;
            }
            diff >>= 1;
            mask <<= 1;
        }
        
        return result;
    }
    
    private void printBits(int input) {
        String result = "";
        for ( int i = 0; i < 32; i++ ) {
            result = String.valueOf(input & 1) + result;
            input >>= 1;
        }
        
        System.out.println(result);
    }
}
