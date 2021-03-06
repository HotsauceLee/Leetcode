# ========== determine if put last put element ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)
        lid = 1
        last_put = nums[0]
        put_again = True
        for i in xrange(1, len(nums)):
            if nums[i] == last_put:
                if put_again:
                    nums[lid] = nums[i]
                    lid += 1
                    put_again = False
            else:
                nums[lid] = nums[i]
                lid += 1
                last_put = nums[i]
                put_again = True
                
        return lid
        
#============ Compare current with lid-2 ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lid = 0
        for n in nums:
            if lid < 2 or n > nums[lid-2]:
                nums[lid] = n
                lid += 1
                
        return lid
    
#=========== Follow up: allow duplicate k time ===========
"""
int removeDuplicates(int A[], int n, int k) {

            if (n <= k) return n;

            int i = 1, j = 1;
            int cnt = 1;
            while (j < n) {
                if (A[j] != A[j-1]) {
                    cnt = 1;
                    A[i++] = A[j];
                }
                else {
                    if (cnt < k) {
                        A[i++] = A[j];
                        cnt++;
                    }
                }
                ++j;
            }
            return i;
}
"""
