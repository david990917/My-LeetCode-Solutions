---
title: easy-346
tags:
  - LeetCode
description: ''
urlname: easy-346
date: 2020-03-23 20:35:30
---

# 题目

[数据流中的移动平均值](https://leetcode-cn.com/problems/moving-average-from-data-stream/)

给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

示例:

```
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```



# 解题思路 √

### Python

1. 直接做

```python
class MovingAverage:

    def __init__(self, size: int):
        self.store=[]  
        self.size=size

    def next(self, val: int) -> float:
        if len(self.store)==self.size:
            self.store.pop(0)
        self.store.append(val)
        return sum(self.store)/len(self.store)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

