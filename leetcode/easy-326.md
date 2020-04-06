---
title: easy-326
tags:
  - LeetCode
description: ''
urlname: easy-326
date: 2020-04-06 22:57:13
---

# 题目

[3的幂](https://leetcode-cn.com/problems/power-of-three/)



# 解题思路 √

### Python

1. 退出条件明面上写出来

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:return False
        while n:
            if n==1:return True
            if n%3!=0:return False
            n//=3
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

