# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result[::-1]

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(15)
    print(Solution().levelOrderBottom(root))






    """
            Time Complexity = O(n)
            Space Complexity = O(n)

            Given a binary tree, return the bottom-up level order traversal of its nodes' values.
            (ie, from left to right, level by level from leaf to root).

            Example:
            Given binary tree [3,9,20,null,null,15,7],

                    3
                   / \
                  9  20
                    /  \
                   15   7
            Return its bottom-up level order traversal as:
            [
              [15,7],
              [9,20],
              [3]
            ]
    """
