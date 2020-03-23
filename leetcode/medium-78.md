---
title: medium-78
tags:
  - LeetCode
description: ''
urlname: medium-78
date: 2020-03-23 09:26:55
---

# 题目

[子集](https://leetcode-cn.com/problems/subsets/)

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

```
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```



# 解题思路 √

### Python

1. 注意初始化条件[[]]

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[[]]
        length=len(nums)
        def backtracking(temp,start):
            if temp:
                results.append(temp)
            if len(temp)==length or start==length:
                return
            for i in range(start,length):
                backtracking(temp+[nums[i]],i+1)
        backtracking([],0)
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

