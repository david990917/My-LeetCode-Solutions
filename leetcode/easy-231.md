---
title: easy-231
tags:
  - LeetCode
description: ''
urlname: easy-231
date: 2020-03-23 22:26:21
---

# 题目

[2的幂](https://leetcode-cn.com/problems/power-of-two/)

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

```
输入: 1
输出: true
解释: 20 = 1
```


示例 2:

```
输入: 16
输出: true
解释: 24 = 16
```


示例 3:

```
输入: 218
输出: false
```



# 解题思路 √

### Python

1. 同时要考虑复数的形式

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:return False
        while n>=2:
            if n%2==1:return False
            n//=2
        return n==1
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

