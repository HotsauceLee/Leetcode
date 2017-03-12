# =============== Two stacks ===================
# Time: O(n + k)
# Space: O(n)
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # inorder
        s1 = []
        self.inorder(root, False, target, s1)
        # reverse inorder
        s2 = []
        self.inorder(root, True, target, s2)
        
        result = []
        while k > 0:
            if not s1: result.append(s2.pop())
            elif not s2: result.append(s1.pop())
            elif abs(float(s1[-1]) - target) < abs(float(s2[-1]) - target): result.append(s1.pop())
            else: result.append(s2.pop())
            k -= 1
            
        return result
        
    def inorder(self, root, reverse, target, s):
        if not root: return
    
        self.inorder(root.right if reverse else root.left, reverse, target, s)
        
        if (reverse and root.val <= target) or (not reverse and root.val > target): return
        s.append(root.val)
        
        self.inorder(root.left if reverse else root.right, reverse, target, s)
        
# ============== getPredecessor + getSuccessor ===================
# Time: O((2+k) * log(n) --> klog(n))
# Space: O(log(n))
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # log(n)
        self.pred_stack = self.initPredStack(root, target)
        # log(n)
        self.succ_stack = self.initSuccStack(root, target)
        if self.pred_stack and self.succ_stack and self.pred_stack[-1].val == self.succ_stack[-1].val:
            self.getSuccessor()
            
        result = []
        # k
        while k > 0:
            # log(n) each
            if not self.pred_stack: result.append(self.getSuccessor().val)
            elif not self.succ_stack: result.append(self.getPredecessor().val)
            elif abs(float(self.pred_stack[-1].val) - target) < abs(float(self.succ_stack[-1].val) - target):
                result.append(self.getPredecessor().val)
            else:
                result.append(self.getSuccessor().val)
            k -= 1
            
        return result
        
    def initPredStack(self, root, target):
        pred_stack = []
        while root:
            if target >= root.val:
                pred_stack.append(root)
                root = root.right
            else:
                root = root.left
        return pred_stack
        
    def initSuccStack(self, root, target):
        succ_stack = []
        while root:
            if target <= root.val:
                succ_stack.append(root)
                root = root.left
            else:
                root = root.right
        return succ_stack
        
    def getPredecessor(self):
        if self.pred_stack:
            pred = self.pred_stack.pop()
            pred_left = pred.left
            while pred_left:
                self.pred_stack.append(pred_left)
                pred_left = pred_left.right
            return pred
            
        return None
        
    def getSuccessor(self):
        if self.succ_stack:
            succ = self.succ_stack.pop()
            succ_right = succ.right
            while succ_right:
                self.succ_stack.append(succ_right)
                succ_right = succ_right.left
            return succ
            
        return None
