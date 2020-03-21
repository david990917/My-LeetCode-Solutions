---
title: medium-109
tags:
  - LeetCode
description: ''
urlname: medium-109
date: 2020-03-21 22:35:13
---

# 题目

[有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

```
      0
     / \
   -3   9
   /   /
 -10  5
```

# 解题思路 √

### Python

1. 递归

```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:return None
        if not head.next:return TreeNode(head.val)
        def preMid(root):
            slow,fast=root,root.next
            pre=root
            while fast and fast.next:
                pre=slow
                slow=slow.next
                fast=fast.next.next
            return pre
        preMid=preMid(head)
        mid=preMid.next
        preMid.next=None

        t=TreeNode(mid.val)
        t.left=self.sortedListToBST(head)
        t.right=self.sortedListToBST(mid.next)
        return t
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

