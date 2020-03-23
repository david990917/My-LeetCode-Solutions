---
title: easy-100
tags:
  - LeetCode
description: ''
urlname: easy-100
date: 2020-03-23 20:48:00
---

# 题目

[相同的树](https://leetcode-cn.com/problems/same-tree/)

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

```
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
```

示例 2:

```
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
```

示例 3:

```
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
```



# 解题思路 √

### Python

1. 递归直接秒杀

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:return True
        if not p or not q:return False
        if p.val!=q.val:return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

