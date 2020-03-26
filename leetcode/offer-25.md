---
title: offer-25
tags:
  - LeetCode
description: ''
urlname: offer-25
date: 2020-03-26 10:33:07
---

# 题目

[合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```


限制：

0 <= 链表长度 <= 1000

# 解题思路 √

### Python

1. 递归的想法很简单

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:return l2
        if not l2:return l1
        v1,v2=l1.val,l2.val
        if v1<=v2:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
```

2. 线性扫描


```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        curr,p,q=head,l1,l2
        while p and q:
            v1,v2=p.val,q.val
            if v1<=v2:
                curr.next=ListNode(v1)
                p=p.next
            else:
                curr.next=ListNode(v2)
                q=q.next
            curr=curr.next
        if p:curr.next=p
        if q:curr.next=q
        return head.next
```



### C++

```cpp

```

---



# 整理与总结

1. 

