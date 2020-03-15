---
title: easy-35
tags:
  - LeetCode
description: ''
urlname: easy-35
date: 2020-03-06 21:25:28
---

# 题目

https://leetcode-cn.com/problems/search-insert-position/

> 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
>
> 你可以假设数组中无重复元素。



# 解题思路 √

### Python

1. 直接操作就行啦

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length=len(nums)
        for i in range(length):
            if target==nums[i] or target<nums[i]:
                return i
        if i==length-1:
            return length
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

