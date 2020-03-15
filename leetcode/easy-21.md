---
title: easy-21
tags:
  - LeetCode
description: '合并两个有序链表'
urlname: easy-21
date: 2020-03-09 09:16:09
---

# 题目

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

# 解题思路 √

### Python

1. 直接操作

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr,p,q = head,l1,l2
        while p and q:
            if p.val<q.val:
                value=p.val
                p=p.next
            else:
                value=q.val
                q=q.next
            curr.next=ListNode(value)
            curr=curr.next
        while p and not q:
            curr.next=ListNode(p.val)
            p=p.next
            curr=curr.next
        while q and not p:
            curr.next=ListNode(q.val)
            q=q.next
            curr=curr.next
        return head.next
```

2. 我在思考Python的代码是不是可以简化


```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr,p,q = head,l1,l2
        while p and q:
            if p.val<q.val:
                value=p.val
                p=p.next
            else:
                value=q.val
                q=q.next
            curr.next=ListNode(value)
            curr=curr.next
        if p and not q:
            curr.next=p
        if q and not p:
            curr.next=q
        return head.next
```



### C++

```cpp

```

---



# 整理与总结

1. 

