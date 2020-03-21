---
title: easy-206
tags:
  - LeetCode
description: 'Reverse Linked List'
urlname: easy-206
date: 2019-09-01 13:59:12
---

# 题目

[反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

反转一个单链表。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

**进阶:**
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# 解题思路 √

理解了头节点特殊一切就没啥说的了

# Python

1. 直接的操作

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:return None
        p=ListNode(head.val)
        while head.next:
            q=ListNode(head.next.val)
            q.next=p
            p=q
            head=head.next
        return p
```

2. 

# 整理与总结

1. 还是要注意 对 空的判断

