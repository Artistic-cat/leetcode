"""
You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:

Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
Replace the leaf node in trees[i] with trees[j].
Remove trees[j] from trees.
Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.

A BST (binary search tree) is a binary tree where each node satisfies the following property:

Every node in the node's left subtree has a value strictly less than the node's value.
Every node in the node's right subtree has a value strictly greater than the node's value.
A leaf is a node that has no children.

Input: trees = [[2,1],[3,2,5],[5,4]]
Output: [3,2,5,1,null,4]
Explanation:
In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].
In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
Delete trees[1], so trees = [[3,2,5,1,null,4]].
The resulting tree, shown above, is a valid BST, so return its root.
"""

trees=[[2,1],[3,2,5],[5,4]]

#find the root node
#keep the range for the nodes/ leaves that are being added

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        leaves=set()
        treeDict={}

        for tree in trees:
            treeDict[tree.val]=tree
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
        
        root=None
        
        for tree in trees:
            if tree.val not in leaves:
                root=tree
                break
        if not root:
            return None

        curLeaves={}

        if root.left:
            curLeaves[root.left.val]=(-sys.maxsize,root.val,root,0) #0 for left 1 for right
        if root.right:
            curLeaves[root.right.val]=(root.val,sys.maxsize,root,1) #0 for left 1 for right
        
        del treeDict[root.val]

        while treeDict:
            findTree=False
            for leaf, (low,high,par,lor) in curLeaves.items():
                if leaf in treeDict:
                    newTree=treeDict[leaf]
                    del curLeaves[leaf]

                    if newTree.left:
                        if low<newTree.left.val<high and newTree.left.val not in curLeaves:
                            curLeaves[newTree.left.val] = (low,newTree.val,newTree,0)
                        else:
                            return None
                    
                    if newTree.right:
                        if low<newTree.right.val<high and newTree.right.val not in curLeaves:
                            curLeaves[newTree.right.val] = (newTree.val,high,newTree,1)
                        else:
                            return None
                    
                    if lor ==0:
                        par.left=newTree
                    else:
                        par.right=newTree
                    
                    findTree=True
                    del treeDict[newTree.val]
                    break
            if not findTree:
                return None
        return root