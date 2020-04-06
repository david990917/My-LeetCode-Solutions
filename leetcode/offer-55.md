---
title: offer-55
tags:
  - LeetCode
description: ''
urlname: offer-55
date: 2020-04-05 22:32:17
---

# 题目

[二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)



# 解题思路 √

### Python

1. 

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

