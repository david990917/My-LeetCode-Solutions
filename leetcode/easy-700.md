---
title: easy-700
tags:
  - LeetCode
description: ''
urlname: easy-700
date: 2020-03-22 09:04:24
---

# 题目

[二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/)

给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

**例**

```
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2     
     / \   
    1   3

在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
```

# 解题思路 √

### Python

1. 中序遍历秒

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.node=None
        def inorder(root):
            if not root:return 
            inorder(root.left)
            if root.val==val:
                self.node=root
                return 
            inorder(root.right)
        inorder(root)
        return self.node
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

