---
title: easy-206
tags:
  - LeetCode
description: 'Reverse Linked List'
urlname: easy-206
date: 2019-09-01 13:59:12
---

# 题目

https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

**Example:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:**

A linked list can be reversed either iteratively or recursively. Could you implement both?

# 解题思路 √

理解了头节点特殊一切就没啥说的了

# Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p=ListNode(head.val)
        while head.next:
            q=ListNode(head.next.val)
            q.next=p
            p=q
            head=head.next
        return p
```



# 整理与总结

1. 还是要注意 对 空的判断

