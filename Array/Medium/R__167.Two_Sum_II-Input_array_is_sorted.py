# ============ Two pointers ===========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers) - 1
        while low < high:
            cur = numbers[low] + numbers[high]
            if cur > target:
                high -= 1
            elif cur < target:
                low += 1
            else:
                return [low + 1, high + 1]
                
#============= Binary search ==============
# Time: O(nlog(n))
# Space: O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(numbers)):
            if numbers[i] > target: break
            diff = target - numbers[i]
            low, high = i + 1, len(numbers) - 1
            while low <= high:
                mid = (low+high)//2
                if numbers[mid] == diff: return [i + 1, mid + 1]
                elif numbers[mid] > diff: high = mid - 1
                else: low = mid + 1
