---
title: easy-561
tags:
  - LeetCode
description: ''
urlname: easy-561
date: 2020-03-06 10:53:43
---

# 题目

https://leetcode-cn.com/problems/array-partition-i/

> 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
>

# 解题思路 √

直接排序，取两个数中间前面的，求和就可以了。



# Python

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```

# C++

```cpp

```

---



# 整理与总结

1. 巧妙使用排序，然后利用Python这些简单的操作快速写出答案！

