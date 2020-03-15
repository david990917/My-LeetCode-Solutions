---
title: easy-
tags:
  - LeetCode
description: 'Ugly Number'
urlname: easy-
date: 2019-09-01 17:11:49
---

# 题目

https://leetcode.com/problems/ugly-number/description/

Write a program to check whether a given number is an ugly number.

Ugly numbers are **positive numbers** whose prime factors only include `2, 3, 5`.

**Example 1:**

```
Input: 6
Output: true
Explanation: 6 = 2 × 3
```

**Example 2:**

```
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
```

**Example 3:**

```
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
```

**Note:**

1. `1` is typically treated as an ugly number.
2. Input is within the 32-bit signed integer range: [−231,  231 − 1].

# 解题思路 √

轻松且容易

![263.ugly-number](easy-263/263.ugly-number.png)

# Python

```python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return 0

        l = [2, 3, 5]
        for i in l:
            while num % i == 0:
                num /= i
        return num == 1

```



# 整理与总结

1. 

