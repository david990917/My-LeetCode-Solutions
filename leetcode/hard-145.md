---
title: hard-145
tags:
  - LeetCode
description: '二叉树的后序遍历'
urlname: hard-145
date: 2020-03-19 20:18:47
---

# 题目

https://leetcode-cn.com/problems/binary-tree-postorder-traversal/submissions/

给定一个二叉树，返回它的 *后序* 遍历。

**示例:**

```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
```

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？



# 解题思路 √

### Python

1. 递归

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        self.result=[]

        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                self.result.append(root.val)
        
        dfs(root)
        return self.result
```

2. 后序遍历【左右中】 - 类比前序遍历【中左右】-> 【中右左】 --反向--> 【左中右】


```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []

        self.result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            self.result.append(node.val)
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
        return self.result[::-1]
```

3. 颜色标记法

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []

        self.result=[]
        stack=[(root,0)]
        while stack:
            node,times=stack.pop()
            if not node:continue
            if times==0:
                stack.append((node,1))
                stack.append((node.left,0))
            elif times==1:
                stack.append((node,2))
                stack.append((node.right,0))
            else:
                self.result.append(node.val)
        return self.result
```



### C++

```cpp

```

---



# 整理与总结

1. 

   

   

