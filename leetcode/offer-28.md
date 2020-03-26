---
title: offer-28
tags:
  - LeetCode
description: ''
urlname: offer-28
date: 2020-03-26 11:08:37
---

# 题目

[对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```

 

示例 1：

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```


示例 2：

```
输入：root = [1,2,2,null,3,null,3]
输出：false
```



# 解题思路 √

### Python

1. 对称需要函数

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True
        def helper(s,t):
            if not s and not t:return True
            if not s or not t:return False
            if s.val!=t.val:return False
            return helper(s.left,t.right) and helper(s.right,t.left)
        
        return helper(root.left,root.right)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

