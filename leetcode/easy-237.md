---
title: easy-237
tags:
  - LeetCode
description: '删除链表中的节点'
urlname: easy-237
date: 2020-03-15 20:28:10
---

# 题目

https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

![img](easy-237/237_example.png)

 

**示例 1:**

```
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

**示例 2:**

```
输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```

**说明:**

- 链表至少包含两个节点。
- 链表中所有节点的值都是唯一的。
- 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
- 不要从你的函数中返回任何结果。

# 解题思路 √

### Python

1. 代替下一个节点

```python
class Solution:
    def deleteNode(self, node):
        node.val,node.next=node.next.val,node.next.next
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. Python的浅拷贝：这个也解释之前一些题目原地修改的问题。我们在函数里面改变的是函数参数引用的对象，但是对于函数外面（真实的）没有改变。

