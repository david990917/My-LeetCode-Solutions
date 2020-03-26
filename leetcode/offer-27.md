---
title: offer-27
tags:
  - LeetCode
description: ''
urlname: offer-27
date: 2020-03-26 11:05:33
---

# 题目

[二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof)

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

输入：

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

 

示例 1：

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```



# 解题思路 √

### Python

1. 递归 - 要有操作

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:return None
        temp=root.left
        root.left=self.mirrorTree(root.right)
        root.right=self.mirrorTree(temp)
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

