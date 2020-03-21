---
title: easy-538
tags:
  - LeetCode
description: ''
urlname: easy-538
date: 2020-03-21 19:42:00
---

# 题目

[把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

例如：

```
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
```



# 解题思路 √

### Python

1. 

```python
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum=0
        def traver(root):
            if not root:return
            traver(root.right)
            self.sum+=root.val
            root.val=self.sum
            traver(root.left)

        traver(root)
        return root
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

