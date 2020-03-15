---
title: easy-128
tags:
  - LeetCode
description: '最长连续序列'
urlname: easy-128
date: 2020-03-11 17:17:34
---

# 题目

https://leetcode-cn.com/problems/longest-consecutive-sequence/

> 给定一个未排序的整数数组，找出最长连续序列的长度。
>
> 要求算法的时间复杂度为 O(n)。
>
> 示例:
>
> 输入: [100, 4, 200, 1, 3, 2]
> 输出: 4
> 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

# 解题思路 √

### Python

1. 排序 - 只不过排序了就不能是$O(n)$了。

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        nums=sorted(set(nums))
        count,maxCount=1,1
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]+1:
                count+=1
                maxCount=max(maxCount,count)
            else:count=1
        return maxCount
```

2. Hash


```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        maxLength=0
        for i in hashset:
            if i-1 not in hashset:
                currentNumber=i
                currentLength=1
                while currentNumber+1 in hashset:
                    currentNumber+=1
                    currentLength+=1
                maxLength=max(maxLength,currentLength)
        return maxLength
```



### C++

```cpp

```

---



# 整理与总结

1. 

