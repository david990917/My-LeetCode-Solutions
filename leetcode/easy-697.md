---
title: easy-697
tags:
  - LeetCode
description: ''
urlname: easy-697
date: 2020-03-06 20:51:29
---

# 题目

https://leetcode-cn.com/problems/degree-of-an-array/

> 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
>
> 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
>



# 解题思路 √

### Python

1. 直接做

   注意有可能有重复最大频数的元素。

   我们要的就是`right-left+1`这些中最小的元素。

```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left,right,count={},{},{}
        length=len(nums)

        for idx, number in enumerate(nums):
            if number not in left:
                left[number],right[number],count[number]=idx,idx,1
            elif right[number]<idx:
                right[number]=idx
                count[number]+=1
        
        minLength=length
        maxDu=max(count.values())
        
        for number in left:
            if count[number]==maxDu:
                minLength=min(minLength,right[number]-left[number]+1)
        return minLength
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

