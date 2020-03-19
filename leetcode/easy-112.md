---
title: easy-112
tags:
  - LeetCode
description: '路径总和'
urlname: easy-112
date: 2020-03-18 21:43:39
---

# 题目

https://leetcode-cn.com/problems/path-sum/

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

**说明:** 叶子节点是指没有子节点的节点。

**示例:** 
给定如下二叉树，以及目标和 `sum = 22`，

```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
```

返回 `true`, 因为存在目标和为 22 的根节点到叶子节点的路径 `5->4->11->2`。

# 解题思路 √

### Python

1. 从上往下分解

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:return False
        if (not root.left and not root.right and root.val==sum):return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
```

2. 迭代-树的常用方法

   > 利用**深度优先**策略访问每个节点，同时更新剩余的目标和。

   所以我们从包含根节点的栈开始模拟，剩余目标和为 `sum - root.val`。

   然后开始迭代：弹出当前元素，如果当前剩余目标和为 `0` 并且在叶子节点上返回 `True`；如果剩余和不为零并且还处在非叶子节点上，将当前节点的所有孩子以及对应的剩余和压入栈中。


```python
class Solution:
    def hasPathSum(self, root, sum):
        if not root:return False
        stack=[(root,sum-root.val)]
        while stack:
            node,value=stack.pop()
            if not node.left and not node.right and value==0:return True
            if node.right:stack.append((node.right,value-node.right.val))
            if node.left:stack.append((node.left,value-node.left.val))
        return False
```



### C++

```cpp

```

---



# 整理与总结

1. 

