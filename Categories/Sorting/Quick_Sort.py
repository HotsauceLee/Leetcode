# Best O(nlog(n)), worst O(n^2)
def quick_sort(nums):
  if not nums or len(nums) <= 1:
    return nums
  
  def helper(nums, lo, hi):
    if hi - lo < 1:
      return
    
    pivot = lo
    i, j = lo, hi
    while i < j:
      while i <= hi and nums[i] <= nums[pivot]:
        i += 1
      while j >= lo and nums[j] > nums[pivot]:
        j -= 1
        
      if i < j:
        nums[i], nums[j] = nums[j], nums[i]
        
    nums[pivot], nums[j] = nums[j], nums[pivot]
    
    helper(nums, lo, j - 1)
    helper(nums, j + 1, hi)
    
  helper(nums, 0, len(nums) - 1)
  return nums
  
tc1 = []
tc2 = [1]
tc3 = [1,1]
tc4 = [1,2,3]
tc5 = [7,6,5,4,3,2,1,1]
tc6 = [6,6,6,5,4,3,3,3,2,2,2,2,1,1,1]
tc7 = [46, 90, 28, 18, 81, 12, 54, 64, 68, 35, 60, 66, 92, 21, 57, 72, 77, 1, 22, 26, 43, 99, 88, 33, 15, 83, 52, 42, 78, 65, 76, 45, 97, 11, 13, 55, 17, 87, 48, 73, 20, 36, 27, 38, 80, 39, 6, 3, 98, 47]

print quick_sort(tc1)
print quick_sort(tc2)
print quick_sort(tc3)
print quick_sort(tc4)
print quick_sort(tc5)
print quick_sort(tc6)
print quick_sort(tc7)
