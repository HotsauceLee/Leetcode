# =============== Merge lists in the same level =============
# Time: ?
# Space: ?
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        left_list = self.findLeaves(root.left)
        right_list = self.findLeaves(root.right)
        merged_list = self.merge_list(left_list, right_list)
            
        merged_list.append([root.val])
        return merged_list
        
    def merge_list(self, list1, list2):
        if not list1 and not list2: return []
        if not list1: return list2
        if not list2: return list1
        
        len1 = len(list1)
        len2 = len(list2)
        if len1 >= len2:
            i = 0
            while i < len2:
                list1[i] += list2[i]
                i += 1
            return list1
        
        k = 0
        while k < len1:
            list2[k] = list1[k] + list2[k]
            k += 1
        return list2
    
#============== Recursion + back tracking ================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(root, result):
            if not root: return 0
        
            l = helper(root.left, result)
            r = helper(root.right, result)
            
            cur = max(l, r)
            if cur >= len(result):
                result.append([root.val])
            else:
                result[cur].append(root.val)
                
            return cur + 1
            
        result = []
        helper(root, result)
        return result
