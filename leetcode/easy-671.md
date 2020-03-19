---
title: easy-671
tags:
  - LeetCode
description: '二叉树中第二小的节点'
urlname: easy-671
date: 2020-03-19 18:21:30
---

# 题目

https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 `2` 或 `0`。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 

给出这样的一个二叉树，你需要输出所有节点中的**第二小的值。**如果第二小的值不存在的话，输出 -1 **。**

**示例 1:**

```
输入: 
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
```

**示例 2:**

```
输入: 
    2
   / \
  2   2

输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。
```

# 解题思路 √

### Python

1. 

```python
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:return -1
        if not root.left and not root.right:return -1
        leftVal=root.left.val
        rightVal=root.right.val
        if leftVal==root.val:leftVal=self.findSecondMinimumValue(root.left)
        if rightVal==root.val:rightVal=self.findSecondMinimumValue(root.right)
        if leftVal!=-1 and rightVal!=-1:return min(leftVal,rightVal)
        if leftVal!=-1:return leftVal
        return rightVal
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

