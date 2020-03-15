---
title: easy-219
tags:
  - LeetCode
description: 'Contains Duplicate II'
urlname: easy-219
date: 2019-09-01 14:05:58
---

# 题目

https://leetcode.com/problems/contains-duplicate-ii/description/

Given an array of integers and an integer *k*, find out whether there are two distinct indices *i* and *j* in the array such that **nums[i] = nums[j]** and the **absolute**difference between *i* and *j* is at most *k*.

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
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

