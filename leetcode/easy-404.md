---
title: easy-404
tags:
  - LeetCode
description: '左叶子节点的和'
urlname: easy-404
date: 2020-03-19 17:14:47
---

# 题目

https://leetcode.com/problems/sum-of-left-leaves/

Find the sum of all left leaves in a given binary tree.

**Example:**

```
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```

# 解题思路 √

### Python

1. 正常的想法

```python
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0
        def isLeaf(root):
            if not root:return False
            if not root.left and not root.right:return True
        if isLeaf(root.left):return root.left.val+self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

