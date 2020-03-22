---
title: easy-938
tags:
  - LeetCode
description: ''
urlname: easy-938
date: 2020-03-22 08:24:02
---

# 题目

[二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst/)

给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。

示例 1：

```
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
```


示例 2：

```
输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23
```


提示：

树中的结点数量最多为 10000 个。
最终的答案保证小于 2^31。





# 解题思路 √

### Python

1. 中序遍历

```python
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.result=0
        def inorder(root):
            if not root:return
            inorder(root.left)
            if root.val>=L and root.val<=R:self.result+=root.val
            inorder(root.right)
        
        inorder(root)
        return self.result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

