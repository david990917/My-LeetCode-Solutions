---
title: easy-665
tags:
  - LeetCode
description: ''
urlname: easy-665
date: 2020-03-22 19:52:07
---

# 题目

[非递减数列](https://leetcode-cn.com/problems/non-decreasing-array/)

给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，总满足 array[i] <= array[i + 1]。

 

示例 1:

```
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
```


示例 2:

```
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
```


说明：

- 1 <= n <= 10 ^ 4

- 10 ^ 5 <= nums[i] <= 10 ^ 5

有。商业转载请联系官方授权，非商业转载请注明出处。



# 解题思路 √

### Python

1. 分析情况

- 常见的就是continue
- 正常情况修改 nums[i-1]=nums[i]
- 如果nums[i-2]>nums[i] 修改的时候 nums[i]=nums[i-1]

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:continue
            count+=1
            if i-2>=0 and nums[i-2]>nums[i]:
                nums[i]=nums[i-1]
            else:nums[i-1]=nums[i]
            if count==2:break
        return count<=1
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

