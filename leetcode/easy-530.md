---
title: easy-530
tags:
  - LeetCode
description: ''
urlname: easy-530
date: 2020-03-21 22:57:12
---

# 题目

[二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)

给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

```
输入：

   1
    \
     3
    /
   2

输出：
1
```

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

# 解题思路 √

### Python

1. 二叉查找树 - 递增数列

```python
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.target,self.preVal=sys.maxsize,None
        def inorder(root):
            if not root:return
            inorder(root.left)
            if isinstance(self.preVal,int):
                self.target=min(self.target,abs(root.val-self.preVal))
            self.preVal=root.val
            inorder(root.right)
        
        inorder(root)
        return self.target
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

