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
    
"""
back tracking with level
public class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        height(root, res);
        return res;
    }
    private int height(TreeNode node, List<List<Integer>> res){
        if(null==node)  return -1;
        int level = 1 + Math.max(height(node.left, res), height(node.right, res));
        if(res.size()<level+1)  res.add(new ArrayList<>());
        res.get(level).add(node.val);
        return level;
    }
}

def findLeaves(self, root):
    def dfs(node):
        if not node:
            return -1
        i = 1 + max(dfs(node.left), dfs(node.right))
        if i == len(out):
            out.append([])
        out[i].append(node.val)
        return i
    out = []
    dfs(root)
    return out
"""
