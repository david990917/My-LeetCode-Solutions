---
title: easy-219
tags:
  - LeetCode
description: 'Contains Duplicate II'
urlname: easy-219
date: 2019-09-01 14:05:58
---

# 题目

[存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii/)

给定一个整数数组和一个整数 *k*，判断数组中是否存在两个不同的索引 *i* 和 *j*，使得 **nums [i] = nums [j]**，并且 *i* 和 *j* 的差的绝对值最大为 *k*。

**示例 1:**

```
输入: nums = [1,2,3,1], k = 3
输出: true
```

**示例 2:**

```
输入: nums = [1,0,1,1], k = 1
输出: true
```

**示例 3:**

```
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
```

# 解题思路 √

由于题目没有对空间复杂度有求，用一个hashmap 存储已经访问过的数字即可, 每次访问都会看hashmap中是否有这个元素，有的话拿出索引进行比对，是否满足条件（相隔不大于k），如果满足返回true即可。

# Python

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, num in enumerate(nums):
            if num in d and index - d[num] <= k:
                return True
            d[num] = index
        return False
```



# 整理与总结

1. 学习一下 hashmap 吧

