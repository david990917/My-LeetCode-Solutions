---
title: medium-2
tags:
  - LeetCode
description: '2. 两数相加'
urlname: medium-2
date: 2020-03-09 08:33:05
---

# 题目

> 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
>
> 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
>
> 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
>
> 示例：
>
> 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
> 输出：7 -> 0 -> 8
> 原因：342 + 465 = 807
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/add-two-numbers
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路 √

**注意的测试用例**

> l1=[0,1]，l2=[0,1,2]	当一个列表比另一个列表长时
> l1=[]，l2=[0,1]	当一个列表为空时，即出现空列表
> l1=[9,9]，l2=[1]	求和运算最后可能出现额外的进位，这一点很容易被遗忘

### Python

1. 学习使用链表

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode(0)
        curr,p,q=result,l1,l2
        carry=0
        while p or q:
            a=p.val if p else 0
            b=q.val if q else 0
            value=a+b+carry
            newNode=ListNode(value%10)
            carry=value//10
            curr.next=newNode
            curr=curr.next

            if p:p=p.next
            if q:q=q.next

        if carry:
            curr.next=ListNode(1)
        return result.next

```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 头节点没有用也没事

   