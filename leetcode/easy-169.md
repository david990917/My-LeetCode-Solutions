---
title: easy-169
tags:
  - LeetCode
description: ''
urlname: easy-169
date: 2020-02-21 23:11:01
---

# 题目

> 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
>
> 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
>
> 示例 1:
>
> 输入: [3,2,3]
> 输出: 3
> 示例 2:
>
> 输入: [2,2,1,1,1,2,2]
> 输出: 2

# 解题思路 √

第一反应就是暴力法能解决。

哈希表的方法。

## 排序：

这个问题实际上就是在找众数，那我们要找的那个数一定出现在下标为$\left \lceil n/2 \right \rceil+1$。

但是这样的计算对于`[1]`来说就是超出了list的长度。

会过来再来分析一下我们的题目，我们要找的那个是超过一半数量的元素，那么我们可以使用$\left \lceil n/2 \right \rceil$来进行提取。



# Python

## 暴力法

时间复杂度$O(n)$

根据题解来看，我的方法好行还不是最暴力的方法，但是和哈希表的方式有一点类似。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lenth=len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        for i in d:
            if d[i]>lenth/2:
                return i
```

## Hash Table

```python
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```

## 众数

```python
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
```



# C++

```cpp

```



# 整理与总结

1. 重新捡回`Python`，Python和其他的语言相比就是有了很多的内置函数。

