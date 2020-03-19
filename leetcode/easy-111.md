---
title: easy-111
tags:
  - LeetCode
description: '二叉树的最小深度'
urlname: easy-111
date: 2020-03-19 15:55:59
---

# 题目

https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

给定二叉树 `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最小深度  2.

# 解题思路 √

### Python

1. 递归-搞明白递归的结束条件 - 叶子节点是指没有子节点的节点
   - 叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
   - 当 root 节点左右孩子都为空时，返回 1
   - 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
   - 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        if not root.left and not root.right:return 1
        if not root.left:return 1+self.minDepth(root.right)
        if not root.right:return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
```


```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        if not root.left and not root.right:return 1
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        if left==0 or right==0:return left+right+1
        return 1+min(left,right)
```



### C++

```cpp

```

---



# 整理与总结

1. 

