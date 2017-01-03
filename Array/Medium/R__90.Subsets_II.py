#======= sort + back-tracking =========
# Time: O(n^2)
# Space:
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, begin, cur_path, result):
            for i in xrange(begin, len(nums)):
                if i > begin and nums[i] == nums[i-1]: continue
                cur_path.append(nums[i])
                result.append(cur_path[:])
                helper(nums, i + 1, cur_path, result)
                cur_path.pop()
        
        nums.sort()
        result = [[]]
        helper(nums, 0, [], result)
        return result
    
# =========== Permutation =============
# Time: Upper bound = O(nlog(n) + 2^n)
# Space: ?
# Idea:
"""
To solve this problem, it is helpful to first think how many subsets are there. If there is no duplicate element, the answer is simply 2^n, where n is the number of elements. This is because you have two choices for each element, either putting it into the subset or not. So all subsets for this no-duplicate set can be easily constructed:
num of subset

(1 to 2^0) empty set is the first subset
(2^0+1 to 2^1) add the first element into subset from (1)
(2^1+1 to 2^2) add the second element into subset (1 to 2^1)
(2^2+1 to 2^3) add the third element into subset (1 to 2^2)
....
(2^(n-1)+1 to 2^n) add the nth element into subset(1 to 2^(n-1))
Then how many subsets are there if there are duplicate elements? We can treat duplicate element as a spacial element. For example, if we have duplicate elements (5, 5), instead of treating them as two elements that are duplicate, we can treat it as one special element 5, but this element has more than two choices: you can either NOT put it into the subset, or put ONE 5 into the subset, or put TWO 5s into the subset. Therefore, we are given an array (a1, a2, a3, ..., an) with each of them appearing (k1, k2, k3, ..., kn) times, the number of subset is (k1+1)(k2+1)...(kn+1). We can easily see how to write down all the subsets similar to the approach above.
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        i = 0
        while i < len(nums):
            count = 0
            while count + i < len(nums) and nums[count + i] == nums[i]: count += 1
            tmp = []
            for j in xrange(1, count + 1):
                for subset in result:
                    tmp.append(subset + [nums[i]]*j)
            result += tmp        
            i += count
            
        return result
    

