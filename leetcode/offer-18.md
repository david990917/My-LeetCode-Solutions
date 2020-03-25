---
title: offer-18
tags:
  - LeetCode
description: ''
urlname: offer-18
date: 2020-03-25 21:52:29
---

# 题目

[删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

```
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```


示例 2:

```
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```


说明：

- 题目保证链表中节点的值互不相同
- 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

# 解题思路 √

### Python

1. 双指针的想法

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val==val:return head.next
        pre,cur=head,head.next
        while cur and cur.val!=val:
            pre,cur=cur,cur.next
        pre.next=cur.next
        return head
```

2. 单指针的想法-再议


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

