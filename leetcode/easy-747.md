---
title: easy-747
tags:
  - LeetCode
description: ''
urlname: easy-747
date: 2020-03-06 11:40:39
---

# 题目

https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

> 在一个给定的数组nums中，总是存在一个最大元素 。
>
> 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
>
> 如果是，则返回最大元素的索引，否则返回-1。
>



# 解题思路 √

线性扫描

# Python

我的直白想法，因为有排序所以就会引起额外复杂度。

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        hashmap={}
        for idx, number in enumerate(nums):
            hashmap[number]=idx
        
        nums=sorted(nums)
        if nums[-1]>=2*nums[-2]:
            return hashmap[nums[-1]]
        else:return -1
```

使用线性扫描

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        if all(m>=2*x for x in nums if x!= m):
            return nums.index(m)
        else:return -1
```

线性扫描同步进行方法-类似动态规划的想法，直接找出最大第二大

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        secMax=allMax=0
        idx=0
        for i in range(len(nums)):
            target=nums[i]
            if target >= allMax:
                secMax=allMax
                allMax=target
                idx=i
            elif target>secMax:
                secMax=target           
        return idx if allMax >= 2*secMax else -1
```

# C++

```cpp

```

---



# 整理与总结

1. 我自己有一些很巧妙的组合方法，但是对于如果使用CPP来说算法复杂度就会很多。不额外使用那些方法，只做思想锻炼的方法。

2. 找最大的两个，初始化的时候设成一个小于下界的值，然后再启动搜索。

    

