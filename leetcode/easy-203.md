---
title: easy-203
tags:
  - LeetCode
description: 'Remove Linked List Elements'
urlname: easy-203
date: 2019-09-01 13:30:49
---

# 题目

[移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements/)

删除链表中等于给定值 **val** 的所有节点。

**示例:**

```
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
```

# 解题思路 √

我自己的方法：

正常的链表删除，然后加上对特殊情况的判断。

标准方法：

- 链表的基本操作（删除指定节点）
- 虚拟节点dummy 简化操作

> 其实设置dummy节点就是为了处理特殊位置（头节点），这这道题就是如果头节点是给定的需要删除的节点呢？ 为了保证代码逻辑的一致性，即不需要为头节点特殊定制逻辑，才采用的虚拟节点。

- 如果连续两个节点都是要删除的节点，这个情况容易被忽略。 eg:

```
// 只有下个节点不是要删除的节点才更新current
if (!next || next.val !== val) {
    current =  next;
}
```

# Python

我自己的代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        while head and head.val == val:
            head = head.next

        q = head
        while q and q.next:
            if q.next.val == val:
                p = q.next
                q.next = p.next
                p.next = None
            else:
                q = q.next
        return head

```

学习使用虚拟节点的方法简化自己的代码

```python
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(0)
        prev.next=head

        q=prev
        while  q.next:
            if q.next.val == val:
                p = q.next
                q.next = p.next
                p.next = None
            else:
                q = q.next
        return prev.next
```

标准方法

```python
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        cur = prev
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return prev.next
```



# 整理与总结

1. 需要考虑空的情况
	```
   []
   1
  ```
  
1. 单字符
  
   ```
   [1]
   1
   ```
   
1. 双字符
  
   ```
   [1,1]
1
   ```

4. 为什么有点困难，因为头节点是特殊的节点，需要特别处理  —> 添加虚拟节点

