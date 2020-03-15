---
title: easy-141
tags:
  - LeetCode
description: '141. 环形链表'
urlname: easy-141
date: 2020-03-09 09:47:27
---

# 题目

https://leetcode-cn.com/problems/linked-list-cycle/

> 给定一个链表，判断链表中是否有环。
>
> 为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。
>
>  
>
> **示例 1：**
>
> ```
> 输入：head = [3,2,0,-4], pos = 1
> 输出：true
> 解释：链表中有一个环，其尾部连接到第二个节点。
> ```
>
> ![img](easy-141/circularlinkedlist.png)
>
> **示例 2：**
>
> ```
> 输入：head = [1,2], pos = 0
> 输出：true
> 解释：链表中有一个环，其尾部连接到第一个节点。
> ```
>
> ![img](easy-141/circularlinkedlist_test2.png)
>
> **示例 3：**
>
> ```
> 输入：head = [1], pos = -1
> 输出：false
> 解释：链表中没有环。
> ```
>
> ![img](easy-141/circularlinkedlist_test3.png)
>
>  
>
> **进阶：**
>
> 你能用 *O(1)*（即，常量）内存解决此问题吗？



# 解题思路 √

### Python

1. hashmap

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashmap={}
        while head:
            if head in hashmap:return True
            else:hashmap[head]=1
            head = head.next
        return False
```

2. #### 双指针


```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        slow,fast=head,head.next
        while slow != fast:
            if not fast or not fast.next:return False
            fast=fast.next.next
            slow=slow.next
        return True
```



### C++

```cpp

```

---



# 整理与总结

1. Python的字典实际上就是一个`Hashmap` o(1)
2. 

