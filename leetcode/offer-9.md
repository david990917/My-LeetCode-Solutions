---
title: offer-9
tags:
  - LeetCode
description: '用两个栈实现队列'
urlname: offer-9
date: 2020-03-15 11:47:28
---

# 题目

https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

**示例 1：**

```
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```


**示例 2：**

```
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```


**提示：**

```
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
```





# 解题思路 √

![Picture0.png](offer-9/b813bda09374058f18449b18cc6536a5b8670d5a7b65867eb65b32066c79c1ae-Picture0.png)

### Python

1. 基础的题目：

   第一个想法就是添加的时候直接添加在末尾，删除的时候倒序倒腾一下。

   优化的想法就是不用每次删除都重新处理stack_b，根据情况判断一下。

   - 当栈 B 不为空： B中仍有已完成倒序的元素，因此直接返回 B 的栈顶元素。
   - 否则，当 A 为空： 即两个栈都为空，无元素，因此返回 -1 。
   - 否则： 将栈 A 元素全部转移至栈 B 中，实现元素倒序，并返回栈 B 的栈顶元素。

```python
class CQueue:
    def __init__(self):
        self.stack_a,self.stack_b=[],[]

    def appendTail(self, value: int) -> None:
        self.stack_a.append(value)

    def deleteHead(self) -> int:
        if self.stack_b: return self.stack_b.pop()
        if not self.stack_a: return -1

        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

