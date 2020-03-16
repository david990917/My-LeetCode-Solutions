---
title: easy-110
tags:
  - LeetCode
description: '平衡二叉树'
urlname: easy-110
date: 2020-03-16 13:08:01
---

# 题目

https://leetcode-cn.com/problems/balanced-binary-tree

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

**示例 1:**

```
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
```

**示例 2:**

```
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
```



# 解题思路 √

### Python

1. 自顶向下的递归

   ![image-20200316131141568](easy-110/image-20200316131141568.png)

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:return -1
            return 1+max(height(root.left),height(root.right))
        
        if not root:return True
        if abs(height(root.left)-height(root.right))>1:return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
```

2. 自底向上的递归


```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:return True,-1
            isLeftBalanced,leftHeight=helper(root.left)
            if not isLeftBalanced:return False,0
            isRightBalanced,rightHeight=helper(root.right)
            if not isRightBalanced:return False,0

            return abs((leftHeight-rightHeight))<2,1+max(leftHeight,rightHeight)
        
        return helper(root)[0]
```



### C++

```cpp

```

---



# 整理与总结

1. 

