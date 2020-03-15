---
title: hard-154
tags:
  - LeetCode
description: ''
urlname: hard-154
date: 2020-03-15 12:54:58
---

# 题目

https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

**示例 1：**

```
输入: [1,3,5]
输出: 1
```


**示例 2：**

```
输入: [2,2,2,0,1]
输出: 0
```


**说明：**

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

# 解题思路 √

### Python

1. 都是和`nums[j]`相比

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        while i<j:
            mid=(i+j)//2
            if nums[mid]>nums[j]:i=mid+1
            elif nums[mid]<nums[j]:j=mid
            else:j-=1
        return nums[i]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

