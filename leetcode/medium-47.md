---
title: medium-47
tags:
  - LeetCode
description: '全排列 II'
urlname: medium-47
date: 2020-03-20 16:36:19
---

# 题目

https://leetcode-cn.com/problemset/all/

给定一个可包含重复数字的序列，返回所有不重复的全排列。

**示例:**

```
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

# 解题思路 √

### Python

1. 在前一道题目上面魔改

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:return []
        results=[]
        length=len(nums)
        visited=[False for i in range(length)]

        def backTrack(curr,length):
            if curr:
                if len(curr)==length:
                    if curr not in results:
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

2. 排序 + 判断


```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:return []
        results=[]
        length=len(nums)
        visited=[False for i in range(length)]
        nums=sorted(nums)

        def backTrack(curr):
            if curr:
                if len(curr)==length:
                    results.append(curr)
                    return
            for i in range(length):
                if i!=0 and nums[i]==nums[i-1] and not visited[i-1]:continue
                if visited[i]:continue
                visited[i]=True
                backTrack(curr+[nums[i]])
                visited[i]=False

        backTrack([])       
        return results
```



### C++

```cpp

```

---



# 整理与总结

1. 全排列 II

   
