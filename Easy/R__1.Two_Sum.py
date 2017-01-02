#================== Dict =====================
# Time: O(n)
# Space: O(n)
class Solution(object):
	d = {}
	for idx, val in enumerate(nums):
		if d.has_key(target - val): return [d[target - val], idx]
		d[val] = idx

	return None
