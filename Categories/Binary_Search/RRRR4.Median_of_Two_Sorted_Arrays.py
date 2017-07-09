"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

# ================ BS on smaller array =================
# Time: O(min(len(nums1), len(nums2)))
# Space: O(1)
# Idea: https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation
"""
1. Simplify even and odd cases into one:
L/R is first one one the left/right
N        Index of L / R
1               0 / 0
2               0 / 1
3               1 / 1  
4               1 / 2      
5               2 / 2
6               2 / 3
7               3 / 3
8               3 / 4
(L + R)/2 = (A[(N-1)/2] + A[N/2])/2

To make L/R in odd number array has the same value, we add imaginary optitions between items:
[6 9 13 18]  ->   [# 6 # 9 # 13 # 18 #]    (N = 4)
position index     0 1 2 3 4 5  6 7  8     (N_Position = 9)
		  
[6 9 11 13 18]->   [# 6 # 9 # 11 # 13 # 18 #]   (N = 5)
position index      0 1 2 3 4 5  6 7  8 9 10    (N_Position = 11)

As you can see, there are always exactly 2*N+1 'positions' regardless of length N.
Therefore, the middle cut should always be made on the Nth position (0-based).
Since index(L) = (N-1)/2 and index(R) = N/2 in this situation,
we can infer that index(L) = (CutPosition-1)/2, index(R) = (CutPosition)/2.


2. If we have L1 > R1, it means there are too many large numbers on the left half of A1, then we must move C1 to the left (i.e. move C2 to the right); 
If L2 > R1, then there are too many large numbers on the left half of A2, and we must move C2 to the left.
Otherwise, this cut is the right one. 
After we find the cut, the medium can be computed as (max(L1, L2) + min(R1, R2)) / 2;

3. The only edge case is when a cut falls on the 0th(first) or the 2Nth(last) position. For instance, if C2 = 2N2, then R2 = A2[2*N2/2] = A2[N2], which exceeds the boundary of the array. To solve this problem, we can imagine that both A1 and A2 actually have two extra elements, INT_MAX at A[-1] and INT_MAX at A[N]. These additions don't change the result, but make the implementation easier: If any L falls out of the left boundary of the array, then L = INT_MIN, and if any R falls out of the right boundary, then R = INT_MAX.
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
            
        if n2 == 0:
            return (nums1[(n1-1)/2] + nums1[n1/2])/2.0
        
        lo, hi = 0, n2*2
        while lo <= hi:
            cut2 = (lo + hi)/2
            cut1 = n1 + n2 - cut2
            
            l1 = float('-inf') if cut1 == 0 else nums1[(cut1-1)/2]
            l2 = float('-inf') if cut2 == 0 else nums2[(cut2-1)/2]
            r1 = float('inf') if cut1 == n1*2 else nums1[cut1/2]
            r2 = float('inf') if cut2 == n2*2 else nums2[cut2/2]
            
            if l1 > r2:
                lo = cut2 + 1
            elif l2 > r1:
                hi = cut2 - 1
            else:
                return (max(l1, l2) + min(r1, r2))/2.0
            
        return -1
