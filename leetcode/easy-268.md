---
title: easy-268
tags:
  - LeetCode
description: ''
urlname: easy-268
date: 2020-03-06 21:12:43
---

# 题目

https://leetcode-cn.com/problems/missing-number/

> 给定一个包含 `0, 1, 2, ..., n` 中 *n* 个数的序列，找出 0 .. *n* 中没有出现在序列中的那个数。



# 解题思路 √

### Python

1. 排序就很容易

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        length=len(nums)
        
        if nums[0]!=0:return 0
        if nums[-1]!=length:return length
        for i in range(length-1):
            if nums[i+1] !=nums[i]+1:
                return nums[i]+1
```

2. 不能排序，就用哈希表。**发现找东西的总有使用哈希表**


```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        nums=set(nums)
        for i in range(length+1):
            if i not in nums:
                return i
```



### C++

```cpp

```

---



# 整理与总结

1. 一定要注意如果涉及两个元素比较，就要注意边界条件。

2. 哈希表(set)的速度相当快，查询最好都用set。

   上面使用list / 下面使用set

   ![image-20200306212331737](easy-268/image-20200306212331737.png)

   

