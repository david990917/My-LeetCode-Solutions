---
title: medium-144
tags:
  - LeetCode
description: '二叉树的前序遍历'
urlname: medium-144
date: 2020-03-19 20:04:31
---

# 题目

https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

给定一个二叉树，返回它的 *前序* 遍历。

 **示例:**

```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
```

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

# 解题思路 √

### Python

1. 使用栈进行前序遍历的时候：顶点-右-左

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.right:stack.append(node.right)
            if node.left:stack.append(node.left)
        return result
```

2. 递归


```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.result=[]
        if not root:return self.result
        def dfs(root):
            if root:
                self.result.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.result
```



### C++

```cpp

```

---



# 整理与总结

1. 

