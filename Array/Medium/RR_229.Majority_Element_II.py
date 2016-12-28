# ======= Dict ==========
# Time: O(n)
# Space: O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        second = first = float('-inf')
        for n in nums:
            if d.has_key(n):
                d[n] += 1
            else:
                d[n] = 1
            
            if d[n] > len(nums)/3:
                if n in [first, second]:
                    continue
                elif d[n] > first:
                    second = first
                    first = n
                elif d[n] > second:
                    second = n
        
        result = []
        if first > float('-inf'):
            result.append(first)
        if second > float('-inf'):
            result.append(second)
            
        return result
        
# ========== Boyer-Moore =================
# Time: O(n + n + n)
# Space: O(1)
# Idea:
"""
1. there are no elements that appears more than n/3 times, then whatever the algorithm 
 got from 1st round wound be rejected in the second round.
2. there are only one elements that appears more than n/3 times, after 1st round one of 
 the candicate must be that appears more than n/3 times(<2n/3 other elements could only
 pair out for <n/3 times), the other candicate is not necessarily be the second most frequent 
 but it would be rejected in 2nd round.
3. there are two elments appears more than n/3 times, candicates would contain both of
 them. (<n/3 other elements couldn't pair out any of the majorities.)
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1, candidate2, count1, count2 = 0.1, 0.1, 0, 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        return [n for n in [candidate1, candidate2] if nums.count(n) > len(nums)//3]
