---
title: easy-104
tags:
  - LeetCode
description: 'Maximum Depth of Binary Tree'
urlname: easy-104
date: 2019-08-30 19:29:01
---

# 题目

[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

**说明:** 叶子节点是指没有子节点的节点。

**示例：**
给定二叉树 `[3,9,20,null,null,15,7]`，

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 

# 思路 √

由于树是一种递归的数据结构，因此用递归去解决的时候往往非常容易，这道题恰巧也是如此，可如果使用迭代呢？ 

我们首先应该想到的是树的各种遍历，由于我们求的是深度，因此 使用层次遍历（BFS）是非常合适的。 我们只需要记录有多少层即可。

## 关键点解析

- 队列
- 队列中用 Null(一个特殊元素)来划分每层，或者在对每层进行迭代之前保存当前队列元素的个数（即当前层所含元素个数）
- 树的基本操作- 遍历 - 层次遍历（BFS）

# Python

1. 我的递归解法：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if (not root.left) and (not root.right):return 1
        return 1 + max(Solution.maxDepth(self,root.left),Solution.maxDepth(self,root.right))
```

2. 迭代解法：

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q, depth = [root, None], 1
        while q:
            node = q.pop(0)
            if node:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            elif q:
                q.append(None)
                depth += 1
        return depth
```

3. 迭代解法

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        deq,maxDepth=[(root,1)],1
        while deq:
            node,depth=deq.pop(0)
            maxDepth=max(maxDepth,depth)
            if node.left:deq.append((node.left,depth+1))
            if node.right:deq.append((node.right,depth+1))
        return maxDepth
```



# 整理与总结

1. 瀚文直接的思路就是：生成一个二叉树，然后递归直接输出树的高度

   ```java
   var maxDepth = function(root) {
     if (!root) return 0;
     if (!root.left && !root.right) return 1;
     return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
   };
   ```

   迭代调用函数的时候，Python 需要添加类名 和 self 参数。

2. 用数组表示的直接也可以对应一个二叉树

   - i -> (2i+1, 2i+2)

3. 尝试使用迭代的方式解决

   - 深度 可以想到使用层次遍历，多少层就得到了高度
   - 使用特殊值划分本层，每当检测到这个值的时候，就知道这层结束了

4. 最外层的 if 可以不使用 else，因为结构明确

5. 总是使用 list 来表示stack queue

   - list 的 pop()

     ```python
     a = '123'
     q = [a, None, a * 2]
     print(q.pop())				# 123123
     q = [a, None, a * 2]
     print(q.pop(0))				# 123
     q = [a, None, a * 2]
     print(q.pop(1))				# None
     ```

     ```python
     123123
     123
     None
     ```

     