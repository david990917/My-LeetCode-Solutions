---
title: medium-90
tags:
  - LeetCode
description: ''
urlname: medium-90
date: 2020-03-23 09:48:50
---

# 题目

[子集 II](https://leetcode-cn.com/problems/subsets-ii/)

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

```
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```



# 解题思路 √

### Python

1. 重复元素：排序 + 前一个使用了后一个才可以使用

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results=[[]]
        visited={}
        nums=sorted(nums)
        length=len(nums)
        def backtracking(temp,start):
            if temp:
                results.append(temp)
            if len(temp)==length or start==length:
                return
            for i in range(start,length):
                if i!=0 and nums[i]==nums[i-1] and not visited.get(i-1,False):
                    continue
                visited[i]=True
                backtracking(temp+[nums[i]],i+1)
                visited[i]=False
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

