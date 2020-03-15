---
title: easy-70
tags:
  - LeetCode
description: 'Climbing Stairs'
urlname: easy-70
date: 2019-09-29 19:03:27
---

# 题目

https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given *n* will be a positive integer.

**Example 1:**

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

# 解题思路 √

### 动态规划

这个题目很好理解，居然由动态规划转变成了斐波那契数列。

> Think how to reach nth stairs.

# Python

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,2
        for i in range(n-1):
            a,b=b,a+b
        return a
```

# C++

```cpp

```



# 整理与总结

1. 数组可以转变成`a,b`的形式。
2. 还是那句话，如果是涉及到了`n-1`就要考虑边界条件。

