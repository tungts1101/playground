"""Recover binary search tree
Given the binary search tree with exactly 2 nodes are mistakenly swapped.
Recover the tree without changing its structure.

Example:
    1                       3
   /                       /
  3             =>        1        
   \                       \
    2                       2
Input: [1, 3, null, null, 2]
Output: [3, 1, null, null, 2]

Output none (modify tree in-place).

Constraints:
    - The number of nodes in the range [2, 1000].
    - -2^31 <= Node.val <= 2^31 - 1
"""

"""
Reference: 
    https://www.geeksforgeeks.org/two-nodes-of-a-bst-are-swapped-correct-the-bst-set-2/
    https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

As in order traverse of the right binary tree will give us a list of node
in increasing value, we could traverse the tree in this order and mark 2 
wrong positions. One node is in wrong position if its value is smaller than 
its previous visited node.
Supplying with Morris traversal, we could achieve O(1) space complexity.

Memory: O(1) with Morris traversal, O(n) with stack or recursion traversal.
Time: O(n).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursion solution
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, node1, node2 = None, None, None
        def inOrderTraverse(node: Optional[TreeNode]) -> None:
            nonlocal prev, node1, node2
            if node is None: return
            inOrderTraverse(node.left)
            if prev is not None and node.val < prev.val:
                if node1 is None:
                    node1 = prev # mark the first wrong position
                node2 = node
            prev = node
            inOrderTraverse(node.right)
        
        inOrderTraverse(root)
        node1.val, node2.val = node2.val, node1.val
    
    # morris solution
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = last = None
        
        def checkNode(curr):
            nonlocal prev, first, last
            if prev is not None and curr.val < prev.val:
                if first is None:
                    first = prev
                last = curr
            prev = curr
        
        def morrisInOrderTraverse():
            nonlocal prev, first, last
            curr = root
            while curr is not None:
                if curr.left is None:
                    checkNode(curr)
                    curr = curr.right
                else:
                    pred = curr.left
                    while pred.right is not None and pred.right is not curr:
                        pred = pred.right
                    # Create a virtual link from the right most node of left
                    # sub tree to the current node.
                    if pred.right is None:
                        pred.right = curr
                        curr = curr.left
                    # Recover the tree.
                    else:
                        checkNode(curr)
                        pred.right = None   # Remove created virtual link.
                        curr = curr.right
        
        morrisInOrderTraverse()
        first.val, last.val = last.val, first.val