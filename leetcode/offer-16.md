---
title: offer-16
tags:
  - LeetCode
description: ''
urlname: offer-16
date: 2020-03-25 16:33:05
---

# 题目

[数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

```
输入: 2.00000, 10
输出: 1024.00000
```


示例 2:

```
输入: 2.10000, 3
输出: 9.26100
```


示例 3:

```
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
```


说明:

- -100.0 < x < 100.0
- n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。



# 解题思路 √

### Python

1. 

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:return self.myPow(1/x,-n)
        if n==0:return 1
        if n==1:return x
        result=self.myPow(x,n>>1)
        result*=result
        if n&0x1==1:
            result*=x
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

