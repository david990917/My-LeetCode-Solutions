---
title: medium-230
tags:
  - LeetCode
description: ''
urlname: medium-230
date: 2020-03-21 19:21:49
---

# 题目

[二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
```


示例 2:

```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
```


进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？



# 解题思路 √

### Python

1. 对于二叉搜索树来说，中序遍历就是从小到大

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.result,self.count=0,0
        self.inorder(root,k)
        return self.result
    def inorder(self,root,k):
        if not root:return
        self.inorder(root.left,k)
        self.count+=1
        if self.count==k:
            self.result=root.val
            return
        self.inorder(root.right,k)
```

2. 递归


```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def count(root):
            if not root:return 0
            return 1+count(root.left)+count(root.right)
        leftCount=count(root.left)
        if leftCount==k-1:return root.val
        if leftCount<k-1:return self.kthSmallest(root.right,k-leftCount-1)
        return self.kthSmallest(root.left,k)
```



### C++

```cpp

```

---



# 整理与总结

1. 

