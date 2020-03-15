---
title: easy-303
tags:
  - LeetCode
description: 'Range Sum Query - Immutable'
urlname: easy-303
date: 2019-09-29 19:17:47
---

# 题目

https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array *nums*, find the sum of the elements between indices *i* and *j* (*i* ≤ *j*), inclusive.

**Example:**

```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```



**Note:**

1. You may assume that the array does not change.
2. There are many calls to *sumRange* function.

# 解题思路 √

自己定义自己的数组结构，我定义的是求和的形式。

nums[0...n-1] 对应的是 sums[1...n]  sums[0]=0

这样的话方便做减法，但是需要注意减的时候：

- j 需要变成 j+1（对应sums的关系）
- i 不用变化，因为（sums中i-1的才是不包含nums[i]本身的）

# Python

```python
class NumArray:
    def __init__(self, nums: List[int]):
        length=len(nums)
        if len(nums)==0:return None
        self.sums=[0]*(length+1)
        for i in range(length):
            self.sums[i+1]=self.sums[i]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1]-self.sums[i]
```

# C++

```cpp

```



# 整理与总结

1. 一共有n+1个元素
2. 

