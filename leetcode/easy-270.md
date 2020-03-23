---
title: easy-270
tags:
  - LeetCode
description: ''
urlname: easy-270
date: 2020-03-23 21:56:08
---

# 题目

[最接近的二叉搜索树值](https://leetcode-cn.com/problems/closest-binary-search-tree-value/)

给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：

给定的目标值 target 是一个浮点数
题目保证在该二叉搜索树中只会存在一个最接近目标值的数
示例：

```
输入: root = [4,2,5,1,3]，目标值 target = 3.714286

    4
   / \
  2   5
 / \
1   3

输出: 4
```



# 解题思路 √

### Python

1. 中序遍历转数组

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

