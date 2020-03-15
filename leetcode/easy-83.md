---
title: easy-83
tags:
  - LeetCode
description: '83. 删除排序链表中的重复元素'
urlname: easy-83
date: 2020-03-09 09:27:33
---

# 题目

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

> 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
>
> **示例 1:**
>
> ```
> 输入: 1->1->2
> 输出: 1->2
> ```
>
> **示例 2:**
>
> ```
> 输入: 1->1->2->3->3
> 输出: 1->2->3
> ```

# 解题思路 √

### Python

1. 判断当前指针和下一个指针是否为空

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return None
        fast=head
        while fast and fast.next:
            if fast.val==fast.next.val:
                fast.next=fast.next.next
            else:fast=fast.next
        return head
```

2. while循环直接删除后面的所有相同重复数字


```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return None
        fast=head
        while fast and fast.next:
            while fast.next and fast.val==fast.next.val:
                fast.next=fast.next.next
            fast=fast.next
        return head
```



### C++

```cpp

```

---



# 整理与总结

1. 

