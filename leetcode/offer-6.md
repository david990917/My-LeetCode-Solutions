---
title: offer-6
tags:
  - LeetCode
description: '从尾到头打印链表'
urlname: offer-6
date: 2020-03-15 09:41:09
---

# 题目

[从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

**示例 1：**

```
输入：head = [1,3,2]
输出：[2,3,1]
```

**限制：**

0 <= 链表长度 <= 10000

# 解题思路 √

### Python

1. Python的队列啥都能干。

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:return []

        result=[]
        p=head
        while p:
            result.append(p.val)
            p=p.next
        
        return result[::-1]
```

2. 递归来做


```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:return []

        return self.reversePrint(head.next)+[head.val]
```



### C++

```cpp

```

---



# 整理与总结

1. 

