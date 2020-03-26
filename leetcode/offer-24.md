---
title: offer-24
tags:
  - LeetCode
description: ''
urlname: offer-24
date: 2020-03-26 10:07:36
---

# 题目

[反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 示例:

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```


限制：

0 <= 节点个数 <= 5000

# 解题思路 √

### Python

1. 新建了一个链表

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

2. 递归

   ![递归.gif](offer-24/1.gif)


```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        temp=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return temp
```

3. 双指针

   ![](offer-24/2.gif)

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre,cur=None,head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
```



### C++

```cpp

```

---



# 整理与总结

1. 

