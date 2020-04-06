---
title: easy-441
tags:
  - LeetCode
description: ''
urlname: easy-441
date: 2020-04-06 22:57:46
---

# 题目

[排列硬币](https://leetcode-cn.com/problems/arranging-coins/)



# 解题思路 √

### Python

1. 判断左右

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        temp=int((2*n)**0.5)
        return temp-1 if temp*(temp+1)>2*n else temp
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

