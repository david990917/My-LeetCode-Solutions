---
title: offer-30
tags:
  - LeetCode
description: ''
urlname: offer-30
date: 2020-03-26 11:39:05
---

# 题目

[包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```



# 解题思路 √

### Python

1. 冲

```python
class MinStack:
    def __init__(self):
        self.stack=[]
        self.mini=sys.maxsize
    def push(self, x: int) -> None:
        self.stack.append(x-self.mini)
        if x<self.mini:
            self.mini=x
    def pop(self) -> None:
        target=self.stack.pop()
        if target<0:
            self.mini=self.mini-target
    def top(self) -> int:
        target=self.stack[-1]
        if target<0:return self.mini
        else:return target+self.mini
    def min(self) -> int:
        return self.mini
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

