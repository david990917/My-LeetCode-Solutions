---
title: easy-572
tags:
  - LeetCode
description: '另一个树的子树'
urlname: easy-572
date: 2020-03-19 09:38:46
---

# 题目

https://leetcode-cn.com/problems/subtree-of-another-tree/

给定两个非空二叉树 **s** 和 **t**，检验 **s** 中是否包含和 **t** 具有相同结构和节点值的子树。**s** 的一个子树包括 **s** 的一个节点和这个节点的所有子孙。**s** 也可以看做它自身的一棵子树。

**示例 1:**
给定的树 s:

```
     3
    / \
   4   5
  / \
 1   2
```

给定的树 t：

```
   4 
  / \
 1   2
```

返回 **true**，因为 t 与 s 的一个子树拥有相同的结构和节点值。

**示例 2:**
给定的树 s：

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```

给定的树 t：

```
   4
  / \
 1   2
```

返回 **false**。

# 解题思路 √

### Python

1. 

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def subTree(s,t):
            if not s and not t:return True
            if not s or not t:return False
            if s.val!=t.val:return False
            return subTree(s.left,t.left) and subTree(s.right,t.right)
        if not s:return False
        return subTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

