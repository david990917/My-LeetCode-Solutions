---
title: easy-226
tags:
  - LeetCode
description: ''
urlname: easy-226
date: 2019-09-01 16:37:43
---

# 题目

https://leetcode.com/problems/invert-binary-tree/description/

Invert a binary tree.

**Example:**

Input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

Output:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**Trivia:**
This problem was inspired by [this original tweet](https://twitter.com/mxcl/status/608682016205344768) by [Max Howell](https://twitter.com/mxcl):

> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

# 解题思路 √

遍历树（随便怎么遍历），然后将左右子树交换位置。

## 关键点解析

- 递归简化操作
- 如果树很高，建议使用栈来代替递归
- 这道题目对顺序没要求的，因此队列数组操作都是一样的，无任何区别

# Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        l = [root]
        while l:
            q = l.pop(0)
            if q.left: l.append(q.left)
            if q.right: l.append(q.right)
            q.left, q.right = q.right, q.left

        return root

```



# 整理与总结

1. 我已经能做到和标准答案差不多了

