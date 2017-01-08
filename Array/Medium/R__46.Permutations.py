#========= Back tracking using more space ============
# Time: ?
# Space: ?
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, cur_path, result):
            if not nums:
                result.append(cur_path[:])
                return
            
            for idx, n in enumerate(nums):
                # more space
                nums_copy = nums[:]
                cur_path.append(n)
                del nums_copy[idx]
                helper(nums_copy, cur_path, result)
                cur_path.pop()
                
        result = []
        helper(nums, [], result)
        return result
        
#========= Back tracking less time less space ============
# Time: ?
# Space: ?
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, cur_path, result):
            if len(cur_path) == len(nums):
                result.append(cur_path[:])
                return
            
        for n in nums:
            if cur_path.count(n) != 0: continue
            cur_path.append(n)
            helper(nums, cur_path, result)
            cur_path.pop()
                
        result = []
        helper(nums, [], result)
        return result
                           
# ========= Swap + back tracking ============
# Time:
# Space: 
# Idea: Swap the currently visited one forward so that it could be used next.
"""
begin       nums      result
  0        [1,2,3]      []
  1        [1,2,3]      []
  2        [1,2,3]      []
  3        [1,2,3]      [[1,2,3]]
  2        [1,3,2]      [[1,2,3]]
  3        [1,3,2]      [[1,2,3], [1,3,2]]
  1        [1,2,3]      [[1,2,3], [1,3,2]]
  2        [2,1,3]      [[1,2,3], [1,3,2]]
  3        [2,1,3]      [[1,2,3], [1,3,2], [2,1,3]]
  2        [2,3,1]      [[1,2,3], [1,3,2], [2,1,3]]
  3        [2,3,1]      [[1,2,3], [1,3,2], [2,1,3], [2,3,1]]
  1        [3,2,1]      [[1,2,3], [1,3,2], [2,1,3], [2,3,1]]
  2        [3,2,1]      [[1,2,3], [1,3,2], [2,1,3], [2,3,1]]
  3        [3,2,1]      [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1]]
  2        [3,1,2]      [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1]]
  3        [3,1,2]      [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(begin, result):
            if begin == len(nums):
                result.append(nums[:])
                return
            
            for i in xrange(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                helper(begin + 1, result)
                nums[i], nums[begin] = nums[begin], nums[i]
        
        result = []
        helper(0, result)
        return result
    
# =========== Insert current num in to each position of each results
# Time:
# Space:
# Idea:
"""
[]
1
12, 21
312, 321, 132, 231, 123, 213
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]   
        for n in nums:
            new_result = []
            for r in result:
                for i in xrange(len(r)+1):   
                    new_result.append(r[:i] + [n] + r[i:])   ###insert n
            result = new_result
        return result
    
# ======== Python library ==============
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return map(list, itertools.permutations(nums))
        # or return a lost of tuples, AC
        return list(itertools.permutations(nums))
    
#=========== TODO: next permutation ===============
"""
Well, have you solved the nextPermutation problem? If so, your code can be used in this problem. The idea is fairly simple:

add nums to res;
generate the next permutation of nums using nextPermutation(), and add it to res;
repeat 2 until the next permutation of nums returns to the original configuration.
The code is as follows.

A final note, the following code can be applied to the problem of Permutations II without any modification since the cases of duplicates have already been handled in nextPermutation(). If you want to learn more about nextPermutation(), please visit this solution.

    bool nextPermutation(vector<int>& nums) {
        int k = -1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                k = i;
                break;
            }
        }
        if (k == -1) {
            reverse(nums.begin(), nums.end());
            return false;
        }
        int l = -1;
        for (int i = nums.size() - 1; i > k; i--) {
            if (nums[i] > nums[k]) {
                l = i;
                break;
            }
        }
        swap(nums[k], nums[l]);
        reverse(nums.begin() + k + 1, nums.end());
        return true;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > res;
        sort(nums.begin(), nums.end());
        res.push_back(nums);
        while (nextPermutation(nums))
            res.push_back(nums);
        return res;
    }
"""







"""
Solution 1: Recursive, take any number as first

Take any number as the first number and append any permutation of the other numbers.

def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
Solution 2: Recursive, insert first number anywhere

Insert the first number anywhere in any permutation of the remaining numbers.

def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
Solution 3: Reduce, insert next number anywhere

Use reduce to insert the next number anywhere in the already built permutations.

def permute(self, nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])
Solution 4: Using the library

def permute(self, nums):
    return list(itertools.permutations(nums))
That returns a list of tuples, but the OJ accepts it anyway. If needed, I could easily turn it into a list of lists:

def permute(self, nums):
    return map(list, itertools.permutations(nums))
"""
