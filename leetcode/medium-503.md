---
title: medium-503
tags:
  - LeetCode
description: ''
urlname: medium-503
date: 2020-03-22 20:56:04
---

# 题目

[下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/)

给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

```
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
```


注意: 输入数组的长度不会超过 10000。

# 解题思路 √

### Python

1. 神奇！

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length=len(nums)
        nums=nums*2  
        stack=[]
        result=[-1 for i in range(length)]
        for idx,number in enumerate(nums):
            while stack and number>nums[stack[-1]]:
                i=stack.pop()
                result[i]=nums[idx]
            if idx<length:stack.append(idx)
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

