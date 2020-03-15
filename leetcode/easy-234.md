---
title: easy-234
tags:
  - LeetCode
description: '回文链表'
urlname: easy-234
date: 2020-03-15 18:42:27
---

# 题目

https://leetcode-cn.com/problems/palindrome-linked-list/

请判断一个链表是否为回文链表。

**示例 1:**

```
输入: 1->2
输出: false
```


**示例 2:**

```
输入: 1->2->2->1
输出: true
```


**进阶：**
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 解题思路 √

### Python

1. 切换成逆序链表的方式来进行比较。

   快慢指针切开的时候前面多后面少，所以循环的时候要`while second`

   不占用新的内存的方法就是原地操作，逆序之后也给他变回去。

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return True
        
        def find_first_half_end(head):
            slow,fast=head,head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def reverse_link(head):
            prev,curr=None,head
            while curr:
                next_node=curr.next
                curr.next=prev
                prev,curr=curr,next_node
            return prev
        
        first_half_end=find_first_half_end(head)
        second_half_start=reverse_link(first_half_end.next)

        flag=True
        f,s=head,second_half_start
        while flag and s:
            if f.val!=s.val:
                flag=False
                break
            f,s=f.next,s.next
        
        first_half_end.next=reverse_link(second_half_start)

        return flag
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 找链表中前一半的末尾

   ```python
   def find_first_half_end(head):
       slow,fast=head,head
       while fast.next and fast.next.next:
           slow=slow.next
           fast=fast.next.next
   ```

2. 逆序链表

   ```python
   def reverse_link(head):
       prev,curr=None,head
       while curr:
           next_node=curr.next
           curr.next=prev
           prev,curr=curr,next_node
           return prev
   ```

   

