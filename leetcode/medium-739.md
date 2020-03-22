---
title: medium-739
tags:
  - LeetCode
description: ''
urlname: medium-739
date: 2020-03-22 20:35:43
---

# 题目

[每日温度](https://leetcode-cn.com/problems/daily-temperatures/)

根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

```
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
```

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。



# 解题思路 √

### Python

1. Python居然有短路逻辑

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        result=[0 for i in range(len(T))]
        for idx,temp in enumerate(T):
            while stack and temp>stack[-1][1]:
                i,prev=stack.pop()
                result[i]=idx-i
            stack.append((idx,temp))
            
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

