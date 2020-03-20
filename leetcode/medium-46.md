---
title: medium-46
tags:
  - LeetCode
description: '全排列'
urlname: medium-46
date: 2020-03-20 16:10:22
---

# 题目

https://leetcode-cn.com/problems/permutations/

给定一个 **没有重复** 数字的序列，返回其所有可能的全排列。

**示例:**

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```



# 解题思路 √

### Python

1. 递归

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:return []
        results=[]
        length=len(nums)
        visited=[False for i in range(length)]

        def backTrack(curr,length):
            if curr:
                if len(curr)==length:
                    results.append(curr)
                    return 
            for i in range(length):
                if visited[i]:continue

                visited[i]=True
                backTrack(curr+[nums[i]],length)
                visited[i]=False
        
        backTrack([],length)
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 全排列

   

