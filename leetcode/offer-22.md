---
title: offer-22
tags:
  - LeetCode
description: ''
urlname: offer-22
date: 2020-03-26 09:58:44
---

# 题目

[链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：

```
给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
```



# 解题思路 √

### Python

1. 

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k==0:return None
        curr,fast=head,head
        for i in range(k-1):
            if fast.next!=None:
                fast=fast.next
            else:return None
        while fast.next!=None:
            curr=curr.next
            fast=fast.next
        return curr
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 
